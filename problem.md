# Restrictions:
I can use any string function, but the strings have to be the same as the ones in the file.  I can't use loops or lists, and I have to stick with the math module and the check module (which is based on the check file I provide to you - I have to use that later to run tests on the function with specific arguments).

## PROBLEM A:

I have to create a function reverse_nat that consumes nothing and will prompt the user to enter a natural integer. The purpose of the function is to print the same input with reverse order of the digits. The function will run until zero is entered. Once zero is entered the function will print the total sum of the reversed integers with appropriate message  then the message Bye! , after which the function will terminate. I need to follow the format in the example I will give you below:

examples:
```py
reverse_nat()
Enter a positive integer: 0
The total is: 0
Bye!

reverse_nat()
>> Enter a positive integer: 4523
>> Enter a positive integer: 12
>> Enter a positive integer: 100
>> Enter a positive integer: 0
Total is: 3276
Bye!
```

Again, please use the names created in the problemA.py file I will send you.  Check.py needs to be in the same directory wherever you save problemA.py.


PROBLEM B:

I have to write the function caesar_encrypt that consumes a string of text, alphabetical letters, and natural number, step, and returns a string after applying a Caesar encryption.

As an example:
```py
>> caesar_encrypt("Nice", 7) => "Upjl"
>> caesar_encrypt("xYz", 3) => "aBc"
>> caesar_encrypt("", 10) => ""
>> caesar_encrypt("Wow", 113) => "Fxf"
>> caesar_encrypt("Wow", 0) => "Wow"
```

I have to use Caaesar encryption: i.e. with right shift of 3, A would be replaced
by D, B would become E, and so on.

I cannot use ord() or chr().

Please use the names created in the problemB.py file I will send you.  Check.py needs to be in the same directory wherever you save problemB.py.
