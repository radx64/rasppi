from django.shortcuts import render
from monitor.models import Temperature
from datetime import datetime, timedelta

CHART_TYPES = {
	'0': "3 godziny",
	'1': '24 godziny',
	'2': '3 dni'
}

def index(request, chart_interval='0'):
	title = "Wykres temperatury z ostatnich %s" % CHART_TYPES[chart_interval]
	
	if chart_interval not in CHART_TYPES.keys():
		chart_interval = '0'

	if chart_interval == '0':
		temperature_list = Temperature.objects.filter(date__gte=(datetime.today()-timedelta(hours=3)))
	elif chart_interval == '1':
		temperature_list = Temperature.objects.filter(date__gte=(datetime.today()-timedelta(days=1)))
	elif chart_interval == '2':
		temperature_list = Temperature.objects.filter(date__gte=(datetime.today()-timedelta(days=3)))

	return render(request, 'index.html', {
		'title': title,
		'chart_types': sorted(CHART_TYPES.iteritems()),
		'chart_interval': chart_interval,
		'temperature_list': temperature_list,
	})

