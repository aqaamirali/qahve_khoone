MENU = {
    
    
    "esperesso":{
        "ingredient":{
        "water":50,
        "coffee":18,
        },
        
        
        "cost":1.5,
    },
    
    
    "latte":{
        "ingredient":{
            "water":200,
            "milk":150,
            "coffee":24
        },
        
        
        "cost":2.5
        
    },
    
    
    "coppuccino":{
        "ingredient":{
                    
        "water":200,
        "milk":150,
        "coffee":24
        },
        
        
        "cost":3.0
    }
}

resources = {
    "water":300,
    "milk":200,
    "coffee":100
}


req_water_co = MENU["coppuccino"]["ingredient"]["water"]
req_milk_co = MENU["coppuccino"]["ingredient"]["milk"]
req_coffee_co = MENU["coppuccino"]["ingredient"]["coffee"]

req_water_la = MENU["latte"]["ingredient"]["water"]
req_milk_la = MENU["latte"]["ingredient"]["milk"]
req_coffee_la = MENU["latte"]["ingredient"]["coffee"]

req_water_es = MENU["esperesso"]["ingredient"]["water"]
req_coffee_es = MENU["esperesso"]["ingredient"]["coffee"]


req_mony_co = MENU["coppuccino"]["cost"]
req_mony_es = MENU["esperesso"]["cost"]
req_mony_la = MENU["latte"]["cost"]


def check_report_or_off(order, money):
    '''this func takes an string(order) and a float number(money) and will print the statue of resourses or shutdown the machin'''
    if order == 'off':
        exit()
    
    elif order == 'report':
        for item in resources:
            if item == 'water':
                print(f"{item}: {resources[item]}ml")
            elif item == 'coffee':
                print(f"{item}: {resources[item]}gr")
            elif item == 'milk':
                print(f"{item}: {resources[item]}ml")
        print(f"money:${money}")


def check_resuorses():
    '''this func checks if resuorses are enough'''
    
    if resources["water"] - req_water_co < 0:
        print("Sorry, there is not enugh water.")
        return False
    elif  resources["water"] - req_water_es < 0:
        print("Sorry, there is not enugh water.")
        return False
    elif  resources["water"] - req_water_la < 0:
        print("Sorry, there is not enugh water.")
        return False
    
    elif resources["milk"] - req_milk_co < 0:
        print("Sorry, there is not enugh milk.")
        return False
    elif resources["milk"] - req_milk_la < 0:
        print("Sorry, there is not enugh milk.")
        return False
    elif resources["coffee"] - req_coffee_es < 0:
        print("Sorry, there is not enugh coffee.")
        return False
    elif (resources["coffee"] - req_coffee_co) < 0:
        print("Sorry, there is not enugh coffee.")
        return False    
    elif (resources["coffee"] - req_coffee_la) < 0:
        print("Sorry, there is not enugh coffee.")
        return False


def cal():
    '''this func calculate the total inserted coins and return the total number'''
    quarter_num = float(input("How many quarters?: ")) * 0.25 
    
    dimes_num = float(input("How many dimes?: ")) * 0.1                
    
    nickles_num = float(input("How many nickles?: ")) * 0.05                
    
    pennies_num = float(input("How many pennies?: ")) * 0.01
    
    total_num = pennies_num + nickles_num + dimes_num + quarter_num
    
    return total_num


money = 0


def main(money):
    '''this is main func of program'''
    while True:
        
        order = input("what would you like? (coppuccino/esperesso/latte): ").lower()
        
        if order == 'report':
            check_report_or_off(order, money)
        
        elif order == 'off':
            check_report_or_off(order, money)
        
        else:       
           if check_resuorses() != False:
                    
                inserted_money = cal()        
                
                if order == 'coppuccino':
                    extra_mony = inserted_money - req_mony_co
                    
                    if inserted_money < req_mony_co:
                        print("Sorry, that's not enough money. money refunded.")
                    else :
                        money += req_mony_co
                        
                        resources["water"] = resources["water"] - req_water_co
                        
                        resources["milk"] = resources["milk"] - req_milk_co
                        
                        resources["coffee"] = resources["coffee"] - req_coffee_co
                        
                        print(f"Here is ${round(extra_mony, 2)} in change")        
                        
                        print(f"here is your {order},,,Enjoy!")

                
                elif order == 'latte':
                    extra_mony = inserted_money - req_mony_la
                    
                    if inserted_money < req_mony_la:
                        print("Sorry, that's not enough money. money refunded.")
                    else:
                        money += req_mony_la
                        
                        resources["water"] = resources["water"] - req_water_la
                        
                        resources["milk"] = resources["milk"] - req_milk_la
                        
                        resources["coffee"] = resources["coffee"] - req_coffee_la
                        
                        print(f"Here is ${extra_mony} in change")        
                        
                        print(f"here is your {order},,,Enjoy!")
                
                
                elif order == 'esperesso':
                    extra_mony = inserted_money - req_mony_es
                    
                    if inserted_money < req_mony_es:
                        print("Sorry, that's not enough money. money refunded.")
                    else:
                        money += req_mony_es
                        
                        resources["water"] = resources["water"] - req_water_es
                        
                        resources["coffee"] = resources["coffee"] - req_coffee_es
                        
                        print(f"Here is ${extra_mony} in change")        
                        
                        print(f"here is your {order},,,Enjoy!")

main(money)