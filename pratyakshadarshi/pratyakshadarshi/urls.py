from django.contrib import admin
from django.urls import path
from pratyakshapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('about/',views.aboutfunction),

    #chunav with description

    path('chunav/',views.chunavfunction),
    path('describe/',views.describefunction),
    path('describe2/',views.describe2function),
    path('describe3/',views.describe3function),
    path('describe4/',views.describe4function),
    path('describe5/',views.describe5function),
    
    path('services/',views.servicesfunction),


    path('advertise/',views.advertisefunction),
    path('advertiseform/',views.useradvertisefunction,name="advertiseform"),


    path('contact/',views.contactfunction),
    path('contacts/',views.contactfunctions,name="contacts"),

    path('job/',views.job),
    path('jobfor/',views.jobfunction,name="jobfor"),

    path('upload/',views.uploadfunction),
    path('uploadform/',views.uploadfunctions,name="uploadform"),


  
   
    


]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)        