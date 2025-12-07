from rest_framework import serializers
from genres.models import Genre


class GenreSerializer(serializers.ModelSerializer):

    class Meta(Genre):
        model = Genre
        fields = '__all__'  # ['id', 'name']
