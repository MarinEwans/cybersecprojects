#enter a password that has min length of 8. check if the password is using all lowercase/uppercase, all numbers 
#output error if it uses lowercase/uppercase and numbers output the password is mid, if it
#contains uppercase,lowercase,numbers and special charecters output is strong
import re 
password=input("please enter your password")
def PassCheck(password):
    if len(password)<8:
        print("password is too short it has to be minimum 8 charecters:")
    else:
        lower_error=password.islower()
        digit_error=password.isdigit()
        upper_error=password.isupper()
        symbol_error=re.search(r"\W",password) is None#regular expression which searches for symbols in password
        lowdig_error=password.islower() or password.isdigit()
        updig_error=password.isupper() or password.isdigit()
        symdig=symbol_error or password.isdigit()
        symup=symbol_error or password.isupper()
        symlow=symbol_error or password.islower()
        password_ok=not (lower_error or digit_error or upper_error or lowdig_error or updig_error)
        return {
        'password_ok' : password_ok,
        'digit_error,weak_password' : digit_error,
        'uppercase_error weak_password' : upper_error,
        'lowercase_error weak_password' : lower_error,
        'symbol_error, weak_password' : symbol_error,
        'lowdig_error mid_password' : lowdig_error,
        'updig_error mid_password' : updig_error,
        'symup mid_password' : symup,
        'symlow mid_password' : symlow,
        'symdig mid_password' : symdig,
       
        
    }
print(PassCheck(password))

