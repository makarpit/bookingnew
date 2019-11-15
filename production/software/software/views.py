from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Page
from blog.models import Member


def index(request):
    member = Member.objects.all()
    return render(request, 'home/index.html',{'member':member})
	
def about(request):
    about = Page.objects.filter(page_id = '3')[0]
    #return HttpResponse(about)
    return render(request, 'home/about.html',{'about':about})
	
def testimonial(request):
    return render(request, 'home/testimonial.html')
	
def member(request):
    id = request.GET.get('q')
    #return HttpResponse(id)
    member = Member.objects.filter(member_id = id)[0]
    return render(request, 'home/member.html',{'member':member})
	
def news(request):
    return render(request, 'home/news.html')	
	
def rules(request):
    return render(request, 'home/rules.html')		
	
def notifications(request):
    page = Page.objects.filter(page_id = '2')[0]
    #return HttpResponse(page)
    return render(request, 'home/notifications.html',
                  {'page':page})			
	
def appointment(request):
    return render(request, 'home/appointment.html')	