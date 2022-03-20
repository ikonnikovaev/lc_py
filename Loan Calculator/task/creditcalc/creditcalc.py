import math
import argparse

N_MONTHS = 12
HUNDRED = 100

def find_loan_principal(annuity_payment, n_periods, interest):
    tmp1 = interest * ((1 + interest) ** n_periods)
    tmp2 = (1 + interest) ** n_periods - 1
    principal = (annuity_payment / (tmp1 / tmp2))
    return math.floor(principal)

def find_monthly_payment(principal, n_periods, interest):
    tmp1 = interest * ((1 + interest) ** n_periods)
    tmp2 = (1 + interest) ** n_periods - 1
    annuity_payment = principal * (tmp1 / tmp2)
    return math.ceil(annuity_payment)

def find_n_payments(principal, annuity_payment, interest):
    tmp = annuity_payment / (annuity_payment - interest * principal)
    n_periods = math.log(tmp, 1 + interest)
    return math.ceil(n_periods)

def find_overpayment(principal, annuity_payment, n_periods):
    return annuity_payment * n_periods - principal

def print_n_payments(n_periods):
    y = n_periods // N_MONTHS
    m = n_periods % N_MONTHS
    output = f'It will take '
    if y > 0:
        output += f'{y} years '
        if m > 0:
            output += f'and '
    if m > 0:
        output += f'{m} months '
    output += ' to repay this loan!'
    print(output)

def find_diff_payments(principal, n_periods, interest):
    diff_payments = [principal / n_periods] * n_periods
    for m in range(0, n_periods):
        tmp = principal - (principal * m) / n_periods
        diff_payments[m] += interest * tmp
    return [math.ceil(d) for d in diff_payments]

def print_diff_payments(diff_payments):
    n_periods = len(diff_payments)
    for m in range(n_periods):
        print(f"Month {m + 1}: payment is {diff_payments[m]}")

def message_error():
    print("Incorrect parameters")

def ask():
    principal, annuity_payment, n_periods, interest = None, None, None, None
    print('What do you want to calculate?')
    print('type "n" for number of monthly payments,')
    print('type "a" for annuity monthly payment amount,')
    print('type "p" for the loan_principal:')
    ans = input().strip()
    if ans != 'p':
        print('Enter the loan principal:')
        principal = int(input())
    if ans != 'a':
        print('Enter the annuity payment:')
        annuity_payment = float(input())
    if ans != 'n':
        print('Enter the number of periods:')
        n_periods = int(input())
    print('Enter the loan interest:')
    interest = float(input()) / (N_MONTHS * HUNDRED)
    if ans == 'p':
        principal = find_loan_principal(annuity_payment, n_periods, interest)
        print(f'Your loan principal = {principal}!')
    elif ans == 'a':
        annuity_payment = find_monthly_payment(principal, n_periods, interest)
        print(f'Your monthly payment = {annuity_payment}!')
    elif ans == 'n':
        n_periods = find_n_payments(principal, annuity_payment, interest)
        print_n_payments(n_periods)


# ask()
parser = argparse.ArgumentParser()
parser.add_argument("--type")  # choices=["annuity", "diff"])
parser.add_argument("--principal")
parser.add_argument("--interest")
parser.add_argument("--periods")
parser.add_argument("--payment")

args = parser.parse_args()

if not args.type or not (args.type in ["annuity", "diff"]):
    message_error()

if args.type == "diff":
    if args.payment:
        message_error()
    elif not (args.principal and args.periods and args.interest):
        message_error()
    else:
        principal = int(args.principal)
        n_periods = int(args.periods)
        interest = float(args.interest) / (N_MONTHS * HUNDRED)
        diff_payments = find_diff_payments(principal, n_periods, interest)
        print_diff_payments(diff_payments)
        overpayment = sum(diff_payments) - principal
        print(f"Overpayment = {overpayment}")
elif args.type == "annuity":
    list_args = [args.principal, args.interest, args.periods, args.payment]
    n_nones = 0
    for arg in list_args:
        if arg is None:
            n_nones += 1
    if n_nones != 1 or not args.interest:
        message_error()
    elif not args.principal:
        interest = float(args.interest) / (N_MONTHS * HUNDRED)
        n_periods = int(args.periods)
        annuity_payment = float(args.payment)
        principal = find_loan_principal(annuity_payment, n_periods, interest)
        print(f'Your loan principal = {principal}!')
        print(f"Overpayment ={find_overpayment(principal, annuity_payment, n_periods)}")
    elif not args.periods:
        principal = int(args.principal)
        interest = float(args.interest) / (N_MONTHS * HUNDRED)
        annuity_payment = float(args.payment)
        n_periods = find_n_payments(principal, annuity_payment, interest)
        print_n_payments(n_periods)
        print(f"Overpayment ={find_overpayment(principal, annuity_payment, n_periods)}")
    elif not args.payment:
        principal = int(args.principal)
        interest = float(args.interest) / (N_MONTHS * HUNDRED)
        n_periods = int(args.periods)
        annuity_payment = find_monthly_payment(principal, n_periods, interest)
        print(f'Your monthly payment = {annuity_payment}!')
        print(f"Overpayment ={find_overpayment(principal, annuity_payment, n_periods)}")










