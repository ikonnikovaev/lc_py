import math
N_MONTHS = 12


def find_loan_principal(a, n, i):
    tmp1 = i * ((1 + i) ** n)
    tmp2 = (1 + i) ** n - 1
    p = (a / (tmp1/tmp2))
    return math.floor(p)

def find_monthly_payment(p, n, i):
    tmp1 = i * ((1 + i) ** n)
    tmp2 = (1 + i) ** n - 1
    a = p * (tmp1/tmp2)
    return math.ceil(a)


def find_n_payments(p, a, i):
    tmp = a / (a - i * p)
    n = math.log(tmp, 1 + i)
    return math.ceil(n)



def ask():
    p, a, n, i = None, None, None, None
    print('What do you want to calculate?')
    print('type "n" for number of monthly payments,')
    print('type "a" for annuity monthly payment amount,')
    print('type "p" for the loan_principal:')
    ans = input().strip()
    if ans != 'p':
        print('Enter the loan principal:')
        p = int(input())
    if ans != 'a':
        print('Enter the annuity payment:')
        a = float(input())
    if ans != 'n':
        print('Enter the number of periods:')
        n = int(input())
    print('Enter the loan interest:')
    i = float(input()) / 1200
    if ans == 'p':
        p = find_loan_principal(a, n, i)
        print(f'Your loan principal = {p}!')
    elif ans == 'a':
        a = find_monthly_payment(p, n, i)
        print(f'Your monthly payment = {a}!')
    elif ans == 'n':
        n = find_n_payments(p, a, i)
        y = n // N_MONTHS
        m = n % N_MONTHS
        output = f'It will take '
        if y > 0:
            output += f'{y} years '
            if m > 0:
                output += f'and '
        if m > 0:
            output += f'{m} months '
        output += ' to repay this loan!'
        print(output)


ask()
