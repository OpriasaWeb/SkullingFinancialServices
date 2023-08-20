# Skulling Financial Services

Instructions: Design a retirement planning calculator for Skulling Financial Services. Allow a user to enter a number of working years remaining in the user's career and the annual amount of money the user can save. 
Assume that the user earns three percent simple interest on savings annually. 
Program output is a schedule that lists each year number in retirement starting with year 0 and the user's savings at the start of that year. Assume that the user spends $50,000 per year in retirement and then earns three percent interest on the remaining balance. End the list after 40 years, or when the user's balance is 0 or less, whichever comes first.



Psuedocode:
          BEGIN
              DECLARE num remaining = 0
              DECLARE num annual = 0
              DECLARE num controlloop = 0
              DECLARE num spend = 50000

              OUTPUT "Enter the number of working years remaining:"
              INPUT remaining
              OUTPUT "Enter the annual amount of money to save:"
              INPUT annual

              WHILE controlloop < remaining AND controlloop < 40 AND annual > 0
                  OUTPUT "Year " + controlloop
                  OUTPUT "User's savings " + annual
                  annual = annual + (annual * 0.03) - spend
                  IF annual <= 0 THEN
                      annual = 0
                  END IF
                  controlloop = controlloop + 1
              END WHILE
          END
          