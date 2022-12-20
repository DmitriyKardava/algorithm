import singleList


if __name__ == '__main__':
    my_list = singleList.List()
    for i in range(0,10):
        my_list.add_first(i)

    print(my_list)
    my_list.reverse()
    print(my_list)

