from django.db import models

class Direction(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField("Ma'lumot",blank=True)
    duration = models.PositiveIntegerField("Davomiyligi",default=10)
    price = models.PositiveIntegerField(verbose_name="UZS", default=100)
    price_usd = models.PositiveIntegerField(verbose_name="USD", default=100)
    image = models.ImageField(upload_to='city_images/')
    leave = models.DateField("Ketish sanasi (To'ldirish shart emas)", blank=True,null=True)
    back_to = models.DateField("Qaytish sanasi (To'ldirish shart emas)", blank=True,null=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Yo'nalish"    
        verbose_name_plural = "Yo'nalishlar" 

