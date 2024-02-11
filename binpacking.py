import timeit
start=timeit.default_timer()
n=15
d={17:(1,2,1),15:(3,1,1),14:(2,2,2),13:(2,3,2),12:(2,3,4),11:(1,2,1),10:(3,1,1),9:(2,2,2),8:(2,3,2),7:(2,3,4)}
a1=20
b1=20
c1=20
c=0
m1=()
m2=()
m3=()
for i in d:
    if(c==0 and (d[i][0]<=a1 and d[i][1]<=b1 and d[i][2]<=c1)):
     print("The packet is packed at",(0,0,0))
     c=c+1
     m1=(d[i][0],0,0)
     m2=(0,d[i][1],0)
     m3=(0,0,d[i][2])
     if((m1[0]<=a1 and m1[0]<=b1 and m1[2]<=c1) or (m2[0]<=a1 and m2[1]<=b1 and m2[2]<c1) or (m3[0]<=a1 and m3[1]<=b1 and m3[2]<=c1)):
         print("Extreme points generated:")
         print(m1)
         print(m2)
         print(m3)
     else:
        print("Bin is full")
    elif(c>0):
     if ((m1[0]+d[i][0]<=a1) and (m1[1]+d[i][1]<=b1) and (m1[2]+d[i][2]<=c1)):
         print("The packet is packed at",m1)
         temp=(m1[0],m1[1],m1[2])
         m1=(temp[0]+d[i][0],temp[1],temp[2])
         m2=(temp[0],temp[1]+d[i][1],temp[2])
         m3=(temp[0],temp[1],temp[2]+d[i][2])
         if((m1[0]<=a1 and m1[0]<=b1 and m1[2]<=c1) or (m2[0]<=a1 and m2[1]<=b1 and m2[2]<c1) or (m3[0]<=a1 and m3[1]<=b1 and m3[2]<=c1)):
             print("Extreme points generated:")
             print(m1)
             print(m2)
             print(m3)
         else:
            print("Bin is full")
        
     elif((m2[0]+d[i][0]<=a1) and (m2[1]+d[i][1]<=b1) and (m2[2]+d[i][2]<=c1)):
         print("The packet is packed at",m2)
         temp=(m2[0],m2[1],m2[2])
         m1=(temp[0]+d[i][0],temp[1],temp[2])
         m2=(temp[0],temp[1]+d[i][1],temp[2])
         m3=(temp[0],temp[1],temp[2]+d[i][2])
         if((m1[0]<=a1 and m1[0]<=b1 and m1[2]<=c1) or (m2[0]<=a1 and m2[1]<=b1 and m2[2]<c1) or (m3[0]<=a1 and m3[1]<=b1 and m3[2]<=c1)):
             print("Extreme points generated:")
             print(m1)
             print(m2)
             print(m3)
         else:
            print("Bin is full")
     elif((m3[0]+d[i][0]<=a1) and (m3[1]+d[i][1]<=b1) and (m3[2]+d[i][2]<=c1)):
         print("The packet is packed at",m3)
         temp=(m3[0],m3[1],m3[2])
         m1=(temp[0]+d[i][0],temp[1],temp[2])
         m2=(temp[0],temp[1]+d[i][1],temp[2])
         m3=(temp[0],temp[1],temp[2]+d[i][2])
         if((m1[0]<=a1 and m1[0]<=b1 and m1[2]<=c1) or (m2[0]<=a1 and m2[1]<=b1 and m2[2]<c1) or (m3[0]<=a1 and m3[1]<=b1 and m3[2]<=c1)):
             print("Extreme points generated:")
             print(m1)
             print(m2)
             print(m3)
         else:
            print("Bin is full")
     else:
        print("The packet can't be packed")
    else:
       print("The packet can't be packed")
stop=timeit.default_timer()
print("time: ",stop-start)