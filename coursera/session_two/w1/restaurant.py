'''Learn to Program: Crafting Quality Code | University of Toranto Computer Science
2018 Gina Fitzgerald'''

# Write a function that has 3 parameters:
#   -a restaurant file open for reading
#   -the price range ($, $$, $$$, $$$$)
#   -a list of cuisines
# Returns a list of restaurants (in that price range)
# serving at least one of those cuisines) and their
# ratings sorted from highest to lowest

'''Process: how to keep track of data
A. list out types of data we need to track
    1. restaurants and their scores
    Georgie Porgie: 87
    Queen St. Cafe: 82
    Dumplings R Us: 71
    Mexican Grill: 85
    Deep Fried Everything: 52

    2. restaurants in each price range
    $: Queen St. Cafe, Dumplings R Us, Deep Fried Everything
    $$: Mexican Grill
    $$$: Georgie Porgie
    $$$$:

    3. Which restaurant serve what typs of food
    Canadian: Georgie Porgie
    Pub Food: Georgie Porgie, Deep Fried Everything
    Malaysian: Queen St. Cafe
    Thai: Queen St. Cafe
    Chinese: Dumplings R Us
    Mexican: Mexican Grill

B. Consider What data structures we should use to represent this data
   1. restaurants and their scores: Dictionary (look up rating by name referencing dict)
   # dict of {str: int}
   name_to_rating = {
   'Georgie Porgie': 87,
   'Queen St. Cafe': 82,
   'Dumplings R Us': 71,
   'Mexican Grill': 85,
   'Deep Fried Everything': 52}

   2. restaurants in each price range: dictionary
   # dict of {str: lst}
   price_to_names = {
   '$': ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything'],
   '$$': ['Mexican Grill'],
   '$$$': ['Georgie Porgie'],
   '$$$$':[]}

   3. Which restaurant serve what typs of food: dictionary
   # dict of {str: lst}
   cuisine_to_names = {
   'Canadian': ['Georgie Porgie'],
   'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
   'Malaysian': ['Queen St. Cafe'],
   'Thai': ['Queen St. Cafe'],
   'Chinese': ['Dumplings R Us'],
   'Mexican': ['Mexican Grill']}



'''

# The file cotain restaurant data
FILENAME = 'restaurant.txt'

def restaurant_recs(file, price, cuisine_list):
    '''(file open for reading, str, list of str) -> lst of [int, str]

    Find restaurants in file that are priced according to price
    and tagged with any of the items in cuisine_list
    Returns a list of lists of the form:
    [ratings, restaurant name], sorted by rating

    >>> restaurant_recs(file, '$', ['Chinese', 'Thai'])
    [[82, 'Queen St. Cafe'], [71, 'Dumplings R Us']]
    '''

    # Read file build data structures
    # a dict of {restaurant name: ratings}
    # a dict of {price: list of restaurant names}
    # a dict of {cuisine: list of restaurant names}
    name_to_rating, price_to_names, cuisine_to_names = read_restaurants(file)


    # Look for price or cuisine first?
    # Price: look up the list of restaurant names for the requested price range


    # Now we have a list of restuarants in hte price range
    # Need a new list of retaurants that serve ond of the cuisines


    # Now we have a list of restaurants in the right price range and seve required cuisine
    # Need to look at ratings and sort list


    # Return sorted list

def read_restaurants(file):
    ''' (file) -> (dict, dict, dict)

    Reads file, returns touple of 3 dictionaries based on information from file
    - a dict of {restaurant name: ratings}
    - a dict of {price: list of restaurant names}
    - a dict of {cuisine: list of restaurant names}
    '''

    name_to_rating = {}
    price_to_names = {'$': [], '$$': [], '$$$': [], '$$$$': []}
    cuisine_to_names = {}

    # accumulate data in dictionary name_to_rating
    # accumulate data in dictionary name_to_rating
    line = file.readline()

    while line != '':
        restaurant_name = line.rstrip('%\n')
        line = file.readline() # move to next line- rating
        name_to_rating[restaurant_name] = int(line.rstrip('%\n'))
        line = file.readline() # move to $$
        line = file.readline() # move to cuisine type
        line = file.readline() # move to \n
        line = file.readline() # move to new restaurant name
            
    return name_to_rating
