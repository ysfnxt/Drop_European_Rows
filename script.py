import pandas as pd


# Reading CSV
df = pd.read_csv("email5.csv")


# List of European Countries 
countries = ['Austria', 'Belgium', 
             'Bulgaria', 'Croatia', 
             'Cyprus', 'Czechia', 'Denmark', 
             'Estonia', 'Finland', 'France', 
             'Germany', 'Greece', 'Hungary', 
             'Ireland', 'Italy', 'Latvia', 
             'Lithuania', 'Luxembourg', 'Malta', 
             'Netherlands', 'Poland', 'Portugal', 
             'Romania', 'Slovakia', 'Slovenia', 
             'Spain', 'Sweden', 'United Kingdom' ]


# Iterating through the list of European Countries
# Then, Changing it to lower case
new_list = []
for country in countries: 
    new_list.append(country.lower())

# Extracting the country from the 'location' column 
df['country'] = df['location'].str.extract(r'([A-Za-z\s]+)$')

# Stripping Whitespace from the column
df['country'] = df['country'].str.strip()

# Dropping rows whose cell matches the list of European countries
df1 = df[~df['country'].isin(new_list)]


# Dropping NULL in Location Column 
df1.dropna(subset=['location'])

# Exporting to csv
df1.to_csv("email5rest.csv")

