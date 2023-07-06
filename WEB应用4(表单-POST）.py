from flask import Flask,render_template,request
from flask_wtf import FlaskForm  #需要打开cmd pip install flask-wtf
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['POST'])
def login():
    username=request.form.get('username')
    return '<h1>欢迎登陆：'+username+'</h1>'

if __name__=='__main__':
    app.run(debug=False)
