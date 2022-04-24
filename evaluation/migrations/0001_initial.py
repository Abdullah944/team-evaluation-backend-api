# Generated by Django 4.0.4 on 2022-04-24 03:30

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0005_project_criteria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('isLocked', models.BooleanField(default=False)),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='linkId', to='project.project')),
            ],
        ),
    ]
