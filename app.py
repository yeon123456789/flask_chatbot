import os
#json으로 바꾸기 위해 
import json
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '챗봇페이지 입니다!!!!'
    
@app.route('/keyboard')
def keyboard():
    
    #keyboard 딕셔너리 생성
    keyboard = {
    "type" : "buttons",
    "buttons" : ["메뉴", "로또", "고양이", "영화"]
    }
    
    #딕셔너리를 json으로 바꿔서 리턴해주기 위함 코드
    json_keyboard = json.dumps(keyboard)
    return json_keyboard

app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
