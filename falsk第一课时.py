from flask import Flask             #导入框架模块

app=Flask(__name__)                 #创建app实例

@app.route('/')                     #编写路由和视图函数
def index():
    return '我的第一个网页'

@app.route('/profile/<name>')       #编写路由和视图函数
def profile(name):
    return 'hello,%s'%name


if __name__=="__main__":
    app.run()

