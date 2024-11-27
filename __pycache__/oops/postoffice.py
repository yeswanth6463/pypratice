from abst import fd_acc

class post_office(fd_acc):
    def intrest_calc(self,name,years,amount,age):
        if age<60:
            if years>=5:
                print(f"*******{amount}******")
                month=years*12
                to_invs_am=month*amount
                intrest=to_invs_am*11.5//100
                returns=to_invs_am+intrest
                print(f"hi {name}\nyour total invst amount is:{to_invs_am} in {years} years \n intrest amount is :{intrest}\ntotal amount along with  invesment amount is ::rs.{returns}")
            elif years==3:
                print(f"*******{amount}******")
                month=years*12
                month=years*12
                to_invs_am=month*amount
                intrest=to_invs_am*9.5//100
                returns=to_invs_am+intrest
                print(f"hi {name}\nyour total invst amount is:{to_invs_am} in {years} years \n intrest amount is :{intrest}\ntotal amount along with  invesment amount is ::rs.{returns}")
            else:
                print(f"*******{amount}******")
                month=years*12
                to_invs_am=month*amount
                intrest=to_invs_am*7.5//100
                returns=to_invs_am+intrest
                print(f"hi {name}\nyour total invst amount is:{to_invs_am} in {years} years \n intrest amount is :{intrest}\ntotal amount along with  invesment amount is ::rs.{returns}")
        else:
            print(f"*******{amount}******")
            if years>=5:
                month=years*12
                to_invs_am=month*amount
                intrest=to_invs_am*14.5//100
                returns=to_invs_am+intrest
                print(f"hi {name}\nyour total invst amount is:{to_invs_am} in {years} years \n intrest amount is :{intrest}\ntotal amount along with  invesment amount is ::rs.{returns}")
            elif years==3:
                month=years*12
                month=years*12
                to_invs_am=month*amount
                intrest=to_invs_am*11.5//100
                returns=to_invs_am+intrest
                print(f"hi {name}\nyour total invst amount is:{to_invs_am} in {years} years \n intrest amount is :{intrest}\ntotal amount along with  invesment amount is ::rs.{returns}")
            else:
                month=years*12
                to_invs_am=month*amount
                intrest=to_invs_am*9.5//100
                returns=to_invs_am+intrest
                print(f"hi {name}\nyour total invst amount is:{to_invs_am} in {years} years \n intrest amount is :{intrest}\ntotal amount along with  invesment amount is ::rs.{returns}")
                
