fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1)

ax.plot([285, 320], [285, 320], color='black', linestyle='--')
s = ax.scatter(temps, temps_1000, c= temps - temps_1000, cmap='bwr', vmin=-5, vmax=5)
fig.colorbar(s)

ax.set_xlabel('Temperature (surface)')
ax.set_ylabel('Temperature (1000 hPa)')
ax.set_title('Temperature Cross Plot')
ax.grid(True)
