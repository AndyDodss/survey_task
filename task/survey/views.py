from django.shortcuts import render,redirect
from . models import Ask,Ans
from django.contrib.auth.models import User
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

def test(request):
    questions=Ask.objects.all()
    Answers=  Ans.objects.all()
    
    context = {
            'questions' : questions ,
            'answers' : Answers
          }
    
    return render(request ,'test.html',context)


def testall(request):
    
    Answers=  Ans.objects.all()
    
    context = {
            
            'answers' : Answers
          }
    
    return render(request,"testall.html",context)





def ans(request):
    questions=Ask.objects.all()
    answers=  Ans.objects.all()
    
    context = {
            'questions' : questions ,
            'answers' : answers
          }
    return render(request,'Ans.html' ,context)


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


def answer(request):
    rate = int(request.POST.get('rate'))
    user_id=int(request.POST.get('user_id'))
    user = User.objects.get(pk=user_id)
    question_id= int(request.POST.get('question_id'))
    question=Ask.objects.get(pk=question_id)
    done=True
    user_answer=Ans(user_id=user,done=done,rate=rate,Question_id=question)
    user_answer.save()    
    return redirect('ans')
