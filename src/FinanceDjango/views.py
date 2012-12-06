# Create your views here.

#from django.template.loader import get_template
#from django.template import Context
from django.shortcuts import render_to_response
from forms import ContactForm

from finance.models import Advertiser, Actual, Campaign
from django.http import HttpResponse, Http404
import datetime

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.template import RequestContext, Context


def hello(request):   
    return render_to_response('learning.html')

def actualRev(request):
    campaign_list = Campaign.objects.order_by('campaign')[50:100]
    date_list = []
    for year in range(2011,2013):
        for month in range(1,13):
            date_list.append(datetime.date(year, month, 1))
    obj_list = []
    for myCampaign in campaign_list:
        #print(myCampaign.campaign)
        temp_list = []
        for date_item in date_list:
            #print(date_item)
            #a = myCampaign.booked_set.filter(date = date_item)
            #if a:
            #    print a[0].bookedRev
            temp_list.append(myCampaign.getActualRev(date_item))
        rev_object = {'id': myCampaign.id,
                      'name': myCampaign.campaign,
                      'rev_list': temp_list}
        obj_list.append(rev_object)          
    return render_to_response('displayRevenue.html', {'obj_list': obj_list, 
                                                      'date_list' : date_list, 
                                                      'title': 'Actual Revenue', })
    
def bookedRev(request):
    campaign_list = Campaign.objects.order_by('campaign')[50:100]
    date_list = []
    for year in range(2011,2013):
        for month in range(1,13):
            date_list.append(datetime.date(year, month, 1))
    obj_list = []
    for myCampaign in campaign_list:
        #print(myCampaign.campaign)
        temp_list = []
        for date_item in date_list:
            #print(date_item)
            #a = myCampaign.booked_set.filter(date = date_item)
            #if a:
            #    print a[0].bookedRev
            temp_list.append(myCampaign.getBookedRev(date_item))
        rev_object = {'id': myCampaign.id,
                      'name': myCampaign.campaign,
                      'rev_list': temp_list}
        obj_list.append(rev_object)          
    return render_to_response('displayRevenue.html', {'obj_list': obj_list, 
                                                      'date_list' : date_list, 
                                                      'title': 'Booked Revenue', })
    

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'rthomas@quantcast.com'),
                ['rthomas@quantcast.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render_to_response('contact_form.html', {'form': form}, RequestContext(request,{}))


def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            advertisers = Advertiser.objects.filter(advertiser__icontains=q)
            return render_to_response('search_results.html',
                {'advertisers': advertisers, 'query': q})
    return render_to_response('search_form.html',
        {'errors': errors})

    
def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))


def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', {'current_date': now})


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)


def my_homepage_view(request):
    return HttpResponse("Quantcast: Measure + Advertise")


from finance.models import Poll, Choice
from forms import PollForm, ChoiceForm

def add_poll(request):
    if request.method == "POST":
        pform = PollForm(request.POST, instance=Poll())
        cforms = [ChoiceForm(request.POST, prefix=str(x), instance=Choice()) for x in range(0,3)]
        if pform.is_valid() and all([cf.is_valid() for cf in cforms]):
            new_poll = pform.save()
            for cf in cforms:
                new_choice = cf.save(commit=False)
                new_choice.poll = new_poll
                new_choice.save()
            return HttpResponseRedirect('/polls/add/')
    else:
        pform = PollForm(instance=Poll())
        cforms = [ChoiceForm(prefix=str(x), instance=Choice()) for x in range(0,3)]
    return render_to_response('add_poll.html', {'poll_form': pform, 'choice_forms': cforms})



#def ajax_color_request(request):
#    # Expect an auto 'type' to be passed in via Ajax and POST
#    if request.is_ajax() and request.method == 'POST
#        auto_type = Auto.objects.filter(type=request.POST.get('type', ''))
#        colors = auto_type.colors.all() # get all the colors for this type of auto.
#    return render_to_response('auto/ajax_color_request.html', locals())









