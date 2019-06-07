


import pandas as pd
from matplotlib import pyplot as plt





species = pd.read_csv('species_info.csv')




species.head()



6





print "Mammal,Reptile,Amphibian,Fish,Vascular Plant,Non Vascular plant"





print "Endangered,In Recovery,Species of concern,Threatened"




conservation_counts=species.groupby('conservation_status').scientific_name.nunique().reset_index()
print conservation_counts





species.fillna('No Intervention', inplace = True)





conservation_counts_fixed=species.groupby('conservation_status').scientific_name.nunique().reset_index()
print conservation_counts_fixed




protection_counts = species.groupby('conservation_status')    .scientific_name.nunique().reset_index()    .sort_values(by='scientific_name')





plt.figure(figsize=(10, 4))
ax = plt.subplot()
plt.bar(range(len(protection_counts)),protection_counts.scientific_name.values)
ax.set_xticks(range(len(protection_counts)))
ax.set_xticklabels(protection_counts.conservation_status.values)
plt.ylabel('Number of Species')
plt.title('Conservation Status by Species')

plt.show()





species['is_protected'] = species.conservation_status != 'No Intervention'





category_counts = species.groupby(['category', 'is_protected']).scientific_name.nunique().reset_index()





category_counts.head()






category_pivot = category_counts.pivot(columns='is_protected',
                      index='category',
                      values='scientific_name')\
                      .reset_index()
  




print category_pivot




category_pivot.columns = ['category', 'not_protected', 'protected']





category_pivot['percent_protected'] = category_pivot.protected / (category_pivot.protected + category_pivot.not_protected)





print category_pivot





contingency = [[30, 146],
              [75, 413]]





from scipy.stats import chi2_contingency





pval = chi2_contingency(contingency)[1]

print(pval)




contingency_reptile_mammal = [[30, 146],
                              [5, 73]]

pval_reptile_mammal = chi2_contingency(contingency_reptile_mammal)[1]
print(pval_reptile_mammal)




contingency_amphibians_fish = [[75, 413],
                              [46, 4216]]

pval_amphibians_fish = chi2_contingency(contingency_amphibians_fish)[1]
print(pval_amphibians_fish)




observations = pd.read_csv('observations.csv')
print observations.head()




# Does "Sheep" occur in this string?
str1 = 'This string contains Sheep'
'Sheep' in str1



# Does "Sheep" occur in this string?
str2 = 'This string contains Cows'
'Sheep' in str2


# Use `apply` and a `lambda` function to create a new column in `species` called `is_sheep` which is `True` if the `common_names` contains `'Sheep'`, and `False` otherwise.



species['is_sheep'] = species.common_names.apply(lambda x: 'Sheep' in x)


# Select the rows of `species` where `is_sheep` is `True` and examine the results.




species_is_sheep = species[species.is_sheep]
print species_is_sheep




sheep_species = species[(species.is_sheep) & (species.category == 'Mammal')]
print sheep_species


# Now merge `sheep_species` with `observations` to get a DataFrame with observations of sheep.  Save this DataFrame as `sheep_observations`.




sheep_observations = observations.merge(sheep_species)

print sheep_observations.head()


# How many total sheep observations (across all three species) were made at each national park?  Use `groupby` to get the `sum` of `observations` for each `park_name`.  Save your answer to `obs_by_park`.
# 
# This is the total number of sheep observed in each park over the past 7 days.





obs_by_park = sheep_observations.groupby('park_name').observations.sum().reset_index()

print obs_by_park





plt.figure(figsize=(16, 4))
ax = plt.subplot()
plt.bar(range(len(obs_by_park)),
        obs_by_park.observations.values)
ax.set_xticks(range(len(obs_by_park)))
ax.set_xticklabels(obs_by_park.park_name.values)
plt.ylabel('Number of Observations')
plt.title('Observations of Sheep per Week')
plt.show()




baseline = 15

minimum_detectable_effect = 100*5./15
print minimum_detectable_effect
sample_size_per_variant = 870

yellowstone_weeks_observing = sample_size_per_variant/507.
print yellowstone_weeks_observing
bryce_weeks_observing = sample_size_per_variant/250.
print  bryce_weeks_observing


# How many weeks would you need to observe sheep at Bryce National Park in order to observe enough sheep?  How many weeks would you need to observe at Yellowstone National Park to observe enough sheep?



#at bryce national park it would take 1.7 weeks  and at yellowstone national park it would take 3.48 weeks

