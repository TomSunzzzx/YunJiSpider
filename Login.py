import requests
import json
import tkinter as tk

from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

from GlobalVars import LOGIN_HEADERS, LOGIN_JSON_DATA
from GetPaKey import generate_random_key, get_pass_key


login_random_key = generate_random_key()
get_pass_key(login_random_key)


def do_login():
    uid = entry_uid.get().strip()
    pwd = entry_pwd.get().strip()
    code = entry_code.get().strip()

    if not uid or not pwd or not code:
        messagebox.showwarning("提示", "请完整填写用户名、密码和验证码！")
        return

    LOGIN_JSON_DATA['UserID'] = uid
    LOGIN_JSON_DATA['Password'] = pwd
    LOGIN_JSON_DATA['KeyStr'] = login_random_key
    LOGIN_JSON_DATA['Code'] = code

    response = requests.post(
        'https://nh2api.yunjichaobiao.com/api/Account/Login',
        headers=LOGIN_HEADERS,
        data=LOGIN_JSON_DATA
    )

    if response.status_code != 200:
        messagebox.showwarning("提示", "登录请求发生错误，请检查网络连接")
        return

    res_json = json.loads(response.json())
    if res_json['IsSuccess']:
        messagebox.showinfo("提示", "登录成功！Token已更新")
        with open('./Save/Token.txt', 'w+') as f:
            f.write(res_json['Token'])
        root.destroy()
    else:
        messagebox.showwarning("提示", "登录请求发生错误，以下是响应信息\n" + response.json())


root = tk.Tk()
root.title("登录")
root.geometry("300x250")
root.resizable(False, False)

tk.Label(root, text="用户ID：").place(x=30, y=20)
entry_uid = ttk.Entry(root)
entry_uid.place(x=100, y=20, width=160)

tk.Label(root, text="密  码：").place(x=30, y=60)
entry_pwd = ttk.Entry(root, show="*")
entry_pwd.place(x=100, y=60, width=160)


tk.Label(root, text="验证码：").place(x=30, y=100)
img = Image.open("Save/captcha.png").resize((80, 30))
img = ImageTk.PhotoImage(img)
tk.Label(root, image=img).place(x=100, y=95)

entry_code = ttk.Entry(root)
entry_code.place(x=190, y=100, width=70)

btn_login = ttk.Button(root, text="登 录", command=do_login)
btn_login.place(x=120, y=160, width=60, height=30)

root.mainloop()