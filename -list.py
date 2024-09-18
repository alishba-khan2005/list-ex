list=["alishba","alizeh","areeb","anas","najia","feroz"]
#indexing
print(list[4])
print(list[-3])
#slicing
print(list[0:6])
print(list[0:5])
print(list[:])
print(list[1:])
print(list[:7])
print(list[-4:-1])
print(list[-1:-5])
#modifylist
list[0]="alish"
print(list)
#remove
list.remove("alish")
print(list)


#one code
def sub(x,y):
    add=x+y
    return(add)
print(sub(3,4))



#second code
def prt(pet_name,animal="dog"):
    print("my" , animal , "name is" , pet_name ,".")
prt("chloe")


#third code
def type_of_int(i):
    if i%2 == 0:
        return 'even'
    else:
        return 'odd'
print(type_of_int(67))