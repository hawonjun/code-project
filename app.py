from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'eks jenkis argocd 파이프라인 구성 웹페이지'
