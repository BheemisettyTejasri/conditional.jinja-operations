from django.shortcuts import render
def conditions(request):
    d={'name':'Tejasri','age':20}
    return render(request,'conditions.html',context=d)

# Create your views here.
