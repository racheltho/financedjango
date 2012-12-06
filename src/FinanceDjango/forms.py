from django import forms
from django.forms.formsets import formset_factory
from finance.models import Campaign
import datetime
    
def make_date_form(start_date, end_date):
    date_list = []
    for year in range(2011,2013):
        for month in range(1,13):
            date_list.append(datetime.date(year, month, 1))
    fields = {}
    counter = 0
    for d in date_list:
        counter = counter + 1
        i = str(counter)
        fields[i+'_date'] = forms.DateField(d)
        fields[i+'_booked'] = forms.DecimalField(max_digits=14, decimal_places = 2)          
    return type('date_booked', (forms.BaseForm,), { 'base_fields': fields })               
            
    
class Calculator(forms.Form):
    class Meta:
        model = Campaign
        fields = ('campaign','start_date','end_date','contracted_deal','revised_deal')
    
    
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)
    message = forms.CharField(widget=forms.Textarea)
    
    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words!")
        return message
 


from finance.models import Poll, Choice

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        exclude = ('poll',)