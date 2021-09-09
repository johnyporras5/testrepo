from django.db import models


class Bookmark(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=5)
    url = models.CharField(max_length=10)
    created_at = models.DateField(null=True)
    user_id = models.CharField(max_length=100, null=True)
    type = models.IntegerField(null=True)  # 1) public, 2)private

    def __str__(self):
        return self.title

    @classmethod
    def get_bookmarks(self):
        return self.objects.all()

    @classmethod
    def get_bookmarks_by_id(self, id: int):
        return self.objects.get(pk=id)

    @classmethod
    def get_bookmarks_by_type(self, type: int):
        return self.objects.filter(type=type).all()

    @classmethod
    def get_bookmarks_by_user(self, user: str):
        return self.objects.filter(user_id=user).all()

