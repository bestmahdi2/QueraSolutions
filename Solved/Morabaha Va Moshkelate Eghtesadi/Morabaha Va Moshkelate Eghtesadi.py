# مربّاها و مشکلات اقتصادی
# ID : 20249
# https://quera.ir/problemset/contest/20249/%D8%B3%D8%A4%D8%A7%D9%84-%D9%85%D8%B1%D8%A8%D8%A7%D9%87%D8%A7-%D9%88-%D9%85%D8%B4%DA%A9%D9%84%D8%A7%D8%AA-%D8%A7%D9%82%D8%AA%D8%B5%D8%A7%D8%AF%DB%8C
# https://b2n.ir/u30756

n, k = [int(i) for i in input().split()]
string = [int(i) for i in input().split()]
sums = sum(string)

print(n - (- (-sums // k)))
