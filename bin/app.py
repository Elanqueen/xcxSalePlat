#coding=utf-8
import web
import json

#页面配置
urls=(
    '/','Index',
    '/desc/(.*)','Pd_desc',
    '/gwc/(.*)','GWC'
)
app=web.application(urls,globals())
render=web.template.render('templates/',base='layout')
#session配置
store = web.session.DiskStore('sessions')
session = web.session.Session(app,store,initializer={'count':0})
#数据库配置
db=web.database(dbn='mysql',
                db='xcxproducts',
                user='root',
                pw='root',
                charset='utf8')

class Index:
    '''登录页面
        产品列表展示页面
    '''
    def GET(self):
        #return render.login()
        products = db.select('product', where='SJflag=1')
        if products:
            return render.product_show(products)

    def POST(self):
        form=web.input()
        if form.name=="":
            return render.login()
        users=db.select('user',where="wxname='%s' and passwd='%s'"
                                     % (form.name,form.passwd))
        if len(users)==0:
            db.insert('user',wxname=form.name,passwd=form.passwd)
        products = db.select('product', where='SJflag=1')
        if products:
            return render.product_show(products)

class Pd_desc:
    '''产品详情页面'''
    def GET(self,p_title):
        print p_title
        product=db.select('product',
                          where="title= '%s'" % p_title)
        return render.product_desc(product[0])

class GWC:
    '''购物车中物品展示页面'''
    def GET(self,user):
        products=db.select("gwc",where="user='%s'"% user)
        return render.gwc(products)

    def POST(self):
        '''获取页面加入购物车请求'''
        pd=web.input()
        user=pd["user"]
        title=pd["pdtitle"]
        gg=pd["pdgg"]
        print pd
        print pd["pdtitle"],pd.get("pdtitle"),pd.pdtitle
        print pd.items()
        print pd.values()
        pddata=db.select("gwc",what="pdsl",where="user='%s'and pdtitle='%s' and pdgg='%s'" % (user,title,gg))
        for i in pddata:
            sl=int(i["pdsl"])
            sl=sl+1
            break
        if len(pddata)==0:
            db.insert("gwc",user=pd["user"],
                      pdtitle=pd["pdtitle"],
                      pdgg=pd["pdgg"],
                      pddj=pd["pddj"],
                      pdsl=1)

        else:
            db.update("gwc",where="user='%s'and pdtitle='%s'and pdgg='%s'"
                                     % (pd["user"], pd["pdtitle"], pd["pdgg"]),pdsl=sl)
        return "true"

if __name__=='__main__':
    app.run()