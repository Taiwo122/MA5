import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('world_fires_1_day.csv')

# Extract latitude, longitude, and brightness values
lats = df['latitude'].values
lons = df['longitude'].values
brightness = df['brightness'].values

# Create a map using Basemap
plt.figure(figsize=(10, 6))
m = Basemap(projection='mill', llcrnrlat=-90, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180)
m.drawcoastlines()
m.drawcountries()

# Convert latitude and longitude to map coordinates
x, y = m(lons, lats)

# Plot fire data using brightness as marker size
m.scatter(x, y, c=brightness, cmap='hot', alpha=0.5, s=brightness)

# Add colorbar for brightness
plt.colorbar(label='Brightness')

plt.title('Global Fire Activity')
plt.show()
