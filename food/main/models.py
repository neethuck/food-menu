from django.db import models

# Create your models here.
class cate(models.Model):
    cat_name= models.CharField(max_length=100,primary_key=True)
    Description = models.TextField()
    Image = models.ImageField(upload_to='category',null=True)
    


    def __str__(self):
        return self.cat_name
    
class Items(models.Model):
    name = models.CharField(max_length=100,primary_key=True)
    category = models.ForeignKey(cate, on_delete=models.CASCADE)  
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    Img = models.ImageField(upload_to='items',null=True)
    is_delivery_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class News(models.Model):
    Title= models.CharField(max_length=200,primary_key=True)
    desc = models.TextField()
    Imag = models.ImageField(upload_to='news',null=True)
    
    def __str__(self) -> str:
        return self.Title