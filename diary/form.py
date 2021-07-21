from django.forms import ModelForm, fields
from diary.models import Diary
class DiaryForm(ModelForm):
    class Meta:
        model=Diary
        fields=('id','text')

 