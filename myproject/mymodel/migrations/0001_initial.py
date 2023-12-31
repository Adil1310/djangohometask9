# Generated by Django 4.2.1 on 2023-07-27 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myapp', '0002_rename_user_myusers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hometown',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('townname', models.CharField(max_length=50)),
                ('fname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hometown_fname', to='myapp.myusers')),
                ('lname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hometown_lname', to='myapp.myusers')),
            ],
        ),
    ]
