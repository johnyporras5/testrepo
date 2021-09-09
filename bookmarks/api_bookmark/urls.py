from django.urls import path
from .views.bookmarkViews import BookmarkViews
from django.views.decorators.csrf import csrf_exempt
app_name = 'api_bookmark'

urlpatterns = [
	path('bookmark/<int:id>', csrf_exempt(BookmarkViews.as_view())),
	path('bookmarks', BookmarkViews.as_view(), name='bookmarks'),
	path('bookmark', BookmarkViews.as_view(), name='bookmarks')
]
