import requests
import matplotlib.pyplot as plt
import numpy as np

# URL for earthquake data
url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_hour.geojson'

# Fetching earthquake data
response = requests.get(url)
data = response.json()

# Extracting earthquake magnitudes
magnitudes = [quake['properties']['mag'] for quake in data['features']]

# Plotting earthquake magnitudes
plt.figure(figsize=(10, 6))
plt.hist(magnitudes, bins=np.arange(4.0, 10.0, 0.5), color='skyblue', edgecolor='black')
plt.xlabel('Magnitude')
plt.ylabel('Frequency')
plt.title('Recent Earthquake Magnitudes')
plt.grid(axis='y', linestyle='--')
plt.xticks(np.arange(4.0, 10.0, 0.5))
plt.show()
