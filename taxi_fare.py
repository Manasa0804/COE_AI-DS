def calculate_fare(distance):
    return 50+(10*distance)
trips=[5,10,3]
total_fare=0
for i,distance in enumerate(trips,start=1):
    fare=calculate_fare(distance)
    print(f"Trip {i}:${fare}")
    total_fare += fare
print(f"Total Fare: ${total_fare}")