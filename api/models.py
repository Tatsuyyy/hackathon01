from django.db import models

class Arrangements(models.Model):
    task = models.ForeignKey('Tasks', models.DO_NOTHING)
    weekday = models.ForeignKey('Weekdays', models.DO_NOTHING)
    required_per_day = models.SmallIntegerField(blank=True, null=True)
    done_per_day = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'arrangements'


class Students(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey('Teachers', models.DO_NOTHING)

    class Meta:
        db_table = 'students'


class Tasks(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    required_time = models.SmallIntegerField()
    is_done = models.BooleanField()
    student = models.ForeignKey(Students, models.DO_NOTHING)

    class Meta:
        db_table = 'tasks'


class Teachers(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'teachers'


class Weekdays(models.Model):
    name = models.CharField(max_length=1)

    class Meta:
        db_table = 'weekdays'
