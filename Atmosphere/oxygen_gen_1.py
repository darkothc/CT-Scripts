log = 0

atmosphere = get_component("atmosphere")

while True:
    co2 = atmosphere.get_co2()
    intake = round(co2/10)
    self.set_intake(intake)
    if log == 1:
        print(f"CO2: {co2}")
        print(f"Intake: {intake}")

    waste = self.waste()
    if log == 1:
        print(f"Waste: {waste}")
  
    if waste >= 60:
        if log == 1:
            print(f"{waste} Waste Dumped")
        self.dump_waste()
