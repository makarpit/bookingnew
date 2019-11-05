from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'home/index.html')
	
def about(request):
        return render(request, 'home/about.html')
	
def testimonial(request):
    return render(request, 'home/testimonial.html')
	
def member(request):
    return render(request, 'home/member.html')
	
def news(request):
    return render(request, 'home/news.html')	
	
def rules(request):
    return render(request, 'home/rules.html')		
	
def notifications(request):
    return render(request, 'home/notifications.html')			
	