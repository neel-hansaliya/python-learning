# Traffic light

# light = input("light : ")

# if light == "red":
#     print("Stop!")
# elif light == "green":
#     print("Go !")
# elif light == "yellow":
#     print("Wait!")

# #######################################################################
# sum of two numbers

# val1 = int(input("enter a number: "))
# val2 = int(input("enter a number: "))

# print ("sum = ", (val1 + val2) / 2)

# ########################################################################
# functons

# name = input("enter a name: ")
# print(len(name))

# name = "hii $i $am $neel"
# print(name.count("$"))

# ########################################################################
# odd even numbers

# val = int(input("enter a number: "))

# if val % 2 == 0:
#     print("even number")
# else:
#     print("odd number")

# ########################################################################
# maximum number find

# val1 = int(input("enter a number: "))
# val2 = int(input("enter a number: "))
# val3 = int(input("enter a number: "))
# val4 = int(input("enter a number: "))

# if val1 > val2 and val1 > val3:
#     print("largest value is :", val1)

# elif val2 > val3:
#         print("largest value is :", val2)

# elif val3 > val4:
#         print("largest value is :", val3)

# else:
#         print("largest value is :", val4)

# ########################################################################
# multiple of 7 or not

# val = int(input("enter a number: "))

# if (val % 7 == 0):
#     print(val, "is a multiple of 7")
# else:
#     print(val, "is not a multiple of 7")

# ########################################################################
# list 

# marks = [90.5 , 85.3 , 70.4 , 93.5]
# # apend add new value last
# marks.append(80.5)
# #sort method use is value set assending order and also string value posible
# marks.sort(reverse=True)
# #insert methd use is any particular index in add value
# marks.insert(3,50.5)
# print(marks[2] , type(marks) , marks[1:4] , marks)

# ########################################################################

# tupple

# tup = (3, 5, 6, 6)
# print(tup[1:3])
# print(type(tup)) 
# after does not change value in tupple

# ##########################################################################

# practice question enter 3 favorite movie and store one list 

# movie1 = input('enter first favorite movie:')
# movie2 = input('enter second favorite movie:')
# movie3 = input('enter third favorite movie:')

# allmovie = []
# allmovie.append(movie1)
# allmovie.append(movie2)
# allmovie.append(movie3)

# print(allmovie)
# print(type(allmovie))

# ############################################################################

# practice question palindrome

# num = ["r" , "a" , "c" , "e" , "c" , "a" , "r"]

# newnum = num.copy()
# newnum.reverse()

# print(num , newnum)

# if(num == newnum):
#     print("your value are palindrome")
# else:
#     print("your value are not palindrome")

# #############################################################################

# practice question one letter how many times in tupple

# tup = (2, 3, 2, 4, 2)
# print(tup.count(2))
# print(type(tup))

# #############################################################################
# practice question sorting in list 

# num = ["A" , "C" , "B" , "F" , "E" , "D" ,]
# num.sort()
# print(num)

# #############################################################################
# Dictionary

# Data = {
#     "name": "neel",
#     "age": 19,
#     "city": "ahemdabad"
# }
# print(Data["city"])
# print(type(Data))

# #############################################################################
# nesting in dictionary

# Data = {
#     "name":"neel",
#     "marks" : {
#         "math": 96,
#         "science": 85,
#         "english": 92,
#     },
#     "age": 19
# }
# print(Data["name"])
# print(Data["marks"])
# print(Data["marks"]["math"])


# ################################################################################

# set 

# colllections = {1, 2, 3, "bus" , "car"}
# print(colllections)
# print(len(colllections))
# print(type(colllections))

# ###################################################################################
# unnion

# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# print(set1.union(set2))

# ###################################################################################
# intersection

# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# print(set1.intersection(set2)) 

# ###################################################################################
# practice questions dicrtionary

# data = {
#     "table": ["a piece of furniture", "list of facts figure"],
#     "cat":"a small animal"
# }

# print(data)
# print(type(data["table"]))
# print(type(data))

# ######################################################################################

# practice questions set count the number of language

# lan = {"java", "python", "c", "python", "javascript", "c++", "java"}
# print(lan)
# print(len(lan))

# #######################################################################################
# practice question create mt dictionary and one by one add subject and marks key value pairs

# marks = {}

# x = int(input("Enter math: "))
# marks.update({"math:": x})

# x = int(input("Enter phy: "))
# marks.update({"phy:": x})

# x = int(input("Enter chem: "))
# marks.update({"chem:": x})

# print(marks)

# ##############################################################################################
# pracctice question store 9 & 9.0 as separate value in set

# val = {9, "9.0"}
# print(val)

# ###############################################################################################
# loops 

# count = 0

# while count < 5:
#     print("hello")
#     count = count + 1

# #########################################
# i = 100

# while i >= 1:
#     print(i)
#     i = i - 1

# #########################################
# i = 1
# n = int(input("enter the number: "))

# while i <= 10:
#     print(n * i)
#     i = i + 1

# ##########################################
# string formating

# first_name = "Neel"
# last_name = "hansaliya"
# print("the first name is {} and last name is {}".format(first_name, last_name))

# ###############################################################################################
# input type

# a = int(input("enter the number: "))
# b = int(input("enter the number: "))

# print(a+b)

# ###############################################################################################
# if else  and nested if else

# age = int(input("enter the age: "))

# if age < 18:
#     print("Minor")
# elif age >= 18 and age <= 45:
#     print("mid age")
# else:
#     print("senior citizen")

# ################################################################################################
# for loop

# lis = [1,2,3,4,5]
# a1 = 0
# for i in lis:
#     a1 = a1 + i
# print(a1)

