import time

Vehicle_Number = ['XXXX-XX-XXXX']
Vehicle_Type = ['Bike']
vehicle_Name = ['Intruder']
Owner_Name = ['Unknown']
Date = ['22-22-3636']
Time = ['22:22:22']
bikes = 100
cars = 250
bicycles = 78

def main():
    global bikes, cars, bicycles
    try:
        while True:
            print("----------------------------------------------------------------------------------------")
            print("\t\tParking Management System")
            print("----------------------------------------------------------------------------------------")
            print("1. Vehicle Entry")
            print("2. Remove Entry")
            print("3. View Parked Vehicles")
            print("4. View Left Parking Space")
            print("5. Amount Details")
            print("6. Bill")
            print("7. Close Programme")
            print("+---------------------------------------------+")
            ch = int(input("\tSelect option: "))
            
            if ch == 1:
                add_vehicle()
                
            elif ch == 2:
                remove_entry()

            elif ch == 3:
                view_parked_vehicles()

            elif ch == 4:
                view_left_parking_space()

            elif ch == 5:
                view_parking_rate()

            elif ch == 6:
                generate_bill()

            elif ch == 7:
                print("..............................................................Thank you for using our service...........................................................................")
                print("                                     **********(: Bye Bye :)**********")
                break

    except Exception as e:
        print(f"An error occurred: {e}")
        main()

def add_vehicle():
    no = True
    while no:
        Vno = input("\tEnter vehicle number (XXXX-XX-XXXX) - ").upper()
        if Vno == "  ":
            print("###### Enter Vehicle No. ######")
        elif Vno in Vehicle_Number:
            print("###### Vehicle Number Already Exists")
        elif len(Vno) == 5:
            no = not True
            Vehicle_Number.append(Vno)
        else:
            print("###### Enter Valid Vehicle Number ######")

    typee = True
    while typee:
        Vtype = input("\tEnter vehicle type (Bicycle=A/Bike=B/Car=C): ").lower()
        if Vtype == "":
            print("###### Enter Vehicle Type ######")
        elif Vtype == "a":
            Vehicle_Type.append("Bicycle")
            bicycles += 1
            typee = not True
        elif Vtype == "b":
            Vehicle_Type.append("Bike")
            bikes += 1
            typee = not True
        elif Vtype == "c":
            Vehicle_Type.append("Car")
            cars += 1
            typee = not True
        else:
            print("###### Rough Input ######")

    name = True
    while name:
        vname = input("\tEnter vehicle name :")
        if vname == "":
            print("########Please Enter Vehicle Name ########")
        else:
            vehicle_Name.append(vname)
            name = not True

d = True
while d:
    date = input("\tEnter Date (DD-MM-YYYY) - ")
    if date == "":
        print("###### Enter Date ######")
    elif len(date) != 10:
            print("###### Enter Valid Date ######")
    else:
            Date.append(date)
            d = not True

    t = True
    while t:
        entry_time = input("\tEnter Time (HH:MM:SS) - ")
        if entry_time == " ":
            print("###### Enter Time ######")
        elif len(entry_time) != 8:
            print("###### Please Enter Valid Time ######")
        else:
            Time.append(entry_time)
            t = not True

    print("\n............................................................Record detail saved..................................................................")

def remove_entry():
    no = True
    while no:
        Vno = input("\tEnter vehicle number to delete (XXXX-XX-XXXX) - ").upper()
        if Vno == " ":
            print("###### Enter Vehicle No. ######")
        elif len(Vno) == 12:
            if Vno in Vehicle_Number:
                i = Vehicle_Number.index(Vno)
                Vehicle_Number.pop(i)
                Vehicle_Type.pop(i)
                vehicle_Name.pop(i)
                Owner_Name.pop(i)
                Date.pop(i)
                Time.pop(i)
                no = not True
                print("\n............................................................Removed Successfully..................................................................")
            elif Vno not in Vehicle_Number:
                print("###### No Such Entry ######")
            else:
                print("Error")
        else:
            print("###### Enter Valid Vehicle Number ######")

def view_parked_vehicles():
    count = 0
    print("----------------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\tParked Vehicles")
    print("----------------------------------------------------------------------------------------------------------------------")
    print("Vehicle No.\tVehicle Type\tVehicle Name\tOwner Name\tDate\t\tTime")
    print("----------------------------------------------------------------------------------------------------------------------")
    for i in range(len(Vehicle_Number)):
        count += 1
        print(Vehicle_Number[i], "\t\t", Vehicle_Type[i], "\t\t", vehicle_Name[i], "\t\t", Owner_Name[i], "\t\t", Date[i], "\t", Time[i])
    print("----------------------------------------------------------------------------------------------------------------------")
    print("------------------------------------------ Total Records - ", count, "-------------------------------------------------------")
    print("----------------------------------------------------------------------------------------------------------------------")

def view_left_parking_space():
    print("----------------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\tSpaces Left For Parking")
    print("----------------------------------------------------------------------------------------------------------------------")
    print("\tSpaces Available for Bicycle - ", bicycles)
    print("\tSpaces Available for Bike - ", bikes)
    print("\tSpaces Available for Car - ", cars)
    print("----------------------------------------------------------------------------------------------------------------------")

def view_parking_rate():
    print("----------------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\tParking Rate")
    print("----------------------------------------------------------------------------------------------------------------------")
    print("*1. Bicycle      Rs20 / Hour")
    print("*2. Bike         Rs40 / Hour")
    print("*3. Car          Rs60 / Hour")
    print("----------------------------------------------------------------------------------------------------------------------")

def generate_bill():
    print(".............................................................. Generating Bill ..........................................................................")
    no = True
    while no:
        Vno = input("\tEnter vehicle number to generate bill (XXXX-XX-XXXX) - ").upper()
        if Vno == "":
            print("###### Enter Vehicle No. ######")
        elif len(Vno) == 12:
            if Vno in Vehicle_Number:
                i = Vehicle_Number.index(Vno)
                no = not True
            elif Vno not in Vehicle_Number:
                print("###### No Such Entry ######")
            else:
                print("Error")
        else:
            print("###### Enter Valid Vehicle Number ######")

    print("\tVehicle Check-in time - ", Time[i])
    print("\tVehicle Check-in Date - ", Date[i])
    print("\tVehicle Type - ", Vehicle_Type[i])

    inp = True
    amt = 0
    while inp:
        hr = input("\tEnter No. of Hours Vehicle Parked - ")
        if hr == "":
            print("###### Please Enter Hours ######")
        elif int(hr) >= 0:
            if Vehicle_Type[i] == "Bicycle":
                amt = int(hr) * 20
                inp = not True
            elif Vehicle_Type[i] == "Bike":
                amt = int(hr) * 40
                inp = not True
            elif Vehicle_Type[i] == "Car":
                amt = int(hr) * 60
                inp = not True
        else:
            print("###### Enter Valid Number of Hours ######")

    print("\tParking Charge - ", amt)

    # Calculate additional charge (18% of the parking charge)
    ac = 0.18 * amt
    print("\tAdd. charge 18% - ", ac)

    # Total charge including additional charge
    total_charge = amt + ac
    print("\tTotal Charge - ", total_charge)

    print("..............................................................Thank you for using our service...........................................................................")
    a = input("\tPress Any Key to Proceed - ")

if __name__ == "__main__":
    main()
