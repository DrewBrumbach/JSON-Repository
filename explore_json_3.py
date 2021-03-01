import json

infile = open("eq_data_1_day_m1.json", "r")
outfile = open("readable_eq_data.json", "w")


eq_data = json.load(infile)

json.dump(eq_data, outfile, indent=4)

# eq_data is the name if the initial dictionary
# eq_data has 3 keys, type, metadata, features

# print(eq_data['features'][0])
# above gives the dictionary, with the key 'features' in the 0 index

# print(eq_data["features"][0]["properties"]["mag"])
# the above gives the dictionary, with the key feature, in the 0 index, with with the properties key, with another
# key, 'mag', which gives us what we want- magnitude of the first index

# below is for loop to cycle through all entries

list_of_eqs = eq_data["features"]

mags = []
lons = []
lats = []
hover_texts = []

for eq in list_of_eqs:
    mag = eq["properties"]["mag"]
    lon = eq["geometry"]["coordinates"][0]
    lat = eq["geometry"]["coordinates"][1]
    hover_text = eq["properties"]["place"]

    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(hover_text)

print(mags[:10])  # from zero to tenth element, 0 to 9, called list slicing
print(lons[:10])
print(lats[:10])
print(hover_texts[:10])
# above basically has eq as the first part of statement, eq_data['features'], for statement adds vars as second part


# graph
from plotly.graph_objs import Scattergeo, Layout  # Remeber case sensitive
from plotly import offline

data = [
    {  # creating a list and an internal dictionary
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "text": hover_texts,
        "marker": {
            "size": [
                5 * mag for mag in mags
            ],  # creates list, goes through each item in mags list, item * 5
            "color": mags,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Magnitude"},
        },
    }
]
my_layout = Layout(title="Global Earthquakes")

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="global_earthquakes.html")