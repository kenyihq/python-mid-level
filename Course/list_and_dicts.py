def run ():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname" : "Kenyi", "lastname" : "Hancco"}

    super_list = [
        {"firstname" : "Axel", "lastname" : "Hancco"},
        {"firstname" : "Ariana", "lastname" : "Hancco"},
        {"firstname" : "Over", "lastname" : "Hancco"},
        {"firstname" : "Martha", "lastname" : "Quispe"}
    ]

    super_dict = {
        "natural_nums" : [1,2,3,4,5],
        "integer_nums" : [-1,0,1],
        "floating_nums" : [1.1,2.1,3.4]
    }

    for key, value in super_dict.items():
        print(key, value)

    for i in my_list:
        print(i)

    for i in super_list:
        for key, values in i.items():
            print(key, values)



if __name__ == '__main__':
    run()