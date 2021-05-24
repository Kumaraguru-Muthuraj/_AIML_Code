from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from MailClient import callSendMail
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import pandas as pd
import json

restaurants = pd.read_csv('zomato.csv', engine='python')
restaurants = restaurants.drop_duplicates().reset_index(drop=True)
restaurants['City'] = restaurants['City'].apply(str.lower)
restaurants['City'] = restaurants['City'].apply(str.strip)
restaurants['Cuisines'] = restaurants['Cuisines'].apply(str.lower)

WeOperate = ['New Delhi', 'Gurgaon', 'Noida', 'Faridabad', 'Allahabad', 'Bhubaneshwar', 'Mangalore', 'Mumbai', 'Ranchi', 'Patna', 'Mysore', 'Aurangabad', 'Amritsar', 'Puducherry', 'Varanasi', 'Nagpur', 'Vadodara', 'Dehradun', 'Vizag', 'Agra', 'Ludhiana', 'Kanpur', 'Lucknow', 'Surat', 'Kochi', 'Indore', 'Ahmedabad', 'Coimbatore', 'Chennai', 'Guwahati', 'Jaipur', 'Hyderabad', 'Bangalore', 'Nashik', 'Pune', 'Kolkata', 'Bhopal', 'Goa', 'Chandigarh', 'Ghaziabad', 'Ooty', 'Gangtok', 'Shimla']


def cusineFound(inCusine, cusines):
    inCusine = inCusine.strip()
    cusines = cusines.strip()
    return cusines.find(inCusine)

def getZomatoRestaurants():   
    return restaurants

def getTopNRatedRestaurantsWithPriceRange(city, cuisine, priceRange, N):
    city = city.strip()
    cus = cuisine.strip()
    
    restaurants = getZomatoRestaurants()
    restaurants = restaurants[['Restaurant Name', 'City', 'Address', 'Cuisines', 'Price range', 'Aggregate rating', 'Average Cost for two']]
    
    f1 = restaurants['Cuisines'].apply(lambda x: cus in x.lower())    
    f2 = restaurants['City'].isin([city])
    f3 = restaurants['Price range'].isin([priceRange])
                                                            
    restaurants = restaurants[f1 & f2 & f3]
    
    retRows = restaurants.sort_values(by = 'Aggregate rating', ascending = False)
    retRows = retRows.head(N)
    return retRows

def getTopNRatedRestaurants(city, cuisine, N):
    city = city.strip()
    cus = cuisine.strip()
    
    restaurants = getZomatoRestaurants()
    restaurants = restaurants[['Restaurant Name', 'City', 'Address', 'Cuisines', 'Price range', 'Aggregate rating', 'Average Cost for two']]
    
    f1 = restaurants['Cuisines'].apply(lambda x: cus in x.lower())    
    f2 = restaurants['City'].isin([city])
                                                
    restaurants = restaurants[f1 & f2]
    
    retRows = restaurants.sort_values(by = 'Aggregate rating', ascending = False)
    retRows = retRows.head(N)
    return retRows

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		cuis = tracker.get_slot('cuisine')

		#if loc not in WeOperate:
		#	response = "We don't operate in that area"	
		#	dispatcher.utter_message(response)
		#	return [SlotSet('location',loc)]

		results = getTopNRatedRestaurants(city=loc, cuisine=cuis, N=5)
		response=""
		if results.shape[0] == 0:
			response= "no results"
		else:
			for restaurant in results.iterrows():
				restaurant = restaurant[1]
				response=response + F"Found {restaurant['Restaurant Name']} in {restaurant['Address']} rated {restaurant['Address']} with avg cost {restaurant['Average Cost for two']} \n\n"
				
		dispatcher.utter_message(response)
		return [SlotSet('location',loc)]


class SendMail(Action):
	def name(self):
		return 'email_restaurant_details'
		
	def run(self, dispatcher, tracker, domain):
		recipient = tracker.get_slot('email')
		loc = tracker.get_slot('location')
		cuis = tracker.get_slot('cuisine')

		results = getTopNRatedRestaurants(city=loc, cuisine=cuis, N=10)
		response=""
		if results.shape[0] == 0:
			response= "no results"
		else:
			for restaurant in results.iterrows():
				restaurant = restaurant[1]
				response=response + F"Found {restaurant['Restaurant Name']} in {restaurant['Address']} rated {restaurant['Address']} with avg cost {restaurant['Average Cost for two']} \n\n"
				
		print("Sending mail to {0}".format(recipient))

		callSendMail(recipient, response)

		dispatcher.utter_message("Have a great day!")
		return 

class Check_location(Action):
	def name(self):
		return 'action_check_location'
		
	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		check = check_location(loc)
		
		return [SlotSet('location',check['location_new']), SlotSet('location_found',check['location_f'])]