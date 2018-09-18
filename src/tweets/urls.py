from django.conf.urls import url


from .views import (
	TweetListView, TweetDetailView, TweetCreateView
    )
urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', TweetListView.as_view(), name='list'), # /tweet/
    #url(r'^(?P<pk>\d+)/$', tweet_detail_view, name='detail'),
    url(r'^create/$', TweetCreateView.as_view(), name='create'), # /tweet/create/

    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'), # /tweet/1/
    
]