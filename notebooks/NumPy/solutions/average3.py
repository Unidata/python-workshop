data = np.array([1, 3, 5, 7, 9, 11])
out = (data[2:] + data[1:-1] + data[:-2]) / 3
print(out)
