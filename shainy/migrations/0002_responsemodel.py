# Generated by Django 3.2.9 on 2022-04-08 10:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shainy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResponseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shainy.postmodel')),
                ('post_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_author_id', to=settings.AUTH_USER_MODEL)),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_user1', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]