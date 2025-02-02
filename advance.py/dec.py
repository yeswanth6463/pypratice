def check_user(func):
    def wrapper(*args, **kwargs):
        for i in args:
            username = i['username']
            usertype = i['usertype']
            active = i['active']
            # prints: arun, yes
            if active:
                print(f"Welcome {username} sir")
                if usertype == 'admin':
                    print("Now you're in admin")
                elif usertype == 'customer':
                    print("Now you're in customer")  # prints: welcome erin sir
                else:
                    print(f"Now you're in {usertype}")  # prints: now you're in mergent
            else:
                print("Hello, your account is inactive. Can you activate the account?")
    return wrapper

# Example dictionary data
dec = (
    {'username': 'erin', 'usertype': 'admin', 'active': True},
    {'username': 'yes', 'usertype': 'mergent', 'active': True}
)

@check_user   
def user_type(*args):
    print("usertype data")
print()
@check_user
def is_active(*args):
    print("active status")

# Calling the decorated functions with the example data
user_type(*dec)
print()
is_active(*dec)
