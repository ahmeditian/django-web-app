from dappx import views
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('social_django.urls', namespace='social')),
    url(r'^$', views.index, name='index'),
    url(r'^special/', views.special, name='special'),
    url(r'^dappx/', include('dappx.urls')),
    url(r'^logout/', views.user_logout, name='logout'),
]

handler404 = 'dappx.views.handler404'
handler500 = 'dappx.views.handler500'