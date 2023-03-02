#sal's shipping
weight= 1.5
#ground shipping
if weight <=2:
  cost_ground=weight*1.5+20
elif weight <=6:
  cost_ground=weight*3+20
elif weight <=10:
  cost_ground=weight*4+20
else:
  cost_ground=weight*4.75+20
print("ground shipping:$")
print(cost_ground)
#premium ground shipping
premium_ground_shipping=125.00
print("Ground Premium Shipping:$")
print(premium_ground_shipping)
#drone shipping
if weight<=2:
 drone_shipping=weight*4.50
elif weight <=6:
  drone_shipping=weight*9
elif weight<=10:
  drone_shipping=weight*12
else:
  drone_shipping=weight*14.25
print("cost of drone shipping:$",drone_shipping)

  