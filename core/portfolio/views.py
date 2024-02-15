from django.http import HttpResponse
from django.shortcuts import redirect, render
import requests
import urllib.parse


TOKEN = "6728604177:AAHzoNld4gEaTg0AXAYGes3C9vE4RPbpk48"
chat_id = "@cloudnaxyz"

def home(request):
    if request.method == "POST":
        subject = request.POST.get('message_subject')
        email = request.POST.get('email')
        comment = request.POST.get('comment')

        text = f"<strong>Subject:</strong> {subject}\n<b>Email:</b> {email}\n<b>Messages:</b> {comment}"
        encoded_text = urllib.parse.quote(text)

        # Construct the Telegram API URL
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&parse_mode=HTML&text={encoded_text}"
        requests.get(url).json() # sends the message trigger
        if HttpResponse.status_code == 200:
            return render(request, 'portfolio/thank.html')

    return render(request, "portfolio/index.html")
