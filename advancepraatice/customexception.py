#customer exception

class break_failure(Exception):
    pass

def bike(km):
    if km>60:
        raise break_failure("You can't break the rules")
    else:
        print("You can ride the bike")
        
    
try:
    bike(70)
except break_failure as e:
    print(f"An error occurred: {e}")
        
        