from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, RegexValidator, MaxValueValidator
from django.db import models


def validate_img(upload):
    ext = upload.name[-4:]
    if not ext in ['.jpg', ".png"]:
        raise ValidationError(u'File type not supported!')
    if upload.size > 1024 * 1024 * 2:
        raise ValidationError(u'File too big!')

class Branch(models.Model):
    name=models.CharField(max_length=100)
    hod=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Notice(models.Model):
    subject= models.CharField(max_length=100)
    message= models.TextField()
    attach1=models.FileField(upload_to="docs//",null=True, blank=True)
    crdate=models.DateTimeField(auto_now_add=True)
    branch=models.ForeignKey(Branch,on_delete=models.CASCADE)
    sem=models.IntegerField(default=1,choices=((1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8)))
    def __str__(self):
        return self.subject

class Student(models.Model):
    name = models.CharField(max_length=100)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)
    sem = models.IntegerField(default=1,  choices=((1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (7,7), (8,8)))
    rn = models.IntegerField(validators=[MinValueValidator(1)], null=True)
    phone_no = models.CharField(validators=[RegexValidator("^0?[6-9]{1}\d{9}$")]  ,max_length=20,null=True)
    marks_10=models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    marks_12=models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    marks_aggr=models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    email=models.EmailField()
    skills=models.TextField(null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Assignment(models.Model):
    subject = models.CharField(max_length=100)
    message = models.TextField()
    attach1 = models.FileField(upload_to ="docs//" ,null=True, blank=True)
    crdate = models.DateTimeField(auto_now_add = True)
    duedate = models.DateTimeField()
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    sem = models.IntegerField(default=1,  choices=((1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (7,7), (8,8)))
    def __str__(self):
        return self.subject


class Results(models.Model):
    subject = models.CharField(max_length=100)
    marks = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    comment = models.TextField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    def __str__(self):
        return self.student.name + " :: " + self.subject + " :: " + str(self.marks)


class Attendance(models.Model):
    subject = models.CharField(max_length=100)
    total_classes = models.FloatField(default=0, validators=[MinValueValidator(0)])
    attend = models.FloatField(default=0, validators=[MinValueValidator(0)])
    comment = models.TextField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    def __str__(self):
        return self.student.name + " :: " + str(self.total_classes) + " :: " + str(self.attend)

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobno = models.IntegerField()
    subject = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


