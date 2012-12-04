from django.contrib import admin
from finance.models import Campaign, Advertiser, Rep, CampaignForm, Actual, Booked

from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import SimpleListFilter
from django.utils.translation import ugettext
import string


def AlphabetFilter(myTitle, parameter):
    
    class AlphabetListFilter(SimpleListFilter):
        # Human-readable title which will be displayed in the
        # right admin sidebar just above the filter options.
        # title = _('Advertiser- First Letter')
        title = ugettext(myTitle)
    
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
                tuples.append((i,ugettext(i)))
            for i in range(0,10):
                tuples.append((str(i),ugettext(str(i))))
            return(tuples)
    
        def queryset(self, request, queryset):
            try:
                return queryset.filter(advertiser__startswith=self.value())
            except:
                return

    return AlphabetListFilter



class RevenueAdmin(admin.TabularInline):
    model = Actual  
#    filter_vertical = ("date","actualRev,")
#    def actual_type(self, instance):
#        return instance.campaign.type
    fields = ['campaign', 'date', 'actualRev']
   
class CampaignRevAdmin(admin.ModelAdmin):
    model = Campaign
    ordering = ['campaign']
#    list_display = ('advertiser', 'industry')
    search_fields = ('campaign',)
    title = 'Advertiser- First Letter'
    parameter = 'advertiser'
    list_filter = (AlphabetFilter(title,parameter),)
    inlines = [RevenueAdmin,]    

class CampaignAdmin(admin.TabularInline):
    model = Campaign
    fields = ['campaign', 'start_date', 'end_date','repId', 'contracted_impr', 'contracted_deal', 'revised_deal', 'product','channel', 'cp']
    form = CampaignForm


class AdvertiserAdmin(admin.ModelAdmin):
    ordering = ['advertiser']
    list_display = ('advertiser', 'industry')
    search_fields = ('advertiser',)
    title = 'Advertiser- First Letter'
    parameter = 'advertiser' 
    list_filter = (AlphabetFilter(title,parameter),)    
    inlines = [CampaignAdmin,]
#    class Media:
#        js = ('/media/javascript/myJS.js',)



admin.site.register(Advertiser, AdvertiserAdmin)
#admin.site.register(Actual, RevenueAdmin)
admin.site.register(Campaign, CampaignRevAdmin)

