### Mad Libs Game - Example 1

#color = input("Enter a color: ")
#plural_noun = input("Enter a Plural Noun: ")
#celebrity = input("Enter a celebrity: ")

#print("Roses are " + color )
#print(plural_noun + " are blue")
#print("I love " + celebrity)

#____________________________________________________________________

#### Lists - Example 2 

#levels = [59, 99, 32, 43]
#friends = ["Geralt", "Spawn", "Spawn", "Sora", "Kairi"]
#friends[3] = "Flora"
#print(friends[3])
#name = input("Enter your favorite character: ")

#friends2 = friends.copy()

#print(friends2)

#____________________________________________________________________
### Tuples (fixed list) - Example 3


#coordinates = [(4, 5), (6,7), (80, 34)]
#print(coordinates)
#___________________________________________

#Functions - Example 4 

#def say_hi(name, age):
    #print("Hello " + name + ", you are " + str(age))


#say_hi("Dan", 34)
#say_hi("Flora", 13)

#________________________________________

#Return statements - Examples 5

#def cube(num):
    #return num*num*num
    #print("code")

#result = cube(5)
#print(result)
#_____________________________________

#If statements - Examples 6

#is_male = False
#is_tall = False

#if is_male and is_tall:
    #print("You are a tall male")
#elif is_male and not(is_tall):
    #print("You are a short male")
#elif not(is_male) and is_tall:
    #print("You are not a  male but are tall")

#else:
    #print("You are either not male and not tall")
#____________________________________________________
# If Statements & Comparisons - Examples 7  

#def max_num(num1, num2, num3):
    #if num1 <= num2 and num1 >= num3:
        #return num1
    #elif num2 >= num1 and num2 >= num3:
        #return num2
    #else:
        #return num3
    
    
#print(max_num(5993, 9, 31))
#____________________________________________________________
#Advanced Calculator - Examples 8 

#num1 = float(input("Enter first number: "))
#op = input("Enter operator: ")
#num2 = float(input("Enter second number: "))

#if op == "+":
    #print(num1 + num2)
#elif op == "-":
    #print(num1 - num2)
#elif op == "/":
    #print(num1 / num2) 
#elif op == "*":
    #print(num1 * num2)
#else: 
    #print("Invalid operator")
#________________________________________________________________
#Dictionary & Key Value Pairs - Examples 9

#monthConversions = {
    #0: "January",
    #1: "February",
    #2: "March",
    #"Apr": "April",
    #"May": "May",
    #"Jun": "June",
    #"Jul": "July",
    #"Aug": "August",
    #"Sep": "September",
    #"Oct": "October",
    #"Nov": "November",
    #"Dec": "December",
#}

#print(monthConversions["Nov"])
#____________________________________________________________
#While Loop - Examples 10

#i = 1
#while i <= 10:
    #print(i)
    #i += 1

#print("Done with Loop")

#_____________________________________________________
#Guessing Game - Examples 11

#secret_word = "Ooloi"
#guess = ""
#guess_count = 0
#guess_limit = 3
#out_of_guesses = False

#while guess != secret_word and not(out_of_guesses):
    #if guess_count < guess_limit:
        #guess = input("Enter guess: ")
        #guess_count += 1
    #else:
        #out_of_guesses = True

#if out_of_guesses:
    #print("Out of Guesses, you lose!")
#else:
    #print("You win!")
#____________________________________________________________
#For Loop - Examples 12
#friends = ["Spawn", "Liu Kang", "Sora"]
#len(friends)
#for name in friends:
    #print(name)
#for index in range(10):
    #print(index)
#for index in range(3, 10):
    #print(index)
#for index in range(len(friends)):
    #print(friends[index])
#for index in range(5):
    #if index == 0:
        #print("first Iteration")
    #else:
        #print("Not first")
#________________________________________________________
#Exponent Function - Examples 13

#def raise_to_power(base_num, pow_num):
    #result = 1
    #for index in range(pow_num):
        #result = result * base_num
    #return result


#print(raise_to_power(2, 3))
#______________________________________
#2D Lists and Nested Loops - Examples 14
#number_grid = [
    #[1, 2, 3],
    #[4, 5, 6],
    #[7, 8, 9],
    #[0]
#]

#for row in number_grid:
    #for col in row:
        #print(col)
#___________________________________________________
#Translating App - Example 15

#def translate(phrase):
    #translation = ""
    #for letter in phrase:
        #if letter.lower() in "aeiou":
            #if letter.isupper():
                #translation = translation + "G"
            #else:
             #translation = translation + "g"

        #else:
            #translation = translation + letter
    #return translation

#print(translate(input("Enter a phrase: ")))

#____________________________________________________________
# Try/Except (Debugging Errors) - Examples 16


#try:
    #number = int(input("Enter a number: "))
    #print(number)
#except ZeroDivisionError as err:
    #print(err)
#except ValueError:
    #print("Invalid Input") 


#_______________________________________________________
#Reading files - Examples 17

#read_file = open("example.txt", "r")
#for read in read_file.readlines():
    #print(read)
#read_file.close()

#_______________________________________________________

#Writing Files - Examples 18

#read_file = open("student.py", "w")

#read_file.write("")
#read_file.close()


#read_file = open("example.txt", "a")

#read_file.write("\nhello world, again")

#read_file.close()
#____________________________________________

#Classes & Objects - Examples 19

class Student:
    
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

#_____________________________________________

# Multiple Question Quiz - Examples 20

#from Question import Question

#question_prompts = [
    #"What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    #"What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    #"What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
#]

#questions = [
    #Question(question_prompts[0], "a"),
    #Question(question_prompts[1], "c"),
    #Question(question_prompts[2], "b"),
#]

#def run_test(questions):  
    #score = 0
    #for question in questions:
        #answer = input(question.prompt)
        #if answer == question.answer:
            #score += 1
    #print("You got " + str(score) + "/" + str(len(questions)) + " correct")    
#run_test(questions)