names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']


deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]


conversion = {"M": 1000000, "B": 1000000000}
def convert_damages_data(damages):
    updated_damages = []
    for damage in damages:
        if damage=='Damages not recorded':
            updated_damages.append(damage)
        if damage.find('M') != -1:
          updated_damages.append(float(damage[0:damage.find('M')])*conversion['M'])
        if damage.find('B') != -1:
            updated_damages.append(float(damage[0:damage.find('B')])*conversion['B'])
            
updated_damages = convert_damages_data(damages)




def hurricane_info(names, months, years, max_sustained_winds, areas_affected, damages, deaths 
):
    hurricanes = dict()
    num_hurricane = len(names)
    for i in range(num_hurricane):
        hurricanes[names[i]]={'Name':names[i],
                             'Months':months[i],
                             'Years':years[i],
                             'Max sustained winds':max_sustained_winds[i],
                             'Areas Affected':areas_affected[i],
                             'Damages':updated_damages[i],
                             'Deaths':deaths[i],
                             'Years':years[i],
                             'Years':years[i]}
    return hurricanes  

hurricanes = hurricane_info(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)


def hurricane_info_by_year(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    hurricanes_by_year_dict ={}
    num_hurricanes = len(years)
    for i in range(num_hurricanes):
        hurricanes_by_year_dict[years[i]] = {'Name':names[i],
                             'Months':months[i],
                             'Years':years[i],
                             'Max sustained winds':max_sustained_winds[i],
                             'Areas Affected':areas_affected[i],
                             'Damages':updated_damages[i],
                             'Deaths':deaths[i],
                             'Years':years[i],
                             'Years':years[i]}
    return hurricanes_by_year_dict 

hurricanes_by_year = hurricane_info_by_year(names, months, years, max_sustained_winds, areas_affected, damages, deaths)

def count_hurricanes(hurricanes):
    count_affected_areas = {}
    for cane in hurricanes:
        for area in hurricanes[cane]['Areas Affected']:
            if area not in count_affected_areas:
                count_affected_areas[area] = 1
            else:
                count_affected_areas[area] += 1
                
    return count_affected_areas 
areas_count = count_hurricanes(hurricanes)


def most_affected_area(count_affected_areas):
    max_area = 'Central America'
    max_area_count = 0
    for area in count_affected_areas:
        if count_affected_areas[area] > max_area_count:
            max_area = area
            max_area_count = count_affected_areas[area]
    return max_area, max_area_count
max_area, max_area_count = most_affected_area(areas_count)


def max_casualty(hurricanes):
    max_mortality_cane = 'Cuba I'    
    max_mortality = 0
    for max_death_toll in hurricanes:
        if max_mortality < hurricanes[max_death_toll]['Deaths']:
            
            max_mortality_cane = max_death_toll
            max_mortality = hurricanes[max_death_toll]['Deaths']
            
    return max_mortality_cane, max_mortality
max_mortality_cane, max_mortality = max_casualty(hurricanes)


def rate_hurricanes(hurricanes):
    mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
    hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
    for cane in hurricanes:
        num_of_mortalities = hurricanes[cane]['Deaths']
        if num_of_mortalities == mortality_scale[0]:
            hurricanes_by_mortality[0].append(cane)
        elif num_of_mortalities>mortality_scale[0] and num_of_mortalities<=mortality_scale[1]:
            hurricanes_by_mortality[1].append(cane)
        elif num_of_mortalities>mortality_scale[1] and num_of_mortalities<=mortality_scale[2]:
            hurricanes_by_mortality[2].append(cane)
        elif num_of_mortalities>mortality_scale[2] and num_of_mortalities<=mortality_scale[3]:
            hurricanes_by_mortality[3].append(cane)
        elif num_of_mortalities>mortality_scale[3] and num_of_mortalities<=mortality_scale[4]:
            hurricanes_by_mortality[4].append(cane)
        elif num_of_mortalities>mortality_scale[4]:
            hurricanes_by_mortality[5].append(cane)
    return hurricanes_by_mortality

hurricanes_by_mortality = rate_hurricanes(hurricanes)

        
       

def max_damage_and_costly(hurricanes):
    max_damage_cane = 'Cuba I'
    max_damage = 0
    for cane in hurricanes:
        if hurricanes[cane]['Damages']=="Damages not recorded":
            pass
        elif max_damage<hurricanes[cane]['Damages']:
            max_damage = hurricanes[cane]['Damages']
            max_damage_cane = cane
    return max_damage_cane, max_damage

max_damage_cane, max_damage = max_damage_and_costly(hurricanes)


def rate_hurricanes_by_damage(hurricanes):
    damage_rating_dict = {0:[],1:[],2:[],3:[],4:[],5:[]}
    damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
    for cane in hurricanes:
        if hurricanes[cane]['Damages']==damage_scale[0]:
            damage_rating_dict[0].append(cane)
            
        elif hurricanes[cane]['Damages'] > damage_scale[0] and hurricanes[cane]['Damages']<=damage_scale[1] :
            damage_rating_dict[1].append(cane)
            
        elif hurricanes[cane]['Damages'] > damage_scale[1] and hurricanes[cane]['Damages']<=damage_scale[2] :
            damage_rating_dict[2].append(cane)
            
        elif hurricanes[cane]['Damages'] > damage_scale[2] and hurricanes[cane]['Damages']<=damage_scale[3] :
            damage_rating_dict[3].append(cane)
            
        elif hurricanes[cane]['Damages'] > damage_scale[3] and hurricanes[cane]['Damages']<=damage_scale[4] :
            damage_rating_dict[4].append(cane)
        
        elif hurricanes[cane]['Damages'] > damage_scale[4]:
            damage_rating_dict[5].append(cane)
    return damage_rating_dict
damage_rating = rate_hurricanes_by_damage(hurricanes)

