# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input("Please provide the $ amount balance for your savings account: "))
    savings_interest= float(input("Please enter the interest rate for your account (eg. 7.5% should be entered as 7.5): "))
    savings_maturity = int(input("Please entere the number of months youre planning to save for?: "))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)
    

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"For the period of {savings_maturity}, your earned interest is: {interest_earned}, and your new updated balance is: {updated_savings_balance}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input("Please provide the $ amount balance for you CD account: "))
    cd_interest= float(input("Please enter the interest rate for your CD account (eg. 7.5% should be entered as 7.5): "))
    cd_maturity = int(input("Please entere the number of months youre planning to save for?: "))


    # # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"For the period of {cd_maturity}, your earned interest is: {interest_earned}, and your new updated balance is: {updated_cd_balance}")

if __name__ == "__main__":
    # Call the main function.
    main()