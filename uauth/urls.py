from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import login_view,register_view


urlpatterns = [
	path('login/', login_view, name='ulogin'),
	path('register/', register_view, name='uregister'),
]

urlpatterns += staticfiles_urlpatterns()