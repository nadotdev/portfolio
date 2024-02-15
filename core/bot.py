import requests
TOKEN = "6728604177:AAHzoNld4gEaTg0AXAYGes3C9vE4RPbpk48"
chat_id = "@cloudnaxyz"
message = '<i>italic</i>'
message += '<b>bold</b>'
message += 'Hey'



url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&parse_mode=HTML&text={message}"

print(requests.get(url).json()) # this sends the message