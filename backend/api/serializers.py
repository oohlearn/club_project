from rest_framework import serializers
from .models import Video, Activity, Albums, Teacher, Experience, IndexStory


class VideoSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    # use_url=True時，序列化器將會返回圖片的URL

    class Meta:
        model = Video
        fields = ["id", "title", "date", "performer",
                  "place", "description", "url", "embed_url", "image"]


class ProgramSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=500)
    composer = serializers.CharField(max_length=100)


class TicketSerializer(serializers.Serializer):
    ticket_key = serializers.CharField(max_length=500)
    ticket_type = serializers.CharField(max_length=500)
    price = serializers.IntegerField()
    description = serializers.CharField(max_length=1000)


class ActivitySerializer(serializers.ModelSerializer):
    poster = serializers.ImageField(max_length=None, use_url=True)
    program = ProgramSerializer(many=True)
    ticket = TicketSerializer(many=True)

    class Meta:
        model = Activity
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Activity
        fields = '__all__'
