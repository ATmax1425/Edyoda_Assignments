from product import Product
from user import User
from data_maneger import load_data, upload_data

YES_LIST = ["Y", "Yes", "y", "yes"]
STYLING_LENGTH = 50


def print_all_food_item(last=True):
    all_food_item = Product.get_all_products()
    for i in all_food_item:
        print(i)
    if last:
        home_option_num = len(all_food_item) + 1
        print(f"{home_option_num}. Go to home page")
        return home_option_num


def order_food(cur_user: User):
    print()
    print("Order food".center(STYLING_LENGTH, "-"))
    home_option_num = print_all_food_item()
    while True:
        inp_ = input("enter food ids(separated by space): ").split()
        if all(map(lambda x: x.isdigit(), inp_)):
            food_ids = list(map(int, inp_))
            break
        else:
            print("Please Enter numeric values.")

    if home_option_num in food_ids:
        return False

    out_of_stoke_items = []
    invalid_food_ids = []
    valid_food_items = []
    for food_id in food_ids:
        food_item = Product.get_product(food_id)
        if food_item:
            if food_item.order_product():
                valid_food_items.append(food_item)
            else:
                out_of_stoke_items.append(food_item.name)
        else:
            invalid_food_ids.append(str(food_id))

    print("{:<5} {:<20} {:<10}".format('id', 'food name', 'price'))
    for item in valid_food_items:
        print("{:<5} {:<20} {:<10}".format(item.food_id, item.name, item.price))

    if out_of_stoke_items:
        if len(out_of_stoke_items) == 1:
            print(f"{out_of_stoke_items[0]} is out of stoke")
        else:
            print(f"{', '.join(out_of_stoke_items)} are out of stoke")
    if invalid_food_ids:
        if len(invalid_food_ids) == 1:
            print(f"food id {invalid_food_ids[0]} is not valid")
        else:
            print(f"food ids {', '.join(invalid_food_ids)} are not valid")

    flag = input(f"Enter {' or '.join(YES_LIST[:2])} if you want to order valid food items?: ")
    if flag in YES_LIST:
        for item in valid_food_items:
            cur_user.ordered_food(item.name)
            print(f"{item} is ordered.")
        return True
    else:
        print("Order cancelled.")
        return False


def add_food_item():
    print()
    print("Add food item".center(STYLING_LENGTH, "-"))
    food_data = {"name": None, "quantity": None, "price": None, "discount": None, "stock": None}
    for i in ["name", "quantity"]:
        while True:
            inp_ = input(f"Enter {i} of food: ")
            if len(inp_) > 3:
                food_data[i] = inp_
                break
            else:
                print(f"for {i} input should be more then 3 characters")
    for i in ["price", "discount", "stock"]:
        while True:
            inp_ = input(f"Enter {i} of food (Please enter numeric value): ")
            if inp_.isdigit():
                food_data[i] = int(inp_)
                break
            else:
                print(f"for {i} please enter numeric value")
    return Product(**food_data)


def edit_food_item():
    print()
    print("Edit food item".center(STYLING_LENGTH, "-"))
    home_option_num = print_all_food_item()
    while True:
        food_id = input("Enter id of product to edit: ")
        if food_id.isdigit():
            food_id = int(food_id)
            break
        else:
            print("Please Enter numeric values.")
    if food_id == home_option_num:
        return
    food_item = Product.get_product(food_id)
    if food_item:
        food_data = {"name": None, "quantity": None, "price": None, "discount": None, "stock": None}
        previous_food_data = food_item.get_product_data()
        print("Left empty for keeping the original value.")
        for i in ["name", "quantity"]:
            food_data[i] = input(f"Enter {i} of food (previous {i} is {previous_food_data[i]}): ")
        for i in ["price", "discount", "stock"]:
            while True:
                inp_ = input(f"Enter {i} of food (previous {i} is {previous_food_data[i]}): ")
                if not inp_:
                    break
                elif inp_.isdigit():
                    food_data[i] = int(inp_)
                    break
                else:
                    print(f"for {i} please enter numeric value.")
        food_item.edit_product(**food_data)
    else:
        print("index not available")


def remove_food_item():
    print()
    print("Remove food item".center(STYLING_LENGTH, "-"))
    home_option_num = print_all_food_item()
    while True:
        food_id = input("Enter Id of food to remove: ")
        if food_id.isdigit():
            food_id = int(food_id)
            break
        else:
            print("Please Enter numeric values.")
    if food_id == home_option_num:
        return
    food_item = Product.get_product(food_id)
    if food_item:
        print(f"Enter {', '.join(YES_LIST[:2])} if you agree.")
        inp_ = input(f"Do you want to remove '{food_item.name}' from list of food:")
        if inp_ in YES_LIST:
            food_item.remove_product()
    else:
        print("index not available")


