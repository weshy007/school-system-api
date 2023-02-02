from django.db import models
from django.contrib import admin

from accounts.models import *


# Create your models here.
class School(models.Model):
    school_name = models.CharField(max_length=255)

    def __str__(self):
        return self.school_name


class Department(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='departments')
    department_name = models.CharField(max_length=255)

    def __str__(self):
        return self.department_name

    @admin.display(ordering='school__school_name')
    def school_name(self):
        return self.school.school_name

