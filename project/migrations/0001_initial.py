# Generated by Django 4.0.4 on 2022-04-25 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('semester', '0001_initial'),
        ('criteria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('weight', models.CharField(max_length=255)),
                ('criteria', models.ManyToManyField(related_name='criteria', to='criteria.criteria')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='semester.semester')),
            ],
        ),
    ]
