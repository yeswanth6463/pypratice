

class break_failure(Exception):
    pass
class empty_fuel(Exception):
    pass
class puncher(Exception):
    pass
# # scenarios=['break_failure','empty_fuel','puncher']
# for  i in range(1,101):
#     distance=i
#     try:
#        if distance==30:
#          raise puncher
#        elif distance==60:
#          raise break_failure
#        elif distance==100:
#         raise empty_fuel
#     except break_failure:
#         print('break is failure')
#     except empty_fuel:
#         print('fuel is empty')
#     except puncher:
#        print('tyre has been gone')
    
class break_failure(Exception):
    pass
class empty_fuel(Exception):
    pass
class puncture(Exception):
    pass
start=0
end=101

def traveling(start,end):
    for i in range(start,end):
        if i==30:
            raise break_failure
        elif i==60:
            raise puncture
        elif i==100:
            raise empty_fuel
while start<end:
    try:
        traveling(start,end)
    except break_failure as e:
        print("break failure")
        start=31
    except puncture as e:
        print("puncture")
        start=61
    except empty_fuel as e:
        print("fuel is empty")
        start=101
