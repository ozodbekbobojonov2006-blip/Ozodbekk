from django.db import models

class Customer(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="Ismi sharifi")
    coupon_code = models.CharField(max_length=50, blank=True, null=True, verbose_name="Kupon kodi")
    customer_type = models.CharField(max_length=50, verbose_name="Mijoz turi")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Telefon raqami")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Mijoz"
        verbose_name_plural = "Mijozlar"

class Book(models.Model):
    book_name = models.CharField(max_length=255, verbose_name="Kitob nomi")
    author = models.CharField(max_length=255, verbose_name="Muallif")
    price = models.IntegerField(verbose_name="Narxi") # IntegerField ga o'zgardi
    stock = models.IntegerField(default=0, verbose_name="Ombordagi qoldiq")

    def __str__(self):
        return self.book_name

    class Meta:
        verbose_name = "Kitob"
        verbose_name_plural = "Kitoblar"

class OrderRental(models.Model):
    name = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="Mijoz")
    status = models.CharField(max_length=50)
    total_price = models.IntegerField(default=0, verbose_name="Umumiy summa")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.customer.full_name}"


class OrderItem(models.Model):
    qty = models.IntegerField(default=1, verbose_name="Soni")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Kitob")
    order = models.ForeignKey(OrderRental, on_delete=models.CASCADE, verbose_name="Buyurtma")
    price_at_order = models.IntegerField(null=True, blank=True)



class Tariff(models.Model):
    tariff_name = models.CharField(max_length=100, verbose_name="Tarif nomi")
    tariff_price = models.IntegerField(verbose_name="Tarif narxi")
    duration_days = models.IntegerField(default=30, verbose_name="Davomiyligi (soat)")

    def __str__(self):
        return self.tariff_name

    class Meta:
        verbose_name = "Tarif"
        verbose_name_plural = "Tariflar"

class TariffCustomer(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="Mijoz")
    tariff = models.ForeignKey(Tariff, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Mijoz tarifi"
        verbose_name_plural = "Mijozlar tariflari"