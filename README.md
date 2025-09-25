# Basic_code_in_Python

This is my very first Python program ✍️

## About Python
- 🐍 Python is a high-level programming language.  
- ✅ It is human understandable and easy to learn.  
- ⚡ Python code is interpreted and executed line by line.  
- 🛠️ If there’s an error, execution stops, so debugging is easier.  
- 📖 It has very simple syntax (almost like English).  

## Code Example
```python
print("Namaskara Karnataka")
````
## How to Run

Install Python (if not installed) → Download here
Clone this repository:
git clone https://github.com/Hegde1527/Basic_code_in_Python.git
Navigate to the folder:
cd Simple_code_with_Me
Run the Python file:

python p1.py


## Program 2: Variables 

* Variables are containers that hold data values.
  
* They are created when we assign a value .
  
* In python there is no need of declaring variables because Python is dynamically typed.
  

Variable Naming Rules:

* Variable names can contain letters(A-Z , a-z), numbers(0-9), and underscorea(_ ).
  
* Variable names must start with a letter or an underscore.
  
  Example:
  ```
                 a = 10       ✓
                 234 = hi     X
                 _hello = hi   ✓
  
* x = 5.0
  ---> Assigning a float value to the variable x .
* w = "monkey"
  ----> Assigning a String value to the varible w .

### Code
```

a = 10
b = 20
print(a)              # Output = 10
print(b)              # Output = 20
print("a")            # Output = a
print(a + b)          # Output = 30

```
* a = 10, b = 20 → assigning values to variables.

* print(a) → prints the value stored in a (10).

* print("a") → prints the letter a, not the value.

* print(a+b) → adds the values of a and b (10 + 20 = 30).

  ## Program 3: Data Types

* Python has various built-in data types.
  
  --->some commonly used are:
  
  1. int:
      * Interger we will use as int in short.
      * example: 1,2,-3,100 etc.....,
  
  
  2. float:
      * Used for floating-point numbers.
      * example: 3.13,7.89,666.9 etc.....,
  
  
  3. str:
      * Used for string .
      * example: "hello world" , "how are you" , "i am so happy to see you" etc......,
  
  
  4. bool:
      * Used for Boolean .
      * The boolean values will be either True / False .
  

* Type Checking :
   ---> we use type() function to check the type of variable .
  
  Example:
  ```
           a = 100
           print(type(a))    #Output: <class 'int'>
           b = 10.9
           print(type(b))   #Output: <class 'float'>
           c = "buddy"
           print(type(c))   #Output: <class 'str'>
           d = true
           print(type(b))   #Output: <class 'bool'>

* Type Conversion :

   --> Python allows us to convert the data types between them using functions like int() ,float() ,str() etc.....,

  Example:
  ```
      x = 10           # x is an integer
      y = 100.98       # y is an float
      z = "hello"      # z is string
      print(x+z)       #TypeError: unsupported operand type(s) for +: 'int' and 'str'
      print(str(x)+z)  #Output: 10hello
      print(x+int(z))  #Output:error
  Note : Cannot convert non-numeric strings like 'hello' into an integer. You need either a number string or input validation.
  

* Arithematic Operations :
  1. Addition ('+')
  2. Subtraction ('-')
  3. Multiplication ('*')
  4. Division ('/')
  5. Floor Division ('//')
  6. Modulus ('%')
  7. Exponentiation ('**')

Example:
```
    a = 20
    b = 30
    print(a+b)    # Output : 50
    print(a-b)    # Output : -10
    print(a*b)    # Output : 600
    print(a/b)    # Output : 0.666666666666
    print(a//b)   # Output : 0
    print(a%b)    # Output : 20
    print(a**b)   # Output : 1073741824000000000000000000000000000000
```


* Assigning Values to Multipe Variables :

  Python allows us to assign c=values to multiple variables in a single line.
  

                
  
