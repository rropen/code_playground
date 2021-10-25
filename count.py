def count(num):
    list_ = []
    for n in str(num):
        list_.append(int(n))
    print(sum(list_))
    print(len(str(num)))


count(12345)
