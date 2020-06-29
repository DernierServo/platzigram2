"""Platzigram views"""

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime
import json

def hello_world(request):
    """ Return a greeting """
    now = datetime.now().strftime('%b %dth, %Y-%H:%M hrs ')
    return HttpResponse(f'Oh, hi! Current server time is {now}')


def sorted_numbers(request):
    """Return a JSON reponse with sorted integers."""
    #import pdb; pdb.set_trace() #Python Debugger
    numbers = [int(n) for n in request.GET['numbers'].split(',')]
    sorted_numb = sorted(numbers)
    response = {
        'status': 'ok',
        'numbers': sorted_numb,
        'message': 'Integers sorted successfully!'
    }
    #import pdb; pdb.set_trace() #Python Debugger
    return HttpResponse(
        json.dumps(response, indent=4), 
        content_type='application/json'
    )


def say_hi(request, p_name, p_age):
    """Say hi!"""
    
    if p_age < 12:
        message = f'Sorry {p_name}, you are not allowed here!'
    else:
        message = f'Hello, {p_name}! Welcome to Platzigram! ;)'

    return HttpResponse(message)