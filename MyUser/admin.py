from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ("id", "firstname", "lastname", "phone", "entries", "address")


admin.site.register(Member, MemberAdmin)

