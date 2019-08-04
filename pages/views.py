from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from django.contrib import humanize
from listings.choices import price_choices, bedroom_choices, state_choices
# Create your views here.


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices
    }
    return render(request, 'pages/index.html', context)


def about(request):
    # get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    # create context
    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request, 'pages/about.html', context)
