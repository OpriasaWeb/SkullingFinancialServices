controlloop = 0
spend = 50000  
remaining = 0
annual_input = 0  
annual = 0

remaining = input("Enter the number of working years remaining: ")
remaining = float(remaining)

annual_input = input("Enter the annual amount of money to save: ")
annual_input = float(annual_input)
annual = annual_input  

while controlloop < remaining and controlloop < 40 and annual > 0:
    print("Year " + str(controlloop))
    print("User's savings " + str(annual))

    annual = annual + (annual * 0.03) - spend

    if annual <= 0:
        annual = 0

    controlloop = controlloop + 1