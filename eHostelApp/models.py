from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class MyUser(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE, primary_key = True)
    is_warden = models.BooleanField(default = False)
    year = models.IntegerField(null = True)
    is_registered = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username


class Hostel(models.Model):
    h_name       =  models.CharField(max_length = 20)
    year =  models.IntegerField(default = 1)
    capacity     =  models.IntegerField(default = 100)
    def __str__(self):
	       return self.h_name

class Student(models.Model):
    student_name = models.CharField(max_length = 100)
    reg_no = models.CharField(max_length = 10,primary_key = True,unique = True)
    email = models.EmailField(max_length = 25)
    phone_no = models.CharField(max_length = 10)
    GENDER_CHOICES = [
        ('male','Male'),
        ('female','Female')
    ]
    gender = models.CharField(choices = GENDER_CHOICES,default = 'male',max_length = 6)
 #   date_of_birth = models.DateField()
    guardian_name = models.CharField(max_length = 100)
    guardian_phone = models.CharField(max_length = 10)
    address       =   models.CharField(max_length=100)
    city          =  models.CharField(max_length = 100,null =True)
    state         =  models.CharField(max_length = 100,null =True)
    pincode       =  models.IntegerField()
    branch        =  models.CharField(max_length = 50)
    year          =  models.IntegerField(default = 2)
    mess_fee      =  models.CharField(max_length = 20)
    academic_fee  =  models.CharField(max_length = 20)
 #   no_due_receipt = models.FileField(upload_to = 'receipt/')
    def __str__(self):
	       return self.student_name

class Room(models.Model):
    room_no     =  models.IntegerField()
    student_1   =  models.ForeignKey(Student, on_delete = models.CASCADE)
    student_2   =  models.ForeignKey(Student , on_delete = models.CASCADE,related_name='student')
    h_name      =  models.CharField(max_length=100)
    def __str__(self):
        return str(self.room_no)

#class Swap(models.Model):
#    student_1   =  models.ForeignKey(Student , on_delete = models.CASCADE, related_name='student_1')
#    student_2   =  models.ForeignKey(Student , on_delete = models.CASCADE, related_name='student_2')
#    accept      =  models.BooleanField(default = False)

class Roommate(models.Model):
    student_1   =  models.ForeignKey(Student , on_delete = models.CASCADE, related_name='student1')
    student_2   =  models.ForeignKey(Student , on_delete = models.CASCADE, related_name='student2')
    accept      =  models.BooleanField(default = False)
