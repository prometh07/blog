from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from blog_app.views import EntryDetailView, EntryListView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<day>\d{2})/(?P<month>\d{2})/(?P<year>\d{4})/(?P<slug>[\w\-]+)/$', EntryDetailView.as_view(), name='entry_detail'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^$', EntryListView.as_view(), name='entry_list'),
)
