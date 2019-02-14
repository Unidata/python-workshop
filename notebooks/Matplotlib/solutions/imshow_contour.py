fig, ax = plt.subplots()
im = ax.imshow(Z, interpolation='bilinear', cmap='PiYG',
               origin='lower', extent=[-3, 3, -3, 3])
c = ax.contour(X, Y, Z, levels=np.arange(-2, 2, 0.5), colors='black')
ax.clabel(c)
