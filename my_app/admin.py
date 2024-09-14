from django.contrib import admin

# Register your models here.
from .models import Company, Salesman, Engineer, Programmer,Web_developer,System_Analyst,Analyst,SEO,HR,Designer
admin.site.register(Company)
admin.site.register(Salesman)
admin.site.register(Programmer)
admin.site.register(System_Analyst)
admin.site.register(Designer)
admin.site.register(Web_developer)
admin.site.register(Analyst)
admin.site.register(SEO)
admin.site.register(HR)
admin.site.register(Engineer)
