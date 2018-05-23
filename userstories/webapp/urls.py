from django.conf.urls import url, include
from django.views import generic

from . import views

urlpatterns = [
    url('^$', generic.RedirectView.as_view(
         url='./userstories/'), name="index"),
    url('^anwendungen/', include(views.AnwendungenViewSet().urls)),
    url('^userstories/', include(views.UserstoriesViewSet().urls)),
    url('^rollen/', include(views.RollenViewSet().urls)),
    url('^schlagworte/', include(views.SchlagworteViewSet().urls)),
    url('^glossarentraege/', include(views.GlossareintraegeViewSet().urls)),
    url('^notizen/', include(views.NotizenViewSet().urls)),
]
