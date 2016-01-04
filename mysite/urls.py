from django.conf.urls import patterns, include, url
from papermanage.views import *        
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^$',index), 
    (r'^home/$',index), 

    (r'^reference/$',reference), 
    (r'^publish/$',publish),

    (r'^search/$',search),
    (r'^searchclass/$',searchclass),
    (r'^pbsearch/$',pbsearch),
    (r'^pbsearchclass/$',pbsearchclass),

    (r'^add/$', add),
    (r'^more/$',more),   
    (r'^delete/$',delete),   
    (r'^modify/$',modify),
    (r'^pbadd/$', pbadd),
    (r'^pbmore/$',pbmore),   
    (r'^pbdelete/$',pbdelete),   
    (r'^pbmodify/$',pbmodify),
    (r'^update/$',update),
    (r'^pbupdate/$',pbupdate),
    (r'^authsearch/$',authsearch),

    (r'^register/$',register),
    (r'^login/$',login),
    (r'^loginout/$',loginout),
    (r'^fix/$',fix),
#    (r'^load/$',load),
#    (r'^pbload/$',pbload),
    (r'^personal/$',personal),
    
    url(r'^admin/', include(admin.site.urls)),

    
)
