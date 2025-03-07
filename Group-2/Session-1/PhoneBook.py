def get_name():
    while True:
        try:
            name = input("enter your name: ").strip()
            if not name.replace(" ", "").isalpha():  # اول فاصله هارو از اسم ورودی حذف میکنه، بعدش چک میکنه که ورودی فقط از جنس حروف هست یا نه
                raise ValueError("name should contain only letters and spaces.")
            return name
        except ValueError as e:
            print(f"invalid input: {e}")
            
def get_phone_number():
    while True:
        try:
            phone_number = input("enter your phone number: ").strip()
            if not phone_number.isdigit():#چک میکنه که شماره تلفن وارد شده فقط حاوی عدد باشه 
                raise ValueError("phone number should contain only digits.")
                
            if len(phone_number) != 11: #چک میکنه که شماره تلفن حتما 11 رقم باشه 
                raise ValueError("phone number must be exactly 11 digits.")
            return phone_number
        except ValueError as e:
            print(f"invalid input: {e}")

def phone_book():
    users = {}  # دیکشنری برای اختصاص دادن شماره به هر فرد و ذخیره مخاطبین

    while True:
        print("\n1. add a new contact")
        print("2. view all contacts")
        print("3. exit")
        choice = input("Choose an option (1,2,3): ").strip()

        if choice == "1":        # اضافه کردن اسم و شماره تلفن به دیکشنری
            name = get_name()
            phone_number = get_phone_number()
            users[name] = phone_number  
            print(f"contact '{name}' added to your phonebook")

        elif choice == "2":     #نمایش لیست افراد ثبت شده 
            if not users:
                print("contact list is empty.")
            else:
                print("\nlist of contacts:")
                for name, phone_number in users.items():
                    print(f"name: {name}, phone Number: {phone_number}")

        elif choice == "3":     #خروج از برنامه
            print("goodbye.")
            break

        else:
            print("please choose 1 , 2 or 3")
phone_book()
