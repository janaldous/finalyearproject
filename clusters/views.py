from django.shortcuts import render
from graphos.sources.simple import SimpleDataSource
from graphos.renderers.gchart import BarChart, ColumnChart

from .models import Cluster

import readcsv as rc

def index(request):
    cluster1 = Cluster.objects.get(pk=1)

    charts = []
    
    questions_to_show = ['Q11', 'QGEN', 'QAGE', 'QETH']

    for question in questions_to_show:
        data =  rc.get_data(question)
        charts.append(BarChart(SimpleDataSource(data=data), options={'title': question, 'isStacked': 'percent'}))

    questions_to_show = ['Q5', 'Q26', 'Q29', 'Q39', 'Q50']

    for question in questions_to_show:
        data =  rc.get_data2(question)
        charts.append(BarChart(SimpleDataSource(data=data), options={'title': question}))

    data = rc.get_data_for_column_chart()
    charts.append(ColumnChart(SimpleDataSource(data=data), options={'title': "Q13"}))

    context = {
        'cluster1': cluster1,
        'charts': charts,
        }
    return render(request, 'clusters/index.html', context)
