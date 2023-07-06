from flask import Flask,request
app=Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    username=request.args.get('user')
    return '<h1>你好！'+username+'</h1>'

@app.route('/message',methods=['GET'])
def test():
    xm=request.args.get('xm')
    xb=request.args.get('xb')
    return '<h2>姓名：'+xm+',性别='+xb+'</h2>'

if __name__=='__main__':
    app.run()
