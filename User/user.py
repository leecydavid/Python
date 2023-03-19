class User():
    def __init__(self, firstname, lastname, email, age):
        self.firstname = firstname 
        self.lastname = lastname 
        self.email = email 
        self.age = age 
        self.member = False
        self.cardpoints = 0

    def display_info(self):
        print("First Name:", self.firstname)
        print('Last Name:', self.lastname)
        print('Email:', self.email)
        print('Age:', 30)
        print('Memeber:', self.member)
        print('Points:', self.cardpoints)
        return self

    def enroll(self, cardpoints):
        self.member = True
        self.cardpoints = cardpoints
        # print('Registered Member:', self.member)
        # print('Total Cardpoints:', self.cardpoints)
        return self

    def spend_points(self, amount):
        self.amount = amount
        if self.cardpoints >= self.amount:
            self.cardpoints = self.cardpoints - self.amount
        
        return self


David = User('David', 'Lee', 'david@gmail.com', 30)
David.display_info().enroll(200).display_info().spend_points(50).display_info()

Harry = User('Harry', 'Potter', 'pottah69@hogwarts,com', 60)
Harry.display_info().enroll(500).display_info().spend_points(100).display_info()

