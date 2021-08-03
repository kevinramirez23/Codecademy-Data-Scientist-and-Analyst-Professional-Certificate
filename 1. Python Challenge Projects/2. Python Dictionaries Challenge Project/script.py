# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def convert_damages_data(damages):
  conversion = {"M": 1000000, "B": 1000000000}
  # list.
  updated_damages = []
  # loop iterates through the "damages" list and converts each value to a float.
  for damage in damages:
    if damage == "Damages not recorded":
      updated_damages.append(damage)
    if damage[-1] == 'M':
      updated_damages.append(float(damage.strip('M'))*conversion["M"])
    if damage[-1] == 'B':
      updated_damages.append(float(damage.strip('B'))*conversion["B"])
  return updated_damages
# function call stored in a variable.
updated_damages = convert_damages_data(damages)
print(updated_damages)


# write your construct hurricane dictionary function here:
def create_dictionary(names, months, years, max_sustained_winds, areas_affected, deaths):
  # dictionary.
  hurricane_dictionary = {}
  # the number of values in the "names" list stored in a variable.
  num_hurricanes = len(names)
  # this loop iterates through each list and creates a dictionary for each dictionary in the below format.
  for hurricane in range(num_hurricanes):
    hurricane_dictionary[names[hurricane]] = {"Name": names[hurricane],
                                             "Month": months[hurricane],
                                             "Year": years[hurricane],
                                             "Max Sustained Wind": max_sustained_winds[hurricane],
                                             "Areas Affected": areas_affected[hurricane],
                                             "Damage": updated_damages[hurricane],
                                             "Deaths": deaths[hurricane]}
  return hurricane_dictionary
# function call stored in a variable.
hurricane_dictionary = create_dictionary(names, months, years, max_sustained_winds, areas_affected, deaths)
print(hurricane_dictionary)


# write your construct hurricane by year dictionary function here:
def create_dictionary_by_year(names, months, years, max_sustained_winds, areas_affected, deaths):
  # dictionary.
  year_dictionary = {}
  # variable that store the number of data values in the "years" dictionary.
  year_hurricanes = len(years)
  # this loop iterates through each list and creates a dictionary for each dictionary in the below format.
  for hurricane in range(year_hurricanes):
    year_dictionary[years[hurricane]] = {"Name": names[hurricane],
                                             "Month": months[hurricane],
                                             "Year": years[hurricane],
                                             "Max Sustained Wind": max_sustained_winds[hurricane],
                                             "Areas Affected": areas_affected[hurricane],
                                             "Damage": updated_damages[hurricane],
                                             "Deaths": deaths[hurricane]}
  return year_dictionary
# function call stored in a variable.
hurricane_year_dictionary = create_dictionary_by_year(names, months, years, max_sustained_winds, areas_affected, deaths)
print(hurricane_year_dictionary)
  

# write your count affected areas function here:
def probability_affected_areas(hurricane_dictionary):
  # dictionary.
  affected_area_dictionary = {}
  # this loop iterates through the hurricane dictionary and then through each affected area.
  for hurricane in hurricane_dictionary:
    for area in hurricane_dictionary[hurricane]["Areas Affected"]:
      # this control flow counts the number of times an area is affected.
      if area in affected_area_dictionary:
        count = count + 1
        affected_area_dictionary[area] = count
      else: 
        count = 1
        affected_area_dictionary[area] = count
  return affected_area_dictionary
# function call stored within a variable. 
affected_area_dictionary = probability_affected_areas(hurricane_dictionary)
print(affected_area_dictionary)
  
      
# write your find most affected area function here:
def area_most_affected(affected_area_dictionary):
  max_area = 'Central America'
  max_area_count = 0
  # iterates through each area within the dictionary to find which area is most affected and returns that key with its value.
  for area in affected_area_dictionary:
    if affected_area_dictionary[area] > max_area_count:
      max_area = area
      max_area_count = affected_area_dictionary[area]
  return max_area, max_area_count
# function call stored within a variable.
max_area, max_area_count = area_most_affected(affected_area_dictionary)
print(max_area, max_area_count)

