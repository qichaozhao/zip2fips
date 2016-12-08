import pandas as pd

data = pd.read_csv('ValueSetConceptDetailResultSummary.txt', sep="\t")

fips_counties = data[['Concept Code','Concept Name','Preferred Concept Name']]
fips_counties.columns = ['FIPS6','county','county_state']

fips_counties = fips_counties.set_index('FIPS6')

fips_dict = fips_counties.to_json('fips2counties.json', orient='index')