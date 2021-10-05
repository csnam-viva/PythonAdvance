'''
1.comprehension :
- compression 코드를 간결하게 작성하기 위한 문법 
- [] {} 를 사용한다
2.Generator expression
- ()를 사용한다

'''
v_list = [1, 2, 3]
v_dict_key = ["korea", "japen", "china"]
v_dict_value = [82, 81, 86]


def list_print_comprehension():
    v_list2 = [x*x for x in v_list]
    
    print(v_list2)

def list_print_for():
    v_list2=[]
    for x in v_list:
        v_list2.append(x*x)
    print(v_list2)

def print_dict_compreshension():
    v_dic = {k:v for k,v in zip(v_dict_key,v_dict_value)}
    print(v_dic)

def print_dict_for():
    v_dic = {}
    for k,v in zip(v_dict_key,v_dict_value):
        v_dic[k]=v
    print(v_dic)

def main():
    # print(v_list)
    # list_print_comprehension()
    # list_print_for()
    # print_dict_compreshension()
    # print_dict_for()
    g1 = make_generator_list()
    show_generator(g1)
    print("--------")
    g1 = make_generator_list2()
    show_generator(g1)


SAMPLE=[1,2,3,4]
def make_generator_list():
    generator1= (x*x for x in SAMPLE)
    print(generator1)
    return generator1
def make_generator_list2():
    generator1= (x for x in range(10))
    print(generator1)
    return generator1

def show_generator(items):
    for x in items:
        print(x)




if __name__ == "__main__":
    main()


