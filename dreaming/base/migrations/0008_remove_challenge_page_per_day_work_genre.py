"""
Este módulo de migração de remoção de campos do modelo challenge.
"""

from django.db import migrations, models


class Migration(migrations.Migration):
    """classe de migração de remoção de campos do modelo."""

    dependencies = [
        ('base', '0007_alter_review_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challenge',
            name='page_per_day',
        ),
        migrations.AddField(
            model_name='work',
            name='genre',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
