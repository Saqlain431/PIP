lst = [] 
  
# number of elemetns as input 
n = int(input("Enter number of elements : ")) 
  
# iterating till the range 
for i in range(0, n): 
    ele = int(input()) 
  
    lst.append(ele) # adding the element 
      
print(lst) 

l=[]

for i in range(0,n):
    if lst[i]%2==0:
      l.append(lst[i])

print(l)
