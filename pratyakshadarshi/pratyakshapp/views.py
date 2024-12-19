

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from pratyakshapp.models import jobmodel ,uploadmodel,advertisemodel,contactmodel,youtubenews,bigimage,videonews,bottomnews,chunavnews,describenews,describenews2,describenews3,describenews4,describenews5




from django.shortcuts import render






def home(request):
     data= youtubenews.objects.all()
     categories= bigimage.objects.all()
     newsvido= videonews.objects.all()
     bottomnewss=bottomnews.objects.all()
     context={'data': data,'category':categories,'newsvido':newsvido,'bottomnewss':bottomnewss}
     return render(request,'index.html',context)

def aboutfunction(request):
    return render(request,'about.html')

def chunavfunction(request):
    chunavnewss=chunavnews.objects.all()
    describenewss2=describenews2.objects.all()
    describenewss3=describenews3.objects.all()
    describenewss4=describenews4.objects.all()
    describenewss5=describenews5.objects.all()
    context={'chunavnewss':chunavnewss,'describenewss2':describenewss2,'describenewss3':describenewss3,'describenewss4':describenewss4,'describenewss5':describenewss5}
    return render(request,'chunav.html',context)

# describe the news

def describefunction(request):
    describenewss=describenews.objects.all()
    describenewss2=describenews2.objects.all()
    describenewss3=describenews3.objects.all()
    describenewss4=describenews4.objects.all()
    describenewss5=describenews5.objects.all()
    context={'describenews':describenewss,'describenewss2':describenewss2,'describenewss3':describenewss3,'describenewss4':describenewss4,'describenewss5':describenewss5}
    return render(request,'descriptiond.html',context)

def describe2function(request):
     describenewss2=describenews2.objects.all()
     context={'describenewss2':describenewss2}

     return render(request,'description2.html',context)

def describe3function(request):
    describenewss3=describenews3.objects.all()
    context={'describenewss3':describenewss3}

    return render(request,'description3.html',context)

def describe4function(request):
    describenewss4=describenews4.objects.all()
    context={'describenewss4':describenewss4}
    return render(request,'description4.html',context)

def describe5function(request):
    describenewss5=describenews5.objects.all()
    context={'describenewss5':describenewss5}
    return render(request,'description5.html',context)


# describe news end
def advertisefunction(request):
    return render(request,'advertise.html')




def useradvertisefunction(request):
    if request.method == "POST":
        Name=request.POST.get('Name')
        Email=request.POST.get('Email')
        Message=request.POST.get('Message')
        

        ad=advertisemodel(Name=Name,Email=Email,Message=Message)
        ad.save()

    return render(request,'index.html')  



def contactfunction(request):
    return render(request,'contact.html')

def contactfunctions(request):
    if request.method == "POST":
        Name=request.POST.get('Name')
        Email=request.POST.get('Email')
        
        Message=request.POST.get('Message')
        

        ct=contactmodel(Name=Name,Email=Email,Message=Message)
        ct.save()



    return render(request,'index.html')



def job(request):
    return render(request,'job.html')

def jobfunction(request):
    if request.method == "POST":
        Name=request.POST.get('Name')
        Email=request.POST.get('Email')
        Phone=request.POST.get('Phone')
        Position=request.POST.get('Position')
        Resume=request.POST.get('Resume')

        jb=jobmodel(Name=Name,Email=Email,Phone=Phone,Position=Position,Resume=Resume)
        jb.save()

    return render(request,'index.html')   
    



def uploadfunction(request):
    return render(request,'upload.html')


def uploadfunctions(request):
     if request.method == "POST":
        Title=request.POST.get('Title')
        Description=request.POST.get('Description')
        File=request.POST.get('File')
       

        ub=uploadmodel(Title=Title,Description=Description,File=File)
        ub.save()


     return render(request,'index.html')

def servicesfunction(request):
    return render(request,'services.html')

def newsfunction(request):
    return  render(request,'newspaper.html'),  
  


# zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz


    


#ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg

