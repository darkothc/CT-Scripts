
log_alien = 0

e_dna = self.contract.earth_ref
samples = self.contract.samples

if log_alien:
    print(f"Earth DNA\n{e_dna}\n ")
    print(f"RAW SAMPLES:")
    print(samples)
    print("\n")

for i in samples:
    if i in e_dna:
        samples.remove(i)
        
if log_alien:
    print(f"FILTERED SAMPLES:")
    print(samples)

c= self.contract
t = get_component("transmitter")
t.connect("earth")
t.transmit(c.id, samples)

 
