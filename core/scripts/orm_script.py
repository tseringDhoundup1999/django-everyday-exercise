from core.models import Restaurant,Rating,Sale
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User 

from pprint import pprint

def run():
    

    print(Rating.objects.exclude(rating__lte=3))
    # print(connection.queries)
    print("-------------------")
    
    










    