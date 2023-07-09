from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'AWS Jenkins ArgoCD 파이프 라인 구성 웹페이지'
