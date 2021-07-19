from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home_view(request,*args, **kwargs):
	print(args, kwargs)
	return render(request,"home.html",{})

def contact_view(request,*args, **kwargs):  
	my_context={

		"my_text":"this is about us",
		"my_gmail":"abc@gmail.com",
		"my_list": [123,434,5355,'abc']


	}
	return render(request,"contact.html", my_context )

def product_view(request,*args, **kwargs):
	return render(request,"prodect.html",{})


def price_view(request,*args, **kwargs):
	return render(request,"price.html",{})

def color_view(request,*args, **kwargs):
	return render(request,"color.html", {})

def models_view(request,*args, **kwargs):
	return render(request,"models.html", {})

def about_view(request, *args, **kwargs):
	my_context2 = {
	"my_text": "this a about us",
	"my_gmail":"abc@gnail.com",
	"customer_care_no":123,
	"my_list": [123,434,5355,'abc']
	}
	return render(request, "about.html", my_context2)