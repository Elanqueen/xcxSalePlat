#coding=utf-8
import MySQLdb

db=MySQLdb.connect(host='localhost',
                   db='xcxproducts',
                   user='root',
                   passwd='root',
                   port=3306,
                   charset='utf8')
cu=db.cursor()

#创建products表
sql = """
    create table if not exists product(
    id int auto_increment primary key,
    title varchar(40) not null,
    GG varchar(40),
    DJ float,
    SL int,
    image varchar(100),
    SJflag int
    )engine = InnoDB default charset=utf8
"""
#cu.execute(sql)

#插入测试数据
sql="insert into product (id,title,GG,DJ,SL,image,SJflag)values(%s,%s,%s,%s,%s,%s,%s)"
prama=(
    (1,'小瓶香油','250g',10,9999,'images/product/4.jpeg',1),
    (2,'大瓶香油','500g',20,9999,'images/product/4.jpeg',1),
    (3,'小瓶芝麻酱','500g',10,9999,'images/product/4.jpeg',1),
    (4,'大瓶芝麻酱','1000g',20,9999,'images/product/4.jpeg',1)
)
#cu.executemany(sql,prama)
#db.commit()

sql = """
    create table if not exists pdbag(
    wxname varchar(40) not null,
    pdtitle varchar(40),
    pdGG varchar(100),
    pdDJ float,
    SL int
    )engine = InnoDB default charset=utf8
"""
cu.execute(sql)

sql = """
    create table if not exists user(
    id int auto_increment primary key,
    wxname varchar(40) not null,
    phone varchar(100)
    )engine = InnoDB default charset=utf8
"""
cu.execute(sql)
