class ATM:
    def __init__(self, balance=1000, pin="1234"):
        self.balance = balance
        self.pin = pin

    def check_pin(self):
        entered_pin = input("PIN kiriting: ")
        return entered_pin == self.pin

    def check_balance(self):
        print(f"Sizning balansingiz: ${self.balance}")

    def deposit(self):
        amount = float(input("Qancha pul qo'shmoqchisiz? $"))
        if amount > 0:
            self.balance += amount
            print(f"${amount} qo'shildi. Yangi balans: ${self.balance}")
        else:
            print("Noto‘g‘ri miqdor kiritildi!")

    def withdraw(self):
        amount = float(input("Qancha pul yechmoqchisiz? $"))
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"${amount} yechildi. Yangi balans: ${self.balance}")
        else:
            print("Noto‘g‘ri miqdor yoki yetarli mablag‘ mavjud emas!")

    def start(self):
        if not self.check_pin():
            print("Noto‘g‘ri PIN! Dasturdan chiqildi.")
            return

        while True:
            print("\n1. Balansni tekshirish")
            print("2. Pul qo‘shish")
            print("3. Pul yechish")
            print("4. Chiqish")
            choice = input("Tanlang: ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                print("Chiqyapsiz...")
                break
            else:
                print("Noto‘g‘ri tanlov! Qayta urinib ko‘ring.")

# Dastur ishga tushadi
atm = ATM()
atm.start()
