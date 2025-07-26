# # 🧮 Student Result Checker – Python Mini Project

# The program:
# - Takes marks of **English**, **Python Language**, and **C# Language** from the user.
# - Checks whether the student has passed or failed in each subject (passing marks ≥ 33).
# - Calculates the **total marks** and **percentage**.
# - Displays whether the student has passed or failed **overall**.
# - Prints a polite and friendly message when the program ends.


print("Write a Python program that takes the marks of 3 subjects from the user:")

sub1=int(input("the marks of english is :"))
sub2=int(input("the marks of python langauge is :"))
sub3=int(input("the marks of c# langauge is :"))

print("the Results are:")
if(sub1>=33):

    print("you are pass in english")

else:

    print("you can try another time for english ")  

        
if(sub2>=33):

    print("you are pass in python langauge")

else:

     print("you can try another time in python ")  



if(sub3>=33):

    print("you are pass in c# langauge")

else:
    print("you can try another time in c#")  



total = sub1 + sub2 + sub3
percentage = total / 3

print("  overall percentage")

print("Total Marks:", total, "/ 300")

print(f"Percentage: {percentage:.2f}%")


if sub1 >= 33 and sub2 >= 33 and sub3 >= 33:

    print("🎉 Congratulations! You passed overall.")
else:

    print("😢 You failed overall. Better luck next time.")


print("the program is ended.....")

print("thanku❤")



    # the output
# Write a Python program that takes the marks of 3 subjects from the user:
# the marks of english is :36
# the marks of python langauge is :78
# the marks of c# langauge is :99
# the Results are:
# you are pass in english
# you are pass in python langauge        
# you are pass in c# langauge
#   overall percentage
# Total Marks: 213 / 300
# Percentage: 71.00%
# 🎉 Congratulations! You passed overall.
# the program is ended.....
# thanku❤
# PS C:\Users\shahz\Desktop\python



# Write a Python program that takes the marks of 3 subjects from the user:
# the marks of english is :33
# the marks of python langauge is :45
# the marks of c# langauge is :12
# the Results are:
# you are pass in english
# you are pass in python langauge
# you can try another time in c#
#   overall percentage
# Total Marks: 90 / 300
# Percentage: 30.00%
# 😢 You failed overall. Better luck next time.
# the program is ended.....
# thanku❤
# PS C:\Users\shahz\Desktop\python





