
from django.shortcuts import render

def groups(request):

    return render(request, 'groups/feeds.html', {
        'groups': [],
        'from_feed': [],
        'page': 1,
        })


