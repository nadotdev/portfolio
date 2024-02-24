from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='portfolio-home'),
    path("in-review", views.review_user_account),
]
