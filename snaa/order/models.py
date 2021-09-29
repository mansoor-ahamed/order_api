from django.db import models

# Create your models here.
class Order (models.Model):
    name=models.CharField( max_length=50)
    description=models.CharField( max_length=250)
    price=models.CharField( max_length=50)
    stock=models.CharField( max_length=50)
    is_active=models.BooleanField(default=True, blank=True)
    image=models.ImageField( upload_to='images/' , blank=True, null=True)
    specification=models.CharField( max_length=250)
    order_at = models.DateTimeField( auto_now_add=True)



    def __str__(self):
        return self.name
    


    

    