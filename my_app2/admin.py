from django.contrib import admin

# Register your models here.
from .models import Voicebar, Clerk, Engineer, Cashier,Accountant,Manager,Analyst,Guard,HR,Designer
admin.site.register(Voicebar)
admin.site.register(Clerk)
admin.site.register(Cashier)
admin.site.register(Accountant)
admin.site.register(Designer)
admin.site.register(Manager)
admin.site.register(Analyst)
admin.site.register(Guard)
admin.site.register(HR)
admin.site.register(Engineer)