from django.db import models

class login_table(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class ip_table(models.Model):
    ip=models.CharField(max_length=50)



