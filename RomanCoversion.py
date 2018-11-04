#Convert an integer in a Roman numeral

def Romandigit(n):
    #initialization
    numeral=""
    no=n
    
    #Convert thoussands
    r=n%1000
    q=n//1000
    for i in range(q):
        numeral+="M"
    
    #Convert hundreds
    n=r
    q=n//100
    r=n%100
    if q<4:
        for i in range(q):
            numeral+="C"
    elif q==4:
        numeral+="CD"
    elif q==5:
        numeral+="D"
    elif q<9:
        numeral+="D"
        for i in range(q-5):
            numeral+="C"
    else:
        numeral+="CM"
    
    #Convert tens
    n=r
    q=n//10
    r=n%10
    if q<4:
        for i in range(q):
            numeral+="X"
    elif q==4:
        numeral+="XL"
    elif q==5:
        numeral+="L"
    elif q<9:
        numeral+="L"
        for i in range(q-5):
            numeral+="X"
    else:
        numeral+="XC"
    
    #Convert units
    n=r
    q=n//1
    r=n%1
    if q<4:
        for i in range(q):
            numeral+="I"
    elif q==4:
        numeral+="IV"
    elif q==5:
        numeral+="V"
    elif q<9:
        numeral+="V"
        for i in range(q-5):
            numeral+="I"
    else:
        numeral+="IX" 
    
    
    print (str(no)+"="+ numeral)
    
Romandigit(1000)
Romandigit(1500)
Romandigit(900)
Romandigit(1756)
Romandigit(1957)
