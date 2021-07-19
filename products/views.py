
from django.shortcuts import render
from .form import Personform 
from .form import RawProductForm
from .form import numbers, calc2
from django.views.generic import TemplateView  #in-built in base.py
from .models import Team

# Create your views here.
from .models import product_person

def product_details(request):
	obj=product_person.objects.get(id=1)  #some mistake here
	context={
	'object': obj
	}
	return render(request, "product/product_detail.html", context) 

'''
def Person_create_view(request):
	form = Personform(request.POST or None)
	if form.is_valid():
		form.save
		form=Personform
	context={
	'form': form
	}
	return render (request, "productH/person_detail.html", context)
'''

def Person_create_view(request):
	context={}
	#print(request.GET)
	#print(request.POST)
	your_first_name=request.POST.get("first name")
	print("user first name:-",your_first_name)
	your_middle_name=request.POST.get("middle name")
	print("user middle name:-",your_middle_name)
	your_last_name=request.POST.get("last name")
	print("user last name:-",your_last_name)
	your_roll_no=request.POST.get("roll no.")
	print("user rol no.:-",your_roll_no)


	return render (request, "productH/person_detail.html", context)



def person_details(request):
	form = Personform(request.POST or None)
	if form.is_valid():
		form.save
		form=Personform
	context={
	'form': form
	}
	#print(request.POST)
	a=request.POST.get("first_name")
	print("user first name :-", a)
	b=request.POST.get("middle_name")
	print("user second name:-",b)
	c=request.POST.get("last_name")
	print("user last name:-", c)
	d=request.POST.get("roll_no")
	print("user roll no. :-", d)
	e=request.POST.get("total_marks")
	print("user total marks", e)
	return render (request, "productH/product_person.html", context)


def product_create_view(request):
	my_form  = RawProductForm()   #this will render datat from form.py
	if request.method =='POST':
		my_form = RawProductForm(request.POST)  #this will save data
		if my_form.is_valid():
			#my_form.save
			
			

			print(my_form.cleaned_data)

		# now the data is good
		'''
		if the data is valid with no errors 
		then it will go forward and print the following
		'''
			
		#product_person.objects.create(**my_form.cleaned_data)
		
	else:
		print(my_form.errors) #this will comment where the errors are
		
	context={
	   "form" : my_form
	}
	return render (request, "productH/product_person.html", context)


def calculator(request):                        #pending project
	my_calc =numbers(request.POST or None)
	context ={
		"form" : my_calc

	}

	def operations():
		a=request.POST.get("first_no")
		a=int(a)
		print("first no.",a)
		b=request.POST.get("operation")
		print("operation",b)
		c=request.POST.get("second_no")
		c=int(c)
		print("second no.",c)

		if (b=='mul'):
			
			print("answer is",a*c)
		elif (b=='sub'):
			print("answer is ",a-c)
		elif (b=='+'):
			print("answer is ",a+c)
		elif (b=='div'):
			print("answer is ",a//c)

	#operations()
	'''
	a=request.POST.get("first_no")
	a=int(a)
	print("first no.",a)
	b=request.POST.get("operation")
	print("operation",b)
	c=request.POST.get("second_no")
	c=int(c)
	print("second no.",c)

	if (b=='mul'):
		
		print("answer is",a*c)
	elif (b=='sub'):
		print("answer is ",a-c)
	elif (b=='+'):
		print("answer is ",a+c)
	elif (b=='div'):
		print("answer is ",a//c)
	'''


	return render (request, "productH/calculator.html", context)

'''
This is Error
'''
class Homepage(TemplateView):   #Templeteview is in-built
	templete_name = 'productH/calc.html'


	def get(self,request, *args, **kwargs):
		form = calc2()     #executing calc2
		return render (request, self.templete_name,  #calling class object templete_name
			{'form': form})

	def post(self,request):
		form = calc2(request,POST)
		if form.is_valid():
			text = form.cleaned_data['num1']
			text2 = form.cleaned_data['num2']

			if 'add' in request.POST:
				result = text+text2

			elif 'sub' in request.POST:
				result = text-text2

			elif 'mul' in request.POST:
				result = text*text2

			elif 'div' in request.POST:
				result = text/text2

			form = calc2

		args={'form': form,'result':result
            }
		return render(request, self.templete_name, args)

	"""
	docstring for Homepage"ProductHf __init__(self, arg):
	super(Homepage,ProductH.__init__()
	self.arg = arg
		"""
		
def render_initial_data(request):
	initial_data = {'title':"mobiles"
	}
	form = RawProductForm(request.POST or None, initial=initial_data)
	context = {
		"form" : form
	}
	return render(request, 'productH/product_person.html', context)

def testing(request):
	queryset = Personform.objects.all()
	context ={
		"object_list": queryset
	}
	return render(request, "ProductH/person_detail.html", context)

def home(request):

    teams = Team.objects.all()
    data = {
    'teams' : teams,
    }
    return render(request,'ProductH/home.html',data)

def about(request):     #reuest= I'm taking the informaation from the browser(url)
    teams = Team.objects.all()
    data = {
    'teams' : teams,
    }
    return render(request, 'ProductH/about.html',data)   #I'm accepting the request toi render to the given page


def services(request):
    return render(request, 'ProductH/services.html')

def contact(request):
    return render(request, 'ProductH/contact.html')
