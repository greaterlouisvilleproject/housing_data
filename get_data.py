# Dataframes and data manipulation
import pandas as pd
# API calls
import requests
# Store the results of the API call
import json

# Read in census API key from a txt file
# You can get your own API key here: https://www.census.gov/data/developers.html
with open('census_key.txt') as key:
  api_key = key.read().strip()
  
# To find tables you want you can use the '2019 ACS Table List'
# Available online here: #https://www.census.gov/programs-surveys/acs/technical-documentation/table-shells.html

# A helper function to call census data by table, state, and country
def get_census_acs_19(table, state, county):
  # Set the core url for the API for 2019 1 year ACS data
  base_url = f'https://api.census.gov/data/2019/acs/acs1?get=NAME,'

  # Add in the table, county, and state info
  data_url = f'{base_url}{table}&for=county:{county}&in=state:{state}&key={api_key}'
  
  # Get the data
  response=requests.get(data_url)

  # Transform data and put into pandas df
  data = response.json()
  df = pd.DataFrame(data[1:], columns=data[0])
  
  return df

# Here we call the helper function, specifying state and county each time
def get_census_peers_19(table):
  df_al = get_census_acs_19(table = table, state = '01', county = '073')
  df_in = get_census_acs_19(table = table, state = '18', county = '097')
  df_ky = get_census_acs_19(table = table, state = '21', county = '111')
  df_mi = get_census_acs_19(table = table, state = '26', county = '081')
  df_mo = get_census_acs_19(table = table, state = '29', county = '095, 189, 510')
  df_ne = get_census_acs_19(table = table, state = '31', county = '055')
  df_nc = get_census_acs_19(table = table, state = '37', county = '081, 119')
  df_oh = get_census_acs_19(table = table, state = '39', county = '049, 061')
  df_ok = get_census_acs_19(table = table, state = '40', county = '109, 143')
  df_sc = get_census_acs_19(table = table, state = '45', county = '045')
  df_tn = get_census_acs_19(table = table, state = '47', county = '037, 093, 157')
  
  #Combine results
  df = (df_al.append(df_in, ignore_index = True)
             .append(df_ky, ignore_index = True)
             .append(df_mi, ignore_index = True)
             .append(df_mo, ignore_index = True)
             .append(df_ne, ignore_index = True)
             .append(df_nc, ignore_index = True)
             .append(df_oh, ignore_index = True)
             .append(df_ok, ignore_index = True)
             .append(df_sc, ignore_index = True)
             .append(df_tn, ignore_index = True))
             
  return df

# Severely Cost-Burdened Low Income Renters
df = get_census_peers_19('group(B25074)')

df.to_csv("low_income_renters.csv")