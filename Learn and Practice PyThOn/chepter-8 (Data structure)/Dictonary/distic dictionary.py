bd_division_info={}
bd_division_info["Barisal"]={"district":6,"Upazila":39,"Union":333}

bd_division_info["Dhaka"]={"district":13,"Upazila":90,"Union":1833}

print(bd_division_info)

divisions = bd_division_info.keys()
print(divisions)

for division in divisions:
         print("Division",division)

for division in divisions:
         print(division,"Upazila",bd_division_info[division]["Upazila"])

for item in bd_division_info:
         print(item)
#how to get key and value
         
for key in bd_division_info:
         print(key)
         print(bd_division_info[key])

#again
for key, value in bd_division_info.items():
         print(key)
         print(value)











