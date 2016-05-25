from bs4 import BeautifulSoup
import csv

input_name = "1975-1989_tagged_NER.csv"      # File names for input and output
output_name = "1975-1989_entities.csv"

locations = {}
people = {}
orgs = {}


def incrementEntity(entity_string, dictionary):
    try:
        dictionary[entity_string] += 1
    except KeyError:
        dictionary[entity_string] = 1


def outputResults(dictionary, entity_type, f):
    for i in sorted(dictionary, key=dictionary.get, reverse=True):
        print (i, '\t', entity_type, '\t', dictionary[i])
        f.writerow([i, entity_type, dictionary[i]])

f = open(input_name, 'r')

soup = BeautifulSoup(f, "html.parser")

for i in soup.find_all():
    entity_name = i.get_text()
    entity_type = i.name

    if (entity_type == 'person'):
        incrementEntity(entity_name, people)
    elif (entity_type == 'organization'):
        incrementEntity(entity_name, orgs)
    elif (entity_type == 'location'):
        incrementEntity(entity_name, locations)
    else:
        continue

output_file = open(output_name, 'w')
f = csv.writer(output_file)
print ("Entity\t\tType\t\tCount")
print ("------\t\t----\t\t-----")
f.writerow(["Entity", "Type", "Count"])
outputResults(people, 'person', f)
outputResults(orgs, 'organization', f)
outputResults(locations, 'location', f)
