# Generated by Django 5.0 on 2023-12-28 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_students_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='grade',
            field=models.CharField(max_length=1),
        ),
    ]
