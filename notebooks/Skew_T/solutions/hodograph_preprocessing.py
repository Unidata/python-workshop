# Calculate the height above ground level (AGL)
sounding['height_agl'] = sounding['height'] - sounding['height'][0]

# Make an array of segment boundaries - don't forget units!
boundaries = [0, 1, 3, 5, 8] * units.km

# Make a list of colors for the segments
colors = ['tab:red', 'tab:green', 'tab:blue', 'tab:olive']
