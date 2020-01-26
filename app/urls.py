from django.urls import path
from app.views import MessageView, StatusView

app_name = 'app'
urlpatterns = [  
    path('', MessageView.as_view()),
    path('status/', StatusView.as_view())
]