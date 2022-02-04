import sys
import time


def login():
    print('\n')
    for i in range(101):
        sys.stdout.write("logging in ..."+str(i)+"%")
        time.sleep(0.005)
        for _ in range(100):
            sys.stdout.write('\33[D')
            sys.stdout.flush()


def put(question, whilee):
    if whilee == True:
        while True:
            p = input(question)
            if 3 <= len(p) <= 30:
                break
    else:
        p = input(question)
    return p


def g_account():
    while True:
        google = put("Email:\n", False)
        if "@" and ".com" in google:
            break
    return google


def password():
    password = put("Create a password:\n", True)
    return password


def matching_google_password(g, p):
    gmail = put("What's your Email:\n", False)
    password = put("What's your Password:\n", False)
    if gmail == g and password == p:
        return True

    else:
        return False


def fixing():
    choice = input("""
1 : Another User | 2 : Forgot Password | 3 : Don't have an account\n""")
    if choice == '1':
        g_account()
    elif choice == '2':
        print("It's not a real program you idiot\nAlso you have just put your password like 2 mins ago!!!\n")
    elif choice == '3':
        print("Sign up again -").com
    else:
        print("Fuck off")


def app_home():
    haha = True
    while haha == True:
        choice = input("""
Welcome To The Idriss Mouch Rajel
_________________________
1 : Sign Up  | 2 : Sign in (Actually you can't sign in without signing up So its just for decoration 🙂 )\n\n""")
        if choice == "1":
            g = g_account()
            p = password()
            choice0 = input("Do you want to sign in now?\n1 : Yes 2 : No\n")
            if choice0 == '1':
                choice = '2'
        if choice == "2":

            m = matching_google_password(g, p)
            login()
            if m == False:
                fixing()
            else:
                print("\n\nAccount and Password do match!\n\nGlad to see you again\n\n")
        print('*'*40)
        print("That's it, hope you like it\n")
        print("""please take in mind that this is a small try for Wassim 
        |
        ___\n""")
        ha = input("Wanna do it again\nY : yes | N : no\n")
        if ha.upper() == 'N':
            haha = False


app_home()
