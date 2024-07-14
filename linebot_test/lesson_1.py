from dotenv import load_dotenv
import os

def _main():
	load_dotenv()
	print(os.environ['CHANNEL_ACCESS_TOKEN'])
	print(os.environ['CHANNEL_SECRET'])
	print(os.environ['Gemini_API_KEY'])

if __name__ == '__main__':
	_main()
