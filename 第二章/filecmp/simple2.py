#!/usr/bin/env python
 
import os, sys
import filecmp
import re
import shutil
holderlist=[]
 
def compareme(dir1, dir2):    #递归获取更新函数
    dircomp=filecmp.dircmp(dir1,dir2)
    only_in_one=dircomp.left_only
    diff_in_one=dircomp.diff_files
    dirpath=os.path.abspath(dir1)
    [holderlist.append(os.path.abspath( os.path.join(dir1,x) )) for x in only_in_one]
    [holderlist.append(os.path.abspath( os.path.join(dir1,x) )) for x in diff_in_one]
    if len(dircomp.common_dirs) > 0:  #判断是否存在相同子目录，存在则递归
        for item in dircomp.common_dirs:   #递归子目录
            compareme(os.path.abspath(os.path.join(dir1,item)), \
            os.path.abspath(os.path.join(dir2,item)))
        return holderlist

def main():
    if len(sys.argv) > 2:
        dir1=sys.argv[1]
        dir2=sys.argv[2]
    else:
        print "Usage: ", sys.argv[0], "datadir backupdir"
        sys.exit()
 
    source_files=compareme(dir1,dir2)
    dir1=os.path.abspath(dir1)

    if not dir2.endswith('/'): dir2=dir2+'/'   #备份目录路径加"/" 符
    dir2=os.path.abspath(dir2)
    destination_files=[]
    createdir_bool=False

    for item in source_files:
        destination_dir=re.sub(dir1, dir2, item)  #将源目录差异路径清单对应替换成备份目录
        destination_files.append(destination_dir)
        if os.path.isdir(item):  #如果差异路径为目录且不存在，则在备份目录中创建
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
                createdir_bool=True

    if createdir_bool:
        destination_files=[]
        source_files=[]
        source_files=compareme(dir1,dir2)
        for item in source_files:
            destination_dir=re.sub(dir1, dir2, item)
            destination_files.append(destination_dir)

    print "update item:"
    print source_files 

    copy_pair=zip(source_files,destination_files)
    for item in copy_pair:
        if os.path.isfile(item[0]):
            shutil.copyfile(item[0], item[1])
 
if __name__ == '__main__':
    main()

  
运行方式：
python simple2.py /home/shiyanlou/pythontest/dir1 /home/shiyanlou/pythontest/dir2
