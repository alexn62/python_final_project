Motivation and background:
Before attending this class, I got into programming for mobile development, 
using Dart (a language developed by Google, similar to Javascript) and Flutter (a framework for Dart).

Because I quickly realized that although I was decent using flutter, I had a hard time with
programming related tasks. In other words, I was okay developing apps, but not writing programs in Dart. 

As a result, I started using codewars.com to practice my programming skills, and quickly got addicted to it. 
By solving technical-interview-style coding questions, I found my love for programming, as I get satisfaction
out of it, that is comparable to math. I can put my problem solving skills to the test. 

One of the questions I came across recently was the one for my program. Instead of solving it, I convinced myself
to use it for my final project. After hours of work, I finally figured out how to solve the problem. 
It was one of my first times using python on codewars. 

The link to the problem is: https://www.codewars.com/kata/54d496788776e49e6b00052f/python

How-to:
Follow the instructions given in the terminal. 
1. Type in number.
2. Number gets checked for validity.
3. Number get added to an array.
4. Array gets checked for max number and all primes.
5. Prime factors are calculated and added to a dictionary. 
6. The user sees the result.
7. The user can restart the program or quit.

Reflection:
I tried to approach the implementation step by step, testing along the way. I started without input and focused on the functionality first.
After that, I added a lot of tests and divided the program into smaller chunks to do even more testing. 
Some of the testing is not really necessary, as the program will not pass on wrong values to some functions, because the values are tested
in a prior function.
The most challenging part was figuring out the math behind the problem and finding a good optimization (stopping the loop after hitting sqrt(num)).
Another challenge was to deal with the test mutating the original values, and adding numbers to the empty initialized list.
I solved the problem through accessing and resetting a global variable in the main body of my program. 
