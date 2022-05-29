num=int(input('enter number of consecutive heads'))
n=0
for i in range (0,num,1):
    n=(n+1)*2
print ('The number of tosses required is ',n)
