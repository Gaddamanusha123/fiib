#my_set={1,2,3,4,5,1,3,5,6,7}
#my_set.add("how")
#print(my_set)

#set={1,2,3,4,5,6,7,5,3,3,3,6,88,99}
#print(set)
#set.add("hey")
#print(set)
#set.remove(3)
#print(set)
#set.remove("hey")
#print(set)

#set.discard(set)
#print(set)

#set.clear()
#print(set)
#set1={1,2,3,4,6}
#set2={2,3,4,5,6,7}
#print(set1.union(set2))

#anu={1,2,3,4,5,8}
#set=(3,4,5,6,7,8)
#print(anu.union (set)



#num=1234
#temp=1234
#length=0
#pos=4
#while num>=:
 #   num=num//10
  #  length=length+1
   # if length>=pos:
    #    while temp!=0:
     #       digit=temp%10
      #      temp=temp//10
       #     if length==pos:
        #        print(digit)
         #       break
          #  length-=1
        #else:
         #   print("not enough position in the number")



# num=2
# nxt_prime_not_found=True
# while nxt_prime_not_found:
#     num=num+1
#     fact=0
#     for i in range(2,num):
#         if num%i=0:
#             fact=1
#             break
#         if fact==0
#         print(f"next prime is{num}")
#         nxt_prime_not_found=False

# a=0
# b=1
# for i in range(1,101):
#     if i==5000:
#         print(a)
#         c=a+b
#         a=b
      
fib=[0,1]

for i in range(2, 100):  # 100 is a safe limit
    next_fib = fib[i - 1] + fib[i - 2]
    if next_fib > 500:
        break
    fib.append(next_fib)

print("Fibonacci numbers between 0 and 500:", fib)
print("Total count:", len(fib))