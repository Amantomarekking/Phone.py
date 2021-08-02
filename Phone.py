# Phone.py

import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone

a=input("enter number:")
phone_number=phonenumbers.parse(a)
print(geocoder.description_for_number(phone_number ,"en"))
print(carrier.name_for_number(phone_number ,"en"))
print(timezone.time_zones_for_number(phoneNumber,"en"))

