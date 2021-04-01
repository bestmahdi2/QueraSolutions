a, string = input(), (input()).split(" ")
string = [int(i) for i in string]
print(sum(string) if sum(string) > 1 else 0)