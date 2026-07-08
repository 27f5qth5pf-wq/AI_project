f_name = input("Enter First name : ")
l_name = input("Enter second name : ")

print ("reverse name is : ","".join(reversed(f_name)))
print ("reverse name is : ","".join(reversed(l_name)))

full_name = f_name + l_name

print ("Full name is : ",full_name)
# Slicing Strings 
print ("reverse name is : ",full_name[::-1])

# reverse string function
print ("reverse name is : ","".join(reversed(full_name)))

# for loop use for reverse name

for ch in full_name:
    ch += full_name
print ("reverse name is : ",full_name)


print(len(f_name))
print(len(l_name))

frn = f_name[-1:-len(f_name)-1:-1]
lrn = l_name[-1:-len(l_name)-1:-1]

print(frn)
print(lrn)