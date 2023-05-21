
degrees = int(input("Please enter temperature in degrees: "))
day_time = input("Please enter day time - [Morning] or [Afternoon] or [Evening]: ")
outfit = ''
shoes = ''

if day_time == 'Morning':
    if 10 <= degrees <= 18:
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif 18 < degrees <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif degrees >=25:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
elif day_time == 'Afternoon':
    if 10 <= degrees <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < degrees <= 24:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif degrees >= 25:
        outfit = 'Swim Suit'
        shoes = 'Barefoot'
elif day_time == 'Evening':
    if degrees >=10:
        outfit = 'Shirt'
        shoes = 'Moccasins'

print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
