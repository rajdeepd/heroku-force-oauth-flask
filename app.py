from flask import Flask, request
import urllib
import urllib2
app = Flask(__name__)

client_id = ''
client_secret = ''
url = 'https://login.salesforce.com/services/oauth2/authorize?response_type=code&' \
    'client_id=' + client_id + '&redirect_uri=http://localhost:5000/auth/salesforce/callback&prompt=login%20consent'

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
               'redirect_uri' : 'http://localhost:5000/auth/salesforce/callback'}

    data = urllib.urlencode(values)
    req = urllib2.Request(url_post, data)
    response = urllib2.urlopen(req)
    r = response.read()
    return r


if __name__ == '__main__':
    app.run()
