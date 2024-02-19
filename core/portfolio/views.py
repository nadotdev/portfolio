from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import render
import requests
import urllib.parse
from portfolio.models import WorkingTimeline


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
        
    # render object of working timelines to home page
    working_timelines_objects = WorkingTimeline.objects.all()
    # print(working_timelines_objects)
    context = {
        'working_timelines_objects': working_timelines_objects
    }      
    return render(request, "portfolio/index.html", context)

# def timeline_view(request):
    try:
        working_timelines_objects = WorkingTimeline.objects.all()
        print(working_timelines_objects)
        context = {
            'working_timelines_objects': working_timelines_objects
        }
        return render(request, 'portfolio/timeline.html', context)
    
    # except SomeSpecificException:
    #     # Handle specific exception
    #     # ...
    #     return HttpResponseNotFound("Resource not found")
    # except AnotherSpecificException:
    #     # Handle another specific exception
    #     # ...
    #     return HttpResponseServerError("Internal server error")
    except Exception as e:
        # Handle any other unexpected exceptions
        # Log the error
        print(e)
        # Return a generic error response
        return HttpResponseServerError("An error occurred")