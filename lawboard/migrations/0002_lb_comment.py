# Generated by Django 2.2.7 on 2020-01-14 12:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lawboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LB_comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', models.TextField()),
                ('comment_writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('lbcomment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lawboard.LawBoard')),
            ],
        ),
    ]
