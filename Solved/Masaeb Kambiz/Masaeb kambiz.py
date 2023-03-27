#ID : 66862
#https://quera.org/problemset/66862/


import itertools

kambiz = input()
slice = [1,2,3]
AllSlices  = itertools.product(slice, repeat=4)

def IsOctet(str_in):
    if int(str_in[0])==0 and len(str_in)!=1:
        return False
    elif int(str_in)>255:
        return False
    else:
        return True

def IsValid(myip, myslice):
    acc = list(itertools.accumulate(myslice))
    if acc[3]!=len(myip):
        return False
    elif IsOctet(myip[:acc[0]]) and IsOctet(myip[acc[0]:acc[1]]) and IsOctet(myip[acc[1]:acc[2]]) and IsOctet(myip[acc[2]:acc[3]]):
        return True
    else:
        return False

for slice in AllSlices:
    if(IsValid(kambiz, slice)):
        acc = list(itertools.accumulate(slice))
        print(f"{kambiz[:acc[0]]}.{kambiz[acc[0]:acc[1]]}.{kambiz[acc[1]:acc[2]]}.{kambiz[acc[2]:acc[3]]}")
