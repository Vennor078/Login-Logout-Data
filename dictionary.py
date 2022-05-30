import datetime
from re import X

WalletAdressLogin = ''

playtime = {
    "treasure": 0,
    "TreasureTime": datetime.datetime.now(),
}

user = {

    "Wallet":'',
    "Pet": 'Nova',
    "Exp": 0,
    "Ablity": 'None',
    "AblityMulitplier": '1x',
    "Coins": 0,
}

users = []

def Layout():

    loop = True
    while loop:

        respond = input("")
        if respond == "treasure":

            if playtime['treasure'] == 1:
                
                curretTime = datetime.datetime.now()
                diff = curretTime - playtime['TreasureTime']

                if(int(diff.seconds) >= 1):
                    playtime['treasure'] = 0

                else:

                    print(
                        " ",
                        "You need to wait " + str(1- int(diff.seconds)) + " Seconds before you can look for treasure again!",
                        " ",
                    )
                
            if playtime['treasure'] == 0:
                import random

                RandomCoins = random.randint(1,5)
                users[WalletAdressLogin]['Coins'] += RandomCoins

                playtime['treasure'] = playtime['treasure'] + 1
                playtime['TreasureTime'] = 0
                playtime['TreasureTime'] = datetime.datetime.now()

                print("You found " + str(RandomCoins) + " Coins"  + "\n")

        if respond == "logout":
            print("You are now logout!"  + "\n")
            Account()

        if respond == "Users":
            for i in users:
                print(i)


def Account():
    global WalletAdressLogin

    loop = True
    while loop:

        walletAdress = input("Enter Your BNB WalletAdress ")
        for i in range(len(users)):
            if str(walletAdress) == users[i]['Wallet']:
               print("Loading your account.."  + "\n")
               print(
                   "Wallet Address: " + users[i]['Wallet'] + "\n",
                   "\n",
                   "Pet: " + users[i]['Pet'] + "\n",
                   "Exp: " + str(users[i]['Exp']) + "\n",
                   "Ablity: " + users[i]['Ablity'] + "\n",
                   "AblityMulitplier: " + users[i]['AblityMulitplier'] + "\n",
                   "Coins: " + str(users[i]['Coins']) + "\n",
               )
               
               WalletAdressLogin = i

               Layout()
               break

        else:

            newUser = user.copy()
            newUser['Wallet'] = walletAdress

            users.append(newUser)

            print("Your account have be create.." + "\n")
            WalletAdressLogin = len(users) - 1
            Layout()

Account()

