Biz block qoymoqchimiz yani unda biringchi hamma sahifada boladigan navbarni html ga kirib olamiz
va pastiga  shularni qoyamiz

    {% block main %}
        
    {% endblock main %}

boshqa file ochib yana navbar qismini yozgandan {% extends 'nomi.html' %} qilib navbar yani hammasida 
boladigan html nomli nomni chaqiramiz va birinchidagi yani navbar bor html qismi qolganlarida ham korinadi
va ikkinchi yani nargi sahifaga pastiga kod yozmoqchi bolsak 

    {% block main %}
        
    {% endblock main %}   qoyamiz va birinchi yani hammasida boladigan navbar qismli html nomdagi file 
    
    ichiga yozgan main ichiga boshqa boshqa kodlarni yozaveramiz yani birinchidagi navbar qismidagi block
    qismi qolganlarni nomiga ham qoyilishi kerak boladi



<!-- Asosiy yani extend bu boshqa html yani hammasida boladigan navbar yokida boshqa joylarda vorislik
olishdir buning foydasi hammasiga bitta qilinadi hammasiga yozib otirilmidi  -->



2 ]      path("salom/<str:ism>" , salom)

                    def salom(request , ism):
                        return HttpResponse(f"salom: {ism} ")

shunday qabul qiladi yani url da ism kiritsa uni bemalol olish mumkin
hattoki son kiritsa ham u ham huddi shunga ohshash.Yani url dan boshqalar kiritgan
malumotni shunchaki ushlab olish degani.

3 ] html qismida {{ }} orqali malumotlarni yozib olishimiz mumkin




<!-- 4 ] url ga name yozish bu html dan qaysi funksiya ishlashini taminlaydi 
yani url orqali biz html dagi kodlarimiz qaysi funksiya ishlashini name orqali hal qilamiz  -->


# def Product1(request):
#    all_1 = Product.objects.all()     >>>>>   hamma malumotlarni chiqaradi
    
#    return render(request , "templates/yangi.html" , {"context":all_1})



# Product_id(request , id):
#    id_1 = id
#    product_id = Product.objects.get(id=id_1) >>>> AYNAN bosilgan malumotlarni chiqarib beradi
    
#    return render(request , "templates/card.html" , {"product_id":product_id})
     

hamma productlarni kormoqchi bolganimizda id ishlatmaymiz aynan oshani bosganda hamma malumot chiqishi uchun esa albatta id ishlatamiz uni albatta url ga ham qoyib ketish kerak boladi

                            


                            <!-- ESLATMA -->

5 ] Ketadigan malumotlarni hammasi html dagi >>>> form >>>>  ichida boladi yani u bizning malumotlar bazamizdan kerakli malumotni olib keladi   

<<<<<<  albatta form dagi  <<< action >>> bu malumotni bosganda qayerga yuborishi >>>>>>

 1 ) Html form dagi <<< method >>> bu malumotimiz qay tartibda ketishi yani POST VA GET larda ketadi

# 2 ) {% csrf_token %}   havfsizlik uchun

3 ) 

3 ) input dagi namelar bizning malumotimiz qanday malumotligini anglatadi yani >> 
# <input type="text" name="username">  input dagi name bu malumotimiz nima ekanligini bildiradi
# <input type="email" name="email">

# 4 ) <button type="submit">Yuborish</button>bu esa yani ketadigan malumot bolganda type doim sumbit bolishi kerak

6 ] Search qismi

inputda bolsa unga name ham berib qoyishimiz ham kerak boladi chunki uni viewsda bunday chaqiramiz

   
# def sourch_product(request):   
#    query = request.Get.get("query") # bu html input dagi nomi
#   
    product = Product.objects.filter(name_contains=query) >>>  query bu inputdagi name boladi
    
#    return render(request , "results.html" , {"context":product})  


# agarda search qismini qiladigan bolsak type sumbit emas search boladi 
# agarda filter ishlatsak uniki type="filter boladi"




2 ) 

# def sourch_product(request):   
#    query = request.GET.get("query") # bu html input dagi nomi
    
#    product = Product.objects.filter(name__contains=query) # >>> query bu input dagi name boladi
    
    # name__contains bu namesi orqali qidiradi masalan  title__contains bolsa titlesi orqali   
    
#    return render(request , "results.html" , {"results":product})  

3 )                           MODELLAR

    # blank=True null = True img majburiy qilib qoymaydi
    # Default ga qiymat kiritmay ketsak Default dagi modelga yozib qoygan qiymatni oladi
    # masalan yoshimizni kiritmay ketsak sayit faqat 18 yoshlilar uchun bolsa default 18 yoshni oladi
    # yani defaultga ozimiz qiymat qoyib ketamiz

# 4 ) {{i.img.url}}   img qoyish


7 ] Html da asosiy qismlaridan biridir !!!
                                 
                                 <!-- HTML eslatma -->

yani biz yozgan funksiya ikkalasi ham bir xil html ga ketayotgan bolsa 
ularni {"nn":bb} shunday yokida boshqacha chaqiramiz agarda biz malumotimizni 
bitta html da chaqirmoqchi bolsak bitta nom ostida yani {"n":n} va boshqa funksiyada {"n":m}
shunday chaqirib otishimiz kerak boladi chunki ketayotgan malumot nomi bir xil turi har xil 
bolishi kerak


Buning misolini biz views dagi misollarda korishimiz mumkin