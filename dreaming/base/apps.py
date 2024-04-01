"""
Configuração do sistema.
"""
from django.apps import AppConfig


class BaseConfig(AppConfig):
    """configuração do base do sistema."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'
