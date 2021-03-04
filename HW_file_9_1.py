import json

infile = open("US_fires_9_1.json", "r")
outfile = open("readable_fi_data.json", "w")

fi_data = json.load(infile)
json.dump(fi_data, outfile, indent=4)

list_of_fis = fi_data

lats = []
lons = []
brights = []

for fi in list_of_fis:
    lat = fi["latitude"]
    lon = fi["longitude"]
    bright = fi["bright_t31"]

    lats.append(lat)
    lons.append(lon)
    brights.append(bright)

print(lats[:10])
print(lons[:10])
print(brights[:10])

# graph
from plotly.graph_objs import Scattergeo, Layout  # Remeber case sensitive
from plotly import offline

data = [
    {
        "type": "scattergeo",
        "lat": lats,
        "lon": lons,
        "marker": {
            "size": [5 * bright for bright in brights],
            "color": brights,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Brightness"},
        },
    }
]

my_layout = Layout(title="West Coast Fires")

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="west_coast_fires.html")