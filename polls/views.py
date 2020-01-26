from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from googlemaps import GoogleMapsScraper
from datetime import datetime, timedelta
import argparse
import csv
from django.urls import reverse
from polls.forms import LoginForm

HEADER = ['id_review', 'rating', 'col1', 'review', 'timestamp', 'url_user', 'time_ago', 'user_name','col2']

def index(request):

    return render(request, "polls/index.html")

def csv_writer(path='polls/mydata/', outfile='gm_reviews.csv'):
	print('in csv')
	targetfile = open(path + outfile, mode='w', encoding='utf-8', newline='\n')
	writer = csv.writer(targetfile, quoting=csv.QUOTE_MINIMAL)
	writer.writerow(HEADER)
	return writer   

def save_file(request):
	print('in save')
	fileName='attachment;filename='+file+'.csv'
	data = open('polls/mydata/gm_reviews.csv','r').read()
	resp = HttpResponse(data, content_type='application/x-download')
	resp['Content-Disposition'] = fileName
	return resp		     

def submit(request):
	global file
	MyLoginForm = LoginForm(request.POST)
	if request.method == "POST":
		if MyLoginForm.is_valid():
			number = MyLoginForm.cleaned_data['number']
			url=MyLoginForm.cleaned_data['url']
			file=MyLoginForm.cleaned_data['file']
			writer = csv_writer() 			
			with GoogleMapsScraper() as scraper:
				# with open(args, 'r') as urls_file:
					# for url in urls_file:
							error = scraper.sort_by_date(url)
							if error == -1:
		                        # store reviews in CSV file
								n = 0
								while n < number:
									reviews = scraper.get_reviews(n)
									for r in reviews:
										writer.writerow(list(r.values()))
									n += len(reviews)
	return HttpResponseRedirect(reverse('polls:save_file'))													