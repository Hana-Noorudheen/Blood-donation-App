# Generated by Django 3.2.3 on 2021-10-02 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor_details', '0003_remove_donor_details_userid'),
    ]

    operations = [
        migrations.DeleteModel(
            name='userdetails',
        ),
        migrations.AlterField(
            model_name='donor_details',
            name='Phone',
            field=models.CharField(max_length=13),
        ),
    ]