RPM= 400
print("RPM:",RPM)
TIME= 20
print("TIME:",TIME,"s")
circle= RPM * TIME / 60
print("the revolution:", circle)
if RPM< 500:
    print("the motor speed is relatively low")
elif RPM>=500 and RPM<=1500:
    print("the motor speed is normal")
else: 
    print("the motor speed is relatively high")
