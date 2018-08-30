import os
#json으로 바꾸기 위해 라이브러리 추가
import json
import random
import requests
from flask import Flask, request, jsonify

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
    
    #딕셔너리를 json으로 바꿔서 리턴해주기 위한 코드
    json_keyboard = json.dumps(keyboard)
    return json_keyboard

@app.route('/message', methods=['POST'])
def message():
    
    # content라는 key의 value를 msg에 저장
    msg = request.json['content']
    img_bool = False
    
    if msg == "메뉴":
        menu = ["버거킹", "북창동순두부", "아비꼬카레", "서브웨이"]
        return_msg = random.choice(menu)
        
    elif msg == "로또":
        # 1~45 리스트
        numbers = list(range(1, 46))
        # 6개 샘플링
        pick = random.sample(numbers, 6)
        # 정렬 후 스트링으로 변환하여 저장
        return_msg = str(sorted(pick))
        
    elif msg == "고양이":
        img_bool = True
        url = "https://api.thecatapi.com/v1/images/search?mime_types=jpg"
        req = requests.get(url).json()
        # print(req[0]['url'])
        cat_url = req[0]['url']
    else:
        return_msg = "현재 '메뉴'와 '로또'만 지원합니다."
    
    if img_bool == True:
            json_return = {
                            "message": {
                            "text": "나도 고양이 키우고 싶다아",
                            "photo": {
                                "url": cat_url,
                                "width":720,
                                "height":640
                                }
                            },
        "keyboard": {
                        "type" : "buttons",
                        "buttons" : ["메뉴", "로또", "고양이", "영화"]
                    }
    }
    
    return jsonify(json_return)
    

app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
