from django.db import models

# Create your models here.'''
class Product(models.Model):



 
    device_name = models.CharField(max_length=255);
    path_number = models.CharField(max_length=255);
    serial_number = models.CharField(max_length=255);
    device_type = models.CharField(max_length=255);
    location = models.CharField(max_length=255);
    status = models.BooleanField(default=True);

    def __str__(self):
        return 'Id:{0} Name:{1}'.format(self.id, self.device_name)
 # return self.device_name
  


  



