# Generated by Django 4.1.1 on 2022-09-28 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_tpc_h_query'),
    ]

    operations = [
        migrations.CreateModel(
            name='Side_Var',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seqnum', models.IntegerField(verbose_name='seqnum')),
                ('name', models.CharField(max_length=100, verbose_name='fullname')),
            ],
        ),
    ]
