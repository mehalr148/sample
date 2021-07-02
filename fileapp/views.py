from django.shortcuts import render

# Create your views here.

import fileapp
from django.http import request
from django.urls import reverse
from django.conf import settings

from django.http import HttpResponse , HttpResponseRedirect

from fileapp import models
from fileapp.models import * 

import PyPDF2
import pandas as pd
# from docx2pdf import convert
import os


def index(request):

	if request.method== "POST":
		print('yes')

		myfile = request.FILES.getlist("uploadfiles[]")
		print(myfile)

		for f in myfile:
			print(f)
			upload_CV(myfiles=f).save()

		extract_info()


        
        
            

	return render(request,'index.html')


def home(request):
  

	return render(request,'home.html')


def extract_info():

	path = os.listdir("C:/Users/User/Desktop/MyDjangoStuff/myproj/media")

	email = []
	mobile = []
	num =0

	for i,files in enumerate(path):


	    filename = files
	    
	    if files[-4:]=='.pdf':
	        num = num+1 
	        
	        text = ''

	        read =  PyPDF2.PdfFileReader(f'C:/Users/User/Desktop/MyDjangoStuff/myproj/media/{filename}')
	        
	        pages = read.getNumPages()
	        
	        for p in range(pages):
	            
	            text+= read.getPage(p).extractText()
	            

	        text = text.split()

	        for word in text:
	            if '@' in word:
	                email.append(word)
	            elif len(word)==10:
	                try:
	                    n = int(word)
	                    mobile.append(n)
	                except:
	                    pass
	                
	                

	        if len(email)== num-1:
	            email.append('NA')
	        if len(mobile)==num-1:
	            mobile.append('NA')
	                    
	print(email)
	print(mobile)


	df = pd.DataFrame(({'Email': email,'Phone': mobile ,}))


	print(df)

	df.to_excel(os.path.join(settings.MEDIA_ROOT, 'Excel_Sample.xlsx')) 
	

def excel(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'Excel_Sample.xlsx')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response


