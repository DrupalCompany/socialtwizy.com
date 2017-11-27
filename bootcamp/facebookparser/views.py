from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import facebook
import requests
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Group
from .models import Posts





# Social Groups Page
def groups(request):

    groups_list = Group.objects.order_by('-facebook_id').all()

    page = request.GET.get('page', 1)

    paginator = Paginator(groups_list, 10)
    try:
        groups = paginator.page(page)
    except PageNotAnInteger:
        groups = paginator.page(1)
    except EmptyPage:
        groups = paginator.page(paginator.num_pages)

    return render(request, 'pages/groups.html', {'groups': groups})

# Social Group Page
def group(request, group_slug, group_id):

    group = Group.objects.get(pk=group_id)

    posts = Posts.objects.filter(group_id = group_id).order_by('-pk')[:10:1]

    return render(request, 'pages/group.html', {'group':group, 'posts':posts})

# Social Group Posts
def posts(request):

    return render('request','pages/posts',{})