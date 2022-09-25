from hashlib import md5
from datetime import datetime


class User:
    user_names = []
    users = []
    __admin_created = False

    def __init__(self, name, password, phone_no, email, address, my_orders=None, loading_data=False):
        self.name = name
        if loading_data:
            self.password = password
        else:
            self.password = md5(password.encode()).hexdigest()
        self.phone_no = phone_no
        self.email = email
        self.address = address
        self.my_orders = my_orders if my_orders else {}
        self.__is_admin = False
        User.user_names.append(self.name)
        User.users.append(self)

    @property
    def is_admin(self):
        return self.__is_admin

    def verify_password(self, password):
        if self.password == md5(password.encode()).hexdigest():
            return True
        else:
            return False

    def update_profile(self, **profile_data):
        if profile_data["name"]:
            self.name = profile_data["name"]
        if profile_data["phone_no"]:
            self.phone_no = profile_data["phone_no"]
        if profile_data["email"]:
            self.email = profile_data["email"]
        if profile_data["address"]:
            self.address = profile_data["address"]
        User.user_names = list(map(lambda x: x.name, User.users))

    def change_password(self, new_password):
        password = new_password
        self.password = md5(password.encode()).hexdigest()

    def ordered_food(self, food):
        now = datetime.now()
        str_now = now.strftime("%d/%m/%Y")
        if str_now in self.my_orders:
            self.my_orders[str_now].append(food)
        else:
            self.my_orders[str_now] = [food]

    def make_admin(self):
        if not User.__admin_created:
            self.__is_admin = True
            User.__admin_created = True
            return "Admin created"
        else:
            return None

    def get_user_data(self):
        user_data = {"name": self.name, "password": self.password, "phone_no": self.phone_no, "email": self.email,
                     "address": self.address}
        return user_data

    def print_ordered_history(self):
        if self.my_orders:
            print("{:<12} {}".format('date', 'food name'))
            for date, food in self.my_orders.items():
                print("{:<12} {}".format(date, ", ".join(food)))
            print("-".center(30, "-"))
        else:
            print("You haven't ordered anything yet")

    @classmethod
    def get_all_users_data(cls):
        users_data = []
        for user in cls.users:
            users_data.append({"name": user.name, "password": user.password, "phone_no": user.phone_no,
                               "email": user.email, "address": user.address, "my_orders": user.my_orders})
        return users_data

    @classmethod
    def get_user(cls, name):
        if name in User.user_names:
            return User.users[User.user_names.index(name)]
        else:
            return None
