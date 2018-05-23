from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

from material.frontend.apps import ModuleMixin

class WebappConfig  (ModuleMixin, AppConfig):
    name = 'userstories.webapp'
    icon = '<i class="material-icons">people</i>'
    verbose_name = _('Userstories Protoyp')
    
