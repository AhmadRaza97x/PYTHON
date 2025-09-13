fruit = "mango"
fruitlen = len(fruit)

print(len(fruit))   # LEN() COUNT NO. OF CHARACTER
print(fruitlen)     
print(fruit)
print("\n")

print(fruit[0:4])   # IT PRINT UP TO 4 CHARACTER 
print(fruit[:4])    # BY DEFAULT USE 0
print(fruit[1:4])  
print(fruit[3])     # IT PRINT 3RD CHARACTER 
print(fruit[:])     # SAME AS [0:4]
print(fruit[0:-3])  # MEANS [0:LEN(FRUIT)-3] OR [0:5-3] OR [0:2]
print(fruit[-3:-1])   # MEANS [2:4]
print(fruit[-1:-3])   # MEANS [4:2] NOTHING HAPPEN
print("\n")
 
print("APPLE is a",len("APPLE"),"character word")
