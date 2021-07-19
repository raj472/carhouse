"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages.views import home_view
from pages.views import contact_view
from pages.views import product_view
from pages.views import price_view
from pages.views import models_view
from pages.views import color_view
from pages.views import about_view
#from products.views import product_details
from products.views import Person_create_view
from products.views import person_details
from products.views import product_create_view
from products.views import calculator            #pending project
from products.views import Homepage
from products.views import render_initial_data
from products.views import testing
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
	path('model/', models_view ),
	path('color/', color_view),
	path('prices/', price_view),
	path('product/', product_view),
	path('contact/', contact_view),
    path('',home_view),
    path('admin/', admin.site.urls),
    #path('product2/', product_details),
    path('about/', about_view),
    path('detail/',Person_create_view),
    path('person_details/',person_details),
    path('product_create/', product_create_view),
    path('calculator/', calculator),      #pending project
    path('calc/', Homepage),
    path('initial_data/', render_initial_data),
    path('test/', testing),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
