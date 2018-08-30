# 파이썬 챗봇 만들기!!!

### 카카오톡 플러스친구 관리자센터

- 가입 후, 플러스친구 생성 -> 관리/상세설정 -> 플러스친구 홈/공개 설정(공개 안되면 검색 안됨)
- 스마트 채팅에서  API형 사용

### c9 개발

- 우측 상단의 톱니바퀴에 들어가서 python support에서 python3로 설정변경
- `sudo pip3 install flask` 플라스크 설치

### keyboard

```python

@app.route('/keyboard')
def keyboard():
    keyboard = {
    "type" : "buttons",
    "buttons" : ["메뉴", "로또", "고양이", "영화"]
    }
    json_keyboard = json.dumps(keyboard)
    return json_keyboard

app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
```
#### API

- request
    - url : 어떤 경로로 보낼거니?
    - method : 어떤 방법으로 보낼거니?
    - parameter : 어떤 정보를 담을거니?

- response
    - data type : 어떤 형식으로 답할까?
    - 
