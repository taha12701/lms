class College:
  msg=".....Welcome to our College....."
  def __init__(self,name='',roll=0):
    self.name=name
    self.roll=roll

  def input(self):
    self.name=str(input("Enter your name : "))
    self.roll=int(input("Enter your roll# : "))
  
  def get_input(self):
    print(f"Student's name: {self.name} ")
    print(f"Student's name: {self.roll} ")

  def passw(self,password):
    self._password=password
    return self._password
  
  @staticmethod
  def message():
    print(College.msg)
    
  def reveal(self):
    print(f"Your password is : {self._password}")

  @staticmethod
  def last_msg():
    print(".....Thank you for using our services.....")

c1=College()

c1.input()
c1.get_input()
c1.message()

