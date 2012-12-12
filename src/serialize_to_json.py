import sys
import os
#import xlrd
#from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers
import datetime

sys.path.append('finance')
sys.path.append('FinanceDjango')

os.environ["DJANGO_SETTINGS_MODULE"] = "FinanceDjango.settings"

#from decimal import *
from finance.models import Rep, Campaign, Actual

def load_data():

    # Create and fill Tables        
    # wb = xlrd.open_workbook('C:/Users/rthomas/Desktop/DatabaseProject/SalesMetricData.xls')
    # wb.sheet_names()
    
    JSONserializer = serializers.get_serializer("json")
    json_serializer = JSONserializer()
   
    campaign_list = Campaign.objects.order_by('campaign')[0:20]
#    date_list = []
#    for year in range(2011,2013):
#        for month in range(1,13):
#            date_list.append(datetime.date(year, month, 1))
#    obj_list = []
    for myCampaign in campaign_list:
        myActual = Actual.objects.filter(campaign = myCampaign)
        filestr = "FinanceDjango/media/json/actual" + str(myCampaign.id) + ".json"     
        jsonfile = open(filestr,"w+")
        with jsonfile as out:
            json_serializer.serialize(myActual, stream=out)           
        jsonfile.close()


# Main
if __name__ == '__main__':
    print("hello")
    load_data()
    
    