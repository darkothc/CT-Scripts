log_status = 0

heater = get_component(self.id)
therm_state = []
power_watts = []


print(f"Thermal_State at launch: {heater.thermal_state()}")

while True:
    
    if heater.efficiency() != 100:

        if heater.thermal_state() in therm_state:
            heater.set_power(power_watts[therm_state.index(heater.thermal_state())])

        if not therm_state or heater.thermal_state() not in therm_state:
            therm_state.append(heater.thermal_state())
        
        
        while power_watts.length < therm_state.length:
            power_watts.append(None)
                    
            for j in range(11):
                heater.set_power(j)
                replaceable = heater.thermal_state()
                replacer = therm_state.index(replaceable)
                power_watts[replacer] = j

                if log_status:
                    print(f"therm_state= {heater.thermal_state()} Power= ({j})watts Eff= {heater.efficiency()}")

                if heater.efficiency() == 100:
                    break
            if heater.efficiency() == 100:
                break


        if log_status:
            print(f"--------\nThermal_State({heater.thermal_state()}) set to optimal Power({power_watts[therm_state.index(heater.thermal_state())]})watts Eff= {heater.efficiency()} \nHeater Output: {heater.output()}\n--------")
