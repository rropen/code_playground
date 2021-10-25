from collections import defaultdict

test_dict = {"input.txt": "Dan", "Code.py": "Stan", "Output.txt": "Dan"}


def group_by_owners(file_dict):
    users_files = defaultdict(list)
    for file, owner in sorted(file_dict.items()):
        users_files[owner].append(file)


print(group_by_owners(test_dict))
