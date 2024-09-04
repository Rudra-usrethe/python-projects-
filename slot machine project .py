import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS =3

symbol_count = {"A":2,"B":4,"C":6,"D":8}
symbol_value = {"A":5,"B":4,"C":3,"D":2}

def check_winnings(columns , lines,  bet , values):
    winnings = 0
    winnings_lines =[]
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
            else : 
                winnings += values[symbol]* bet
                winnings_lines.append(lines + 1)
    return winnings , winnings_lines


def get_slot_machine_spin(rows , cols, symbols) :
    all_symbols =[]
    for symbol, symbol_count in symbols.items():
         for _ in range(symbol_count):
             all_symbols.append(symbol)
    columns = []
    for col in range(cols):
        column = []
        current_symbols =  all_symbols[:]
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns  

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns) :
            if i != len(columns) -1:
                print(column[row], end =" | ") 
            else:
                print(column[row], end="")  
        print()             


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount >0:
                break
            else:
                print("Please enter a amount greater than 0..")
        else:
            print("Please enter a number : ")
    return amount

def get_number_of_line():
    while True:
        lines= input("Enter the number of lines to bet on (1-" + str(MAX_LINES)+ ")?")
        if lines.isdigit():
            lines= int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of line.")
        else:
            print("Please enter a number : ")
    return lines

def get_bet():
    while True:
        amount= input("How much would you like bet on each line? := $")
        if amount.isdigit():
            amount= int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f'Must amout be between ${MIN_BET} - ${MAX_BET}.')
        else:
            print("Please enter a number : ")
    return amount

def spin(balance):
    lines = get_number_of_line()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f'you are out of balance , your balance is : ${balance}')
        else :
            break    
    print(f'You are betting  ${bet} on ${lines} lines. Total bet in equal to :${total_bet} ')
    # print(balance, lines)
    slots = get_slot_machine_spin(ROWS ,COLS, symbol_count )
    print_slot_machine(slots)
    winnings ,winning_line =  check_winnings(slots,  lines , bet , symbol_value)
    print(f' You WIn ${winnings}.')
    print(f'You WOn on lines  ', *winning_line)
    return winnings - total_bet


def main():
    balance =  deposit()
    while True:
        print(f'current balance is ${balance}')
        answer= input("press enter to play (q to quit). otherwise type cash :  ")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}") 


main()

