# Import for the bonus exercise
from metpy.plots import add_timestamp

# Make the image plot
img = ImagePlot()
img.data = ds
img.field = 'Sectorized_CMI'
img.colormap = 'WVCIMSS_r'

# Make the map panel and add the image to it
panel = MapPanel()
panel.plots = [img]

# Make the panel container and add the panel to it
pc = PanelContainer()
pc.panels = [panel]

# Bonus
start_time = datetime.strptime(ds.start_date_time, '%Y%j%H%M%S')
add_timestamp(panel.ax, time=start_time)

# Show the plot
pc.show()