def plusMinus(arr):
    # Write your code here
    pC= 0
    nC = 0
    zc=0
    for i in arr:
        if i>0:
            nC= (nC+1)*1.0
        if i<0:
            pC =(pC+ 1)*1.0
        if i==0:
            zc=(zc+1)*1.0
    n= len(arr)
    
    print(pC/n)
    print(nC/n)
    print(zc/n)
         
arr = [1,1,-1,0,-1]   
plusMinus(arr)