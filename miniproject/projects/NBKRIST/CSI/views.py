from django.shortcuts import render
from django.http import HttpResponse

from .models import Photo,Year,academicyear20_21, winners,Contact,registrationforevents
from NBKRIST.forms import contactformemail
from .models import individualeventspics as yearthumbnails
from django.contrib import messages
from django.core.mail import send_mail


def about(req):
    return render(req,'CSI/about.html')
def home(req):
    pic=Photo.objects.all()
    check1=Photo.objects.filter(id__in=[1,2,3,4])
    check2=Photo.objects.filter(id__in=[5,6,7,8])
    check3=Photo.objects.filter(id__in=[9,10,11,12])
    check4=Photo.objects.filter(id__in=[13,14,15,16])
    return render(req,'CSI/home.html',{'pic':pic,'check1':check1,'check2':check2,'check3':check3,'check4':check4})
def officelist(req):
    return render (req,'CSI/officelist.html')
def snaps(req):
    years=Year.objects.all()
    yearthumbnail=yearthumbnails.objects.all()
    year1=Year.objects.get(name="2020-2021")
    context={'years':years,'yearthumbnail':yearthumbnail,'year1':year1}
    return render(req,'CSI/snaps.html',context)

def past(req):
    return render(req,'CSI/past.html')
def individualeventspics(req):
    years=Year.objects.all()
    yearthumbnail=yearthumbnails.objects.all()
    context={'years':years,'yearthumbnail':yearthumbnail}
    return render(req,'CSI/individualeventspics.html',context)
def academic20_21(req):
    eventdetails=academicyear20_21.objects.all().order_by('date')
    identities=academicyear20_21.objects.all().order_by('pk')
    firstevent=academicyear20_21.objects.get(eventnumber="EVENT 1")
    context={'eventdetails':eventdetails,'identities':identities,'firstevent':firstevent}
    return render(req,'CSI/2020-2021.html',context)
def win(req,id):
    prizewinner=winners.objects.all().order_by('eventno')
    eventexception1=academicyear20_21.objects.get(eventnumber="EVENT 1")
    eventexception2=academicyear20_21.objects.get(eventnumber="EVENT 2")
    context={'prizewinner':prizewinner,'eventexception1':eventexception1,'eventexception2':eventexception2,'id':id}
    return render(req,'CSI/winners.html',context)
def upcoming(req):
    return render(req,'CSI/upcoming.html')
def contact(req):
    if req.method=="POST":
        name=req.POST['name']
        email=req.POST['email']
        content=req.POST['content']
        if len(name)<2 or len(email)<3 or len(content)<10:
            messages.warning(req,"please fill the form correctly")
        else:
            contacts=Contact(name=name,email=email,content=content)
            contacts.save()
            messages.success(req,"Your message has been successfully sent ")

    return render(req,'CSI/contact.html')
def contactsendmail(req):
    if req.method=="GET":
        form=contactformemail()
    else:
        form=contactformemail(req.POST)
        if form.is_valid():
            messagetosender="We would get back to you soon!"
            subjecttosender="Your message has reached us"
            name=form.cleaned_data['name']
            fromemail=form.cleaned_data['fromemail']
            subject=form.cleaned_data['Subject']
            message=form.cleaned_data['Message']
            if len(name)<2 or len(fromemail)<3 or len(message)<10:
                messages.warning(req,"please fill the form correctly, check for mail to be in the format abc@xyz.com")
            else:
                send_mail(subject,message,fromemail,['csi.events@nbkrist.org'])
                send_mail(subjecttosender,messagetosender,fromemail,[fromemail])
                messages.success(req,"Your message has been successfully sent ")
    return render(req,'CSI/contactpage.html',{'form':form})

def registrations(req):
    return render(req,'CSI/registrations.html')
def eventregistration(req):
    if req.method=="POST":
        name=req.POST['name']
        email=req.POST['email']
        rollnumber=req.POST['rollnumber']
        year=req.POST['year']
        section=req.POST['section']
        if len(name)<2 or len(email)<3 or len(rollnumber)<3:
            messages.warning(req,"please fill the form correctly")
        else:
            registered=registrationforevents(name=name,email=email,year=year,section=section,rollnumber=rollnumber)
            registered.save()
            messages.success(req,"You have successfully registered! ")
    return render(req,'CSI/eventregistration.html')




























# Create your views here.
