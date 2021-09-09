from django.test import TestCase
from .models import Bookmark


class BookmarkTest(TestCase):
    """ Test module for Bookmark model """

    def setUp(self):
        Bookmark.objects.create(
            title='Title 1', description="ssss", url='google.com', type=1, user_id="johnyporras")
        Bookmark.objects.create(
            title='Title 1', description="pppp", url='facebook.com', type=2 , user_id="johnyporras")

    def test_bookmark_users(self):
        bookmarks = Bookmark.get_bookmarks_by_user('johnyporras')
        self.assertTrue(bookmarks.count() > 0)

    def test_bookmark_type(self):
        bookmarks = Bookmark.get_bookmarks_by_type(1)
        self.assertTrue(bookmarks.count() > 0)

