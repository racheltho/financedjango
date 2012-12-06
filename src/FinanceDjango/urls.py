from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('FinanceDjango.views',
    # Examples:
    (r'^time/plus/(\d{1,2})/$', 'hours_ahead'),
    ('^$', 'hello'),
    ('^time/$', 'current_datetime'),
    ('^meta/$', 'display_meta'),
    ('^contact/$', 'contact'),      
#    (r'^search-form/$', search_form),
    (r'^search/$', 'search'),
    (r'^booked/$', 'bookedRev'),
    (r'^actual/$', 'actualRev'),    
    (r'^add_poll/$', 'add_poll'),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
#    (r'^', include('FinanceDjango.urls')),
)