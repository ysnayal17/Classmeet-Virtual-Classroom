from django.conf.urls import url
from lecture import views
from django.urls import path

app_name = 'lecture'

urlpatterns = [
	# /lecture/
    path('', views.index, name='index'),

    # /lecture/id


      # /lecture/id/favorite
    # url(r'^(?P<course_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    path('classroom', views.classroom, name='classroom'),
    path('video', views.video, name='video'),
    path('desktop', views.desktop, name='desktop'),
    path('collaboration', views.collaboration, name='collaboration'),
    path('evaluation', views.evaluation, name='evaluation'),
    path('answer', views.answer, name='answer'),
    path('profile', views.profile, name='profile'),
    path('register', views.register, name='register'),
    path('login_user', views.login_user, name='login_user'),
    path('^logout_user', views.logout_user, name='logout_user'),
    
    path('(?P<course_id>[0-9]+)', views.detail, name='detail'),
    path('(?P<podcast_id>[0-9]+)/favorite', views.favorite, name='favorite'),
    path('podcasts/(?P<filter_by>[a-zA_Z]+)', views.podcasts, name='podcasts'),



    path('create_coursepack', views.create_coursepack, name='create_coursepack'),
    path('(?P<course_id>[0-9]+)/create_podcast', views.create_podcast, name='create_podcast'),
    path('(?P<course_id>[0-9]+)/delete_podcast/(?P<podcast_id>[0-9]+)', views.delete_podcast, name='delete_podcast'),
    path('(?P<course_id>[0-9]+)/favorite_course', views.favorite_course, name='favorite_course'),
    path('(?P<course_id>[0-9]+)/delete_course', views.delete_course, name='delete_course'),

]