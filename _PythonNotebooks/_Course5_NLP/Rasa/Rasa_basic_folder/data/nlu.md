## regex:greet
- hey[^\s]*

## regex:pincode
- [0-9]{6}

## regex:price
- ((^)(low|moderate|high))[^\\s]*

## regex:greet
- hey[^\\s]*

## regex:email
- [a-zA-Z0-9_.+]+@[a-zA-Z]+[.][a-zA-Z0-9-.]+$

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:more than 700
- >700
- mt 700

## synonym:between 300 to 700
- bw 300 and 700
- 300-700
- bw 300 & 700
- btw 300-700

## synonym:lesser than 300
- <300
- less 300
- less than 300
- lower 300
- 300 or less

## synonym:vegetarian
- veggie
- vegg
- veg

## synonym:4
- four

## synonym:Delhi
- New Delhi
- Dilli
- Delhi

## synonym:bangalore
- Bengaluru
- Begalore
- bangalore

## synonym:Kolkota
- Calcutta

## synonym:Chennai
- Madras

## intent:greet
- hey    
- howdy
- hey there    
- hello
- hi
- hi there      
- hey
- hi.
- Hi
- good morning
- good evening
- dear sir
- yess
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- i'm looking for a place in the [north](location) of town
- show me [chinese](cuisine) restaurants
- show me [chines](cuisine) restaurants in the [north](location)
- show me a [mexican](cuisine) place in the [centre](location)
- search for restaurants
- anywhere in [delhi](location)
- anywhere in [kolkata](location)
- anywhere in [kormangala](location)
- anywhere in [delhi](location)
- anywhere near [18328](location)
- I am looking for [asian](cuisine) fusion food
- I am looking a restaurant in [29432](location)
- in [London](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [italian](cuisine)
- [italian](cuisine)
- [italian](cuisine) food
- [Mexican](cuisine)
- [mexican](cuisine)
- [mexican](cuisine) food
- [Chinese](cuisine)
- [chinese](cuisine)
- [Lithuania](cuisine)
- in [delhi](location)
- in [ooty](location)
- in [calcutta](location)
- in [Calcutta](location)
- in [Ooty](location)
- In [Delhi](location)
- In [Delhi](location).
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Delhi](location)
- I am looking for some restaurants in [patna](location)
- I am looking for some restaurants in [Ooty](location)
- I am looking for some restaurants in [Calcutta](location)
- I am looking for some restaurants in [Koramangala](location)
- I am looking for some restaurants in [delhi](location)
- I am looking for [mexican](cuisine) [indian](cuisine) fusion
- can you book a table in rome with [british](cuisine) food for four people
- [american](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- i want to have [mexican](cuisine) food. suggest me some restaurants
- looking for [chinese](cuisine) places
- restaurants where [thai](cuisine) food is available
- find me some top [mexican](cuisine) restaurants in [mumbai](location)
- please suggest me some bakery of [kolkata](location)
- suggest me some restaurants where [biryani](cuisine) is available
- list me some top north [indian](cuisine) restaurants of [Mumbai](location)
- suggest some good cafes in [bangalore](location)
- i want to have [lebanese](cuisine) food in [chandigarh](location). Suggest me some restaurants
- suggest some good [vegetarian](cuisine) places to eat
- restaurants in budget [lesser than 300](price)
- restaurants with budget [between 300 to 700](price) for two people
- restaurants with budget [between 300-700](price) for two people
- show me restaurants where the budget for two people is [more than 700](price)
- show me restaurants where the budget for two people is [>700](price)
- [>700](price)
- [>700](price) price range
- [<300](price)
- [<300](price) price range
- [300-700](price)
- [300-700](price) price range
- [more than 700](price)
- [lesser than 300](price)
- [<300](price)
- [between 300 to 700](price)
- [Mumbai](location)
- [Delhi](location)
- [Bengaluru](location)
- [Ahmedabad](location)
- [Hyderabad](location)
- [Chennai](location)
- [Kolkata](location)
- [Pune](location)
- [Jaipur](location)
- [Lucknow](location)
- [Kanpur](location)
- [Nagpur](location)
- [Patna](location)
- [Indore](location)
- [Thane](location)
- [Bhopal](location)
- [Visakhapatnam](location)
- [Vadodara](location)
- [Firozabad](location)
- [Ludhiana](location)
- [Rajkot](location)
- [Agra](location)
- [american](cuisine) restaurant
- [show me american](cuisine) restaurants
- [show me american](cuisine) restaurants in [delhi](location)
- [american](cuisine) food
- i want to eat [american](cuisine)
- tell me where could I get [american](cuisine) food
- suggest me some [american](cuisine) restaurants in [chennai](location)
- [thai](cuisine) restaurant
- show me [thai](cuisine) restaurants
- show me [thai](cuisine) restaurants in [pune](location)
- [thai](cuisine) food
- i want to eat [thai](cuisine)
- [american](cuisine)
- tell me where I could get [thai](cuisine) food
- suggest me [thai](cuisine) restaurants
- [thai](cuisine)
- [north indian](cuisine)
- [north indian](cuisine) restaurant
- show me [north indian](cuisine) restaurant
- show me [north indian](cuisine) restaurants in [jaipur](location)
- [north indian](cuisine) food
- i want to eat [north indian](cuisine)
- tell me where I could get [north indian](cuisine) food
- suggest me [north indian](cuisine) restaurants in [mysore](location)
- find me some good resturants in [ooty](location)
- find me some restaurants in [calcutta](location)
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines](cuisine:chinese) restaurants in the [New Delhi](location:Delhi)
- show me [chines]{"entity": "cuisine", "value": "chinese"} restaurants in [New Delhi]{"entity": "location", "value": "Delhi"}
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese](cuisine:chinese)
- [chinese](cuisine)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- can you book a table in [rome](location) in a [moderate](price:mid) price range with [british](cuisine) food for [four](people:4) people
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- [mumbai](location)
- [Chinese](cuisine:chinese)
- show me restaurants
- [mumbai](location)
- [Italian](cuisine)
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one

## intent:affirm
- yes. please send it to [muthurajguru@gmail.com](email)
- yeah. please send it to [muthurajguru@gmail.com](email)
- cool. send all the restaurant details to [muthurajguru@gmail.com](email)
- [muthurajguru@gmail.com](email)
- okay, send it to [muthurajguru@gmail.com](email)
- can you please share the details on this id: [muthurajguru@gmail.com](email)
- yeah. cool. send it on [muthurajguru@gmail.com](email)
- yes. please email all the details to this address: [muthurajguru@gmail.com](email)
- thanks. sure send it.
- sure send it.
- please
- yes. please email all the details to this address: [muthurajguru@gmail.com](email)
- [muthurajguru@gmail.com](email)
- can you please share the details on this id: [muthurajguru@gmail.com](email)
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks
- thanks

## intent:deny
- no. thanks
- no
- noo
- nope
- no
- no. not required
- nope
- thanks. but not required
- naa
- i don't require it over mail. thanks