from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db.models.fields import DateTimeField

# Create your models here.

class Note(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    subject=models.CharField(max_length=100,null=True,blank=True)
    module=models.CharField(max_length=100,null=True,blank=True)
    heading=models.CharField(max_length=100,null=True,blank=True)
    content=RichTextUploadingField(blank=True,null=True)
   
    def __str__(self):
        return self.subject
    class Meta:
        db_table='note'
class Equation(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    subject=models.CharField(max_length=100,null=True,blank=True)
    module=models.CharField(max_length=100,null=True,blank=True)
    heading=models.CharField(max_length=100,null=True,blank=True)
    equation=RichTextUploadingField(blank=True,null=True)
   
    def __str__(self):
        return self.heading
    # class Meta:
    #     db_table='equation'

class TimeTable(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    timetable=RichTextUploadingField(blank=True,null=True)

    class Meta:
        db_table='timetable'

    
class ExamTimeTable(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    date=models.DateTimeField(null=True,blank=True)
    subject=models.CharField(max_length=100)


