from flask import Flask
application = Flask(__name__)
@application.route('/')
def hello_world():
	return 'Govind Madhava Jha will return to Bangalore after mother"s surgery'
