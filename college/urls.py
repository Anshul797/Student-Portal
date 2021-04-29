from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.views.generic.base import RedirectView
from college import views

urlpatterns=[
    url('^$', views.home, name='home'),
    url('^contact$', views.contact,name='contact'),
    url('^student$', views.MyList.as_view(), name='student'),
    url('^notice$', views.NoticeList.as_view(), name='nlist'),
    url('^notice/(?P<pk>[0-9]+)$', views.NoticeDetail.as_view(), name='ndet'),
    url('^assignment/$', views.AssignmentList.as_view(), name = 'alist'),
    url('^assignment/(?P<pk>[0-9]+)$', views.AssignmentDetail.as_view(), name = 'adet'),
    url('^results/$', views.ResultsList.as_view(), name = 'rlist'),
    url('^results/(?P<pk>[0-9]+)$', views.ResultsDetail.as_view(), name = 'rdet'),
    url('^attendance/$', views.AttendanceList.as_view(), name = 'atlist'),
    url('^attendance/(?P<pk>[0-9]+)$', views.AttendanceDetail.as_view(), name = 'atdet'),
    url(r'^student/edit/(?P<pk>\d+)$', views.StudentUpdate.as_view(), name='student_edit'),
    url('^chkstu/', views.chkstu, name="chkstu"),
    url('^feedback/$', views.FeedCreate.as_view(),name='feed'),
    url('^submit_feedback/', views.SubmitFeedback, name='subFeed')
]