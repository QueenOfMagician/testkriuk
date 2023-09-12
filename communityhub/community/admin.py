from django.contrib import admin
from .models import Group, GroupMember, PesanGrup
# Register your models here.

admin.site.register(GroupMember)
admin.site.register(Group)
admin.site.register(PesanGrup)

