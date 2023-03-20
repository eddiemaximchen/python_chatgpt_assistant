import openai
from gtts import gTTS
from flask import Flask
from flask import Response

app = Flask(__name__)


@app.route('/chat',defaults={'chat':'Hello'})
@app.route('/chat/<chat>')
def chat(chat):
    openai.api_key="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"
    response=openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role":"user","content":"%s!" %chat},
    ]
    )
    rtest=response['choices'][0]['message']['content']
    tts=gTTS(text=rtest,lang='en')
    mp3file='test.mp3'
    tts.save(mp3file) #聲音檔有變 只是沒有response 


if __name__ == '__main__':
    # app.run(debug=True) # so the other machine can visit the website by ip
    app.run(host='0.0.0.0')





