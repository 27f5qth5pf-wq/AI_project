print(" ")
s_data = [
    
    ('Ahmad' , 18, 'A+' , 3.9),
    ('uZAIR' , 19, 'A'  , 3.8) ,
    ('Toqeer', 20, 'B+' , 3.7),
    ('Ijaz'  , 22, 'B'  , 3.65),
    ('Hamad' , 19, 'B'  , 3.67),
]
for i in s_data:
    print(i)

h_gpa = s_data[0][-1],s_data[1][-1],s_data[2][-1],s_data[3][-1]
average = s_data[0][1],s_data[1][1],s_data[2][1],s_data[3][1]

sum_average = sum(average) / len(s_data)
gpa_max = max(h_gpa)
index_gpa = h_gpa.index(gpa_max)
print(" ") 
n_data = s_data[index_gpa]

print ("Student  GPA : ", h_gpa)
print("Highest GPA : ", gpa_max)
print("Index : ",index_gpa)

print('Highest gpa in list of student : ',n_data )

print('Average of age :',sum_average)