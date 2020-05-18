def safe_print_list(my_list=[], x=0):
    count = 0
    for item in my_list:
        if count in range(x):
            try:
                print(item, end="")
                count += 1
            except:
                break
    print('')
    return count
