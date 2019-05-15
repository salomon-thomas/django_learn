from django.contrib import admin
from django.urls import include,path
from django.conf.urls.static import static
from pages.views import home_view,contact_view,about_view,blog_view

urlpatterns = [
	path('', home_view, name='home'),
	path('home/', home_view, name='home'),
	path('contact/', contact_view, name='contact'),
	path('about/', about_view, name='about'),
	path('blog/', blog_view, name='blog'),
	]