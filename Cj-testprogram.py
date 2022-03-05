def get_age():
   age = int(input("Age"))
   if(age>=18 and age<=75):
       return age

   else:
       raise ValueError("Age is out of range or invalid")

def fat_burning_heart_rate(age):

   return (0.7 * (220 - age))

   
try:

   age = get_age()

   print("Fat burning heart rate for a",age,"year-old:",fat_burning_heart_rate(age),"bpm")

except ValueError as ve:

   print(ve.args[0], "Could not calculate heart rate info.")