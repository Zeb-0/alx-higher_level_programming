0x00. Python - Hello, World


0. Write a Shell script that runs a Python script.
	
The Python file name will be saved in the environment variable $PYFILE	


1. Write a Shell script that runs Python code.

The Python code will be saved in the environment variable $PYCODE


2. Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.

	i. Use the function print


3. Complete this source code in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.

	i. The output of the script should be:
		
		the number, followed by Battery street,

		followed by a new line

	ii. You are not allowed to cast the variable number into a string
		
	iii. Your code must be 3 lines long

	iv. You have to use f-strings tips


4. Complete the source code in order to print the float stored in the variable number with a precision of 2 digits.

	i. The output of the program should be:
	
		. Float:, followed by the float with only 2 digits

		. followed by a new line

	ii. You are not allowed to cast number to string

	iii. You have to use f-strings


5. Complete this source code in order to print 3 times a string stored in the variable str, followed by its first 9 characters.


	i. You can find the source code here

	ii. The output of the program should be:

		. 3 times the value of str
	
		. followed by a new line

		. followed by the 9 first characters of str
	
		. followed by a new line

	iii. You are not allowed to use any loops or conditional statement
		
	iv. Your program should be maximum 5 lines long


6. Complete this source code to print Welcome to Holberton School!

	i. You can find the source code here

	ii. You are not allowed to use any loops or conditional statements.

	iii. You have to use the variables str1 and str2 in your new line of code

	iv. Your program should be exactly 5 lines long


7. Complete this source code

	i. You can find the source code here

	ii. You are not allowed to use any loops or conditional statements

	iii. Your program should be exactly 8 lines long

	iv. word_first_3 should contain the first 3 letters of the variable word

	v. word_last_2 should contain the last 2 letters of the variable word
		
	vi. middle_word should contain the value of the variable word without the first and last letters


8. Complete this source code to print object-oriented programming with Python, followed by a new line.


	i. You can find the source code here

	ii. You are not allowed to use any loops or conditional statements

	iii. Your program should be exactly 5 lines long

	iv. You are not allowed to create new variables

	v. You are not allowed to use string literals


9. Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.


	i. Your script should be maximum 98 characters long (please check with wc -m 9-easter_egg.py)


10. Technical interview preparation:

	. You are not allowed to google anything
	
	. Whiteboard first

	. This task and all future technical interview prep tasks will include checks for the efficiency of your solution, i.e. is your solution’s runtime fast enough, does your solution require extra memory usage / mallocs, etc.

Write a function in C that checks if a singly linked list has a cycle in it.

	. Prototype: int check_cycle(listint_t *list);

	. Return: 0 if there is no cycle, 1 if there is a cycle

Requirements:

	.Only these functions are allowed: write, printf, putchar, puts, malloc, free


11. Write a Python script that prints exactly and that piece of art is useful - Dora Korpar, 2015-10-19, followed by a new line.

	. Use the function write from the sys module
	
	. you are not allowed to use print

	. Your script should print to stderr

	. Your script should exit with the status code 1


12. Write a script that compiles a Python script file.

The Python file name will be stored in the environment variable $PYFILE

The output filename has to be $PYFILEc (ex: export PYFILE=my_main.py => output filename: my_main.pyc)


13. Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:


		 3           0 LOAD_CONST               1 (98)
		             3 LOAD_FAST                0 (a)
		             6 LOAD_FAST                1 (b)
		             9 BINARY_POWER
		             10 BINARY_ADD
		             11 RETURN_VALUE

		Tip: Python bytecode
