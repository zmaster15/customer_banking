# customer_banking
Homework &amp; Project Assignments for Artificial Intelligence Bootcamp | module 3 challenge

**Customer Banking Application**

## Table of Contents
* [Introduction](#introduction)
* [Installation Requirements](#requirements)
* [Usage](#usage)
* [License](#license)
* [Acknowledgement / Contributing](#acknowledgementcontributing)

## Introduction
This project is the second coding module challenge that we had to complete as part of the Denver University AI Bootcamp coursework. 

The initial code provided for the challenge had class defined for Accounts, and then two functions that calculates savings account and CD account balances at maturity. The main function, 'customer_banking' calls on these functions to then help the user understand their balances at maturity based on input arguements provided. 

The user is requested to provide the following three arguements to calculate balance at maturity for both the Savings & CD: $ Balance, Interest, and Time (months). 

The user must enter these arguements as numbers:
-  float > Balance and Interest
-  integer > time (months)


\*NOTE: There is no validation for user inputs for the input arguements: Balance, Interest, Time. If user enters an invalid character (ie. not an integer/ float) for the input arguements, the code will error out and inform them of the same. 

## Installation Requirements
*Requirements*: You must run Python 3.12.7 to execute the code as the code uses match case sytax that is older versions of python will not recognize.

## Usage
Anyone that would like to understand how interest would incur on their exisiting balance across a savings account or a closed deposit account can utilize this code to calculate their balances at the end of the maturity. This will allow the user to guage what account type is best to reach their financial goal as each account type is uniquely calculated. 

## License
I've included the MIT License to encourage collaboration and use by the community.

## Acknowledgement / Contributing
Thank to the guidance of the Denver University AI Bootcamp Teachers Assistant's and their hints via comments that helped me complete this assignment. Without this I would've been completely lost. 

While a section of this code was written by the Denver University AI Bootcamp Teachers Assistant, it has been modified / completed by me. 

