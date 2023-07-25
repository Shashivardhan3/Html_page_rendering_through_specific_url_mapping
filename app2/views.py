from django.shortcuts import render

# Create your views here.


def fun3(request):
    return render(request,'telugu.html')

def fun4(request):
    return render(request,'kurnool.html')