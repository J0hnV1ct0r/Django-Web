"""
Este módulo de migração alteração no modelo de work.
"""

from django.db import migrations


class Migration(migrations.Migration):
    """classe de migração alteração no modelo de work."""

    dependencies = [
        ('base', '0002_challenge_page_per_day_work_page_nuber'),
    ]

    operations = [
        migrations.RenameField(
            model_name='work',
            old_name='page_nuber',
            new_name='page_number',
        ),
    ]
