from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)



# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    deck = models.TextField()
    img = models.ImageField(upload_to="picture" , blank=True , null=True)  
    category = models.ForeignKey(Category , on_delete=models.CASCADE , default=1)
    
    # blank=True null = True img majburiy qilib qoymaydi
    # Default ga qiymat kiritmay ketsak Default dagi modelga yozib qoygan qiymatni oladi
    # masalan yoshimizni kiritmay ketsak sayit faqat 18 yoshlilar uchun bolsa default 18 yoshni oladi
    # yani defaultga ozimiz qiymat qoyib ketamiz
    # upload_to = "picture" file nomi rasimlar saqlanadigan

    def __str__(self):
        return f"{self.name}"
    










