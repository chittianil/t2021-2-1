number_list=[1,2,8,9,12,46,76,82,15,20,30]
multiple=[1,2,3,4,5,6,7,8,9]
new_dict={}
for i in multiple:
    mul=int(i)
    count=0
    for j in range(len(number_list)):
        if (number_list[j]%mul==0):
            count=count+1
    new_dict[i]=count
print(new_dict)