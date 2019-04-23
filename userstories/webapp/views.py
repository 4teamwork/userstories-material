import json
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from django.utils.translation import ugettext, ugettext_lazy as _
from django.views import generic

from material.frontend.views import ModelViewSet, ListModelView
from material import Layout, Row, Fieldset

from . import models # forms

class UserstoriesViewSet(ModelViewSet):
    model = models.Userstories
    list_display = ('titel','rolle','erfuellungsgrad')
    list_filter = ['titel', 'rolle', ]
    search_fields = ['titel', 'rolle',]

class RollenViewSet(ModelViewSet):
    model = models.Rollen
    list_display = ('rolle',)

class SchlagworteViewSet(ModelViewSet):
    model = models.Schlagworte
    list_display = ('schlagwort',)

class GlossareintraegeViewSet(ModelViewSet):
    model = models.Glossareintraege
    list_display = ('titel', 'beschreibung')

class AnwendungenViewSet(ModelViewSet):
    model = models.Anwendungen
    list_display = ('titel', 'beschreibung')

class NotizenViewSet(ModelViewSet):
    model = models.Notizen
    list_display = ('text','user','datum')
