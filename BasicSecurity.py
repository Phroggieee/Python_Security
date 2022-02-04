import time
t = 0


def name_and_password():
    global FN
    global LN
    global Password1
    FN = input("First Name? ")
    time.sleep(0.5)
    LN = input("Last Name? ")
    print("\n")
    time.sleep(0.2)
    print("Hello", FN, LN, )
    Password1 = input("What is your password? ")
    write_password()
    read_password()
    write_name()
    read_name()
    check_login_password()


def write_name():
    global Full
    name_enter = open("NameFolder", "w")
    name_enter.write(FN)
    name_enter.write(" ")
    name_enter.write(LN)
    name_enter.close()
    Full = FN + " " + LN


def read_name():
    global file_name
    name_read = open("NameFolder", "r")
    for x, line in enumerate(name_read):
        if x != 2:
            file_name = line
    name_read.close()


def write_password():
    password_enter = open("PasswordFolder", "w")
    password_enter.write(Password1)
    password_enter.close()


def read_password():
    global password
    password_read = open("PasswordFolder", "r")
    for v, line in enumerate(password_read):
        if v != 2:
            password = line
    password_read.close()


def check_login_password():
    global login_password
    check_pass = open("HostLoginPasswords", "r")
    for u, line in enumerate(check_pass):
        if u != 2:
            login_password = line
    check_pass.close()
    if password == login_password:
        time.sleep(0.2)
        print("Processing...")
        time.sleep(0.8)
        host_check()
    else:
        print("Welcome")


def read_host_password():
    global host_password
    host_password_read = open("HostPassword", "r")
    for y, line in enumerate(host_password_read):
        if y != 2:
            host_password = line
    host_password_read.close
    print("Host Account")
    pw = input("Enter Password- ")
    if pw == host_password:
        print("Welcome Host")
    else:
        print("Welcome")


def host_check():
    global host_name
    host_checker = open("Host", "r")
    for z, line in enumerate(host_checker):
        if z != 2:
            host_name = line
    host_checker.close()
    if host_name == Full:
        read_host_password()
    else:
        print("Welcome")


def create():
    global FN2
    global LN2
    global Password2
    FN2 = input("What is your First Name? ")
    time.sleep(0.5)
    LN2 = input("What is your Last Name? ")
    print("\n")
    time.sleep(0.2)
    print("Hello", FN2, LN2, )
    Password2 = input("What is your password? ")


def Account_Check():
    global qst1
    qst1 = input("Do you have an account? Y/N ")
    menu()


def menu():
    global t
    if qst1 == "Y":
        time.sleep(0.1)
        name_and_password()
    elif qst1 == "y":
        time.sleep(0.4)
        entr = input("Login > Entr")
        if entr == "" \
                   "":
            time.sleep(0.1)
            name_and_password()
    elif qst1 == "N":
        CO = input("Create one?")
        if CO == "Y":
            create()
        elif CO == "N":
            exit()
        else:
            print("Invalid")
            exit()
    elif qst1 == "n":
        CO2 = input("Create one? ")
        if CO2 == "Y":
            time.sleep(0.2)
            create()
        elif CO2 == "y":
            time.sleep(0.2)
            create()
        elif CO2 == "N":
            time.sleep(0.2)
            print("Goodbye")
            exit()
        elif CO2 == "n":
            time.sleep(0.2)
            print("Goodbye")
            exit()
        else:
            time.sleep(0.2)
            print("Invalid")
            print("Try Again")
            Account_Check()
    else:
        if t != 2:
            time.sleep(0.2)
            print("Invalid Answer")
            print("Try Again")
            print("\n")
            t += 1
            Account_Check()
        else:
            time.sleep(0.2)
            print("\n")
            print("Too Many Invalid Answers")
            time.sleep(1)


Account_Check()
