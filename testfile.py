print("Enter the number of friends joining (including you):")
try:
    count = int(input())
except ValueError:
    print("No one is joining for the party")
else:
    if count <= 0:
        print("No one is joining for the party")
    else:
        print("Enter the name of every friend (including you), each on a new line:")
        friends = {}
        for _ in range(count):
            name = input()
            friends[name] = 0
        print("Enter the total bill value:")
        try:
            bill = int(input())
        except ValueError:
            bill = 0
        """
        per_person = bill / count
        for friend in friends:
            friends[friend] = round(per_person, 2)
        print(friends)
        """
        print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
        choice = input()
        if choice == "Yes":
            import random
            lucky_one = random.choice(list(friends.keys()))
            print(f"{lucky_one} is the lucky one!")
            per_person = bill / (count - 1)
            for friend in friends:
                if friend == lucky_one:
                    friends[friend] = 0
                else:
                    friends[friend] = round(per_person, 2)
            print(friends)
        else:
            print("No one is going to be lucky")
            per_person = bill / count
            for friend in friends:
                friends[friend] = round(per_person, 2)
            print(friends)
