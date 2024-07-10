# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json


# for this challenge, we're going to summarize the earthquake data as follows:
# 1: How many quakes are there in total?
# 2: How many quakes were felt by at least 100 people?
# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
# 4: Print the top 10 most significant events, with the significance value of each

# open the data file and load the JSON
with open("/workspaces/advanced-python-working-with-data-4312001/30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

totalquakes = len(data["features"])
def felt(q):
    if(q["properties"]["felt"] is not None
       and q["properties"]["felt"] >= 100):
        return True
    return False

results = list(filter(felt, data["features"]))
totalfelt = len(results)

mostfelt = list(filter(max(["properties"]["felt"]), data["features"]))

print(f"Total quakes: {totalquakes}")
print(f"Total quakes felt by at least 100 people: {totalfelt}")
print(f"Most felt quake: {mostfelt} Reports: ")
print("Top 10 most significant events: Significance value: ")