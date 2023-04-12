from django.db import models
from datetime import date, timedelta


class AbstractPerson(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=13)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.phone_number:
            phone_list = list(self.phone_number)
            phone_list.pop(0)
            phone = ''.join(phone_list)
            self.phone_number = f'+996{phone}'
        super().save(*args, **kwargs)


class Language(models.Model):
    name = models.CharField(max_length=20)
    month_to_learn = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if 'java script' in self.name:
            self.name = 'Java Script'
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} - {self.month_to_learn}'


class Student(AbstractPerson):
    work_study_place = models.CharField(max_length=20, null=True, blank=True)
    has_own_notebook = models.BooleanField()
    preferred_os = models.CharField(choices=(
        ('windows', 'Windows'),
        ('mac', 'MacOS'),
        ('linux', 'Linux')
    ))

    def __str__(self):
        return f'{self.work_study_place} - {self.has_own_notebook} - {self.preferred_os}'


class Mentor(AbstractPerson):
    main_work = models.CharField(max_length=20, null=True, blank=True)
    experience = models.DateField()
    student = models.ManyToManyField(Student, through='Course')

    def __str__(self):
        return f'{self.main_work} - {self.experience} - {self.student}'


class Course(models.Model):
    name = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    date_started = models.DateField()
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def get_end_date(self):
        one_month = 30
        if 'UX-UI' in self.language:
            one_month = 60
            date_start = timedelta(self.date_started)
            date_end = timedelta(days=one_month)
            result = date_start - date_end
            return result
        else:
            one_month = 180
            date_start = timedelta(self.date_started)
            date_end = timedelta(days=one_month)
            result = date_start + date_end
            return result

    def __str__(self):
        return f'{self.name} - {self.language} - {self.date_started} - {self.mentor} - {self.student}'



