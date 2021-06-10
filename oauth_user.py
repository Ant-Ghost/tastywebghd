from flask import Flask, url_for, session, request, redirect
from authlib.integrations.flask_client import OAuth

class Google():
	
	app = Flask(__name__)
	app.secret_key='random key'

	oauth = OAuth(app)
	google = oauth.register(
	    name='google',
	    client_id='605004903750-9idp7cggojabevccn697qbbg2cthb1bc.apps.googleusercontent.com',
	    client_secret='fF9LnK2QFou9Wb6TM10fl_rf',
	    access_token_url='https://accounts.google.com/o/oauth2/token',
	    access_token_params=None,
	    authorize_url='https://accounts.google.com/o/oauth2/auth',
	    authorize_params=None,
	    api_base_url='https://www.googleapis.com/oauth2/v1/',
	    userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',  # This is only needed if using openId to fetch user info
	    client_kwargs={'scope': 'openid email profile'},
    )

	g = oauth.create_client('google')


	def to_auth_page(self):
		return self.g

	def send_user_info(self):
		token=(self.oauth).google.authorize_access_token()
		resp = (self.oauth).google.get('userinfo')
		return resp.json()


class Facebook():
	app = Flask(__name__)
	app.secret_key='random key'
	
	oauth = OAuth(app)
	facebook = oauth.register(
	    name='facebook',
	    client_id='2896973843953926',
	    client_secret='ca2531220b6a1259e046d0c406633a42',
	    access_token_url='https://graph.facebook.com/v6.0/oauth/access_token',
	    access_token_params=None,
	    authorize_url='https://www.facebook.com/v6.0/dialog/oauth',
	    authorize_params=None,
	    api_base_url='https://graph.facebook.com/',
	    userinfo_endpoint='https://graph.facebook.com/me',  # This is only needed if using openId to fetch user info
	    client_kwargs={'scope': 'email'},
	    )
	f = oauth.create_client('facebook')
	
	def to_auth_page(self):
		return self.f

	def send_user_info(self):
		token = (self.oauth).facebook.authorize_access_token()
		print(token)
		resp = (self.oauth).facebook.get('/me',params={'fields':'name,email'})
		user_info = resp.json()
		return user_info
	
	
class Linkedin():
	app = Flask(__name__)
	app.secret_key = 'random key'
	
	oauth = OAuth(app)
	linkedin = oauth.register(
	    name='linkedin',
	    client_id='78u7oehwxtcfhl',
	    client_secret='Wib8hXLBq2if1Aki',
	    access_token_url='https://www.linkedin.com/oauth/v2/accessToken',
	    access_token_params=None,
	    access_token_method='POST',
	    authorize_url='https://www.linkedin.com/oauth/v2/authorization',
	    api_base_url='https://api.linkedin.com/v2',
	    client_kwargs={'scope': 'r_liteprofile r_emailaddress'},
	)
	
	l = oauth.create_client('linkedin')
	
	def to_auth_page(self):
		return self.l
	
	def send_user_info(self):
		token = (self.oauth).linkedin.authorize_access_token()
		resp1 = (self.oauth).linkedin.get('https://api.linkedin.com/v2/me').json()
		resp2 = (self.oauth).linkedin.get('https://api.linkedin.com/v2/emailAddress', params={'q':'members','projection':'(elements*(handle~))'}).json()
		user_info = {}
		user_info['firstname']=resp1['localizedFirstName']
		user_info['lastname']=resp1['localizedLastName']
		user_info['id']=resp1['id']
		user_info['email']=resp2['elements'][0]['handle~']['emailaddress']
		return user_info
	
