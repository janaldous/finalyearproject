from django.shortcuts import render
from graphos.sources.simple import SimpleDataSource
from graphos.renderers.gchart import BarChart

from .models import Cluster

def index(request):
    cluster1 = Cluster.objects.get(pk=1)

    data =  [
        ['Year', 'Sales', 'Expenses'],
        [2004, 1000, 400],
        [2005, 1170, 460],
        [2006, 660, 1120],
        [2007, 1030, 540],
    ]
    chart = BarChart(SimpleDataSource(data=data), options={'isStacked': 'percent'})

    context = {
        'cluster1': cluster1,
        'chart': chart,
        }
    return render(request, 'clusters/index.html', context)
