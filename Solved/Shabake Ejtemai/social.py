comm = []
dataset= []
mess = []
find_ind =1
try:
    while(" ".join(comm[0:2]) != 'exit 0'):
        base_dict = dict()
        comm = input().split(' ')
        if(comm[0] == 'Add'):
            base_dict['name'],base_dict['gender'],base_dict['age'],base_dict['id']=comm[1:]
            dataset.append((comm[4],base_dict))
            mess.append(f"User {comm[-1]} added successfully")
        if(comm[0] == 'Find'):
            flag = 0
            count = 1
            for dic in sorted(dataset):
                if dic[1]['id'].startswith(comm[1]) and count<= 10:
                    mess.append(f"{find_ind} {dic[1]['name']} {dic[1]['gender']} {dic[1]['age']} {dic[1]['id']}")
                    flag = 1
                    count +=1
            if(flag==0):
                mess.append(f"{find_ind} No user found")
            find_ind+=1
except Exception as e:
    pass

for item in mess:
    print(item)
