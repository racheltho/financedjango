from django.db import models
from django import forms

import datetime
from django.utils import timezone

# Create your models here.

class Type(models.Model):
    type = models.CharField(max_length=20)
    def __unicode__(self):
        return self.type
    
class Product(models.Model):
    product = models.CharField(max_length=20)
    def __unicode__(self):
        return self.product

class Channel(models.Model):
    channel = models.CharField(max_length=20)
    def __unicode__(self):
        return self.channel

class Dept(models.Model):
    dept = models.CharField(max_length=20)
    def __unicode__(self):
        return self.channel    
    
class Rep(models.Model):
    repID = models.CharField(max_length=4)
    last_name = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    employeeID = models.CharField(max_length=4, null=True, blank=True) 
    date_of_hire = models.DateField(null=True, blank=True)
    department = models.ForeignKey(Dept, null=True, blank=True)
    channel = models.ForeignKey(Channel, null=True, blank=True)
    manager = models.ForeignKey('self', null=True, blank=True)
    class Meta:
        ordering = ["last_name"]
    def __unicode__(self):
        #return self.repID
        return u"%s, %s" % (self.last_name, self.first_name)


class Industry(models.Model):
    sic = models.IntegerField('SIC code', null=True, blank=True)
    naics = models.IntegerField('NAICS code', null=True, blank=True)
    industry_name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.industry_name
   
class ParentAgency(models.Model):   
    parent = models.CharField(max_length=200)
    def __unicode__(self):
        return self.parent
   
class Advertiser(models.Model):
    advertiser = models.CharField(max_length=200)
    parent = models.ForeignKey(ParentAgency, null=True, blank=True)
    industry = models.ForeignKey(Industry,null=True, blank=True)
    def __unicode__(self):
        return self.advertiser


class CP(models.Model):
    cp = models.CharField('CPA/CPM', max_length=4)
    def __unicode__(self):
        return self.cp
 
class Campaign(models.Model):
    campaign = models.CharField(max_length=200)
    type = models.ForeignKey(Type, null=True, blank=True)
    product = models.ForeignKey(Product, null=True, blank=True)
    channel = models.ForeignKey(Channel, null=True, blank=True)    
    advertiser = models.ForeignKey(Advertiser, null=True, blank=True)
    repId = models.ForeignKey(Rep, null=True, blank=True)
    cp = models.ForeignKey(CP, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    cpm_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    contracted_impr = models.IntegerField(null=True, blank=True)
    contracted_deal = models.DecimalField(max_digits=18, decimal_places=2, null=True, blank=True)
    revised_deal = models.DecimalField(max_digits=18, decimal_places=2, null=True, blank=True)
    def __unicode__(self):
        return self.campaign
    def get_absolute_url(self):
        return u"/note/%s/" % self.campaign


class Booked(models.Model):
    campaign = models.ForeignKey(Campaign)
    date = models.DateField()
    bookedRev = models.DecimalField(max_digits=14, decimal_places = 2)
    def __unicode__(self):
        return self.bookedRev
    
       
class Actual(models.Model):
    campaign = models.ForeignKey(Campaign)
    date = models.DateField()    
    actualRev = models.DecimalField(max_digits=14, decimal_places = 2)    
    def __unicode__(self):
        return str(self.actualRev)
    def __str__(self):
        return self.actualRev

class CampaignForm(forms.ModelForm):       
    class Meta:
        model = Campaign

    
#    REPID_CHOICES = [('', '-- choose a Rep --'), ] + [(r.rep, r.rep) for r in Rep.objects.all()]
#    CHANNEL_CHOICES = [(c.channel, c.channel) for c in Channel.objects.all()]
#    CHANNEL_CHOICES.insert(0, ('', '-- choose a Rep first --'))
    
#    repId = forms.ChoiceField(widget=forms.Select(attrs={'onchange':'get_channel();'}))
#    channel = forms.ChoiceField(choices=CHANNEL_CHOICES)    
    
    def clean_channel(self):
        repId = self.cleaned_data['repId']
        formChannel = self.cleaned_data['channel']
        repChannel = Rep.objects.get(repID = repId).channel
        if not repChannel == formChannel:
            raise forms.ValidationError("RepId and Channel do not match!")
        return formChannel


class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.question
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()
    def __unicode__(self):
        return self.choice