from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Page
from blog.models import Member
from blog.models import Testimonial
from blog.models import Service
from blog.models import NewsAndEvent
from blog.models import Video




def index(request):
    testimonialdata = Testimonial.objects.all()
    member = Member.objects.all()
    servicedata = Service.objects.all()
    news = NewsAndEvent.objects.all()
    about = Page.objects.filter(page_id = '3')[0]
    return render(request, 'home/index.html',
                  {'testimonialdata': testimonialdata,'member':member,'about': about,'servicedata':servicedata,'news':news})
	
def about(request):
    about = Page.objects.filter(page_id = '3')[0]
    #return HttpResponse(about)
    return render(request, 'home/about.html',{'about':about})
	
def testimonial(request, id):
    singletestimonial = Testimonial.objects.filter(testimonial_id = id)[0]
    return render(request, 'home/testimonial.html',
                  {'singletestimonial':singletestimonial})
				  
def service(request, id):
    singletesservice = Service.objects.filter(service_id = id)[0]
    return render(request, 'home/service.html',
                  {'singletesservice':singletesservice})
	
def member(request):
    id = request.GET.get('q')
    #return HttpResponse(id)
    member = Member.objects.filter(member_id = id)[0]
    return render(request, 'home/member.html',{'member':member})
	
def news(request, id):
    singlenews = NewsAndEvent.objects.filter(news_id = id)[0]
    return render(request, 'home/news.html',{'singlenews':singlenews})	
	
def live(request):
    myposts = Video.objects.all()
    return render(request, 'home/live.html',
                  {'myposts': myposts})	
	
def rules(request):
    page = Page.objects.filter(page_id = '1')[0]
    return render(request, 'home/rules.html',
                  {'page':page})		
	
def notifications(request):
    page = Page.objects.filter(page_id = '2')[0]
    #return HttpResponse(page)
    return render(request, 'home/notifications.html',
                  {'page':page})			
	
def appointment(request):
    return render(request, 'home/appointment.html')	