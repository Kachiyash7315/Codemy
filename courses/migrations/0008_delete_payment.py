# Generated by Django 4.0.5 on 2022-07-15 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_usercourse_payment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
