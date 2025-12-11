def mapa(x=0):
    import folium
    mapa = folium.Map(location=[23.1363, -82.3585], zoom_start=14 )
    folium.Marker(location=[23.12406, -82.38129],popup="mypime 1",tooltip="Click aquí").add_to(mapa)
    folium.Marker(location=[23.12598, -82.38265],popup="mypime 2",tooltip="Click aquí").add_to(mapa)
    folium.Marker(location=[23.12636, -82.38299],popup="mypime 3",tooltip="Click aquí").add_to(mapa)
    folium.Marker(location=[23.1244, -82.38061],popup="mypime 4",tooltip="Click aquí").add_to(mapa)
    folium.Marker(location=[23.12934, -82.38332],popup="mypime 5",tooltip="Click aquí").add_to(mapa)
    folium.Marker(location=[23.12551, -82.38061],popup="mypime 6",tooltip="Click aquí").add_to(mapa)
    folium.Marker(location=[23.119598,-82.383310],popup="mypime 7",tooltip="Click aquí").add_to(mapa)
    folium.Marker(location=[23.119001,-82.383618],popup="mypime 8",tooltip="Click aquí").add_to(mapa)
    folium.Marker(location=[23.116405, -82.384981],popup="mypime 9",tooltip="Click aquí").add_to(mapa)
    folium.Marker(location=[23.11575, -82.38536],popup="mypime 10",tooltip="Click aquí").add_to(mapa)
    folium.Marker(location=[23.1162, -82.38705],popup="mypime 11",tooltip="Click aquí").add_to(mapa)
    folium.Marker(location=[23.11662, -82.38807],popup="mypime 12",tooltip="Click aquí").add_to(mapa)
    folium.Marker(location=[23.11615, -82.38604],popup="mypime 13",tooltip="Click aquí").add_to(mapa)
    folium.Marker(location=[23.12055, -82.39281],popup="mypime 14",tooltip="Click aquí").add_to(mapa)
    folium.Marker(location=[23.11862, -82.39112],popup="mypime 15",tooltip="Click aquí").add_to(mapa)
    folium.Marker(location=[23.11654, -82.38638],popup="mypime 16",tooltip="Click aquí").add_to(mapa)
    folium.Marker(location=[23.11572, -82.40066],popup="mypime 17",tooltip="Click aquí").add_to(mapa)
    folium.Marker(location=[23.11684, -82.400271],popup="mypime 18",tooltip="Click aquí").add_to(mapa)
    folium.Marker(location=[23.11867, -82.40249],popup="mypime 19",tooltip="Click aquí").add_to(mapa)
    folium.Marker(location=[23.12114, -82.40501],popup="mypime 20",tooltip="Click aquí").add_to(mapa)
    folium.Marker(location=[23.12124, -82.40448],popup="mypime 21",tooltip="Click aquí").add_to(mapa)
    folium.Marker(location=[23.12922, -82.40289],popup="mypime 22",tooltip="Click aquí").add_to(mapa)
    folium.Marker(location=[23.13827, -82.40094],popup="mypime 23",tooltip="Click aquí").add_to(mapa)
    folium.Marker(location=[23.12936, -82.37943],popup="mypime 24",tooltip="Click aquí").add_to(mapa)
    folium.Marker(location=[23.12916, -82.3796],popup="mypime 25",tooltip="Click aquí").add_to(mapa)
    folium.Marker(location=[23.13056, -82.38011],popup="mypime 26",tooltip="Click aquí").add_to(mapa)
    folium.Marker(location=[23.12956, -82.38028],popup="mypime 27",tooltip="Click aquí").add_to(mapa)
    folium.Marker(location=[23.12945, -82.38061],popup="mypime 28",tooltip="Click aquí").add_to(mapa)
    folium.Marker(location=[23.13335, -82.37857],popup="mypime 29",tooltip="Click aquí").add_to(mapa)
    folium.Marker(location=[23.12942, -82.37817],popup="mypime 30",tooltip="Click aquí").add_to(mapa)



    return mapa
  
  
  
  
def mapa_simple(x=0):
    import folium
    
    mapa = folium.Map(location=[23.1363, -82.3585], zoom_start=14)
    
    # Lista de todas tus coordenadas
    coordenadas = [
        (23.12406, -82.38129, "MYPIME 1"),
        (23.12598, -82.38265, "MYPIME 2"),
        (23.12636, -82.38299, "MYPIME 3"),
        (23.1244, -82.38061, "MYPIME 4"),
        (23.12934, -82.38332, "MYPIME 5"),
        (23.12551, -82.38061, "MYPIME 6"),
        (23.119598, -82.383310, "MYPIME 7"),
        (23.119001, -82.383618, "MYPIME 8"),
        (23.116405, -82.384981, "MYPIME 9"),
        (23.11575, -82.38536, "MYPIME 10"),
        (23.1162, -82.38705, "MYPIME 11"),
        (23.11662, -82.38807, "MYPIME 12"),
        (23.11615, -82.38604, "MYPIME 13"),
        (23.12055, -82.39281, "MYPIME 14"),
        (23.11862, -82.39112, "MYPIME 15"),
        (23.11654, -82.38638, "MYPIME 16"),
        (23.11572, -82.40066, "MYPIME 17"),
        (23.11684, -82.400271, "MYPIME 18"),
        (23.11867, -82.40249, "MYPIME 19"),
        (23.12114, -82.40501, "MYPIME 20"),
        (23.12124, -82.40448, "MYPIME 21"),
        (23.12922, -82.40289, "MYPIME 22"),
        (23.13827, -82.40094, "MYPIME 23"),
        (23.12936, -82.37943, "MYPIME 24"),
        (23.12916, -82.3796, "MYPIME 25"),
        (23.13056, -82.38011, "MYPIME 26"),
        (23.12956, -82.38028, "MYPIME 27"),
        (23.12945, -82.38061, "MYPIME 28"),
        (23.13335, -82.37857, "MYPIME 29"),
        (23.12942, -82.37817, "MYPIME 30"),
    ]
    
   
    for lat, lon, nombre in coordenadas:
        folium.Marker(
            location=[lat, lon],
            popup=nombre.lower(),
            tooltip=folium.Tooltip(nombre, permanent=True)  
        ).add_to(mapa)
    
    return mapa