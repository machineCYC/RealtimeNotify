import requests
import conf

def notify_Line_Message(token, msg):
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    params = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = params)
    print(r.status_code)
    return r.status_code

# 修改為你要傳送的訊息內容
message = 'Notify from LINE, GG'

notify_Line_Message(conf.token, message)