from django.contrib import admin
from .models import User, Profile, Address, Post, Comment, Like, Category, Tag


# ================= ADDRESS =================
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("id", "city", "country", "street", "zipcode", "address")
    search_fields = ("city", "country", "street", "zipcode")
    list_filter = ("city", "country")
    ordering = ("-id",)
    readonly_fields = ("address",)


# ================= PROFILE INLINE =================
class ProfileInline(admin.StackedInline):
    model = Profile
    extra = 0


# ================= USER =================
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "full_name", "phone_number", "is_staff", "is_active")
    search_fields = ("username", "full_name", "phone_number")
    list_filter = ("is_staff", "is_superuser", "is_active")
    inlines = [ProfileInline]
    ordering = ("-id",)


# ================= PROFILE =================
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "address")
    search_fields = ("user__username", "user__full_name")
    list_filter = ("address",)
    autocomplete_fields = ("user", "address")


# ================= CATEGORY =================
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "parent")
    search_fields = ("name",)
    list_filter = ("parent",)


# ================= TAG =================
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "color")
    search_fields = ("name",)


# ================= COMMENT INLINE =================
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    autocomplete_fields = ("author",)


# ================= LIKE INLINE =================
class LikeInline(admin.TabularInline):
    model = Like
    extra = 0
    autocomplete_fields = ("user", "comment")


# ================= POST =================
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "status", "views", "is_published", "pub_date")
    list_filter = ("status", "is_published", "author", "tags")
    search_fields = ("title", "content", "author__username")
    prepopulated_fields = {"slug": ("title",)}
    autocomplete_fields = ("author", "tags")
    readonly_fields = ("views", "pub_date", "created_at", "updated_at")
    inlines = [CommentInline, LikeInline]
    ordering = ("-id",)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related("author").prefetch_related("tags")


# ================= COMMENT =================
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "short_desc", "author", "created_at")
    search_fields = ("description", "author__username")
    autocomplete_fields = ("author",)

    def short_desc(self, obj):
        return obj.description[:40]
    short_desc.short_description = "Comment"


# ================= LIKE =================
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "post", "comment", "created_at")
    autocomplete_fields = ("user", "post", "comment")