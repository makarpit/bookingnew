from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    head0 = RichTextField(blank=True, null=True)
    chead0 = RichTextField(blank=True, null=True)
    head1 = models.CharField(max_length=500, default="")
    chead1 = models.CharField(max_length=5000, default="")
    head2 = models.CharField(max_length=500, default="")
    chead2 = models.CharField(max_length=5000, default="")
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to='shop/images', default="")
    def __str__(self):
       return self.title
	   
class Page(models.Model):
    page_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = RichTextField(blank=True, null=True)
    meta_title = models.CharField(max_length=70, default="")
    meta_desc = models.CharField(max_length=500, default="")
    image = models.ImageField(upload_to='shop/images', default="")
    def __str__(self):
        return self.name
		
class NewsAndEvent(models.Model):
    news_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = RichTextField(blank=True, null=True)
    meta_title = models.CharField(max_length=70, default="")
    meta_desc = models.CharField(max_length=500, default="")
    image = models.ImageField(upload_to='shop/images', default="")
    def __str__(self):
        return self.name
		
class Testimonial(models.Model):
    testimonial_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = RichTextField(blank=True, null=True)
    meta_title = models.CharField(max_length=70, default="")
    meta_desc = models.CharField(max_length=500, default="")
    image = models.ImageField(upload_to='shop/images', default="")
    def __str__(self):
        return self.name
		
class Member(models.Model):
    member_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=50)
    description = RichTextField(blank=True, null=True)
    meta_title = models.CharField(max_length=70, default="")
    meta_desc = models.CharField(max_length=500, default="")
    image = models.ImageField(upload_to='shop/images', default="")
    def __str__(self):
        return self.name

