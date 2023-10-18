capital = int(input("How much do you want to borrow? "))
borrowdays = int(input("How many days do you want to borrow? "));
interest = 0.20;
totalinterest = interest * capital * borrowdays;
print("Your interest will be " + format(totalinterest));
payout = totalinterest + capital;
print("Your totalpayout will be " + format(payout));
proceed = input("Do you still want to proceed? ")
if proceed == "NO":
    print("Thank you for your enquiries");
else:
    installment = int(input("How many installemts do you want to pay back? Please note, you are allowed to pay max of 2 times. "));
firstinstallment = payout / 2;
print("Your first installment will be " + format(firstinstallment));
agree = input("I agree to the terms"),
if agree == "NO":
    print("Thank you for your time");
else:
    secondinstallment = payout / 2;
print("Your second installment will be " + format(secondinstallment));
agree = input("I agree to the terms"),
if agree == "NO":
    print("Thank you for your time");
print("Thank you for doing business with Mary loan Bank");