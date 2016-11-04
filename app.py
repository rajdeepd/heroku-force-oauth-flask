from flask import Flask, request
import urllib
from OpenSSL import SSL
import os
import urllib2
#from urllib2 import urlopen
app = Flask(__name__)

client_id = '3MVG9ZL0ppGP5UrBMsor2EoRrW0__Bqk8ytOi7_7T.afqqthzPfztjH8MLeT8bfkYwz45_3mVUJO5pdWE_EJa'
client_secret = '5045264606824676005'
url = 'https://login.salesforce.com/services/oauth2/authorize?response_type=code&' \
    'client_id=' + client_id + '&redirect_uri=https://127.0.0.1:5000/auth/salesforce/callback&prompt=login%20consent'
context = SSL.Context(SSL.SSLv23_METHOD)
cer = os.path.join(os.path.dirname(__file__), 'test.crt')
key = os.path.join(os.path.dirname(__file__), 'test.key')

@app.route('/')
@app.route('/login', methods=['GET'])
def login():
    print url
    return '<a href="' + url + '">Login</a>'

@app.route('/auth/salesforce/callback')
def callback():
    code = request.args['code']
    print code
    url_post = 'https://login.salesforce.com/services/oauth2/token'
    values = {'code' : code,
              'grant_type' : 'authorization_code',
              'client_id' : client_id,
              'client_secret' : client_secret,
               'redirect_uri' : 'https://127.0.0.1:5000/auth/salesforce/callback'}

    data = urllib.urlencode(values)
    req = urllib2.Request(url_post, data)
    response = urllib2.urlopen(req)
    r = response.read()
    return r


if __name__ == '__main__':
    context = (cer, key)
    app.run( host='0.0.0.0', port=5000, debug = True, ssl_context=context)
