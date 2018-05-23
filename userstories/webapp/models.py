from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
import os
import subprocess # PDF File Preview
from django.db.models.signals import post_save
from django.conf import settings

class Anwendungen(models.Model):
    titel = models.CharField(max_length=150)

    class Meta:
        verbose_name = _('Anwendung')
        verbose_name_plural = _('Anwendungen')
        db_table = 'anwendungen'

    def __str__(self):
        return "{}".format(self.titel)

    def get_absolute_url(self):
        return "/webapp/anwendungen/{}/detail".format(self.id)

class Rollen(models.Model):
    anwendung = models.ForeignKey(Anwendungen, blank=True, verbose_name=_('Anwendung'))
    rolle = models.CharField(max_length=250, verbose_name=_('Rolle'))
    beschreibung = models.TextField(blank=True, verbose_name=_('Beschreibung'))

    class Meta:
        verbose_name = _('Rolle')
        verbose_name_plural = _('Rollen')
        db_table = 'rollen'

    def __str__(self):
        return "{}".format(self.rolle)

    def get_absolute_url(self):
        return "/webapp/rollen/{}/detail".format(self.id)

class Schlagworte(models.Model):
    schlagwort = models.CharField(max_length=250)
    class Meta:
        verbose_name = _('Schlagwort')
        verbose_name_plural = _('Schlagworte')
        db_table = 'schlagworte'

    def __str__(self):
        return "{}".format(self.schlagwort)

    def get_absolute_url(self):
        return "/webapp/schlagworte/{}/detail".format(self.id)

class Glossareintraege(models.Model):
    titel = models.CharField(max_length=250)
    beschreibung = models.TextField(blank=True, verbose_name=_('Beschreibung'))

    class Meta:
        verbose_name = _('Glossareintrag')
        verbose_name_plural = _('Glossareinträge')
        db_table = 'glossarentraege'

    def __str__(self):
        return "{}".format(self.titel)

    def get_absolute_url(self):
        return "/webapp/glossarentraege/{}/detail".format(self.id)

class Userstories(models.Model):
    anwendung = models.ForeignKey(Anwendungen, blank=True, verbose_name=_('Anwendung'))
    titel = models.CharField(max_length=150)
    rolle = models.ForeignKey(Rollen, blank=True, verbose_name=_('Als...'))
    text_als = models.TextField(verbose_name=_('Möchte ich...'))
    text_damit = models.TextField(verbose_name=_('Damit ich...'))

    schlagworte = models.ManyToManyField(Schlagworte, blank=True, verbose_name=_('Schlagworte'))
    erfuellungsgrad = models.PositiveSmallIntegerField(verbose_name=_('Erfüllungsgrad'))

    class Meta:
        verbose_name = _('Userstory')
        verbose_name_plural = _('Userstories')
        db_table = 'userstories'

    def __str__(self):
        return "{}".format(self.titel)

    def color(self):
        if self.erfuellungsgrad == 100:
            return "green darken-1"        
        if self.erfuellungsgrad > 80:
            return "green lighten-4"
        elif self.erfuellungsgrad < 30:
            return "deep-orange darken-1"
        else:
            return "orange lighten-3"

    def get_absolute_url(self):
        return "/webapp/userstories/{}/detail".format(self.id)


class Notizen(models.Model):
    text = models.TextField()

    datum = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User)

    userstory = models.ForeignKey(Userstories, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Notiz')
        verbose_name_plural = _('Notizen')
        db_table = 'notizen'

    def __str__(self):
        return "{}".format(self.text[:20])

    def get_title(self):
        return self.text[:30]

    def get_absolute_url(self):
        return "/webapp/notizen/{}/detail".format(self.id)
