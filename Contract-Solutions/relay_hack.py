log_attempts = 0

code = [0,0,0,0,0,0]
lock = self.contract.lock
result = lock.intercept(code)

while True:
    if log_attempts:
        print(f"Code: {code} \n Check: {result}")

    if all(result):
        print(f"---------\n Codefound {code}")
        break

    for i in range(6):
        if code[i] > 100:
            break
            
        if not result[i]:
            code[i] += 1


t = get_component("transmitter")
t.connect("earth")
t.transmit(self.contract.id, code)
