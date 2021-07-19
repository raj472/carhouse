from django import forms
from .models import product_person

class Personform(forms.ModelForm):
	first_name = forms.CharField(label= 'your name', 
		widget= forms.TextInput(
			attrs={
			"placeholder":"enter your name"
			}))


	class Meta:
		model=product_person
		fields=[
		'first_name',
		'middle_name',
		'last_name',
		'roll_no',
		'total_marks'
		]

	def class_title(self, *arg, **kwargs):
		first_name = self.cleaned_data.get("first_name")
		if "CFE" not in  first_name:
			raise ValidationError("this is not a valid name")
		
		return first_name
			
'''
	def class_title(self, *arg, **kwargs):
		first_name = self.cleaned_data.get("first_name")
		if not "raj" in first_name:
			raise forms.ValidationError("this is not valid name")
		if not "rajendra" in first_name:
			raise forms.ValidationError("this is not valid name")
		return first_name
'''


'''
	email = forms.EmailField()

	description = forms.CharField(required= False, 
		widget = forms.Textarea(
			attrs={
			"placeholder":'your description',
			"class":"new-class-name two",
			"id":'my-id-form-textarea',
			"rows":20,
			"cols":120
			}))
	price = forms.DecimalField(initial=199.999)
'''

	
	

'''	

	def class_email(self, *args, **kwargs):
		email =self.cleaned_data.get("email")
		if not email.endwith("com"):
			raise forms.ValidationsError("this is not a valid email")
		return email

'''

class RawProductForm(forms.Form):
	title = forms.CharField(max_length=30, label='title',
		                                 widget=forms.TextInput(
		                                 attrs={
		                                       "placeholder": "your title",  #appears transparent view
		                                        }
		                                    )
		                                )
	description = forms.CharField(max_length=100,
		                             required=True,
	                                 widget=forms.Textarea(
		                             attrs={
		                                  "placeholder":"your description"
		                                  
		                                  }
		                                )
	                            )  
	price = forms.DecimalField(initial=199.99)
	

  
	'''
	docstring for RawProductionForm"forms.Formf __init__(self, arg):
		super(RawProductionForm,forms.Form.__init__()
		self.arg = arg
	'''

class numbers(forms.Form):
	first_no = forms.DecimalField(max_digits=4, decimal_places=2, label ='first no',
                                  widget=forms.NumberInput(
                                  	attrs={
                                  	     "placeholder": "enter your first no"
                                  	     

                                  	}))
	operation = forms.CharField(max_length=4,label ='operation',
                                  widget=forms.TextInput(
                                  	attrs={
                                  	     "placeholder": "enter your first no"}
                                  	     
))
	second_no = forms.DecimalField(max_digits=4, decimal_places=2,label ='second no',
                                  widget=forms.NumberInput(
                                  	attrs={
                                  	     "placeholder": "enter your second no"}
                                  	     
))
	#answer = forms.DecimalField(max_digits=100, decimal_places=3,label='answer',
		                       #   widget=)
'''

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
		return operations()
	'''

class calc2(forms.Form):
	first_no = forms.IntegerField(required=False)
	second_no = forms.IntegerField(required=False)
	"""
	docstring for calc2"forms.Formf 
	first_no = forms.IntegerField(required=False)
	second_no = forms.Integerfield(required=False)__init__(self, arg):
		super(calc2,forms.Form._
		first_no = forms.IntegerField(required=False)
		second_no = forms.Integerfield(required=False)_init__()
		self.arg = arg
	"""
		