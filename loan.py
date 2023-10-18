capital = 500
interest = 200
totalinterest = 500 + "interest" 
print(totalinterest);
borrowdays = 30
loandays = "totalinterest * 30"

interest=$((100*$days))
echo "your interest will be $interest"
echo "how many times do you want to pay back the capital?"
read times
payback=$(($capital+$interest))
echo "your payback loan is $payback"
echo "you have chosen to pay back in $times installments."
installments=$(($payback/$times))
echo "your total payback is $installments per installment."
echo "We appreciate your business with Mary microfinance Bank."


#print("Welcome to Mary's Python Loan");
#yes = input("Do you need a loan? ");
#print("I need a loan " + yes)
#borrowdays = input("How many days do you want to borrow? ");
#print("I need a loan for " + borrowdays + " days.")
#print("Installments are allowed just twice");
#installment = input("How many installment do you want to pay back? ");
#print("I will pay the installment " + installment);
conclusion = "In conclusion, You need a loan of usd {0}, an interest of {3}";
print(conclusion.format(capital, + interest, + borrowdays));