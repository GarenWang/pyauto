#!/usr/bin/python
import difflib
import sys

try:
    textfile1=sys.argv[1]
    textfile2=sys.argv[2]
except Exception,e:
    print "Error:"+str(e)
    print "Usage: simple3.py filename1 filename2"
    sys.exit()

def readfile(filename):     #文件读取分隔函数
    try:
        fileHandle = open (filename, 'rb' ) 
        text=fileHandle.read().splitlines()     #读取后以行进行分隔
        fileHandle.close()
        return text
    except IOError as error:
       print('Read file Error:'+str(error))
       sys.exit()

if textfile1=="" or textfile2=="":
    print "Usage: simple3.py filename1 filename2"
    sys.exit()


text1_lines = readfile(textfile1)      #使用readfile函数，获取分隔后的字符串
text2_lines = readfile(textfile2) 

d = difflib.HtmlDiff()
print d.make_file(text1_lines, text2_lines)



运行方式：
#python simple3.py nginx.conf.v1 nginx.conf.v2 > diff.html
