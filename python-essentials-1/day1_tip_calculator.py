bill = input("Please state how much your bill is: £")
tip_amount = input("Please choose one of the tip options: 10%, 15% or 20%: ")
bill = int(bill)
tip_amount = int(tip_amount)
tip_10 = bill // 10
tip_15 = bill // 15
tip_20 = bill // 20

if tip_amount == 10:
    print("Total tip is: £",tip_10)
elif tip_amount == 15:
    print("Total tip is: £",tip_15)
elif tip_amount == 20:
    print("Total tip is: £",tip_20)
