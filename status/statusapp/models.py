from django.db import models

class Contact_Us(models.Model):
    name = models.CharField(max_length=25, null= True)
    email = models.EmailField()
    mobile_no = models.IntegerField()
    message = models.TextField() 



    def __str__(self):
        return self.name 