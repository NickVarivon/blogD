
# from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

# from main.models import Blogs
# from main.serializers import BlogsSerializer


class BlogsAPIView(APIView):
    def get(self, request):
        return Response({'title': 'Дети в школу'})



# class BlogsAPIView(generics.ListAPIView):
#     queryset = Blogs.objects.all()
#     serializer_class = BlogsSerializer
