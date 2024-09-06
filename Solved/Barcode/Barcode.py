#ID : 52544
#https://quera.org/problemset/52544/

barcode = []
standard = [['1', '1', '1', '#', '#', '#', '1', '1', '1'],
 ['1', '0', '1', '#', '#', '#', '1', '0', '1'],
  ['1', '1', '1', '#', '#', '#', '1', '1', '1'],
   ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
     ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
      ['1', '1', '1', '#', '#', '#', '1', '1', '1'],
       ['1', '0', '1', '#', '#', '#', '1', '0', '1'],
        ['1', '1', '1', '#', '#', '#', '1', '1', '1']]
for _ in range(9):
    barcode.append(list(input()))

def IsOk():
    flag = True
    for r in range(9):
        for c in range(9):
            if (r<3 and c<3) or (r<3 and c<9 and c>=6) or (r>=6 and r<9 and c<3) or (r>=6 and r<9 and c>=6 and c<9):
                if (barcode[r][c] != standard[r][c] and barcode[r][c] != '2'):
                    flag = False
    return flag

def Count2():
    twos = 0
    for r in range(9):
        for c in range(9):
            if not ((r<3 and c<3) or (r<3 and c<9 and c>=6) or (r>=6 and r<9 and c<3) or (r>=6 and r<9 and c>=6 and c<9)) and barcode[r][c]=='2':
                twos+=1
    return twos

if(IsOk()):
    print(2**Count2())
else:
    print(0)