#Sal's Shipping 
weight = 41.5
# Ground Shipping
if weight <= 2:
  cost = (weight * 1.50) + 20
elif weight <= 6:
  cost = (weight * 3.00) + 20
elif weight <= 10:
  cost = (weight * 4.00) + 20
elif weight > 10:
  cost = (weight * 4.75) + 20 
print("Ground Shipping $",cost) 


premium_ground_shipping = 125.00
print("Ground Shipping $",premium_ground_shipping)

#Drone Shipping
if weight <= 2:
  cost_drone = (weight * 4.50) 
elif weight <= 6:
  cost_drone = (weight * 9.00) 
elif weight <= 10:
  cost_drone = (weight * 12.00) 
elif weight > 10:
  cost_drone = (weight * 14.25)

print('Drone Shipping $', cost_drone) 
