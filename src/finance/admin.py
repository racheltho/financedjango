from django.contrib import admin
from finance.models import Campaign, Advertiser, Rep, CampaignForm, Actual, Booked

from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import SimpleListFilter


#import string

class AlphabetListFilter(SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Advertiser- First Letter')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'advertiser'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """             
#        tuples = '('
#        
#        for i in string.ascii_uppercase:
#            tuples += '(\''
#            tuples += i
#            tuples += '\',_(\''
#            tuples += i
#            tuples += '\')),'
#       
#        tuples = tuples + ')'
                   
        return (
                ('A',_('A')),
                ('B',_('B')),
                ('C',_('C')),
                ('D',_('D')),
                ('E',_('E')),
                ('F',_('F')),
                ('G',_('G')),
                ('H',_('H')),
                ('I',_('I')),
                ('J',_('J')),
                ('K',_('K')),
                ('L',_('L')),                
                ('M',_('M')),
                ('N',_('N')),
                ('O',_('O')),
                ('P',_('P')),
                ('Q',_('Q')),
                ('R',_('R')),                
                ('S',_('S')),
                ('T',_('T')),
                ('U',_('U')),
                ('V',_('V')),
                ('W',_('W')),                
                ('X',_('X')),
                ('Y',_('Y')),
                ('Z',_('Z')),
                ('0',_('0')),
                ('1',_('1')),
                ('2',_('2')),
                ('3',_('3')),
                ('4',_('4')),
                ('5',_('5')),
                ('6',_('6')),
                ('7',_('7')),
                ('8',_('8')),
                ('9',_('9')),
                )

    def queryset(self, request, queryset):
        try:
            return queryset.filter(advertiser__startswith=self.value())
        except:
            return


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
    list_filter = (AlphabetListFilter,)
    inlines = [RevenueAdmin,]    

class CampaignAdmin(admin.TabularInline):
    model = Campaign
    fields = ['campaign', 'start_date', 'end_date','repId', 'contracted_impr', 'contracted_deal', 'revised_deal', 'product','channel', 'cp']
    form = CampaignForm


class AdvertiserAdmin(admin.ModelAdmin):
    ordering = ['advertiser']
    list_display = ('advertiser', 'industry')
    search_fields = ('advertiser',)
    list_filter = (AlphabetListFilter,)
    inlines = [CampaignAdmin,]
#    class Media:
#        js = ('/media/javascript/myJS.js',)



admin.site.register(Advertiser, AdvertiserAdmin)
#admin.site.register(Actual, RevenueAdmin)
admin.site.register(Campaign, CampaignRevAdmin)

