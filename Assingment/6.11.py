cities_armaghan={
 'Lahore':{
 'Country':'Pakistan',
 'Population':'11.13 Million',
 'Fact':'Biggest city of the region'
 },
 'New York':{
 'Country':'United States',
 'Population':'8.468 Million',
 'Fact':'About 22 percent of New York City\'s land is used for 
public parks '
 },
 'Mumbai':{
 'Country':'India',
 'Population':'20.96 Million',
 'Fact':'Mumbai was earlier called as Bombay'
 }
}
for cities,info in cities_armaghan.items():
 print("\nCity Name: "+cities)
 print("\tContry: "+info['Country'])
 print("\tPopulation: "+info['Population'])
 print("\tFact: "+info['Fact'])
City Name: Lahore
Contry: Pakistan
Population: 11.13 Million
Fact: Biggest city of the region
City Name: New York
Contry: United States
Population: 8.468 Million
Fact: About 22 percent of New York City's land is used for public
parks 
City Name: Mumbai
Contry: India
Population: 20.96 Million
Fact: Mumbai was earlier called as Bombay