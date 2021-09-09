from rest_framework.serializers import ModelSerializer

from api_bookmark.models import Bookmark


class BookmarkSerializer(ModelSerializer):
    def to_representation(self, instance: Bookmark):
        return {
            'title': instance.title,
            'description': instance.description,
            'path': instance.url,
            'user': instance.user_id,
            'id' : instance.id
        }

    class Meta:
        model = Bookmark

        fields = ['title', 'description', 'url', 'user_id', 'type']