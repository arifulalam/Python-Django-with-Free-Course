# Generated by Django 4.2.16 on 2024-09-12 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PyApp', '0002_testimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Icon', models.CharField(max_length=50)),
                ('Title', models.CharField(max_length=100)),
                ('Description', models.TextField(max_length=500)),
            ],
        ),
    ]
