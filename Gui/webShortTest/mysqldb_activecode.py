#!/usr/bin/python
# -*- coding:utf-8 -*-

import MySQLdb
import random
import string

def gene_active_code(number,length):
    '''''
    @number:生成激活码的个数
    @length:生成激活码的长度
    '''
    result = {}
    source = list(string.ascii_uppercase)
    for index in range(0,10):
        source.append(str(index))
    while len(result) < number:
        key= ''
        for index in range(length):
            key += random.choice(source)
        if key in result:
           pass
        else:
           result[key] = 1
    return result

def save_mysql(host,user,passwd,port,number,length):
    """''
  @user:数据库用户名
  @passwd:密码
  @port:端口
  @number:生成激活码的个数
  @length:生成激活码的长度
  """
    result = gene_active_code(number,length)
    values = []
    index = 0;
    for key in result:
        values.append((index,key))
        index += 1
    conn = MySQLdb.connect(host=host,user=user,passwd=passwd,port=port) #连接数据库
    conn.select_db('test')  #选择数据库
    cur = conn.cursor()     #获取操作游标
    cur.execute('create table activecode(id int,name varchar(20))')         #创建数据表
    cur.executemany('insert into activecode values(%s,%s)',values)      #向数据表中插入数据
    conn.commit()   #提交事务
    cur.close()     #关闭操作游标
    conn.close()        #关闭数据库连接

if __name__ == "__main__":
    host = 'localhost'
    user = 'root'
    passwd = '612412'
    port = 3306
    number = 10
    length = 16
    save_mysql(host,user,passwd,port,number,length)