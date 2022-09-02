class Account:
    def __init__(self):
        self.balance = 0
        self.pin = ""
        self.menu()

    def menu(self):
        prompt = '''
        1. type 1 to create new account
        2. type 2 to add/withdraw funds
        4. type 3 to check balance\n
        '''
        choice = int(input(prompt))
        if choice == 1:
            self.write_pin()
        elif choice == 2:
            self.write_bal()
        elif choice == 3:
            self.check_funds()

    def set_pin(self):
        self.write_pin()

    def check_funds(self):
        if self.check_pin():
            print(f"your current balance is {self.balance}")
            self.menu()
        else:
            print("invalid pin")
            self.menu()

    def check_pin(self):
        temp_pin = int(input("enter pin (4 digit number): "))
        self.pin = temp_pin
        temp_datafile = open("Data.txt", "r")
        data_list = temp_datafile.readlines()
        temp_list = [

        ]
        for entry in data_list:
            temp_list.append(str(entry))
        temp_list1 = [

        ]
        bal_list = [

        ]
        for entry1 in temp_list:
            temp_list1.append(entry1[:4])
        for entry1 in temp_list:
            bal_list.append(entry1[4:])
        try:
            account = temp_list1.index(str(self.pin))
            self.balance = int(bal_list[account])
            return True
        except:
            return False

    def write_pin(self):
        if not self.check_pin():
            temp_pin = int(input("confirm pin (4 digit number): "))
            self.pin = temp_pin
            temp_datafile = open("Data.txt", "r")
            data_list = temp_datafile.readlines()
            temp_list = [

            ]
            for entry in data_list:
                temp_list.append(str(entry))

            temp_list2 = list(temp_list)
            temp_list2.append(f"\n{self.pin}{str(0)}")
            temp_datafile2 = open("Data.txt", "w")
            for acc in temp_list2:
                temp_datafile2.write(acc)
        else:
            print("account already exists")
            self.write_pin()

    def write_bal(self):
        if self.check_pin():
            temp_datafile = open("Data.txt", "r")
            data_list = temp_datafile.readlines()
            temp_list = [

            ]
            for entry in data_list:
                temp_list.append(str(entry))
            pin_list = [

            ]
            bal_list = [

            ]
            for entry1 in temp_list:
                pin_list.append(entry1[:4])
            for entry1 in temp_list:
                bal_list.append(entry1[4:])

            pin_to_check = str(self.pin)
            pin_no = pin_list.index(pin_to_check)
            temp_list.pop(pin_no)
            pop_bal = int(bal_list[pin_no])
            print(f"your current balance is {pop_bal}")
            prompt = """
             1. type 1 to add funds
             2. type 2 to withdraw funds\n
        
            """
            choice = int(input(prompt))
            if choice == 1:
                add_fund = int(input("enter amount: "))
                self.balance = pop_bal + add_fund
                print(f"your current balance is {self.balance}")
                temp_list.append(f"\n{pin_to_check}{str(self.balance)}")
                temp_datafile2 = open("Data.txt", "w")
                for acc in temp_list:
                    temp_datafile2.write(f"{acc}")

            elif choice == 2:
                withdraw_fund = int(input("funds to withdraw: "))
                self.balance = pop_bal
                if withdraw_fund >= int(self.balance):
                    print("insufficient funds")
                    self.menu()
                else:
                    self.balance = pop_bal - withdraw_fund
                    print(f"your current balance is {self.balance}")
                    temp_list.append(f"\n{pin_to_check}{str(self.balance)}")
                    temp_datafile2 = open("Data.txt", "w")
                    for acc in temp_list:
                        temp_datafile2.write(f"{acc}")
        else:
            print("invalid pin")
            self.menu()
