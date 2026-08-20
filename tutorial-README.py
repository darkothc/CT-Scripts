# TUTORIAL COMMANDS + Solar_tracker

# boot.py ---------------------------------------------------------------------------------
boot()

# planet_power.py ---------------------------------------------------------------------------------
activate_power()

# planet_sensors.py ---------------------------------------------------------------------------------
activate_sensors()

# uplink.py ---------------------------------------------------------------------------------
component = get_component("thermometer")
value = component.get_value()

t = get_component("transmitter")
t.connect("earth")
t.transmit("current_temperature", value)

# oxygen_sensor.py ---------------------------------------------------------------------------------
component = get_component("oxygen_sensor")
value = component.get_value()
print(value)
new_value = self.calibrate(value * 100)

# pressure_sensor.py ---------------------------------------------------------------------------------
component = get_component("pressure_sensor")
value = component.get_value()

if value % 2:
    new_value = value +1 # if odd
else:
    new_value = value # if even

component.stabilize(new_value)

# solar_tracker_1 ---------------------------------------------------------------------------------
while True:
    clock = get_component("clock")
    self.set_tilt(90 - clock.get_elevation())


