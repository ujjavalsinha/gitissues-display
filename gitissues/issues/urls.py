from django.conf.urls import url
from issues import views
from django.contrib.auth.views import login,logout
from django.urls import reverse_lazy

app_name = 'issues'

urlpatterns=[

    url(r'^(?P<id>\d+)/$',views.detail, name='issue_detail'),
    url('login/', login,{'template_name':'issues/login.html'},name='login'),
    url('logout/',logout,{'next_page':reverse_lazy('issues_list')},name='logout'),
]
