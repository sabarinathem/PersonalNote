from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
class Diary(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    text=RichTextUploadingField(blank=True,null=True)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return 'Diary  {}'.format(self.id)
    class Meta:
        verbose_name_plural='Diary'
        db_table='diary'

