from django.apps import AppConfig
from .Gpt_api.client import GPTModel
"""
Configuração do sistema.
"""


class BaseConfig(AppConfig):
    """configuração do base do sistema."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'

    def ready(self):
        from . import signals

        self.gpt_model_instance = GPTModel()
