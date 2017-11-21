from django.conf.urls import include, url

from core.views import index, article_detail, hello_world


urlpatterns = [
    url(r'^$', index, name='core_index'),
    url(r'^detail/(?P<pk>\d+)/$', article_detail, name='core_article_detail'),
    url(r'^helloworld/$', hello_world, name='core_hello_world'),
]
