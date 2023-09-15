# mycode = []
# mycode= list(input("kkfdkfkl : "))
# print(mycode)
# if len(mycode) !=9:
#     print("your code is not corect!")
import pdb

# pdb.set_trace() 

lIst_1=list(input("your National Code : ")) 
National_Code=lIst_1 
#print(len(lIst_1))

if len(lIst_1) >10 or len(lIst_1) <10: 
    print("Your national code is not correct")
else:

    
    list_position_number = 0
    multiply_by_National_Code=10
    for num in range(11):
        National_Code[list_position_number] * multiply_by_National_Code
        list_position_number +=1
        multiply_by_National_Code-=1
   
    print("hvufgv")
    
  
    #print(National_Code)

    
    sum =( National_Code[0] + National_Code[1] + National_Code[2] +National_Code[3]+National_Code[4]+National_Code[5]+National_Code[6]+National_Code[7] +National_Code[8])
    print(sum)
    
    # sum = sum %11
    
    # if sum <2:
    #     print("yor cod nashnal is crcet")
    
    
    
    
    
    # elif sum >=2:
    #     sum = sum-11
    #     if sum == mycode[9]:
    #         print("yor cod nashnal is crcet")
    #     else :
    #         print("yor cod nashnal is not crcet!")
    
    







