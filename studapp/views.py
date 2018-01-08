from django.shortcuts import render,render_to_response
from studapp import forms
from studapp.forms import StudentForm, MarksForm
from studapp.models import Student, StudMarks
# Create your views here.

def index(request):
    return render(request,'studapp/index.html')

def sform(request):
    form = forms.StudentForm()

    if request.method == 'GET':
        return render(request,'studapp/form.html',{'form':form})

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return render(request,'studapp/index.html')

def sformtwo(request):
    formtwo = forms.MarksForm()

    if request.method == 'GET':
        return render(request,'studapp/formtwo.html',{'formtwo':formtwo})

    if request.method == 'POST':
        formtwo = MarksForm(request.POST)
        if formtwo.is_valid():
            formtwo.save(commit=True)
        return render(request,'studapp/index.html')

def student_details(request):
    s_detail = Student.objects.all()
    return render_to_response('studapp/details.html',{'s_detail':s_detail})

def stud_search(request):

    if request.method =='GET':
        return render(request,'studapp/search.html')

    if request.method == 'POST':
        roll = request.POST.get('usn')

        s_det = Student.objects.get(usn=roll)
        s_marks = StudMarks.objects.get(usn=roll)

        avg_dict= {}
        avg=0.0

        avg=((s_marks.sem_1+s_marks.sem_2+s_marks.sem_3+s_marks.sem_4+s_marks.sem_5+s_marks.sem_6+s_marks.sem_7+s_marks.sem_8)/8)
        avg_dict = (dict({roll:avg}))

        return render(request,'studapp/show_stud.html',{'s_det':s_det,'s_marks':s_marks,'avg_dict':avg_dict})
