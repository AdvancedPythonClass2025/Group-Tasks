class Manager(Employee):
    def manage_team(self):
        print(f"{self.name} در حال مدیریت تیم است.")
        
class developer(Employee):
     def write_code(self):
         print(f"{self.name} در حال نوشتن کد است.")
