import random
import json
import requests
import base64

from GlobalVars import GET_PASS_KEY_HEADERS, GET_PASS_KEY_JSON_DATA, RANDOM_KEY_ARR

def generate_random_key() -> str:
    return ''.join(random.sample(RANDOM_KEY_ARR, 12))

def get_pass_key(key_str: str) -> None:

    GET_PASS_KEY_JSON_DATA['keyStr'] = key_str

    try:
        response = requests.post(
            f'https://nh2api.yunjichaobiao.com/api/Account/GetCaptcha?keyStr={key_str}',
            headers=GET_PASS_KEY_HEADERS,
            data=GET_PASS_KEY_JSON_DATA
            )

        if response.status_code != 200:
            print("请求失败")
            return

        base64_str = json.loads(response.json())["Data"].strip('"')

        img_data = base64.b64decode(base64_str)
        with open("Save/captcha.png", "wb") as f:
            f.write(img_data)
        print("验证码已保存为captcha.png")
    except Exception as e:
        print(e)