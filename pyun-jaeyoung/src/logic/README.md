# Logic (1)

Python has different variable types that hold data to be used for later.

In other languages, you can attribute these different types to a certain keyword. Python has very broad, different types that assign 
data to different variables. Let's start with the boilerplate of all data types:


## Variables
int = integer number (think [1, 2, 3])
double = decimal point number (think [2.3, 4.1, 6.0])
float = same as double, but can be bigger in terms of size
boolean = true / false
char = single character 
string = multiple chars that make up a string of some sort

in other languages (like C++) you'll have to declare what type a variable is before declaring what it is

(think: int x = 2)
(think: string x = "hello world")
(think: char gender = 'M')
(think: boolean yes = true)

you don't have to remember all of these now, but you will later on. it's something that comes second hand

for Python, it automatically assumes the variable you're putting in, but it takes into account specifics in order to understand what you want the variable to be

so instead of declaring the type like in the example previously, you can just declare it as so:

``x = 3``

This variable is assigned as a number, specifically an integer.

In the `example.py`, try assigning the values True, 7.2, and "false" to a variable. 

Run the file to see what type they are. You can fiddle around with them once you're done.

## Arithmetic Operations
Mathematics in python is not very complicated overall, but is a little bit beginner-wise.

Like regular math, you can shove an operator between two numbers to get a result. This only works with integers and doubles, like declared last time.

Try figuring out how to add 2 and 3, and then print the result.

+ = adding
- = subtracting
/ = division
* = multiplication
^ = power
% = modulus (which is a whole new concept & is a college-level arithmetic operator)

Assuming that you know entirely everything of arithmetic mathematics, we'll move onto modulus.

Think of dividing 27 / 2. It would result in a non-whole number.

But 27 % 2 would equate to 1. Why? Because 2 goes into 27 around 13 times before not being about to be divided anymore. 

How about 2 % 27? This would equate to 2. It goes into 27 0 times and has a remainder of 2. 

What modulus is is just the remainder of a division operation. 

In `example.py`, assign a, b, c, a number that results in 26 through addition, 89 through subtraction, and 5 through modulus. 

## Commenting Code
Last on the list is commenting; this isn't necessary to logic, but rather is a self-benefit, and benefit to others. It's good practice to get this in now, and comments in an internship can genuinely get you back a return offer for 6 digit salaries. It's worth it.

Whenever you have a lengthy function or lengthy anything in general, just comment a short description of it to help other people understand and visualize what it's supposed to be about.

Check `example.py` about a function that you need to comment more information about. Push this file back to the cloud once you're done.

You don't really need to practice, but this is really good to know. Some people will not comment on their code and leave others to waste when trying to fix it or even understand it in general. It's best for you to put this in practice.


