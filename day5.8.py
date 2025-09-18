#cafe charges  to calculate  the total bill after adding a 5% service charge
coffee_price=int(input("Enter price of one coffee:"))
snack_price=int(input("Enter price of one snack:"))
coffees_ordered=int(input("Enter number of coffees  ordered:"))
snacks_ordered=int(input("Enter number of snacks ordered:"))
total_cost=(coffee_price*coffees_ordered)+(snack_price*snacks_ordered)
service_charge=total_cost*0.05
total_bill=total_cost+service_charge
print("Total bill including 5% service charge:",total_bill)



