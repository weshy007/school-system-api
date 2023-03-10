from django.db import models
from django.contrib import admin
from django.core.validators import MinValueValidator, MaxValueValidator

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


class Unit(models.Model):
    unit_name = models.CharField(max_length=255, null=False)
    unit_code = models.CharField(max_length=255, null=False)


class UnitDetails(models.Model):
    REGISTRATION_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No')
    ]
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='units')
    student = models.ForeignKey('accounts.Student', on_delete=models.CASCADE, related_name='units',
                                null=False)
    registration_status = models.CharField(max_length=255, choices=REGISTRATION_CHOICES, null=False,
                                           default='No')

    def __str__(self):
        return self.unit.unit_name

    @admin.display(ordering='unit__unit_code')
    def unit_code(self):
        return self.unit.unit_code

    @admin.display(ordering='student__registration_number')
    def reg_number(self):
        return self.student.registration_number


class Hostel(models.Model):
    hostel_name = models.CharField(max_length=200)
    capacity = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])

    def __str__(self) -> str:
        return self.hostel_name

    class Meta:
        ordering = ['capacity']


class StudentHostel(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed')
    ]

    student = models.OneToOneField('accounts.Student', on_delete=models.CASCADE, related_name='student', unique=True)
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE, related_name='hostel')
    payment_status = models.CharField(max_length=200, choices=PAYMENT_STATUS_CHOICES, default='Pending')

    def __str__(self) -> str:
        return self.student.registration_number

    @admin.display(ordering='student__registration_number')
    def registration_number(self):
        return self.student.registration_number

    @admin.display(ordering='student__first_name')
    def first_name(self):
        return self.student.user.first_name

    @admin.display(ordering='student__last_name')
    def last_name(self):
        return self.student.user.last_name


class Exam(models.Model):
    EXAM_TYPE_CHOICES = [
        ('SUP', 'SUPPLEMENTARY EXAM'),
        ('SPE', 'SPECIAL EXAM'),
        ('RE', 'RETAKE EXAM'),
        ('MAIN', 'MAIN EXAM')
    ]
    exam_type = models.CharField(max_length=255, choices=EXAM_TYPE_CHOICES)
    date = models.DateTimeField()

    def __str__(self):
        return self.exam_type


class Result(models.Model):
    student = models.ForeignKey('accounts.Student', on_delete=models.CASCADE, related_name='student_result')
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='unit')
    cat = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(30)])
    exam = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(70)])

    @admin.display(ordering='student__registration_number')
    def registration_number(self):
        return self.student.registration_number

    @admin.display(ordering='unit__unit_code')
    def unit_code(self):
        return self.unit.unit_code


class Attendance(models.Model):
    date = models.DateTimeField(auto_now=True)
    student = models.ForeignKey('accounts.Student', on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return self.student.registration_number

    admin.display(ordering='student__registration_number')

    def registration_number(self):
        return self.student.registration_number

    @admin.display(ordering='unit__unit_code')
    def unit_code(self):
        return self.unit.unit_code
