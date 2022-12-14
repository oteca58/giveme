# Generated by Django 4.1.1 on 2022-09-14 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('client_code', models.CharField(blank='true', max_length=10)),
                ('due_date', models.DateField(auto_now_add=True)),
                ('assignment', models.CharField(choices=[('USER1', 'USER1'), ('USER2', 'USER2')], max_length=10)),
                ('status', models.CharField(choices=[('PROGRESS', 'PROGRESS'), ('COMPLETED', 'COMPLETED')], max_length=10)),
                ('effort', models.IntegerField()),
                ('billable_to', models.CharField(choices=[('test1', 'test1'), ('test2', 'test2')], max_length=10)),
                ('invoiced', models.BooleanField()),
            ],
        ),
    ]
