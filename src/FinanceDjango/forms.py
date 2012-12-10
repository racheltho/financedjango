from django import forms
from django.forms.formsets import formset_factory
from finance.models import Campaign
import datetime
    
    
class CalculatorForm(forms.ModelForm):
    numberDays = forms.IntegerField()
    
    class Meta:
        model = Campaign
        fields = ['campaign', 'start_date', 'end_date','repId','contracted_impr', 'contracted_deal', 'revised_deal', 'product','channel', 'cp']
        #fields = ('campaign','start_date','end_date', 'revised_deal')

    extra_field_count = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        extra_fields = kwargs.pop('extra', 0)

        super(CalculatorForm, self).__init__(*args, **kwargs)
        
        self.fields['extra_field_count'].initial = extra_fields

        for index in range(extra_fields):
            # generate extra fields in the number specified via extra_fields
            self.fields['extra_field_{index}'.format(index=index)] = \
                forms.DecimalField()
        
        
        
    
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