# write your greatest number of deaths function here:
def hurricane_mortality(hurricane_dictionary):
  max_mortality_cane = 'Cuba I'
  max_mortality = 0

  for typhoon in hurricane_dictionary:
    if hurricane_dictionary[typhoon]['Deaths'] > max_mortality:
      max_mortality_cane = typhoon
      max_mortality = hurricane_dictionary[typhoon]['Deaths']
  return max_mortality_cane, max_mortality

max_mortality_cane, max_mortality = hurricane_mortality(hurricane_dictionary)
print(max_mortality_cane, max_mortality)


# write your catgeorize by mortality function here:
def categorize_mortality(hurricane_dictionary):
  mortality_scale = {0: 0,
                    1: 100,
                    2: 500,
                    3: 1000,
                    4: 10000}
  hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for typhoon in hurricane_dictionary:
    num_deaths = hurricane_dictionary[typhoon]['Deaths']
    if num_deaths == mortality_scale[0]:
      hurricanes_by_mortality[0].append(hurricane_dictionary[typhoon])
    elif num_deaths > mortality_scale[0] and num_deaths <= mortality_scale[1]:
      hurricanes_by_mortality[1].append(hurricane_dictionary[typhoon])
    elif num_deaths > mortality_scale[1] and num_deaths <= mortality_scale[2]:
      hurricanes_by_mortality[2].append(hurricane_dictionary[typhoon])
    elif num_deaths > mortality_scale[2] and num_deaths <= mortality_scale[3]:
      hurricanes_by_mortality[3].append(hurricane_dictionary[typhoon])
    elif num_deaths > mortality_scale[3] and num_deaths <= mortality_scale[4]:
      hurricanes_by_mortality[4].append(hurricane_dictionary[typhoon])
    elif num_deaths > mortality_scale[4]:
      hurricanes_by_mortality[5].append(hurricane_dictionary[typhoon])
  return hurricanes_by_mortality

hurricanes_by_mortality = categorize_mortality(hurricane_dictionary)
print(hurricanes_by_mortality)


# write your greatest damage function here:
def greatest_damage(hurricane_dictionary):
  max_damage_cane = 'Cuba I'
  max_damage = 0

  for typhoon in hurricane_dictionary:
    if hurricane_dictionary[typhoon]['Damage'] == 'damage not recorded':
      pass
    elif hurricane_dictionary[typhoon]['Damage'] > max_damage:
      max_damage_cane = typhoon
      max_damage = hurricane_dictionary[typhoon]['Damage']
  return max_damage_cane, max_damage

max_damage_cane, max_damage = greatest_damage(hurricane_dictionary)
print(max_damage_cane, max_damage)


# write your catgeorize by damage function here:
def categorize_damage(hurricane_dictionary):
  damage_scale = {0: 0,
                  1: 100000000,
                  2: 1000000000,
                  3: 10000000000,
                  4: 50000000000}
  hurricanes_by_damages = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for typhoon in hurricane_dictionary:
    num_damages = hurricane_dictionary[typhoon]['Damages']
    if num_damages == damage_scale[0]:
      hurricanes_by_damages[0].append(hurricane_dictionary[typhoon])
    elif num_damages > damage_scale[0] and num_damages <= damage_scale[1]:
      hurricanes_by_damages[1].append(hurricane_dictionary[typhoon])
    elif num_damages > damage_scale[1] and num_damages <= damage_scale[2]:
      hurricanes_by_damages[2].append(hurricane_dictionary[typhoon])
    elif num_damages > damage_scale[2] and num_damages <= damage_scale[3]:
      hurricanes_by_damages[3].append(hurricane_dictionary[typhoon])
    elif num_damages > damage_scale[3] and num_damages <= damage_scale[4]:
      hurricanes_by_damages[4].append(hurricane_dictionary[typhoon])
    elif num_damages > damage_scale[4]:
      hurricanes_by_damages[5].append(hurricane_dictionary[typhoon])
  return hurricanes_by_damages

hurricanes_by_damages = categorize_damage(hurricane_dictionary)
print(hurricanes_by_damages)