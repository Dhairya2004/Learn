# ------------------------- MOBILE MANAGMENT SYSTEM  --------------------

from buyer import buyer_options
from admin import admin_options
import base64

# ------------------------- ALL NECESARY REQUIREMENTS ----------------------------

identity=int()
admin_password=base64.b64decode(b'Y2E=').decode("utf-8")

# ------------------------------ ERROR HANDLING --------------------------------- 

def errors():
    print('-'*50,'\n',"    ! SORRY AN UNEXPECTED ERROR OCCCURED !\n",' '*8," ! PLEASE INPUT CAREFULLY !")
    check()

# -------------------- TO CHECK WHETHER USER IS ADMIN OR CUSTOMER --------------------------

def check():
    try:
        global identity
        print('-'*50,'\n            WELCOME TO CENTRAL MOBILES\n           PLEASE CONFIRM YOUR IDENTITY\n',end='-'*50)
        print("\nPRESS 1 - IF YOU ARE A CUSTOMER\nPRESS 2 - IF YOU ARE ADMIN\nPRESS 3 - TO EXIT")
        identity=int(input('--> '))
        if identity==1:
            customer()
        elif identity==2:
            admin()
        elif identity==3:
            print('-'*50,'\n       THANKS FOR VISITING CENTRAL MOBILES\n               SEE YOU SOON !\n',end='-'*50)
        else:
            errors()
    except:
        errors()

# --------------------------- IF USER IS A CUSTOMER -------------------------------

def customer():
    buyer_options()

# ---------------------------  IF USER IS A ADMIN  -------------------------------

def admin():
    try:
        global admin_password
        print('\nPLEASE ENTER PASSWORD TO ACCESS ADMIN PANEL')
        password=input("--> ")
        if password == admin_password:
            admin_options()
        elif password == 'admin':
            print('-'*50,'\n        ! YOU USED BACKUP PASSWORD  ! \n( WE RECOMMEND USING MAIN PASSWORD INSTEAD )\n',end='-'*50)
            admin_options()
        else:
            print('\n             SORRY, INVALID PASSWORD !')
            check()
    except:
        errors()

check()

# ------------------------- A PROJECT BY DHAIRYA GUPTA - CA AMBABARI ----------------------------------

9636055632