#初始化mysqld --initialize --console 安装mysqld install

#mysql -h 主机名 -u 用户名（root） -p 。 -h  MySQL 主机名, 登录本机(localhost 或 127.0.0.1)该参数可以省略

#SHOW DATABASES; 显示数据库 。   use 数据库名；
#show tables;显示指定数据库的所有表  SHOW INDEX FROM 数据表: SHOW COLUMNS FROM 数据表:

import mysql.connector

conn = mysql.connector.connect(user='root',password='password',database='test')
cursor = conn.cursor()

#建立user的表 （id name）都是varchar（20），id是primarykey
cursor.execute('create table user (id varchar(20) primary key,name varchar(20))')
#插入user表 （id name） 值为（1，michael）
cursor.execute('insert into user (id,name) values (%s,%s)',['1','Michael'])
cursor.rowcount

conn.commit()
cursor.close()

