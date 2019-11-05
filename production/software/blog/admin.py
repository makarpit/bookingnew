from django.contrib import admin

# Register your models here.
from .models import Blogpost, Page, NewsAndEvent, Testimonial, Member

admin.site.register(Blogpost)
admin.site.register(Page)
admin.site.register(NewsAndEvent)
admin.site.register(Testimonial)
admin.site.register(Member)

