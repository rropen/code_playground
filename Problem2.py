from collections import defaultdict

def group_by_owners(file_dict):
    res = defaultdict(list)
    for key, val in sorted(file_dict.items()):
        res[val].append(key)
    print(str(dict(res)))

group_by_owners({'input.txt' : 'Dan', "code.py" : "Stan", "output.txt" : "Dan"})