# Generated by Django 4.1.1 on 2022-09-29 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0004_book_purchase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='book',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Purchase',
        ),
    ]
