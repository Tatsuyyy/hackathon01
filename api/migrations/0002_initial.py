# Generated by Django 3.2.3 on 2022-04-22 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ('api', '0001_initial'),
    ]

    operations = [
    # echonest_artist UNKNOWN DATA
    migrations.RunSQL(
    """
    INSERT INTO weekdays(name) VALUES('月');
    INSERT INTO weekdays(name) VALUES('火');
    INSERT INTO weekdays(name) VALUES('水');
    INSERT INTO weekdays(name) VALUES('木');
    INSERT INTO weekdays(name) VALUES('金');
    INSERT INTO weekdays(name) VALUES('土');
    INSERT INTO weekdays(name) VALUES('日');
    """),
    ]