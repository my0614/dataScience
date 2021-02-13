import folium

m = folium.Map(
    location=[37.5838699,127.0565831],
    zoom_start=15
)

folium.Marker(
  location=[37.5838699,127.0565831],
  popup='University of Seoul',
  icon=folium.Icon(color='red',icon='star')
).add_to(m)

m.save('map.html')
