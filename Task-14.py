'''Using the URl https://restcountries.com/v3.1/all write a python program which wll do the following
1) Using the OOPS concept for the following concept
2) USE CLASS CONSTRUCTOR FOR TAKING INPUT THE ABOVE MENTIONED url FOR THE TASK
3) CREATE A METHOD THAT WILL fETCH ALL THE json DATA FROM THE url MENTIONED ABOVE
4) Create a Method that will display the name of Countries, Currencies and Currency symbols.
5)create a Method that will display all those sountries which will have DOLLAR as its currency
6) Create a method tha wil display all those countries which have EURO as its currency.'''




import requests


# 1) Using the OOPS concept for the following concept
class country:
    def __init__(self,url): # 2) USE CLASS CONSTRUCTOR FOR TAKING INPUT THE ABOVE MENTIONED url FOR THE TASK
        self.url = url
        self.data = self.json_data()

# 3) CREATE A mETHOD THAT WILL fETCH ALL THE json DATA FROM THE url MENTIONED ABOVE
    def json_data(self):
        response = requests.get(self.url)
        return response.json()

# 4) Create a Method that will display the name of Countries, Currencies and Currency symbols
# for convenience only common name is taken
    def name_currency(self):
        for country_data in self.json_data():
            print("Country: ", country_data["name"]["common"])
            currencies = country_data.get("currencies",{})
            for currency_data in currencies:
                print( "--Uses ",currency_data,"currency called as ",currencies[currency_data].get("name"),"and it's symbol is "
                      ,currencies.get(currency_data).get("symbol"))
            print()

# 5)create a Method that will display all those sountries which will have DOLLAR as its currency

    def dollar_currency(self):
        print("Countries using Dollar(American,Australian,Canadian,Newzealand) as currency are: ")
        dollar_countries = set()
        for country_data in self.data:
            currencies = country_data.get("currencies",{})
            for currency_data in currencies:
                currency = currencies[currency_data].get("name")
                if "dollar" in currency:
                    dollar_countries.add(country_data.get("name").get("common"))
        return dollar_countries
        

# 6) Create a method tha wil display all those countries which have EURO as its currency
 
    def euro_currency(self):
        print("Countries using EURO as currency are: ")
        euro_country_set = set()
        for country_data in self.data:
            currencies = country_data.get("currencies",{})
            for currency_data in currencies:
                currency = currencies[currency_data].get("name")
                if "euro" or "Euro" in currency:
                    euro_country_set.add(country_data.get("name").get("common"))
        return euro_country_set




url = "https://restcountries.com/v3.1/all"
c = country(url)
# Countries Name and their currencies and their symbol 
c.name_currency()

# Countries using DOLLAR as Currencies
dollar_countries = c.dollar_currency()
for country in dollar_countries:
    print("--",country)
print()

# Countries using EURO as Currencies
euro_countries = c.euro_currency()
for country in euro_countries:
    print("--",country)







#visit the URL https://www.openbrewerydb.org/documentation import requests which will do the following:
# 1) List the names of all breweries present in the sttes of Alaska Maine and Newyork.
# 2) What is the count of breweries in each of the states mentioned above?
# 3) Count the number of types of breweries present in individual cities of the state mentioned above
# 4) count and list how many breweries have websites in the states of Alaska. Mmaine and New york.


import requests

class Brewery:
    def __init__(self, url):
        self.url = url
        self.full_data = {} # contains all the data from all the three states [viz Alaska, Maine, New York ]
        self.brewery_names_in_state_data = {}
        self.brewery_types_city_data = {}


    def fetch_full_data(self,state):
        params = {"by_state": state}
        response = requests.get(self.url, params=params)
        state_data = response.json()
        self.full_data[state] = state_data 


# 1) List the names of all breweries present in the sttes of Alaska Maine and Newyork.
    def brewery_names_in_state(self):
        brewery_names_dict = {}
        for state,state_data in self.full_data.items():
            for entry in state_data:
                brewery_name = entry.get("name")
                if state not in brewery_names_dict:
                    brewery_names_dict[state] = []
                else:
                    brewery_names_dict[state].append(brewery_name)
        self.brewery_names_in_state_data = brewery_names_dict
        return brewery_names_dict
    

#2) What is the count of breweries in each of the states mentioned above?
    def brewery_count_in_state(self):
        brewery_count_dict = {}
        for state,state_data in self.brewery_names_in_state_data.items():
            brewery_count = len(state_data)
            if state not in brewery_count_dict:
                brewery_count_dict[state] = brewery_count
        
        return brewery_count_dict


#3) Count the number of types of breweries present in individual cities of the state mentioned above
    def brewery_types_in_city(self):
        types_city_dict = {}
        for state, state_data in self.full_data.items():
            types_city_dict[state] = {}
            for entry in state_data:
                city = entry.get("city")
                brewery_type = entry.get("brewery_type")
            
                if city not in types_city_dict[state]:
                    types_city_dict[state][city] = set()
                
                types_city_dict[state][city].add(brewery_type)

        self.brewery_types_city_data = types_city_dict


# 4) count and list how many breweries have websites in the states of Alaska. Mmaine and New york.
    def count_breweries_with_websites(self):
        website_count_dict = {}
        breweries_with_websites = {}

        for state,state_data in self.full_data.items():
            website_count_dict[state] = 0
            breweries_with_websites[state] = []
            for entry in state_data:
                website = entry.get("website_url")

                if website:
                    website_count_dict[state] += 1
                    breweries_with_websites[state].append(entry.get("name"))

        return website_count_dict, breweries_with_websites

    

url = "https://api.openbrewerydb.org/breweries"
brewery_info = Brewery(url)

states = ["Alaska", "Maine","New York"]
for state in states:
    brewery_info.fetch_full_data(state)
print()
print("Names of all breweries present in state of Alaska, Maine and New York")
for state,state_data in brewery_info.brewery_names_in_state().items():
    print("Name of all breweries in State: ",state)
    for entry in state_data:
        print("--",entry)
    print()

print()
print()
print("Count of breweries in Each States")
print(f"    {brewery_info.brewery_count_in_state()}")
print()
print()
print("Types of breweries in each city in all the states:")
brewery_info.brewery_types_in_city()
for state,city_data in brewery_info.brewery_types_city_data.items():
    print("Cities with brewery type in State:",state)
    for city,brewery_type in city_data.items():
        print("For City: ",city,"have ",len(brewery_type),"type of brewery")
        for types in brewery_type:
            print("--",types)
    print()

website_count,breweries_name_having_ws = brewery_info.count_breweries_with_websites()
print("list of breweries having websites in all three states viz Alaska, Maine,NewYork")
for state,breweries_with_ws in breweries_name_having_ws.items():
    print("Breweries with website in state: ",state)
    for entry in breweries_with_ws:
        print("--",entry)
    print()
print("Number of Breweries having websites in each states")
print(f"        {website_count}")
