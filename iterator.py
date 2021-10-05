'''
iterable: 한번에 모든값을 반환할수도 있음.
iterator: 한번에 한나씩 반환하는 개체
1) 어떤 상태를 저장,next로 하나씩 반환하는 개체
2) 더이상없으면 StopIteration 발생
3) for문은 내부적으로 StopIteration 예외가 처리되어 있음.
4) iter함술르 통해 변환되었을때만 이터레이터라고 할 수 있음.
'''
def study():
    x = [1,2,3]
    y ={"red": 1, "blue": 2, "green": 3}

    x_iterator = iter(x)
    y_iterator = iter(y)
    print("x type: %s" % type(x))
    print("x type: %s" % type(y))
    print("x iter: %s" % type(x_iterator))
    print("x iter: %s" % type(y_iterator))

    print("x iter next: %s" % next(x_iterator))
    print("x iter next: %s" % next(y_iterator))

    #print("x next: %s" % next(x))
    #print("x next: %s" % next(y))
'''
이터레이터 vs 제너레이터 이터레이터
1)이터레이터 next: container에 있는 다음항목
    모두연산한후 하나씩 반환
2)제너레이터 next:  제너레이터함수를 실행하거나  마지막으로 yield구문에서 시작
  값을 반환할때 연산을 수행
  
yield가 있어야 generator임
yield 만나면 그상태를 보관하고 있다가 next호출하면 로직 수행 
yield를 통해 값을 반환
next를 호출해야 실행됨,for문에서는 next함수로 호출해서 값이 출력됨

제너레이터가 이터레이터보다 압도적으로 빠르다.
lazy evaluation:필요할 대 실행




'''
def gen():
    yield 1
    yield 2
    yield 3

def normal():
    return 1
    return 2
    return 3

def main():
    print ("=== print gen function ===")
    print (gen())

    print ("=== print normal function===")
    print (normal())

    print ("=== print gen function in loop ===")
    for g in gen():
        print (g)

    print ("=== print normal function in loop ===")
    for n in normal():
        print (n)

def gen(items):
    count =0 
    for item in items:
        if count ==10:
            return -1
        count += 1
        yield item

def main2():
    print(range(15))
    for i in gen(range(15)):
        print(i)

if __name__ == "__main__":
    #main()
    main2()

