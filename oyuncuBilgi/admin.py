from django.contrib import admin
from .models import OyuncuBilgi, karakter



@admin.register(OyuncuBilgi)  # Bu tabloyu özelleştirecez diye. Classı decoratöre yolluyoruz.
class OyuncuBilgiAdmin(admin.ModelAdmin):
    list_display = ["kullanici", "gecirilenGun", "moneyUsed", "kayitGunu"]
    list_display_links = ["kullanici", "moneyUsed"]
    list_filter = ["kayitGunu"]
    search_fields = ["moneyUsed"]




    class Meta:  # Meta yapmamızı django istiyor ilişkilendirmek için
        model = OyuncuBilgi



# Register your models here.
