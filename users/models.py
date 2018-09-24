from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

    
class Institute(models.Model):
    STATE_CHOICES = (('AP' , 'Andhra Pradesh',),('AR' , 'Arunachal Pradesh',),('AS' , 'Assam',),('BR' , 'Bihar',),('CT' , 'Chhattisgarh',),
    ('GA' , 'Goa',),('GJ' , 'Gujarat',),('HR' , 'Haryana',),('HP' , 'Himachal Pradesh',),('JK' , 'Jammu and Kashmir',),('JH' , 'Jharkhand',),
    ('KA' , 'Karnataka',),('KL' , 'Kerala',),('MP' , 'Madhya Pradesh',),('MH' , 'Maharashtra',),('MN' , 'Manipur',),('ML' , 'Meghalaya',),
    ('MZ' , 'Mizoram',),('NL' , 'Nagaland',),('OR' , 'Odisha',),('PB' , 'Punjab',),('RJ' , 'Rajasthan',),('SK' , 'Sikkim',),
    ('TN' , 'Tamil Nadu',),('TG' , 'Telangana',),('TR' , 'Tripura',),('UT' , 'Uttarakhand',),('UP' , 'Uttar Pradesh',),('WB' , 'West Bengal',))
    institute_name = models.CharField(max_length = 200)
    institute_state = models.CharField(max_length = 50, choices = STATE_CHOICES)

    def __str__(self):
        return self.institute_name

class Course(models.Model):
    course_institute = models.ForeignKey(Institute, on_delete = models.CASCADE, null = True, blank = True)
    course_name = models.CharField(max_length = 100)
    course_capacity = models.IntegerField(null = True, blank = True)

    def __str__(self):
        return (str(self.course_institute) + ', ' + str(self.course_name))

class CustomUser(AbstractUser):
    pass

class Student(models.Model):
    STATE_CHOICES = (('AP' , 'Andhra Pradesh',),('AR' , 'Arunachal Pradesh',),('AS' , 'Assam',),('BR' , 'Bihar',),('CT' , 'Chhattisgarh',),
    ('GA' , 'Goa',),('GJ' , 'Gujarat',),('HR' , 'Haryana',),('HP' , 'Himachal Pradesh',),('JK' , 'Jammu and Kashmir',),('JH' , 'Jharkhand',),
    ('KA' , 'Karnataka',),('KL' , 'Kerala',),('MP' , 'Madhya Pradesh',),('MH' , 'Maharashtra',),('MN' , 'Manipur',),('ML' , 'Meghalaya',),
    ('MZ' , 'Mizoram',),('NL' , 'Nagaland',),('OR' , 'Odisha',),('PB' , 'Punjab',),('RJ' , 'Rajasthan',),('SK' , 'Sikkim',),
    ('TN' , 'Tamil Nadu',),('TG' , 'Telangana',),('TR' , 'Tripura',),('UT' , 'Uttarakhand',),('UP' , 'Uttar Pradesh',),('WB' , 'West Bengal',))
    CATEGORY_CHOICES = (('gen', 'General'), ('obc', 'OBC'), ('sc', 'SC'), ('st', 'ST'))
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, unique = True)
    student_name = models.CharField(max_length = 100)
    #student_email = models.CharField(max_length = 100)
    student_rank = models.IntegerField()
    student_state = models.CharField(max_length = 100, choices = STATE_CHOICES)
    student_category = models.CharField(max_length = 100, choices = CATEGORY_CHOICES)
    course_assigned = models.ForeignKey(Course, related_name='course_allocated', on_delete = models.CASCADE, null = True, blank = True)
    choice_list = models.ManyToManyField(Course)
    #student_id = id*4013 + 16

    def __str__(self):
        return self.student_name