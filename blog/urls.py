from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import article_list_view,article_create_view,article_edit_view,article_view,article_delete_view


urlpatterns = [
	path('list/', article_list_view, name='article-list'),
	path('create/', article_create_view, name='article-create'),
	path('<int:id>/edit/', article_edit_view, name='article-edit'),
	path('<int:id>/view/', article_view, name='article-view'),
	path('<int:id>/delete/', article_delete_view, name='article-delete'),
]

urlpatterns += staticfiles_urlpatterns()