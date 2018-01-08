from django import forms
from studapp.models import Student, StudMarks

class StudentForm(forms.ModelForm):
    class Meta():
        model = Student
        fields = '__all__'
    first_name = forms.CharField(label='First Name',required=True)
    last_name = forms.CharField(label='Last Name',required=True)
    usn = forms.CharField(label='USN',required=True)
    college = forms.CharField(label='College',required=True)

class MarksForm(forms.ModelForm):
    class Meta():
        model = StudMarks
        fields = '__all__'
    usn = forms.CharField(label='USN',required=True)
    sem_1 = forms.IntegerField(label='Sem 1',required=False)
    sem_2 = forms.IntegerField(label='Sem 2',required=False)
    sem_3 = forms.IntegerField(label='Sem 3',required=False)
    sem_4 = forms.IntegerField(label='Sem 4',required=False)
    sem_5 = forms.IntegerField(label='Sem 5',required=False)
    sem_6 = forms.IntegerField(label='Sem 6',required=False)
    sem_7 = forms.IntegerField(label='Sem 7',required=False)
    sem_8 = forms.IntegerField(label='Sem 8',required=False)
