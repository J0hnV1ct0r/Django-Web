from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Challenge
from .Gpt_api.client import get_challenge_ai_description

@receiver(pre_save, sender=Challenge)
def challenge_pre_save(sender, instance, **kwargs):
    if not instance.description:
        ai_description = get_challenge_ai_description(instance.title,instance.book.title)
        instance.description = ai_description