import sys
import os
#import xlrd
#from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers

sys.path.append('finance')
sys.path.append('FinanceDjango')

os.environ["DJANGO_SETTINGS_MODULE"] = "FinanceDjango.settings"

#from decimal import *
from finance.models import Rep, Campaign

def load_data():

    # Create and fill Tables        
    # wb = xlrd.open_workbook('C:/Users/rthomas/Desktop/DatabaseProject/SalesMetricData.xls')
    # wb.sheet_names()
    
    JSONserializer = serializers.get_serializer("json")
    json_serializer = JSONserializer()
#    json_serializer.serialize(queryset)
#    data = json_serializer.getvalue()
    
    with open("FinanceDjango/media/javascript/campaign.json", "w") as out:
        json_serializer.serialize(Campaign.objects.all(), stream=out)


# Main
if __name__ == '__main__':
    print("hello")
    load_data()
    
    