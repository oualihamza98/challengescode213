'''
Exercise 1: Variable Swap and Conditional Printing

Create two variables, x and y, and assign them values of your choice.
Swap the values of x and y without using a temporary variable. (Hint: Use arithmetic operations)
Implement a condition:
If the value of x is greater than y, print "x is greater than y."
If the value of x is less than y, print "x is less than y."
If the values are equal, print "x and y are equal."
'''
x=10;y=10
x=x+y
y=x-y
x=x-y
print(f"x={x} et y={y}")
if x>y:
    print("x is greater than y.")
elif x<y:
    print("x is less than y.")
else:
    print("x is equal to y.")
'''

Exercise 2: Arithmetic Calculator

Create two variables, num1 and num2, and assign them numeric values.
Implement a menu-driven program with the following options ( using loops ) :
Enter '1' to add num1 and num2.
Enter '2' to subtract num2 from num1.
Enter '3' to multiply num1 and num2.
Enter '4' to divide num1 by num2.
Enter '5' to exit the program.
Depending on the user's choice, perform the corresponding arithmetic operation and display the result. If the user enters an invalid choice, show an error message and display the menu again.
 
'''
'''
un menu: num1=x; num2=y
     BIENVENUE
1-addition
2-soustraction
3-multiplication
4-division
5-quitter
'''
print("*****BIENVENUE*****\n*Pour l'addition tapez 1.\n*Pour la soustraction tapez 2.\n*Pour la multiplication tapez 3.\n*Pour la division tapez 4.\n*Pour QUITTER tapez 5.")


def addition(x, y):
    return x + y

def soustraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "attention vous avez diviser par 0"

while True:
    var = input("Veuillez choisir une opération arythmétique (1, 2, 3, 4) ou tapez 5 pour quitter: ")
    var = int(var)
    
    if var == 5:
        print("Merci d'avoir utilisé la calculatrice. Au revoir!")
        break
    
    x1 = float(input("Veuillez choisir le premier nombre: "))
    x2 = float(input("Veuillez choisir le deuxième nombre: "))
    
    if var == 1:
        print(f"{x1} + {x2} = {addition(x1, x2)}")
    elif var == 2:
        print(f"{x1} - {x2} = {soustraction(x1, x2)}")
    elif var == 3:
        print(f"{x1} * {x2} = {multiplication(x1, x2)}")
    elif var == 4:
        result = division(x1, x2)
        print(f"{x1} / {x2} = {result}")
    else:
        print("VEULLEZ CHOISIIR ENTRE (1,2,3,4) POUR LES OPERATIONS")
    
    continuer = input("Voulez-vous continuer? Tapez 'oui' pour continuer, ou 'non' pour arrêter: ")
    if continuer != 'oui':
        print("Merci d'avoir utiliséé la calculatrice. C'est Ciao!")
        break


'''
Exercise 3: Temperature Converter

Create a variable, temperature, and assign a temperature value in Celsius.
Implement a menu-driven program with the following options:
Enter '1' to convert the temperature from Celsius to Fahrenheit.
Enter '2' to convert the temperature from Celsius to Kelvin.
Enter '3' to exit the program.
Implement the temperature conversion formulas and display the converted temperature. Ensure that the program handles invalid menu choices gracefully.
 '''

print("*****BIENVENIDO*****\n*Enter '1' to convert the temperature from Celsius to Fahrenheit.\n*Enter '2' to convert the temperature from Celsius to Kelvin.\n*Enter '3' to exit the program.")


def celsius_to_far(temp):
    return (temp*9/5) + 32

def celsius_to_kelvin(temp):
    return temp+273.15


while True:
    var = input("choose the conversion you want (1, 2) or 3 to exit ")
    var = int(var)
    
    if var == 3:
        print("thanks for using my temperature converter, See ya!")
        break
    
    x = float(input("enter a celsius temperature, it must be bigger than -273,15 C  "))
    
    while x< -273.15:
        print("the temperature you want to convert must be bigger than -273,15 C ")
        x = float(input("Enter a Celsius temperature again: "))
    
    if var == 1:
        print(f"{x} °C is  {celsius_to_far(x)} in Fahrenheit")
    elif var == 2:
        print(f"{x} °C is  {celsius_to_kelvin(x)} in Kelvin")
    else:
        print("please choose between (1,2,3) ")
    
    continuer = input("Wanna continue? write 'yes' to continue, or 'no' to stop ")
    if continuer != 'yes':
        print("thanks for using my converter. Ciao!")
        break


'''
Exercise 4: Odd or Even Number Checker

Create a variable, number, and assign it an integer value.
Implement a condition to check if the number is odd or even.
If it's an even number, print "The number is even." odd=IMPAIR // even=pair
If it's an odd number, print "The number is odd."
 
'''
variable=input("veuillez rentrer un nombre entier")
variable=int(variable)
if variable % 2 ==0:
    print ("The number is even.")
else:
    print ("The number is odd.")



'''
Exercise 5: Password Checker

Create a variable, password, and assign it a string value.
Implement a condition to check the strength of the password.
If the password has at least 8 characters and includes both letters and numbers, print "Strong Password."
If the password has fewer than 8 characters or does not include both letters and numbers, print "Weak Password."
These exercises will help you practice Python basics, including variables, operators, and conditions.
You can use these exercises to test your skills and deepen your understanding of these fundamental concepts.
'''
while True:
    une_liste=input("veuillez entrer un mot de passe: ")


    if (len(une_liste)>=8 and une_liste.isdigit()==False and une_liste.isalpha()==False and une_liste.isalnum()==True):
        print("Strong Password")
        break
    else:
        print("Weak Password")
        continuer=input("voulez-vous continuer: oui/non : ").lower()
        if continuer!="oui":
            print("A toute a l'heure !")
            break

