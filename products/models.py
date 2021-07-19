from django.db import models

# Create your models here.

class product_person(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30)
    roll_no = models.DecimalField(max_digits=3, decimal_places=0)
    total_marks = models.DecimalField(max_digits=4, decimal_places=2)
    '''
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12, decimal_places=0)
    '''


class venue(models.Model):
 	name = models.CharField('Venue name',max_length=120)
 	address = models.CharField(max_length=300)
 	zip_code = models.CharField('zip/post code',max_length=120)
 	phone = models.CharField('contact phone',max_length=20, blank=True)
 	web = models.URLField('web Address', blank=True)
 	email_address = models.EmailField('Email Address', blank=True)

'''
 	docstring for venue"models.Modelef
 	name = models.CharField('Venue name', max_length=120)
 	address = models.CharField(max_length=300)
 	zip_code = models.CharField('zip/post code', max_lenght=12)
 	phone = models.CharField('contact phone', max_length=20, blank=True)
 	web = models.URLField('web Address', blank=True)
 	email_address = models.EmailField('Email Address', blank=True)
 '''
def __str__(self):
 	return self.name
'''
def __init__(self, *args, **kwargs):
    user = kwargs.pop('cfe')
    super(venue, self).__init__(*args, **kwargs)
'''

'''
 		super(venue,models.Model._
 		name = models.CharField('Venue name', max_length=120)
 		address = models.CharField(max_length=300)
 		zip_code = models.CharField('zip/post code', max_lenght=12)
 		phone = models.CharField('contact phone', max_length=20, blank=True)
 		web = models.URLField('web Address', blank=True)
 		email_address = models.EmailField('Email Address', blank=True)
 		_init__()
 		self.arg = arg


'''
class Team(models.Model):
    first_name = models.CharField(max_length= 255)
    last_name = models.CharField(max_length= 255)
    designation = models.CharField(max_length= 255)
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    facebook_link = models.URLField(max_length=100)
    twitter = models.URLField(max_length=100)
    google_plus = models.URLField(max_length=100)
    create_date = models.DateTimeField(auto_now = True)		


    def __str__(self):
        return self.first_name


   

  
	
