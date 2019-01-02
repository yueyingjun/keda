# 1. python 代码执行不了，将python的安装目录放到环境变量里面
#  windows
#  在pycharm里面你的代码运行不了，需要在编辑器里面配置 python安装目录
# python -m pip install -U pip
from flask import Flask
from  urllib import request

res=request.urlopen("http://www.baidu.com")
con=res.read().decode("utf8")
print(con);


app=Flask(__name__)
@app.route("/")
def index():
    return "hello world"

app.run()