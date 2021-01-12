from dappx import views
from django.conf.urls import url


# SET THE NAMESPACE!
app_name = 'dappx'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^update_profile/$', views.update_profile, name='update_profile'),
    url(r'^feedback/$', views.feedback, name='feedback'),
    url('news/', views.news, name='news'),
]
