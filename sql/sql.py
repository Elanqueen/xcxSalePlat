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
    create table if not exists products(
    id int auto_increment primary key,
    title varchar(40),
    GGDW varchar(40),
    GGSL int,
    DJDW varchar(40),
    DJ float,
    images varchar(100),
    SJflag int
    )engine = InnoDB default charset=utf8
"""
#cu.execute(sql)

#插入测试数据
sql="insert into products (id,title,GGDW,GGSL,DJDW,DJ,images,SJflag)values(%s,%s,%s,%s,%s,%s,%s,%s)"
prama=(
    (1,'小瓶香油','g',250,'元','10','/images/ad/ad1.jpg',1),
    (2,'大瓶香油','g',500,'元','20','/images/ad/ad1.jpg',1),
    (3,'小瓶芝麻酱','g',500,'元','10','/images/ad/ad1.jpg',1),
    (4,'大瓶芝麻酱','g',1000,'元','20','/images/ad/ad1.jpg',1)
)
cu.executemany(sql,prama)
db.commit()
