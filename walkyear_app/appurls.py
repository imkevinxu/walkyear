from coffin.conf.urls.defaults import *
from coffin.shortcuts import redirect
from django.contrib.auth.views import logout

from walkyear.jinja2 import login

def smartlogin(request, **kwargs):
    if request.user.is_authenticated():
        return redirect('index')
    else:
        return login(request, **kwargs)

urlpatterns = patterns('walkyear_app.views',
    url(r'^$', 'index', name='index'),
    url(r'^login/$', smartlogin, kwargs=dict(template_name='login.html'), name='login'),
    url(r'^logout/$', logout, kwargs=dict(next_page='/'), name='logout'),

)