def user_registration():
    print()
    print("User registration".center(STYLING_LENGTH, "-"))
    user_data = {"name": None, "password": None, "phone_no": None, "email": None, "address": None}
    for i in user_data.keys():
        if i == "name":
            while True:
                name = input(f"Enter your {i}: ")
                if User.get_user(name):
                    print(f"{name} is not available, please try different name")
                else:
                    user_data[i] = name
                    break
        elif i == "password":
            while True:
                password1 = input("Enter your password: ")
                password2 = input("Enter your password again: ")
                if password1 == password2:
                    user_data[i] = password1
                    print("Password set.")
                    break
                else:
                    print("Entered Passwords are not same Please Try again.")
        elif i == "phone_no":
            while True:
                phone_no = input(f"Enter your {i}: ")
                if phone_no.isdigit():
                    user_data[i] = int(phone_no)
                    break
                else:
                    print("Please enter numeric value")
        else:
            user_data[i] = input(f"Enter your {i}: ")
    print(f"Welcome {user_data['name']}")
    return User(**user_data)


def user_login():
    print()
    print("User login".center(STYLING_LENGTH, "-"))
    name = input("Enter your name: ")
    cur_user = User.get_user(name)
    if cur_user:
        chances = 3
        while True:
            password = input("Enter your password: ")
            verified = cur_user.verify_password(password)
            if verified:
                return cur_user
            else:
                print(f"Incorrect password, you have {chances} chances left")
                if chances == 0:
                    print("redirecting to Login page.")
                    return
                else:
                    chances -= 1
    else:
        print("user dus not exits.")


def update_user_profile(cur_user: User):
    print()
    print("Update user profile".center(STYLING_LENGTH, "-"))
    user_data = {"name": None, "phone_no": None, "email": None, "address": None}
    original_user_data = cur_user.get_user_data()
    print("Left empty for keeping the original value.")
    for i in user_data.keys():
        if i == "name":
            while True:
                name = input(f"Your current {i} is {original_user_data[i]}, enter new {i}: ")
                if not name:
                    break
                elif User.get_user(name):
                    print(f"{name} is not available, please try different name")
                else:
                    user_data[i] = name
                    break
        elif i == "phone_no":
            while True:
                phone_no = input(f"Your current {i} is {original_user_data[i]}, enter new {i}: ")
                if not phone_no:
                    break
                elif phone_no.isdigit():
                    user_data[i] = int(phone_no)
                    break
                else:
                    print("Please enter numeric value")
        else:
            user_data[i] = input(f"Your current {i} is {original_user_data[i]}, enter new {i}: ")

    cur_user.update_profile(**user_data)
    print("your profile has been updated.")
    return cur_user


def change_user_password(cur_user: User):
    print()
    print("Change user password".center(STYLING_LENGTH, "-"))
    while True:
        password1 = input("Enter your password: ")
        password2 = input("Enter your password again: ")
        if password1 == password2:
            cur_user.change_password(password1)
            print("New password is set.")
            break
        else:
            print("Entered Passwords are not same Please Try again.")


def create_loaded_data():
    data = load_data()
    if not data:
        Product("Tandoori Chicken", "4 pieces", 240, 5)
        Product("Vegan Burger", "1 pieces", 320, 5)
        Product("Truffle Cake", "500gm", 900, 5)

        admin = User("admin", "admins_secret", 1234567891, "admin@admin.com", "admin ki duniya")
        admin.make_admin()
        del admin
        return

    users_data, products_data = data["user"], data["product"]
    for user_data in users_data:
        user_data["loading_data"] = True
        User(**user_data)
    admin = User.get_user("admin")
    admin.make_admin()
    for product_data in products_data:
        Product(**product_data)


# main Code
print("Welcome to Food Ordering app".center(STYLING_LENGTH, "-"))
create_loaded_data()
while True:
    while True:
        print()
        print("Login Page".center(STYLING_LENGTH, "-"))
        print("1. Log in to your account\n2. Create a new account\n3. Close the app")
        inp = input(": ")
        if inp.isdigit():
            inp = int(inp)
            if inp == 1:
                user = user_login()
                if user:
                    break
            elif inp == 2:
                user = user_registration()
                break
            elif inp == 3:
                print("closing the app")
                upload_data(User.get_all_users_data(), Product.get_all_products_data())
                exit()
            else:
                print("invalid!!! Please Enter valid input")
            input("Enter to get redirected to Login page")
        else:
            print("invalid!!! Please Enter numeric value")
    print(f"Logged in as {user.name}.")
    input("Enter to get redirected to home page")

    user_is_logged_in = True
    while user_is_logged_in:
        print()
        print("Home Page".center(STYLING_LENGTH, "-"))
        print("1. Give an order\n2. Edit your profile info\n3. Show order history\n"
              "4. change your Password\n5. log out")
        if user.is_admin:
            print("6. Add food item\n7. Edit food items\n8. Remove food items")
        inp = input(": ")
        if inp.isdigit():
            inp = int(inp)
            if inp == 1:
                order_food(user)
            elif inp == 2:
                update_user_profile(user)
            elif inp == 3:
                user.print_ordered_history()
            elif inp == 4:
                change_user_password(user)
            elif inp == 5:
                user_is_logged_in = False
                user = None
            elif user.is_admin:
                if inp == 6:
                    add_food_item()
                elif inp == 7:
                    edit_food_item()
                elif inp == 8:
                    remove_food_item()
                else:
                    print("invalid!!! Please Enter valid input")
            else:
                print("invalid!!! Please Enter valid input")
        else:
            print("invalid!!! Please Enter numeric value")
        input("Enter to get redirected to home page")
