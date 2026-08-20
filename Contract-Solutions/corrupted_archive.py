# Logging options
log_pairs = 0 # Print found pairs to console
log_raw = 0 # Print raw Cell Grid Reference and Word per step to console


archive = self.contract.archive
pairs = []

for r1 in range(10):
    for c1 in range(10):
        word1 = archive.flip(r1, c1)

        for r2 in range(10):
            for c2 in range(10):
                word2 = archive.flip(r2, c2)
                #print(pairs)
                
                if (r1 > r2) or (r1 == r2 and c1 >= c2):
                    continue
    
                if word1 == word2:
                    pairs.append([r1, c1, r2, c2])
                    
                if log_pairs:
                    if word1 == word2:
                        print(f"NEW LIST: {pairs} \n Pairs found: {len(pairs)}")
    
                if log_raw:
                    print(f"Raw: {r1} {c1}, {r2} {c2} \n Words: {word1} & {word2}")

if len(pairs) == 50:
    transmitter = get_component("transmitter")
    transmitter.connect("earth")

    transmitter.transmit(self.contract.id, pairs)
