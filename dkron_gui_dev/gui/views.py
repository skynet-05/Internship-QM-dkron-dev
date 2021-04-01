from django.shortcuts import render
#from pydkron import DkronClient


# Create your views here.

def index(request):
    return render(request,"index.html")

def status(request):
    return render(request,"status.html")
def schedule(request):
    data={
        "jname":request.POST.get("jobname", False),
        "fname":request.POST.get("disname", False),
        "sname":request.POST.get("schedulefor", False),
        "rname":request.POST.get("retries", False),
        "yname":request.POST.get("year", False),
        "mname":request.POST.get("month", False),
        "wname":request.POST.get("week", False),
        "dname":request.POST.get("day", False),
        "hname":request.POST.get("hour", False),
        "miname":request.POST.get("minute", False),
    }
    return render(request,"dummy.html", data)
def create(request):
    return render(request,"create.html")