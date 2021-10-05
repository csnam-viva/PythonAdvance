'''
데코레이션:
함수나 클래슬 인자로 받음
'''

import time
from functools import update_wrapper, wraps


def deco(func):
    def wrapper():
        print("before")
        ret = func()
        print("after" )
        return ret
    return wrapper
@deco #base 함수를 데코레이션 꾸미는 함수
def base():  
    print("base function")

'''
데코레이션 없이 클로져로 동일코드 구현
'''

def deco_no(func):
    def wrapper():
        print("before")
        ret = func()
        print("after" )
        return ret
    return wrapper

def base_no_deco():
    print("base no func - no deco")
'''
 방법6)  데코레이션 사용
 1.인자있는 decorator
 2.여러개의 decodator
'''
def decorate1(func):
    def wraper(name):
        #print("---------------")
        aa= func(name)
        #print("---------------")
        return "<p> {0} </p>".format(aa)
    return wraper

def deco_strong(func):
    def wraper(name):
           return "<strong> {0} </strong>".format(func(name))
    return wraper

@deco_strong  ## 여러개의 decodator
@decorate1        
def getText(name):
     a = "vivakorea {%s} bravo" % (name)
     return a;

'''
방법7) 데코레이션 사용   
'''

def measure(func):
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(" %s runningtime = %s" % (func.__name__,end-start))
    return wrapper

@measure
def work(delaytime):
    time.sleep(delaytime)

'''
방법8)
'''
import datetime

def parameter_log(func):
  
    @wraps(func)
    def wrapper(*args,**kwargs):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("%s  args: %s, kwarg: %s" % (timestamp,args,kwargs))
        func(*args,**kwargs)
        print("parameter_log end")
        return 
    return wrapper

@measure
@parameter_log
def work2(delaytime):
    time.sleep(delaytime)

'''
방법9)
항상 내부함수에서 wraps 데코레이터를 선언해줌
from functools import wraps
@wraps(func)
def wrapper(*args,**kwargs):
'''

'''
클래스 Decorator
'''
class MeasureCheck:
    def __init__(self,f):
        print("__init_start")
        self.func = f
        update_wrapper(self,self.func) 
        print("__init_end")
        # 

    # 클로저 형태로 되어있지 않음
    # @ 데코레이터 사용하지 않음 -> update_wrapper 사용   
    # 데코레터 BASE  위에 데코레이터 키워드를 사용 @MeasureCheck  
    def __call__(self, *args, **kwds):
        start = time.time()
        result = self.func(*args,**kwds)
        end = time.time()
        print("%s func running time= %s" % (self.func.__name__,end-start))
        #return result

@MeasureCheck        
def worker_class(delay):
    time.sleep(delay)

'''
클래스로 사용하기
__init__ 메서드로 worker함수가 전달
__call__ 메서드로  매개변수 전달받음.
클래스로 구현한 데코레이터에서는 클로져 형태로 구현할 필요가 없음
'''
'''
방법 10)
데코레이터에 매매변수가 있는 경우는 클로져 형태로 클래스구현
'''        
class MeasureCheck2:
    def __init__(self,active_state):
        self.measure_active = active_state
    def __call__(self,func):
        
        def wrapper(*args,**kwargs):
            if self.measure_active is False:
                print("measure_active %s" % self.measure_active)
                return func(*args,**kwargs)
            start = time.time()
            result = func(*args,**kwargs)
            end = time.time()
            print("%s  %s" % (func.__name__, end-start))
            return result
        return wrapper     #클로져 형태로 구현

@MeasureCheck2(True)
def active_worker(delay):
    time.sleep(delay)

@MeasureCheck2(False)   
def inactive_worker(delay):
    time.sleep(delay)

            

if __name__ == "__main__":
    #방법1
    #base() # 데코레이션 이션
    #방법2
    #deco_no(base_no_deco)()
    #방법4
    #f = base_no_deco
    #deco_no(f)()
    #방법5
    #print("--5")
    #g = base_no_deco
    #fg= deco(base_no_deco)
    #fg()

    #방법6)decorator사용 
    #print(getText("csnam"))
    #print(getText("lee"))

    #방법7)데코레이션 사용
    #measure(work)(5)
    #work(5)
    #방법8)데코레이션 사용
    #work2(7)
    #방법9
    #worker_class(3)
    #방법10
    active_worker(3)
    inactive_worker(3)



