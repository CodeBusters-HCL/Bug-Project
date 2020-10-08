from django.contrib import admin  #commentout all below code if inbuilt user is needed
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'staff_req', 'is_active', 'is_staff', 'is_admin', 'is_superuser' )
    list_display_links = ('username','email',)
    list_editable = ('is_staff', 'is_admin', 'is_superuser' )

admin.site.register(User, UserAdmin)
