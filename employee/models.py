from django.db import models  
class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.CharField(max_length=30)  
    econtact = models.CharField(max_length=15) 
    lugarr = models.CharField(max_length=50)
    cedulaa = models.CharField(max_length=40)
    usuarioo = models.CharField(max_length=60)

    def __str__(self):
        return "%s " %(self.ename) 
    class Meta:  
        db_table = "employee"  