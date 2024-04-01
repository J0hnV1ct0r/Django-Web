"""
Este módulo de migração de alteração work.
"""
from django.db import migrations, models


class Migration(migrations.Migration):
    """classe de migração de alteração do campo image."""

    dependencies = [
        ('base', '0003_rename_page_nuber_work_page_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
