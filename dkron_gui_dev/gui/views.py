from django.shortcuts import render
#from pydkron import DkronClient



# Create your views here.

def index(request):
    return render(request,"index.html")

def status(request):
    return render(request,"status.html")

def schedule(request):
    Id=request.POST.get("id",False)
    Name=request.POST.get("name",False)
    DispName=request.POST.get("disp",False)
    TimeZone=request.POST.get("tz",False)
    Schedule=request.POST.get("sch",False)  
    Owner=request.POST.get("own",False)
    Owner_email=request.POST.get("ownem",False)
    Parent_job=request.POST.get("pj",False)
    Concur=request.POST.get("conc",False)

def create(request):
    return render(request,"create.html")