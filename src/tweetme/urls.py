"""tweetme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path 

from django.conf import settings
from django.conf.urls.static import static

from hashtags.views import HashTagView
from tweets.views import TweetListView
from .views import home 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TweetListView.as_view(), name='home'),
    re_path(r'^tags/(?P<hashtag>.*)/$', HashTagView.as_view(), name='hashtag'),
    
    
    path('tweets/',  include(('tweets.urls', 'tweets'), namespace='tweet')),
    path('api/tweets/',  include(('tweets.api.urls', 'tweets-api'), namespace='tweets-api')),
    path('', include(('accounts.urls', 'accounts'), namespace='profiles')),
]

if settings.DEBUG:

       urlpatterns += (static(settings.STATIC_URL, document_root = settings.STATIC_ROOT))
