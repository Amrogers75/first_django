from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from main.models import State, City, StateCapital
from django.template import RequestContext
from main.forms import ContactForm, CityEditForm
from main.forms import StateCapitalEditForm
from django.core.mail import send_mail
from django.conf import settings




def state_list(request):

    context = {}
    # text_string = "this is a string of text."
    states = State.objects.all()

    context['states'] = states

    return render_to_response('state_list.html', context, context_instance=RequestContext(request))


def state_detail(request, pk):

    context = {}

    state = State.objects.get(pk=pk)

    context['state'] = state

    return render_to_response('state_detail.html', context, context_instance=RequestContext(request))


def state_search(request):

    context = {}

    context['request'] = request

    # context['get_vars'] = request.GET.get('a', None)

    state = request.GET.get('state', None)

    if state !=None:
        states = State.objects.filter(name__icontains=state)
    else:
        states = State.objects.all()

    context['states'] = states

    return render_to_response('state_search.html', context, context_instance=RequestContext(request))

    # var1 = '%s' % dir(request)
    # var1 = str(request)

    # string = "<pre>%s %s</pre>" % (request.GET, request.POST)

    # return HttpResponse(var1)


def city_search(request):

    context = {}

    context['request'] = request

    city = request.GET.get('city', None)

    if city !=None:
        cities = City.objects.filter(name__icontains=city)
    else:
        cities = City.objects.all()

    context['cities'] = cities

    return render_to_response('city_search.html', context, context_instance=RequestContext(request))


def city_detail(request, pk):

    context = {}

    city = City.objects.get(pk=pk)

    context['city'] = city

    return render_to_response('city_detail.html', context, context_instance=RequestContext(request))


def city_create(request):

    context = {}

    context['request'] = request.method

    if request.method == 'POST':
        name = request.GET.get('name', None)
        county = request.GET.get('county', None)
        zip_code = request.GET.get('zip_code', None)
        latitude = request.GET.get('latitude', None)
        longitude = request.GET.get('longitude', None)
        state_id = request.POST.get('state', None)

        if state_id != None:
            state = State.objects.get(pk=state_id)
        else:
            state = State.objects.get(name=Texas)

        the_city, created = City.objects.get_or_create(name=name)

        the_city.county = county
        the_city.zip_code = zip_code
        the_city.latitude = latitude
        the_city.longitude = longitude

        the_city.save()

        context['created'] = 'Operation Successful'

    elif request.method == 'GET':
        print "it was a GET request"

    return render_to_response('city_create.html', context, context_instance=RequestContext(request))


def city_edit(request, pk):
    context = {}

    city = City.objects.get(pk=pk)

    form = CityEditForm(request.POST or None, instance=city)

    context['city'] = city
    context['form'] = form

    if form.is_valid():
        form.save()
        return redirect('/state_list/')


    return render_to_response('city_edit.html', context, context_instance=RequestContext(request))


def city_list(request):

    context = {}
    # text_string = "this is a string of text."
    cities = City.objects.all()

    context['cities'] = cities

    return render_to_response('city_list.html', context, context_instance=RequestContext(request))


def statecapital_detail(request, pk):

    context = {}

    statecapital = StateCapital.objects.get(pk=pk)

    context['statecapital'] = statecapital

    return render_to_response('statecapital_detail.html', context, context_instance=RequestContext(request))


def contact_view(request):

    context = {}
    
    form = ContactForm

    context['form'] = form
    if request.method == 'POST':
        form = ContactForm(request.POST)
        context['form'] = form
        if form.is_valid():

            name = form.cleaned.data['name']
            email = form.cleaned.data['email']
            phone = form.cleaned.data['phone']
            message = form.cleaned.data['message'] 
            
            send_mail('STATES SITE MESSAGE FROM %s' %
                        message,
                        email,
                        [settings.EMAIL_HOST_USER],
                        fail_silently=False
                        )
            context['message'] = "email sent"
        else:
            context['errors'] = forms.errors
    elif request.method == 'GET':
        form = ContactForm()
        context['form'] = form


    return render_to_response('contact_view.html', context, context_instance=RequestContext(request))


def statecapital_create(request):
    #pass
    context = {}

    context['request'] = request.method

    if request.method == 'POST':
        name = request.GET.get('name', None)
        county = request.GET.get('county', None)
        zip_code = request.GET.get('zip_code', None)
        latitude = request.GET.get('latitude', None)
        longitude = request.GET.get('longitude', None)
        state_id = request.POST.get('state', None)
            
        if state_id != None:
            state = State.objects.get(pk=state_id)
        else:
            state = State.objects.get(name=Texas)

        the_statecapital, created = State.objects.get_or_create(name=name)

        the_statecapital.county = county
        the_statecapital.zip_code = zip_code
        the_statecapital.latitude = latitude
        the_statecapital.longitude = longitude

        the_statecapital.save()

        context['created'] = 'Operation Successful'

    elif request.method == 'GET':
        print "it was a GET request"

    return render_to_response('statecapital_create.html', context, context_instance=RequestContext(request))


def statecapital_edit(request, pk):

    context = {}

    statecapital = State.objects.get(pk=pk)

    form = StateCapitalEditForm(request.POST or None, instance=statecapital)

    context['statecapital'] = statecapital
    context['form'] = form

    if form.is_valid():
        form.save()
        return redirect('/state_list/')


    return render_to_response('statecapital_edit.html', context, context_instance=RequestContext(request))


def statecapital_list(request):

    context = {}
    # text_string = "this is a string of text."
    statecapitals = StateCapital.objects.all()

    context['statecapitals'] = statecapitals

    return render_to_response('statecapital_list.html', context, context_instance=RequestContext(request))