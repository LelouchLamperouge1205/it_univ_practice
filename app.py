from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('Lk0pLmjl/OGLuQHxtXdpnHc6Inmuf7j0Acgf6Gur0QT4ifGQYqAH+zmNR5dvJ5cGQnqHT+kAt747ldN6uCDnS5lBMiEtVFkKWbw3KPE2FmgoOfdc4UtNrzVWC1MSs1ssA8703mqDL/hujKqrOAhQowdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('d845fb45c202709205b985c72c27928b')

@app.route("/")
def test():
    return "OK"


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
