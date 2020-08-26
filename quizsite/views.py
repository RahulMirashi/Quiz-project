from django.shortcuts import render
from .models import Exam
def examonline(request):
    
    results=Exam.objects.all()
    print(results)
    print(type(results))
    context = {"Exam":results}
    return render(request,'index.html',context=context)
    