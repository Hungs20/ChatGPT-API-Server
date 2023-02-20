from revChatGPT.V1 import Chatbot
from flask import Flask
from flask import jsonify
from flask import request
from dotenv import load_dotenv
import os
load_dotenv()
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def welcome():
    return "ChatGPT API!"


EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

chatbot = Chatbot(config={
    "email": EMAIL,
    "password": PASSWORD
})

# ChatGPT V1


@app.route('/api/v1/chatgpt/', methods=['POST'])
def chatgpt():
    jsonData = request.get_json()
    prompt = jsonData.get('prompt')
    response = ""

    for data in chatbot.ask(prompt):
        response = data
    if response == "":
        response = {
            "success": False,
            "message": "Đã có lỗi xảy ra, vui lòng thử lại"
        }
    else:
        response["success"] = True
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105, debug=True)
