from flask import Flask
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

@app.route("/")
def index():
	return("<h1>My first web page</h1>")

@app.route("/pwd")
def pwd():
	return f'''
		<h2>{os.environ['CHANNEL_ACCESS_TOKEN']}</h2>
		<h2>{os.environ['CHANNEL_SECRET']}</h2>
		<h2>{os.environ['Gemini_API_KEY']}</h2>
	'''
