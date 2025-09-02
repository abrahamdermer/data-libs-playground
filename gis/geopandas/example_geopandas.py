# GeoPandas quickstart
# עברית: קריאת שכבת מדינות, סינון לפי יבשת, וחישוב צנטרואיד.
import geopandas as gpd

# Built-in small dataset
world = gpd.read_file("gis/geopandas/data/110m_cultural/ne_110m_admin_0_countries.shp")

print("Columns:", list(world.columns))


# print(world[["name","continent","geometry"]].head())

# Filter
europe = world[world["CONTINENT"]=="Europe"].copy()
print("\nEuropean countries:", len(europe))


# שומר את החישוב של המרכז הגאוגרפי(צנטרואיד)
# Compute centroids
europe["centroid"] = europe.geometry.centroid
print(europe[["NAME","centroid"]].head())

# מחיקה של המרכז ושמירה לקובץ
europe = europe.drop(columns=["centroid"])
# Save to GeoJSON (output)
europe.to_file("gis/geopandas/data/europe.geojson", driver="GeoJSON")
print("\nSaved to gis/geopandas/data/europe.geojson")
