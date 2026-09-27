from django.shortcuts import render
from django.http import HttpResponse
from .models import Product , Category
import sys


def Product1(request):
    all_1 = Product.objects.all()
    categorys = Category.objects.all()

    
    return render(request , "templates/yangi.html" , {"context":all_1 , "categorys":categorys})



def Product_id(request , id):
    id_1 = id
    product_id = Product.objects.get(id=id_1)
    
    return render(request , "templates/card.html" , {"product_id":product_id})
     
     
     
#    QIDIRUV  N1
   
     
def sourch_product(request):   
    query = request.GET.get("query")
     # bu html input dagi nomi yani ozgaruvchi nomiga imputdagi 
    # aynan osha yoziladigan joyni ovolyabmiz
    
    if query: # query topilmay qolmasa
        
        product = Product.objects.filter(name__contains=query) # >>> query bu input dagi name boladi
    
    # name__contains bu namesi orqali qidiradi masalan  title__contains bolsa titlesi orqali
    
    else:
        product = Product.objects.all()
        
        
    return render(request , "results.html" , {"results":product}) 


        #   Filter qismi N2
        
def Filter(request):
    query1 = request.GET.get("category_1") # filter html dagi namesi 
     # yani ozgaruvchi nomiga imputdagi 
    # aynan osha yoziladigan joyni ovolyabmiz
    
    if query1 != '0':
        natija = Product.objects.filter(category=query1) # modeldagi productga ulangan categoriya nomi
        
    else:
        natija = Product.objects.all()
        
    categorys = Category.objects.all()


    return render(request , "templates/yangi.html" , {"context":natija , "categorys":categorys})




def index(request):
    return render(request , "templates/base.html")

def card(request):
    return render(request , 'templates/card.html')




# boshqacha qilb ham >>> def salom(request , yil)
#                                context = {
#                                     "yosh":2026 - yil >> shu orqali html ga {{yosh}} qav ichiga malumot 
#                                                                         chiqarilsa ham boladi
#                                           }
                               
        
        

#                             <!-- ESLATMA -->

# 5 ] Ketadigan malumotlarni hammasi html dagi >>>> form >>>>  ichida boladi yani u bizning 
# malumotlar bazamizdan kerakli malumotni olib keladi   

# <<<<<<  albatta form dagi action bu malumotni bosganda qayerga yuborishi >>>>>>
        
# 1 ) Html form dagi <<< method >>> bu malumotimiz qay tartibda ketishi yani POST VA GET larda ketadi

# 2 ) {% csrf_token %}   havfsizlik uchun

# 3 ) input dagi namelar bizning malumotimiz qanday malumotligini anglatadi yani >> 
# <input type="text" name="username">views da yozilsa name si orqali uni qaysinga tegishli ekanligini bilamiz
# <input type="email" name="email"> yani namesi orqali funksiyaga chaqiriladi

# 4 ) <button type="submit">Yuborish</button>bu esa yani ketadigan malumot bolganda type doim sumbit bolishi kerak

# agarda search qismini qiladigan bolsak type sumbit emas search boladi 
# agarda filter ishlatsak uniki type="filter boladi"


   
# def sourch_product(request):   
#     query = request.Get.get("query") # bu html input dagi nomi
    
#     product = Product.objects.filter(name_contains=query) >> query bu inputdagi name boladi
    
    # name__contains bu namesi orqali qidiradi masalan  title__contains bolsa titlesi orqali

#     return render(request , "results.html" , {"context":product})  





# ha demak hammasi bitta html ga yuborganligi
# sababli ularni chaqirib olish nomlari bir xil bolishi kerakmi
