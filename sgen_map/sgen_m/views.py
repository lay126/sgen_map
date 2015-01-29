from django.shortcuts import render
from django.http import *

from django import forms
from django.shortcuts import *
from django.http import *
from django.core.context_processors import *
from django.views.decorators.csrf import *


def sgen_map(request):
	page_title = 'sgen_map'

	return render_to_response('sgen_map_total.html')