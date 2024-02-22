from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import render, get_object_or_404

import requests
import urllib.parse
from portfolio.models import WorkingTimeline, Education, About, Technology


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
        requests.get(url).json()    # sends the message trigger
        if HttpResponse.status_code == 200:
            return render(request, 'portfolio/thank.html')
        
    # render object of timelines to home page
    working_timelines = WorkingTimeline.objects.all()
    edu_timelines = Education.objects.all()
    # about = get_object_or_404(About, id=None)
    about_obj = About.objects.latest('created_at')
    technologies = Technology.objects.all()

    context = {
        'working_timelines': working_timelines,
        'edu_timelines': edu_timelines,
        'about_obj': about_obj,
        'technologies': technologies
    }      
    return render(request, "portfolio/home.html", context)
