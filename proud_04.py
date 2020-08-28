'''
tuples versus lists
tuples are immutable, in this example coordinates

create a function
'''

cities = ["Barcelona", "Stockholm", "Frankfurt", "Milano", "London"]

coordinates = [(41.41,2.14), (59.33,18.06),(50.86,8.46),(46.98,9.97),(51.87,-0.12)]

def where_is_city(city):
    if city in cities:
        ind = cities.index(city)
        print(coordinates[ind])
    else:
        print("City is not in the list")

where_is_city(input("Enter a city to get coordinates: "))

