"""
Este módulo de migração alteração no modelo de Review.
"""

from django.db import migrations


class Migration(migrations.Migration):
    """classe de migração de alteração no modelo de Review."""

    dependencies = [
        ('base', '0004_alter_work_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='description',
            new_name='review',
        ),
    ]
