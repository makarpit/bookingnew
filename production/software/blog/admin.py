from django.contrib import admin
from .models import Blogpost, Page, NewsAndEvent, Testimonial, Member

class BlogpostAdmin(admin.ModelAdmin):
	  list_display = ['title','head0','head1']
	  search_fields = ['title','head0','head1']
	  list_filter = ['title','head0','head1']


	  
admin.site.register(Blogpost, BlogpostAdmin)

class PageAdmin(admin.ModelAdmin):
	  list_display = ['name','meta_title','image']
	  search_fields = ['name','meta_title','image']
	  list_filter = ['name','meta_title']


admin.site.register(Page, PageAdmin)

class NewsAndEventAdmin(admin.ModelAdmin):
	  list_display = ['name','meta_title','image']
	  search_fields = ['name','meta_title','image']
	  list_filter = ['name','meta_title']



admin.site.register(NewsAndEvent, NewsAndEventAdmin)

class TestimonialAdmin(admin.ModelAdmin):
	  list_display = ['name','meta_title','image']
	  search_fields = ['name','meta_title','image']
	  list_filter = ['name','meta_title']



admin.site.register(Testimonial, TestimonialAdmin)

class MemberAdmin(admin.ModelAdmin):
	  list_display = ['name','meta_title','image']
	  search_fields = ['name','meta_title','image']
	  list_filter = ['name','meta_title']



admin.site.register(Member, MemberAdmin)

class Media:
    js = ("blog/js/typed.js",)
	