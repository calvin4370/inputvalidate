import inputvalidate

age = inputvalidate.get_float('Your Age (0-200): ', min=0, max=200)

print(f'You are {age}')