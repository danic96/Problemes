# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('isobres', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.TextField(max_length=50)),
                ('web', models.TextField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='sobre',
            name='politic',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sobre',
            name='empresa',
            field=models.ForeignKey(default=1, to='isobres.Empresa'),
            preserve_default=False,
        ),
    ]
