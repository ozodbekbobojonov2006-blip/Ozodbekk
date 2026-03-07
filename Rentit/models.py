from django.db import models

class Profile(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="To'liq ism")
    phone = models.CharField(max_length=20, unique=True, verbose_name="Telefon raqam")
    email = models.EmailField(blank=True, verbose_name="Elektron pochta")
    address = models.CharField(max_length=255, verbose_name="Manzil")
    balance = models.IntegerField(default=0, verbose_name="Balans")
    rating = models.FloatField(default=5.0, verbose_name="Reyting")
    joined_at = models.DateTimeField(auto_now_add=True, verbose_name="Ro'yxatdan o'tgan sana")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profillar"

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kategoriya nomi")
    slug = models.SlugField(unique=True, verbose_name="Slug")
    description = models.TextField(blank=True, verbose_name="Tavsif")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"

class Item(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="Esh egasi")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="Kategoriya")
    title = models.CharField(max_length=255, verbose_name="Nomi")
    description = models.TextField(verbose_name="Tavsif")
    price_per_day = models.IntegerField(verbose_name="Kunlik narxi")
    image_main = models.ImageField(upload_to='items/', verbose_name="Asosiy rasm")
    city = models.CharField(max_length=100, verbose_name="Shahar")
    is_available = models.BooleanField(default=True, verbose_name="Mavjudmi?")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"

class Rental(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name="Mahsulot")
    renter = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="Ijaraga oluvchi")
    start_date = models.DateField(verbose_name="Boshlanish sanasi")
    end_date = models.DateField(verbose_name="Tugash sanasi")
    total_price = models.IntegerField(verbose_name="Umumiy narx")
    is_confirmed = models.BooleanField(default=False, verbose_name="Tasdiqlanganmi?")

    def __str__(self):
        return f"{self.item.title} - {self.renter.full_name}"

    class Meta:
        verbose_name = "Ijara"
        verbose_name_plural = "Ijaralar"

class Review(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name="Mahsulot")
    reviewer_name = models.CharField(max_length=100, verbose_name="Sharh qoldiruvchi")
    rating = models.IntegerField(default=5, verbose_name="Reyting")
    comment = models.TextField(verbose_name="Izoh")

    def __str__(self):
        return f"{self.item.title} uchun sharh"

    class Meta:
        verbose_name = "Sharh"
        verbose_name_plural = "Sharhlar"

class Wishlist(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="Profil")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name="Mahsulot")

    def __str__(self):
        return f"{self.profile.full_name} - Tanlanganlar"

    class Meta:
        verbose_name = "Tanlangan mahsulot"
        verbose_name_plural = "Tanlangan mahsulotlar"

class FAQ(models.Model):
    question = models.CharField(max_length=255, verbose_name="Savol")
    answer = models.TextField(verbose_name="Javob")

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "Ko'p beriladigan savol"
        verbose_name_plural = "Ko'p beriladigan savollar"

class Transaction(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="Profil")
    amount = models.IntegerField(verbose_name="Miqdor")
    payment_type = models.CharField(max_length=50, verbose_name="To'lov turi")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Vaqti")

    def __str__(self):
        return f"{self.profile.full_name} - {self.amount}"

    class Meta:
        verbose_name = "kelishuv"
        verbose_name_plural = "kelishuvlar"     