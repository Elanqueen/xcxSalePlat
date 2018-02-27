#coding=utf-8
import web

#页面配置
urls=(
    '/','Index',
    '/desc/(.*)','Product'
)
app=web.application(urls,globals())
render=web.template.render('templates/',base='layout')

#数据库配置

db=web.database(dbn='mysql',
                db='xcxproducts',
                user='root',
                pw='root',
                charset='utf8')

class Index:
    def GET(self):
        products=db.select('products',where='SJflag=1')
        if products:
            return render.product_show(products)

class Product:
    def GET(self,p_title):
        print p_title
        product=db.select('products',
                          where="title= '%s'" % p_title)
        return render.product_desc(product[0])

if __name__=='__main__':
    app.run()