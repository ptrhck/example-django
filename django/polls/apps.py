from django.apps import AppConfig
import os
from django.conf import settings



class PollsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
    path = os.path.join(settings.BASE_DIR, 'polls')