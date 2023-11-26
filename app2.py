import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
map = folium.Map(location=[39.419, -111.950], zoom_start=6)


def cp(l):
    if el < 1000:
        return 'green'
    elif 1000 <= el < 3000:
        return 'orange'
    else:
        return 'red'


fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(
        folium.Marker(location=[lt, ln], popup=folium.Popup(str(el), parse_html=True), icon=folium.Icon(color=cp(el))))

map.add_child(fg)

map.save("Map1.html")
