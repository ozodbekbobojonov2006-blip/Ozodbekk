import uuid
import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from ckeditor.fields import RichTextField


STATUS_POST = (
    ('NEW', 'new'),
    ('CONFIRMED', 'confirmed'),
    ('REJECTED', 'rejected'),
)


# ================= BASE =================
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# ================= ADDRESS =================
class Address(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    test_demo = models.CharField(max_length=255, null=True, blank=True)

    @property
    def address(self):
        return f"{self.street}, {self.city}, {self.country}, {self.zipcode}"

    def save(self, *args, **kwargs):
        self.test_demo = self.address
        super().save(*args, **kwargs)

    def __str__(self):
        return self.address


# ================= USER =================
class User(AbstractUser):
    full_name = models.CharField("F.I.O", max_length=100, blank=True)
    phone_number = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.username


# ================= PROFILE =================
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    email = models.EmailField(blank=True)
    bio = RichTextField(blank=True)

    def __str__(self):
        return self.user.username


# ================= CATEGORY =================
class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children"
    )

    def __str__(self):
        return self.name


# ================= TAG =================
class Tag(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=10, default="#ffffff")

    def __str__(self):
        return self.name


# ================= POST =================
class Post(BaseModel):


    title = models.CharField(max_length=100)
    content = models.TextField()

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

    image = models.ImageField(upload_to="posts/", null=True, blank=True)

    slug = models.SlugField(max_length=150, unique=True, blank=True)

    tags = models.ManyToManyField(Tag, blank=True, related_name="posts")

    status = models.CharField(max_length=10, choices=STATUS_POST, default="NEW")

    is_published = models.BooleanField(default=False)

    views = models.PositiveIntegerField(default=0)

    pub_date = models.DateTimeField(null=True, blank=True, editable=False)

    # ---------- SAVE LOGIC ----------
    def save(self, *args, **kwargs):

        # slug auto generate
        if not self.slug:
            self.slug = slugify(self.title)

        # pub_date type protection
        if self.pub_date and not isinstance(self.pub_date, datetime.datetime):
            self.pub_date = None

        # publish logic
        if self.is_published:
            if not self.pub_date:
                self.pub_date = timezone.now()
        else:
            self.pub_date = None

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


# ================= COMMENT =================
class Comment(BaseModel):
    description = models.TextField()

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    def ___str__(self):
        return self.description[:30]


# ================= LIKE =================
class Like(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="likes")

    class Meta:
        unique_together = ("user", "post", "comment")

    def __str__(self):
        return f"{self.user} ❤️"
    