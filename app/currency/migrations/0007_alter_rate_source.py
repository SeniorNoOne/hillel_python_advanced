# Generated by Django 4.1.7 on 2023-03-21 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0006_requestresponselog_alter_contactus_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    to='currency.source'),
        ),
    ]
