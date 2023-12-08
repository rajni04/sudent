# Generated by Django 3.2.23 on 2023-12-08 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_auto_20231208_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='profile_image',
            field=models.ImageField(default=1, upload_to='student/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='stdclass',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='student.classdetail'),
        ),
    ]
