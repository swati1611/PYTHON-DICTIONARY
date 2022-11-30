# a=[[78,76,94,86,88],[91,71,98,65,76],[95,45,78,52,49]]
# i=0
# while i<len(a):
#     j=0
#     sum=0
#     totalmarks=0
#     while j<len(a[i]):
#         sum=sum+(a[i][j])
#         totalmarks+=1
#         j=j+1
#     i=i+1
# print(i,"year ka avg",sum//totalmarks)

# a=[12,23,14,56,19,9,15,25,31,42]
# i=0
# c=0
# c1=0
# while i<len(a):
#     if a[i]%2==0:
#         c=c+1
#     else:
#         c1+=1
#     i+=1
# print("even",c)
# print ("odd",c1)

# a=[1,2,3,4,5,6]
# i=0
# sum=0
# sum1=0
# while i<len(a):
#     if a[i]%2==0:
#         sum=sum+(a[i])
#     else:
#         sum1=sum1+(a[i])
#     i=i+1    
# print(sum)
# print (sum1)


# list1= [19,17,12,17,17,18,10,17,14,12,19,17,12,13,11]
# new=[]
# for a in list1:
#     n=list1.count(a)
#     if n >1:
#         if new.count(a)==0:
#             new.append(a)
# print(new)

# a=[19,17,12,17,17,18,10,17,14,12,19,17,12,13,11]
# new=[]
# i=0
# while i<len(a):
#     n=a.count(i)
#     if n>1:
#         if new.count(i)==0:
#             new.count(i)
# print(new)          
# # 

# a=['flour','cheese','carrots']
# i=0
# while i<len(a):
#     print(i,":",a[i])
#     i+=1


# a=[1,2,2,5,8,4,4,8]
# b=[]
# pro=1
# i=0
# while i<len(a):
#     if a[i] not in b:
#        # pro=pro*(i%10)
#         b.append(a[i])
#        # print(b)
#         pro=pro*(a[i])
#     i+=1
# print(b)
# print("count=",len(b))

# a="9119"
# i=0
# while i<len(a):
#     b=int(a[i])**2
#     print(b,end=" ")
#     i=i+1

    

# a="pinck"
# i=1
# while i<=len(a):
#     print(a[-i])
#     i=i+1


# a=[1,2,5,6,4,0]
# i=0
# min=1
# while i<len(a):
#     if (a[i])<min:
#         min=a[i]
#     i=i+1
# print(min)

# a=[1,1,2,2,4,4,3,3]
# i=0
# b=[]
# while i<len(a):
#     if a[i]not in b:
#         b.append(a[i])
#     i=i+1
# print(b)


# a=[1,2,[3,5,6],[7,9]]
# i=0
# sum=0
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             sum=sum+(a[i][j])
#             j=j+1
#     i=i+1
# print(sum)
        

# a=[[0],[1,3],[5,7],[9,11],[13,15,17]]
# i=0
# max=0
# min=1
# c=[]
# k=[0]
# while i<len(a):
#     if max<len(a[i]):
#         max=len(a[i])
#         c=a[i]
#     if min>len(a[i]):
#         k=a[i]
#     i+=1
# print(max,c)
# print(min,k)




