from django.db import models

# Create your models here.

class Dept(models.Model):
    Deptno=models.IntegerField(primary_key=True)
    Dloc=models.CharField(max_length=100,unique=True)
    Deptname=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.Deptname

class Emp(models.Model):
    Empid=models.IntegerField(primary_key=True)
    Ename=models.CharField(max_length=100,unique=True)
    Esal=models.IntegerField()
    Deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)
    Hiredate=models.DateField(unique=True)
    def __str__(self) -> str:
        return self.Ename