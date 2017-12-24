#!/usr/bin/python  
# -*- coding: utf-8 -*-

# 例：FTP编程  
from ftplib import FTP  
      
ftp = FTP()  
timeout = 30  
port = 21  
ftp.connect('192.168.1.188',port,timeout) # 连接FTP服务器  
ftp.login('UserName','888888') # 登录  
print ftp.getwelcome()  # 获得欢迎信息   
ftp.cwd('file/test')    # 设置FTP路径  
list = ftp.nlst()       # 获得目录列表  
for name in list:  
    print(name)             # 打印文件名字  
path = 'd:/data/' + name    # 文件保存路径  
f = open(path,'wb')         # 打开要保存文件  
filename = 'RETR ' + name   # 保存FTP文件  
ftp.retrbinary(filename,f.write) # 保存FTP上的文件  
ftp.delete(name)            # 删除FTP文件  
ftp.storbinary('STOR '+filename, open(path, 'rb')) # 上传FTP文件  
ftp.quit()                  # 退出FTP服务器  



# 
# import os  
# import ftplib  
# import socket  
# 
# 
# 
# HOST = 'ftp.mozilla.org'  
# DIRN = 'pub/mozilla.org/webtools'  
# FILE = 'bugzilla-3.6.7.tar.gz'  
# def main():  
#     try:  
#         f = ftplib.FTP(HOST)  
#     except (socket.error, socket.gaierror):  
#         print 'ERROR:cannot reach " %s"' % HOST  
#         return  
#     print '***Connected to host "%s"' % HOST  
#   
#     try:  
#         f.login()  
#     except ftplib.error_perm:  
#         print 'ERROR: cannot login anonymously'  
#         f.quit()  
#         return  
#     print '*** Logged in as "anonymously"'  
#     try:  
#         f.cwd(DIRN)  
#     except ftplib.error_perm:  
#         print 'ERRORL cannot CD to "%s"' % DIRN  
#         f.quit()  
#         return  
#     print '*** Changed to "%s" folder' % DIRN  
#     try:  
#         #传一个回调函数给retrbinary() 它在每接收一个二进制数据时都会被调用  
#         f.retrbinary('RETR %s' % FILE, open(FILE, 'wb').write)  
#     except ftplib.error_perm:  
#         print 'ERROR: cannot read file "%s"' % FILE  
#         os.unlink(FILE)  
#     else:  
#         print '*** Downloaded "%s" to CWD' % FILE  
#     f.quit()  
#     return  
#   
# if __name__ == '__main__':  
#     main()  