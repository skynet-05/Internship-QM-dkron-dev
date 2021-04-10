from django.shortcuts import render
from pydkron.client import DkronClient


# Create your views here.

def index(request):
    return render(request,"index.html")

def status(request):
    return render(request,"status.html")

def schedule(request):
    dc=DkronClient(hosts=["192.168.0.109:8080","192.168.0.110:8080",])
    if request.POST.get("pre",False)=='1':
        schedule="@at "+request.POST.get("Date",False)+"T"+request.POST.get("Time",False)+":00+05:30"
    elif request.POST.get("pre",False)=='2':
        schedule="@every "+request.POST.get('mins',False)+"m"
    elif request.POST.get("pre",False)=='3':
        schedule="0 "+request.POST.get("Time",False)[3:5]+" "+request.POST.get("Time",False)[0:2]+"/"+request.POST.get("hours",False)+" * * *"
    elif request.POST.get("pre",False)=='4':
        schedule="0 "+request.POST.get("Time",False)[3:5]+" "+request.POST.get("Time",False)[0:2]+" * * *"
    elif request.POST.get("pre",False)=='5':
        schedule="0 "+request.POST.get("Time",False)[3:5]+" "+request.POST.get("Time",False)[0:2]+" * * "+request.POST.get("day_week",False)
    elif request.POST.get("pre",False)=='6':
        schedule="0 "+request.POST.get("Time",False)[3:5]+" "+request.POST.get("Time",False)[0:2]+" "+request.POST.get("day_month",False)+" * *"
    jd={
        "name":request.POST.get('jobname',False),
        "schedule":schedule,
        "tags":{
            "role":"dkron:1",
        },
        "executor":"shell",
        "executor_config":{
            "command":"python3 send_mail.py"
        }
    }
    job=dc.create_job(jd)
    job.save()
    return render(request,"dummy.html", jd)

def create(request):
    return render(request,"create.html")
