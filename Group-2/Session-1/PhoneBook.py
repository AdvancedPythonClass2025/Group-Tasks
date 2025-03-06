def get_name():
    while True:
        try:
            name = input("enter your name: ").strip()
            if not name.replace(" ", "").isalpha():  # اول فاصله هارو از اسم ورودی حذف میکنه، بعدش چک میکنه که ورودی فقط از جنس حروف هست یا نه
                raise ValueError("name should contain only letters and spaces.")
            return name
        except ValueError as e:
            print(f"invalid input: {e}")