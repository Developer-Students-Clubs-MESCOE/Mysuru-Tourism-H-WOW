from django.shortcuts import render
from .models import Contact,Feed,Valo

def homepage(request):
	if(request.method=="POST"):
		name = request.POST.get('name', '')
		tel = request.POST.get('tel', '')
		email = request.POST.get('email', '')
		message = request.POST.get('message', '')

		if (name != ""):
			contact = Contact(name=name, tel=tel, email=email, message=message)
			contact.save()

		elif (name == ""):
			feed = Feed(email=email, message=message)
			feed.save()
	return render(request, 'index.html')

# def feedback(request):
	
# 	if request.method=="POST":
# 		email = request.POST.get('email', '')
# 		message = request.POST.get('message', '')
# 		feed = Feed(email=email, message=message)
# 		feed.save()
# 	return render(request, 'feedback.html')


def volunteer(request):
	
	if request.method=="POST":
		name = request.POST.get('name', '')
		email = request.POST.get('email', '')
		message = request.POST.get('message', '')
		valo = Valo(name=name, email=email, message=message)
		valo.save()
	return render(request, 'valo.html')


def Zoo(request):
    return render(request, 'Chamarajendra.html')

def Palace(request):
    return render(request, 'PALACE.html')

def Hills(request):
    return render(request, 'Chamundi.html')

def Gardens(request):
    return render(request, 'Brindavan.html')

def DEVS(request):
    return render(request, 'dev1.html')

def DEVS2(request):
    return render(request, 'dev2.html')
