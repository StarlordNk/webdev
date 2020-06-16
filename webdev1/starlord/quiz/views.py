from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Question
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
def getQuestion(id):
    cur=Question.objects.get(pk=id)
    id2=cur.next
    try:
        next=Question.objects.get(pk=id2)
    except:
        next=None
    return cur,next

def connector():
    q=Question.objects.all()
    temp=0
    for i in q:
        i.next=temp
        temp=i.id
        i.save()
    return temp
    
        
def checkAnswer(id,choice):
    score=0
    q,qu=getQuestion(id)
    if choice == q.option1  and q.op1:
        score +=1
    elif choice==q.option2 and q.op2:
        score +=1
    elif choice==q.option3 and q.op3:
        score +=1
    elif choice==q.option4 and q.op4:
        score +=1
    return score,qu

def quiz(request):
    if request.method=='POST':
        id = int(request.POST['id'])
        choice = request.POST['choice']
        score,ques=checkAnswer(id,choice) 
        if ques != None:
            return render(request , 'quiz.html' ,{'ques':ques})
        else:
            messages.info(request, 'Score is',score)
            return render(request , 'result.htm', {'score' :score} )
    else:
        if request.user.is_active: 
            id=connector()  
            ques=Question.objects.get(pk=id)
            return render(request , 'quiz.html' ,{'ques': ques })
        else:
            messages.info(request,'Login First ')
            return render(request, 'login.html')

