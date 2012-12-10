from django.contrib import admin
from finance.models import Campaign, Advertiser, Rep, CampaignForm, Actual, Booked
from FinanceDjango.forms import CalculatorForm
import copy  # (1) use python copy

from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import SimpleListFilter
import string

from django.forms import TextInput, Textarea
from django.db import models
from django import forms


def advertiserAlphabetFilter(myTitle, parameter):
    class AlphabetListFilter(SimpleListFilter):
        # Human-readable title which will be displayed in the
        # right admin sidebar just above the filter options.
        # title = _('Advertiser- First Letter')
        title = _(myTitle)
    
        # Parameter for the filter that will be used in the URL query.
        # parameter_name = 'advertiser'
        parameter_name = parameter
    
        def lookups(self, request, model_admin):
            """
            Returns a list of tuples. The first element in each
            tuple is the coded value for the option that will
            appear in the URL query. The second element is the
            human-readable name for the option that will appear
            in the right sidebar.
            """  
            tuples = []
            for i in string.ascii_uppercase:
                tuples.append((i,_(i)))
            for i in range(0,10):
                tuples.append((str(i),_(str(i))))
            return(tuples)
    
        def queryset(self, request, queryset):
            try:
                return queryset.filter(advertiser__startswith=self.value())
            except:
                return
    return AlphabetListFilter

def campaignAlphabetFilter(myTitle, parameter):
    class AlphabetListFilter(SimpleListFilter):
        # Human-readable title which will be displayed in the
        # right admin sidebar just above the filter options.
        # title = _('Advertiser- First Letter')
        title = _(myTitle)
    
        # Parameter for the filter that will be used in the URL query.
        # parameter_name = 'advertiser'
        parameter_name = parameter
    
        def lookups(self, request, model_admin):
            """
            Returns a list of tuples. The first element in each
            tuple is the coded value for the option that will
            appear in the URL query. The second element is the
            human-readable name for the option that will appear
            in the right sidebar.
            """  
            tuples = []
            for i in string.ascii_uppercase:
                tuples.append((i,_(i)))
            for i in range(0,10):
                tuples.append((str(i),_(str(i))))
            return(tuples)
        
        def queryset(self, request, queryset):
            try:
                return queryset.filter(campaign__startswith=self.value())
            except:
                return
    return AlphabetListFilter


def copy_campaign(modeladmin, request, queryset):
    # cam is an instance of Campaign
    for cam in queryset:
        cam_copy = copy.copy(cam) # (2) django copy object
        cam_copy.id = None   # (3) set 'id' to None to create new object
        cam_copy.save()    # initial save

        # zero out some fields  
        # (6) Use __dict__ to access "regular" attributes (not FK or M2M)
        for attr_name in ['start_date', 'end_date', 'contracted_impr', 'contracted_deal', 'revised_deal']:
            cam_copy.__dict__.update({ attr_name : 0})
 
        # cam_copy.save()  # (7) save the copy to the database for M2M relations

    copy_campaign.short_description = "Make a Copy of Campaign"



class ActualAdmin(admin.TabularInline):
    model = Actual  
#    formfield_overrides = {
#        models.DecimalField: {'widget': TextInput(attrs={'size':'10'})},
#        #models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
#    }

 
class BookedAdmin(admin.TabularInline):
    model = Booked  
   
class CampaignRevAdmin(admin.ModelAdmin):
    model = Campaign
    ordering = ['campaign']
#    fields = [('campaign', 'start_date', 'end_date','repId','contracted_impr', 'contracted_deal', 'revised_deal', 'product','channel', 'cp'),]
#    list_display = ('advertiser', 'industry')
    search_fields = ('campaign',)
    title = 'Campaign- First Letter'
    parameter = 'campaign'
    list_filter = (campaignAlphabetFilter(title,parameter),)
    inlines = [BookedAdmin, ActualAdmin,]    
    form = CalculatorForm

    
    
class CampaignAdmin(admin.TabularInline):   
    model = Campaign
    fields = ['campaign', 'start_date', 'end_date','repId', 'contracted_impr', 'contracted_deal', 'revised_deal', 'product','channel', 'cp']
    form = CampaignForm


class AdvertiserAdmin(admin.ModelAdmin):
    actions = [copy_campaign] 
    ordering = ['advertiser']
    list_display = ('advertiser', 'industry')
    search_fields = ('advertiser',)
    title = 'Advertiser- First Letter'
    parameter = 'advertiser' 
    list_filter = (advertiserAlphabetFilter(title,parameter),)    
    inlines = [CampaignAdmin,]
#    class Media:
#        js = ('/media/javascript/myJS.js',)

class CalculatorAdmin(admin.ModelAdmin):
    model = Campaign


admin.site.register(Advertiser, AdvertiserAdmin)
#admin.site.register(Actual, RevenueAdmin)
admin.site.register(Campaign, CampaignRevAdmin)
#admin.site.register(Campaign, CalculatorAdmin)

