from ckeditor import fields
from django import forms
from django import forms
from django.forms import widgets
from book.models import Note,Equation,TimeTable
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NoteForm(forms.ModelForm):
    class Meta:
        model=Note
        fields=['subject','module','heading','content']
        widgets={
            'subject':widgets.TextInput(attrs={'placeholder':'Subject'}),
            'module':widgets.TextInput(attrs={'placeholder':'Module'}),
            'heading':widgets.TextInput(attrs={'placeholder':'Heading'}),
            'content':widgets.TextInput(attrs={'placeholder':'Content'})
        }
class EquationForm(forms.ModelForm):
    class Meta:
        model=Equation
        fields=['subject','module','heading','equation']
        widgets={
            'subject':widgets.TextInput(attrs={'placeholder':'Subject'}),
            'module':widgets.TextInput(attrs={'placeholder':'Module'}),
            'heading':widgets.TextInput(attrs={'placeholder':'Heading'}),
            'equation':widgets.TextInput(attrs={'placeholder':'Equation'})
        }




class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class TimeTableForm(forms.ModelForm):
    class Meta:
        model=TimeTable
        fields=['timetable']
   
        