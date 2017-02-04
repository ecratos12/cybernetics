# -*- coding: utf-8 -*
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=250)
    short_name = models.CharField(max_length=250)
    chef = models.ForeignKey('Professor', null=True, blank=True,related_name='chef')
    short_info = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=150)
    adress = models.CharField(max_length=150)
    domen = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    specialization = models.ForeignKey('Specialization', null=True, blank=True)
    reserch = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Professor(models.Model):
    name = models.CharField(max_length=250)
    department = models.ForeignKey(Department, null=True, blank=True)
    position = models.CharField(max_length=250)
    interest = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=150)
    adress = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    domen = models.CharField(max_length=150)
    detail = models.TextField(null=True, blank=True)
    photo = models.ImageField()

    def __str__(self):
        return self.name

class Administration(models.Model):
    name = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    phone = models.CharField(max_length=150)
    adress = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    domen = models.CharField(max_length=150)
    photo = models.ImageField()

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField(null=True, blank=True)
    pub_date = models.DateField()
    photo = models.ImageField(null=True, upload_to="img")
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class CustomUser(User):
    department = models.ForeignKey(Department, null=True, blank=True)

    def cheak_permision(self, department):
        return self.department == department


class Photo(models.Model):
    alt = models.CharField(max_length=250)
    photo = models.ImageField()
    in_gallery = models.BooleanField(default=False)
    def __str__ (self):
        return self.alt

class Article(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField(null=True, blank=True)
    image = models.ManyToManyField(Photo, null=True, blank=True)
    slug = models.CharField(max_length=250)
    parent = models.ForeignKey('self', null=True, blank=True)

    nav_bar = models.CharField(max_length=250, null=True, blank=True)

    def __str__ (self):
        return self.title

class Person(models.Model):
    name = models.CharField(max_length=250)
    text = models.TextField()
    photo = models.ImageField(upload_to='media')

    def __str__ (self):
        return self.name

class OKR(models.Model):
    name = models.CharField(max_length=250)
    text = models.TextField(null=True, blank=True)
    statistic_need = models.BooleanField(default=False)
    def __str__ (self):
        return self.name    

    def get_specialization(self):
        return Specialization.objects.filter(okr=self, parent=None)

class Specialization(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    okr = models.ForeignKey(OKR, null=True, blank=True)  
    day_student = models.IntegerField(null=True, blank=True)
    night_student = models.IntegerField(null=True, blank=True)

    parent = models.ForeignKey('self', null=True, blank=True)    
    
    def __str__(self):
        return self.name

    def get_children(self):
        return Specialization.objects.filter(parent=self)

class Year(models.Model):
    number = models.CharField(max_length=250)
    value = models.DecimalField(null=True, blank=True, decimal_places=5, max_digits=5)
    okr = models.ForeignKey(OKR, null=True, blank=True)
    def __str__(self):
        return self.number

class Statistic(models.Model):
    name = models.CharField(max_length=250)
    year = models.ManyToManyField("Year", null=True, blank=True)
    okr = models.ForeignKey(OKR, null=True, blank=True)

    def __str__(self):
        return self.name

class Grup(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Schedule_block(models.Model):
    CHECKOUT = (
        (1, 'Понеділок'),
        (2, 'Вівторок'),
        (3, 'Середа'),
        (4, 'Четвер'),
        (5, "П'ятниця"),
    )
    date = models.IntegerField(choices=CHECKOUT, null=True, blank=True)
    grup  = models.ForeignKey(Grup, null=True, blank=True)
    up_week = models.BooleanField(default=False)

    def get_date(self):
        return self.CHECKOUT[self.date-1][1]

    def get_para(self):
        return Pare.objects.filter(block=self)

    def __str__(self):
        return self.grup.name + '  ' + self.CHECKOUT[self.date-1][1] 

class Pare(models.Model):
    number = models.IntegerField(default=1)
    name = models.CharField(max_length=250)
    professor = models.CharField(max_length=250)
    adress = models.CharField(max_length=250)
    block  = models.ForeignKey(Schedule_block, null=True, blank=True)


class Contacts(models.Model):
    desc = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)

class Student_action(models.Model):
    name = models.CharField(max_length=250)
    text = models.TextField()
    photo = models.ImageField(upload_to='media')

class Study_info(models.Model):
    first_start = models.DateField()
    first_end = models.DateField()
    second_start = models.DateField()
    second_end = models.DateField()


class Libery(models.Model):
    slug = models.CharField(max_length=250)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def get_res(self):
        return Publication.objects.filter(libery=self)
        
class Publication(models.Model):
    libery = models.ForeignKey(Libery, null=True, blank=True)
    desc  = models.TextField()

    def __str__(self):
        return self.desc

class Olimp(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def get_res(self):
        return Olimp_result.objects.filter(olimp=self)

class Olimp_result(models.Model):
    olimp = models.ForeignKey(Olimp, null=True, blank=True)
    date = models.CharField(max_length=250)
    result = models.TextField()
    plase = models.CharField(max_length=250)



    def __str__(self):
        return self.desc
