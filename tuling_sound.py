import json
import urllib.request
import pyttsx3  # 导入语音库

engine = pyttsx3.init()  # 初始化语音库
# 语速
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 50)

api_url = "http://openapi.tuling123.com/openapi/api/v2"  # 图灵机器人api网址
while 1:
    text_input = input('我：')

    req = {
        "perception":
            {
                "inputText":
                    {
                        "text": text_input
                    },

                "selfInfo":
                    {
                        "location":
                            {
                                "city": "深圳",
                                "province": "广东",
                                "street": "南山区招商街道"
                            }
                    }
            },

        "userInfo":
            {
                "apiKey": "706b2ed6dff743cda7c619b0737f7525",  # 你的apiKey
                "userId": "OnlyUseAlphabet"  # 不知道用途
            }
    }
    # print(req)
    # 将字典格式的req编码为utf8
    req = json.dumps(req).encode('utf8')
    # print(req)

    http_post = urllib.request.Request(api_url, data=req, headers={'content-type': 'application/json'})
    response = urllib.request.urlopen(http_post)
    response_str = response.read().decode('utf8')
    # print(response_str)
    response_dic = json.loads(response_str)
    # print(response_dic)

    intent_code = response_dic['intent']['code']
    results_text = response_dic['results'][0]['values']['text']
    print('Turing的回答：')
    # print('code：' + str(intent_code))
    print(' ' + results_text)  # 打印机器人的回复
    engine.say(results_text)  # 合成语音
    engine.runAndWait()
