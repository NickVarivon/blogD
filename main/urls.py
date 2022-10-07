from django.urls import path

from main.views import BlogsAPIView

app_name = 'main'
urlpatterns = [
    path('api/v1/blogs/', BlogsAPIView.as_view(), name='blogs')
]
