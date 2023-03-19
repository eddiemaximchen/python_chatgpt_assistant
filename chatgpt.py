import openai
from gtts import gTTS
import os

#set your OpenAI API key
openai.api_key="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"
while True:
    print('type to chat:')
    chat=input()
    response=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role":"user","content":f"{chat}"},
        ]
    )
    rtest=response['choices'][0]['message']['content']
    tts=gTTS(text=rtest,lang='en')
    mp3file='test.mp3'
    tts.save(mp3file)
    os.system('mpg123 ' +'test.mp3')
    tts=gTTS(text='Anythings I can assist you? press control key plus c to quit',lang='en')
    mp3file='test.mp3'
    tts.save(mp3file)
    os.system('mpg123 ' +'test.mp3')










