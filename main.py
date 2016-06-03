from flask import Flask,request, make_response
from config.config import *
import hashlib

app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def hello_world():
    print("OKcx")
    return 'Hello World!'

@app.route('/weixin',methods=['GET','POST'])
def wechat_auth():
    print("OK")
    if request.method == 'GET':
            token = WECHAT_CONFIG['token']
            data = request.args
            signature = data.get('signature','')
            timestamp = data.get('timestamp','')
            nonce = data.get('nonce','')
            echostr = data.get('echostr','')
            s = [timestamp,nonce,token]
            s.sort()
            s = ''.join(s)
            if hashlib.sha1(s).hexdigest() == signature:
                return make_response(echostr)


if __name__ == '__main__':
    app.run('0.0.0.0', port=80, debug=True)
