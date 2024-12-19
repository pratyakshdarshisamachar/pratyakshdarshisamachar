from django.db import models

# Create your models here.


class jobmodel(models.Model):
    id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=100)
    Email=models.EmailField()
    Phone=models.CharField(max_length=55)
    Position=models.CharField(max_length=100)
    Resume=models.ImageField(upload_to="uploads/")
    
    class Meta:
        db_table="jobtb"


class uploadmodel(models.Model):
    id=models.AutoField(primary_key=True)
    Title=models.CharField(max_length=100,null=True, blank=True)
    Description=models.TextField(max_length=400)
    File=models.FileField(upload_to="usernews/")
    
    class Meta:
        db_table="uploadtb"

class advertisemodel(models.Model):
    id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=100)
    Email=models.EmailField()
    Message=models.TextField(max_length=400)

    class Meta:
        db_table="advertisetb"
    

class contactmodel(models.Model):
    id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=100)
    Email=models.EmailField()
   
    Message=models.TextField(max_length=400)

    class Meta:
        db_table="contacttb"  




#fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff

class youtubenews(models.Model):
    id=models.AutoField(primary_key=True)
    ytlink=models.URLField(null=True)
    heading=models.CharField(max_length=100)
    pic=models.ImageField(upload_to="uploads/") 

    class Meta:
        db_table="youtubetb"
    

class bigimage(models.Model):
    id=models.AutoField(primary_key=True)
    ytlink=models.URLField(null=True)
    heading=models.CharField(max_length=100)
    pic=models.ImageField(upload_to="uploads/") 

    class Meta:
        db_table="bigimagetb"
    


class videonews(models.Model):
    id=models.AutoField(primary_key=True)
    heading=models.CharField(max_length=100)
    vido=models.FileField(upload_to="uploads/")
    

    class Meta:
        db_table="videotb"
    

class bottomnews(models.Model):
    id=models.AutoField(primary_key=True)
    pic=models.ImageField(upload_to="uploads/")
    explain=models.CharField(max_length=400)
    ytlink=models.URLField()

    class Meta:
        db_table="bottomtb"
    

class chunavnews(models.Model):
    id=models.AutoField(primary_key=True)
    pic=models.ImageField(upload_to="uploads/")
    explain=models.CharField(max_length=400)
    heading=models.CharField(max_length=100)
    textfornews=models.CharField(max_length=1000)

    class Meta:
        db_table="chunavtb"
    

class describenews(models.Model):
    id=models.AutoField(primary_key=True)
    pic=models.ImageField(upload_to="uploads/")
    textfornews=models.CharField(max_length=1000)

    class Meta:
        db_table='describe1tb'



class describenews2(models.Model):
    id=models.AutoField(primary_key=True)
    pic=models.ImageField(upload_to="uploads/")
    heading=models.CharField(null=True ,max_length=100)
    explain=models.CharField(max_length=100,null=True)
    textfornews=models.CharField(max_length=1000)

    class Meta:
        db_table='describe2tb'        


class describenews3(models.Model):
    id=models.AutoField(primary_key=True)
    pic=models.ImageField(upload_to="uploads/")
    heading=models.CharField(null=True ,max_length=100)
    explain=models.CharField(max_length=100,null=True)
    textfornews=models.CharField(max_length=1000)

    class Meta:
        db_table='describe3tb'                



class describenews4(models.Model):
    id=models.AutoField(primary_key=True)
    pic=models.ImageField(upload_to="uploads/")
    heading=models.CharField(null=True ,max_length=100)
    explain=models.CharField(max_length=100)
    textfornews=models.CharField(max_length=1000)

    class Meta:
        db_table='describe4tb'              



class describenews5(models.Model):
    id=models.AutoField(primary_key=True)
    pic=models.ImageField(upload_to="uploads/")
    heading=models.CharField(null=True ,max_length=100)
    explain=models.CharField(max_length=100)
    textfornews=models.CharField(max_length=1000)

    class Meta:
        db_table='describe5tb'                      