# ################################################################################################
# even and odd number sum

# lis = [2,2,2,3,3,3]
# odd_sum = 0
# eve_sum = 0

# for i in lis:
#     if (i%2==0):
#         eve_sum = eve_sum + i
#     else:
#         odd_sum = odd_sum + i

# print("odd sum is: {}".format(odd_sum))
# print("eve sum is: {}".format(eve_sum))

# ###################################################################################################
# while loop

# i = 0

# while(i <= 10):
#     print(i)
#     if(i == 5):
#         break
#     i = i + 1

# ###################################################################################################
# inbuilt number method
# Absolute

# a1 = -50
# print(abs(a1))

# ###################################################################################################
# ceil

# import math
# a1 = 50.5
# a2 = 50.01
# a3 = -40.4
# print(math.ceil(a1))
# print(math.ceil(a2))
# print(math.ceil(a3))

# ####################################################################################################
# floor

# import math
# a1 = 50.5
# a2 = 50.9
# a3 = -30.1
# print(math.floor(a1))
# print(math.floor(a2))
# print(math.floor(a3))

# ####################################################################################################
# exponential #exp

# import math
# a1 = 1
# print(math.exp(a1))

# #####################################################################################################
# fabs

# import math
# a1 = 5
# a2 = 10
# a3 = -40
# print(math.fabs(a1))
# print(math.fabs(a2))
# print(math.fabs(a3))

# ######################################################################################################
# log

# import math
# a1 = 10
# print(math.log(a1))

# ######################################################################################################
# max

# a1 = 22,23,100
# a2 = -22, -33, -44

# print(max(a1))
# print(max(a2))

# ########################################################################################################
# min

# a1 = 10,23,100
# a2 = -22, -33, -44

# print(min(a1))
# print(min(a2))

# #########################################################################################################
# pow

# import math
# print(math.pow(2,5))
# print(math.pow(3,3))

# #########################################################################################################
# sqrt

# import math
# a1 = 16
# a2 = 9
# print(math.sqrt(a1))
# print(math.sqrt(a2))

# ########################################################################################################
# trignometric function

# import math
# print(math.sin(1))
# print(math.cos(1))

# ########################################################################################################
# hypotenuse

# import math

# print(math.hypot(4,4))

# ########################################################################################################
# modf #Modulus and Fraction

# import math

# print(math.modf(230))

# ########################################################################################################
# practice que check max num

# a1 = 10 , 50 , 100
# print(max(a1))

# ########################################################################################################
# nested indexing value change

# lst = ["neel" , "het"]
# fin = lst[1]
# ch = list(fin)
# ch[1] = "i"
# lst[1] = ''.join(ch)
# print(lst)

# ##########################################################################################################
# set #it's ordered

# sat = {"avengers", "hulk" , "marvels"}

# for i in sat:
#     print(i)
#     print(type(sat))

# ##########################################################################################################
# dict

# info = {
#     "name" : "Neel",
#     "age" : 23,
#     "city" : "delhi"
# }
# info["car"]="audi"
# print(info)
# print(type(info))

# #nested dict

# car1_model = {"audi" : 2000}
# car2_model = {"bmw" : 2002}
# car3_model = {"volvo" : 2004}

# car_type = {'car1' : car1_model, 'car2' : car2_model, 'car3' : car3_model}
# print (car_type)
# print(car_type["car2"]["bmw"])

# ###########################################################################################################
# tupple

# tup = ("avengers", "marvels", "hulk")

# print(tup)
# print(type(tup))

# ############################################################################################################
# numpy

# import numpy as np

# lst = ([1,2,3], [4,5,6], [7,8,9], [10,11,12])
# arr = np.array(lst)

# arr1 = arr[0:,0:1]
# print(arr1)
# print(type(arr))

# #############################################################################################################
# reshape

# import numpy as np

# lst = ([1,2,3], [4,5,6], [7,8,9], [10,11,12])
# arr = np.array(lst)

# arr1 = arr.reshape(6,2)
# print(arr1)
# print(type(arr))

################################################################################################################
#list vs numpy

# a = [1,2,3]
# b = [1,2,3]
# print(a*b) # not executed that is throw error but numpy in posible 

# import numpy as np

# a = np.array([1,2,3])
# b = np.array([1,2,3])

# print(a*b) # numpy in posible multiplication in two array ans is = [1 4 9]

#################################################################################################################
# multi dimensional array in find specific value using indexing

# import numpy as np

# a = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])

# print(a[1,3]) # this is used for find specific value
# print(a[1,:]) # two dots meaning is all column are show
# print(a[1,2:]) # second row and second column to all value are show
# print(a[1,:2]) # second row first tow element are show

#################################################################################################################

#pandas # convert dataframe

# import pandas as pd
# import numpy as np

# arr = np.arange(0,21).reshape(3,7)
# arr2 = pd.DataFrame(data = arr, index=["row1", "row2", "row3"], columns=["col1", "col2", "col3", "col4", "col5", "col6", "col7"])
# # arr3 = arr2[["col1", "col2", "col3"]]             #find data column wise
# # arr4 = arr2.loc[['row2' , 'row3']]                #find particular row in dataframe
# # arr5 = arr2.iloc[1:,0:2]                          #column and row find both to use "iloc" 
# # arr6 = arr2.iloc[:, [0, -1]]                      #find first column last column data find
# # arr7 = arr2.iloc[0:,0:4].values                   #convert dataframe into arrays
# print(arr2)

#Note
# -> multiple row and multiple coulmumn are dataframe but one row or one column it's a series
