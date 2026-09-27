import random

def spin_row():
    symbols = ['🍒', '🌸', '🍉', '⭐', '💰']

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("\n*************")
    print(" | ".join(row))
    print("*************")

def payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🌸':
            return bet * 5
        elif row[0] == '🍉':
            return bet * 7
        elif row[0] == '⭐':
            return bet * 10
        elif row[0] == '💰':
            return bet * 20

    return 0

def play_again():
    while True:
        choice = input("DO YOU WANT TO PLAY AGAIN? (Y/N): ").lower()

        if choice == "y":
            return True
        elif choice == "n":
            print("THANK YOU FOR PLAYING!")
            return False
        else:
            print("INVALID INPUT, PLEASE TRY EITHER Y OR N")


def main():
    balance = 100

    print("***************************")
    print("WELCOME TO THE SLOT MACHINE")
    print("SYMBOLS: 🍒 🌸 🍉 ⭐ 💰")
    print("***************************")

    while balance > 0:

        print(f"\nCURRENT BALANCE: ${balance}")

        try:
            bet = int(input("PLACE YOUR BET AMOUNT: "))
            if bet > balance:
                print("\nINSUFFICIENT BALANCE")
                continue
            elif bet <= 0:
                print("\nBET SHOULD BE GREATER THAN 0")
                continue
        except ValueError:
            print("\nINVALID INPUT")
            continue

        balance -= bet

        row = spin_row()

        print("\nSPINNING......")
        print_row(row)

        pay = payout(row, bet)
        if pay > 0:
            print(f"\nYOU HAVE WON ${pay}")
        else:
            print("\nYOU LOST")

        balance += pay
        if not play_again():
            break

    if balance <= 0:
        print("\nYOU RAN OUT OF MONEY!")

    print(f"FINAL BALANCE: ${balance}")
