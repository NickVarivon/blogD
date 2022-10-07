from rest_framework import serializers

from main.models import Blogs


class BlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = ('title', 'short_text')