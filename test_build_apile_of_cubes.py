import Build_apile_of_cubes as B

# --------------------------------------------------------------------------------------------
status = 0
if B.find_nb(1) != 1:
    print("The Value of 1 as an argument is not returning the correct n value")
status = B.find_nb(1)
print("The expected result is 1, got", status)
print(" ")
# --------------------------------------------------------------------------------------------
status = 0
if B.find_nb(8) != -1:
    print("The Value of 8 as an argument is not returning the correct n value")
status = B.find_nb(8)
print("The expected result is -1, got", status)
print(" ")
# --------------------------------------------------------------------------------------------



