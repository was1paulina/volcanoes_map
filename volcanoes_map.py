import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1500:
        return "green"
    elif 1500 <= elevation < 3000:
        return "orange"
    else:
        return "red"

map = folium.Map(location=[47.61492118876099, -122.34873984582637], zoom_start=10, tiles = "Stamen Watercolor")

#volcanoes layer
fgv = folium.FeatureGroup(name="Volcanoes")
for  lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], popup=str(el)+"m", 
                                     fill_color=color_producer(el), fill_opacity=0.7, 
                                     color='white', fill=True))
    
#population layer
fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), 
                            style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
                                                      else 'yellow' if 10000000 <= x['properties']['POP2005'] < 20000000
                                                     else 'red'}))

map.add_child(fgv)
map.add_child(fgp)

#control layer
map.add_child(folium.LayerControl())

map.save("Map1.html")



