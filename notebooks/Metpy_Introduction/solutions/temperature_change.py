temperature_change_rate = -2.3 * units.delta_degF / (10 * units.minutes)
temperature = 25 * units.degC
dt = 1.5 * units.hours
print(temperature + temperature_change_rate * dt)
