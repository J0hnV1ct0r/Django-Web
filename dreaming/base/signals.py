from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.apps import apps
from .models import Challenge


@receiver(pre_save, sender=Challenge)
def challenge_pre_save(sender, instance, **kwargs):
    if not instance.description:
        gpt_model = apps.get_app_config('base').gpt_model_instance
        prompt = f'''
            crie um desafio litearrio para a obra {instance.book.title} em apenas 50 caracteres. O desafio tem que durar no maximo 30 dias e 
            tem o objetivo{instance.title}.
            '''
        max_tokens=130
        ai_description = gpt_model.get_text_ia(prompt,max_tokens)
        instance.description = ai_description