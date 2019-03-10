from django.shortcuts import render,redirect
from . models import Ask

# Create your views here.
def index(request):
    questions = Ask.objects.all()
    context = {
        'questions': questions
    }
    return render(request,'index.html' , context)


def create(request):
    print(request.POST)
    title = request.GET['name']
    content = request.GET['content']
    question_details = Ask(name=title, content=content)
    question_details.save()
    return redirect('/')

def add_question(request):
	return render(request,'add_question.html')


def delete(request, id):
    questions = Ask.objects.get(pk=id)
    questions.delete()
    return redirect('/')

def ans(request):
	questions = Ask.objects.all()
	context = {
		'questions' : questions
	}
	return render(request,'Ans.html' ,context)