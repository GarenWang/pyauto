import pxssh
import getpass
try:
    s = pxssh.pxssh() #创建pxssh对象s
    hostname = raw_input('hostname: ')
    username = raw_input('username: ')
    password = getpass.getpass('password: ') #接受密码输入
    s.login (hostname, username, password)  #建立ssh连接
    s.sendline ('uptime')  # run a command
    s.prompt()             # match the prompt 匹配系统提示符
    print s.before         # print everything before the prompt.
    s.sendline ('ls -l')
    s.prompt()
    print s.before
    s.sendline ('df')
    s.prompt()
    print s.before
    s.logout()
except pxssh.ExceptionPxssh, e:
    print "pxssh failed on login."
    print str(e)
