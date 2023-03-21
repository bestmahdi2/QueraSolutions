#ID : 66872
#https://quera.org/problemset/66872/

def copy(string, n):
    if n == 0:
        return ""
    return string + copy(string, n-1)

def compare(string1, string2):
    if string1 == string2:
        return True
    return False

def substr(string1, string2):
    mcount = 0
    if len(string1) > len(string2):
        return 0 
    for i in range(len(string2)-len(string1)+1):
        if compare(string1, string2[i:i+len(string1)]):    #baab   baabaab
            mcount += 1                                    #4       #7
    return mcount

def lenght(string,mylen):
    if len(string)==mylen:
        return True
    return False

def attach(mystring, str_a, count ,key):
    if substr(str_a+key, mystring) == count:
        return True
    return False

string = input()
order = ""
order_list = []
while(order != "Is it right or not?"):
    order = input()
    order_list.append(order)
khoobi =0 
for order in order_list:
    tmp = order.split()
    if tmp[0] == "copy":
        string = (copy(tmp[1], int(tmp[2])) + string[len(tmp[1])*int(tmp[2]):])
    elif tmp[0] == "compare":
        if compare(string, tmp[1]):
            khoobi += 1
    elif tmp[0] == "substr":
        if(int(tmp[2]) == substr(tmp[1], string)):
            khoobi += 1
    elif tmp[0] == "length":
        if lenght(string, int(tmp[1])):
            khoobi += 1
    elif tmp[0] == "attach":
        if attach(string, tmp[1], int(tmp[2]), tmp[3]):
            khoobi += 1
    
if(khoobi>=(len(order_list)-1)/2):
    print("Eyval")
else:
    print("HeifShod")

