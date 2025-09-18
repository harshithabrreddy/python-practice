Guest_list=[]
while(True):
    print("---Guest list Menu---")
    print("1.To view the Guest list")
    print("2.To Add the Guest")
    print("3.To check the particular guest is attending the party or not")
    print("4.Remove a guest from guest list")
    print("5.To print the finalized Guest list and exit")
    choice=int(input("Enter your choice:"))
    if(choice==1):
        if(len(Guest_list==0)):
            print("Guest list is Empty")
        else:
            print("Guest list:")
            print("Guest_list,\n")
    elif(choice==2):
        Guest=input("Enter the Guest Name:")
        Guest_list.append(Guest)
        print(f"{Guest} is added to the guest list...!")
        print()
    elif(choice==3):
        Guest=input("Enter the guest name to check the status")
        if Guest in Guest_list:
            print(f"{Guest} is Attending the party....!")
        else:
            print(f"{Guest} is not Attending the party")
    elif(choice==4):
        Guest=input("Enter the name of the Guest who's not Attending  the party")
        if Guest in Guest_list:
            Guest_list.remove(Guest)
            print(f"{Guest}'s name is removed from the guest list")
            print()
    elif(choice==5):
        print("finished Guest list:")
        print()
        print(Guest_list)
    break