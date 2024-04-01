"""
Este módulo de migração alteração no modelo de Work.
"""
from django.db import migrations, models


class Migration(migrations.Migration):
    """classe de migração de alteração do campo image."""

    dependencies = [
        ('base', '0008_remove_challenge_page_per_day_work_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='imagens/'),
        ),
    ]
