advec = (wind_vec * -grad_vec).sum(axis=-1)
print(advec.shape)