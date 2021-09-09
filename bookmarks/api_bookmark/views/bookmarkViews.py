import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from rest_framework.views import APIView

from  api_bookmark.models.bookmark import Bookmark
from  api_bookmark.serializers.bookmarkSerializer import BookmarkSerializer


class BookmarkViews(APIView):
	def get(self, request, id = None):
		print(request.user.is_authenticated)
		print(request.user)
		if not request.user.is_authenticated:
			bookmarks = Bookmark.get_bookmarks_by_type(1)
		else:
			bookmarks = Bookmark.get_bookmarks_by_user(str(request.user)) | Bookmark.get_bookmarks_by_type(1)
		serializer = BookmarkSerializer(bookmarks, many=True)
		return JsonResponse(serializer.data, safe=False)

	@method_decorator(login_required(login_url='/nologged/'), name='dispatch')
	def post(self, request, id = None):

		request_body = json.loads(request.body.decode('utf-8'))
		request_body['user_id'] = str(request.user) #This should be the user_id retreived by jwt token
		bookmark = BookmarkSerializer(data=request_body)
		if bookmark.is_valid():
			bookmark.save()
			return JsonResponse(bookmark.data, status=201)
		return JsonResponse(bookmark.errors, status=401)

	@method_decorator(login_required(login_url='/nologged/'), name='dispatch')
	def put(self, request, id = None):
		request_body = json.loads(request.body.decode('utf-8'))
		try:
			bookmark = Bookmark.get_bookmarks_by_id(id)
		except:
			return HttpResponse(status=404)

		bookmark_serializer = BookmarkSerializer(bookmark, data=request_body)
		if bookmark_serializer.is_valid():
			bookmark_serializer.save()
			return JsonResponse(bookmark_serializer.data, status=201)
		return JsonResponse(bookmark_serializer.errors, status=401)

	@method_decorator(login_required(login_url='/nologged/'), name='dispatch')
	def delete(self, request,  id = None):
		try:
			bookmark = Bookmark.get_bookmarks_by_id(id)
		except:
			return HttpResponse(status=404)

		bookmark.delete()
		return HttpResponse(status=204)






