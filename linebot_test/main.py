import os
from flask import Flask, request, abort
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import google.generativeai as genai

load_dotenv()

app = Flask(__name__)
line_bot_api = LineBotApi(os.environ['CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['CHANNEL_SECRET'])


@app.route("/")
def index():
	return("<h1>LineBot 的 webhook 程式</h1>")

# Method use POST, NOT GET
# Web browser 用 GET，所以 web browser 無法看到 callback 內容
@app.route("/callback", methods=['POST'])
def callback():
	signature = request.headers['X-Line-Signature']
	body = request.get_data(as_text=True)
	app.logger.info("Request body:" + body)
	try:
		handler.handle(body, signature)
	except InvalidSignatureError:
		abort(400)
	return 'OK'

# LineBot webhook event handler
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
	# Setup API key
	genai.configure(api_key=os.environ['Gemini_API_KEY'])
	# Select AI model
	model=  genai.GenerativeModel('gemini-1.5-flash')
	# Send the question
	response=  model.generate_content(event.message.text)
	# Get and print out the answer and reply to line-bot
	#  pack answer in message packet
	message = TextSendMessage(text=response.text)
	line_bot_api.reply_message(event.reply_token, message)
