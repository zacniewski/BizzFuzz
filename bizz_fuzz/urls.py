from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import HomePageView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bizz_fuzz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^my-users/', include('bizz_fuzz_app.urls', namespace='bizz_fuzz_app', app_name='bizz_fuzz_app')),
    url(r'^$', HomePageView.as_view()),
)
