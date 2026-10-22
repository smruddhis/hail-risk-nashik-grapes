import imdlib as imd

# Download daily rainfall data for Nashik region
# Nashik is roughly 19–20°N, 73–74.5°E

data = imd.open_data(
    variable='rainfall',  # or 'temperature'
    start_year=2010,
    end_year=2023,
    lat1=19.0,      # south boundary
    lat2=20.5,      # north boundary
    lon1=73.0,      # west boundary
    lon2=74.5       # east boundary
)

# Save to a file
data.to_netcdf('data/raw/imd_rainfall_nashik_2010_2023.nc')

print("Download complete! File saved to data/raw/imd_rainfall_nashik_2010_2023.nc")
