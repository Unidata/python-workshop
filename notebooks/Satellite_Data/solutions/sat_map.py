#Import for colortables
from metpy.plots import colortables

# Import for the bonus exercise
from metpy.plots import add_timestamp

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(1, 1, 1, projection=proj)
ax.add_feature(cfeature.COASTLINE.with_scale('50m'), linewidth=2)
ax.add_feature(cfeature.STATES.with_scale('50m'), linestyle=':', edgecolor='black')
ax.add_feature(cfeature.BORDERS.with_scale('50m'), linewidth=2, edgecolor='black')

im = ax.imshow(dat, extent=(x.min(), x.max(), y.min(), y.max()), origin='upper')

wv_cmap = colortables.get_colortable('WVCIMSS_r')
im.set_cmap(wv_cmap)

#Bonus
start_time = datetime.strptime(ds.start_date_time, '%Y%j%H%M%S')
add_timestamp(ax, time=start_time, pretext=f'GOES-16 Ch. {channel} ',
              high_contrast=True, fontsize=16, y=0.01)

plt.show()