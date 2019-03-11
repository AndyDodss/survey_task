from django.shortcuts import render,redirect
from . models import Ask
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth import login,authenticate
# Create your views here.
def index(request):
    questions = Ask.objects.all()
    context = {
        'questions': questions
    }
    return render(request,'index.html' , context)

def login_check(request):
    if request.user.is_superuser == 0 :  
      #  return HttpResponse(request.user.id)
         return redirect('ans')


    else:
         #return HttpResponse("admin page") 
          return index(request)
      


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username , password = password)
            login(request , user)
            return redirect('ans')
    else :
         form = UserCreationForm()    

    context = {'form' : form}
    return render(request,'registration/registration.html',context)

def create(request):
    print(request.POST)
    title = request.GET['name']
    content = request.GET['content']
    question_details = Ask(name=title, content=content)
    question_details.save()
    return redirect('/myadmin')

def add_question(request):
	return render(request,'add_question.html')


def delete(request, id):
    questions = Ask.objects.get(pk=id)
    questions.delete()
    return redirect('/myadmin')

def ans(request):
	questions = Ask.objects.all()
	context = {
		'questions' : questions
	}
	return render(request,'Ans.html' ,context)