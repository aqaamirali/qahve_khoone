x = True
people = []
money = []
while x:
    auction = {
        "people": people,
        "bid": money,
    }
    name = input("what is your name: ")
    people.append(name)
    bid = int(input("what is your bid:$"))
    money.append(bid)
    go_on = input("is there anyone else: 'yes' or 'no'")
    if go_on == 'n':
        x = False
    elif go_on == 'y':
        x = True
    else:
        print("something went wrong")
        go_on = input("is there anyone else: 'yes' or 'no'")
        if go_on == 'n':
            x = False
        elif go_on == 'y':
            x = True
    print(auction)

MAX = 0

for (key, value) in auction.items():
    for number in auction["bid"]:
        if int(number) > MAX:
            MAX = int(number)
            index = auction["bid"].index(number)

winner = auction["people"][index]

print(f"the winner is {winner} with a bid ${MAX}")
