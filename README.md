# Code Wars Exercises #

Here you will find a list of Codewars exercises and their solutions.



## Convert String to Camel Case ##

*Description*:

<li>Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).</li>

*Examples*:

<li>"the-stealth-warrior" gets converted to "theStealthWarrior"</li>
<li>"The_Stealth_Warrior" gets converted to "TheStealthWarrior"</li>



## Bit Counting ##

*Description*:

<li>Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.</li>

*Examples*:

<li>The binary representation of 1234 is 10011010010, so the function should return 5 in this case</li>



## Simple Pig Latin ##

*Description*:

<li>Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.</li>

*Examples*:

```
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
```
```
pig_it('Hello world !')     # elloHay orldway !
```



## Counting Sheeps ##

*Description*:

<lli>Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).</li>

*Examples*:

```
[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
```
The correct answer would be 17



## Pillars ##

*Description*:

<li>There are pillars near the road. The distance between the pillars is the same and the width of the pillars is the same. Calculate the distance between the first and the last pillar in centimeters (without the width of the first and last pillar). Your function accepts three arguments:</li>

```
    1) number of pillars (≥ 1);
    2) distance between pillars (10 - 30 meters);
    3) width of the pillar (10 - 50 centimeters).
```


## Your Order Please! ##

*Description*:

<li>Your task is to sort a given string. Each word in the string will contain a single number.
This number is the position the word should have in the result.</li>
<li>Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).</li>

<li>If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.</li>


*Examples*:

```
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""
```


## A Wolf in Sheep's Clothing ##

*Description*:

Wolves have been reintroduced to Great Britain.
You are a sheep farmer, and are now plagued by wolves which pretend to be sheep. Fortunately, you are good at spotting them.

Warn the sheep in front of the wolf that it is about to be eaten.
Remember that you are standing at the front of the queue which is at the end of the array:

```
[sheep, sheep, sheep, sheep, sheep, wolf, sheep, sheep]      (YOU ARE HERE AT THE FRONT OF THE QUEUE)
   7      6      5      4      3            2      1
```

If the wolf is the closest animal to you, return "Pls go away and stop eating my sheep".
Otherwise, return "Oi! Sheep number N! You are about to be eaten by a wolf!" where N is the sheep's position in the queue.

Note: there will always be exactly one wolf in the array.

*Examples*:

```
Input: ["sheep", "sheep", "sheep", "wolf", "sheep"]
Output: "Oi! Sheep number 1! You are about to be eaten by a wolf!"

Input: ["sheep", "sheep", "wolf"]
Output: "Pls go away and stop eating my sheep"

Input: ["wolf"]
Output: "Pls go away and stop eating my sheep"
```


## Count by X ##

*Description*:

Create a function with two arguments that will return an array of the first (n) multiples of (x).
Assume both the given number and the number of times to count will be positive numbers greater than 0.
Return the results as an array.

*Examples*:

```
count_by(1,10) #should return [1,2,3,4,5,6,7,8,9,10]
count_by(2,5) #should return [2,4,6,8,10]
```



## Remove The Minimum ##

*Description*:

Given an array of integers, remove the smallest value.
Do not mutate the original array/list. If there are multiple elements with the same value, remove the one with a lower index.
If you get an empty array/list, return an empty array/list.

Don't change the order of the elements that are left.

*Examples*:

```
* Input: [1,2,3,4,5], output= [2,3,4,5]
* Input: [5,3,2,1,4], output = [5,3,2,4]
* Input: [2,2,1,2,1], output = [2,2,2,1]
```



## Isogram ##

*Description*:

An isogram is a word that has no repeating letters, consecutive or non-consecutive.
Implement a function that determines whether a string that contains only letters is an isogram.
Assume the empty string is an isogram. Ignore letter case.



## Number of People in the Bus ##

*Description*:

You are provided with a list (or array) of integer pairs.
Elements of each pair represent number of people get into bus (The first item) and
number of people get off the bus (The second item) in a bus stop.

Your task is to return number of people who are still in the bus after the last bus station (after the last array).
Even though it is the last bus stop, the bus is not empty and some people are still in the bus,
and they are probably sleeping there :D


*Examples*:

```
([[10,0],[3,5],[5,8]]),5
([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]),17
([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]),21
```


## Human Readable Time ##

*Description*:

Write a function, which takes a non-negative integer (seconds) as input and returns
the time in a human-readable format (HH:MM:SS)

    HH = hours, padded to 2 digits, range: 00 - 99
    MM = minutes, padded to 2 digits, range: 00 - 59
    SS = seconds, padded to 2 digits, range: 00 - 59

The maximum time never exceeds 359999 (99:59:59)


## Dot Calculator ##

*Description*:

You have to write a calculator that receives strings for input. The dots will represent the number in the equation. There will be dots on one side, an operator, and dots again after the operator. The dots and the operator will be separated by one space.

Here are the following valid operators :

    + Addition
    - Subtraction
    * Multiplication
    // Integer Division


You'll have to return a string that contains dots, as many the equation returns. If the result is 0, return the empty string. When it comes to subtraction, the first number will always be greater than or equal to the second number.

*Examples*:

```
* "..... + ..............." => "...................."
* "..... - ..."             => ".."
* "..... - ."               => "...."
* "..... * ..."             => "..............."
* "..... * .."              => ".........."
* "..... // .."             => ".."
* "..... // ."              => "....."
* ". // .."                 => ""
* ".. - .."                 => ""
```


## Who Likes It? ##

*Description*:

You probably know the "like" system from Facebook and other pages.
People can "like" blog posts, pictures or other items.
We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item.


*Examples*:

```
[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
```


## Find the Odd Int ##

*Description*:

Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.


*Examples*:

```
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).
```


## Printer Errors ##

*Description*:

In a factory a printer prints labels for boxes.
For one kind of boxes the printer has to use colors which, for the sake of simplicity, are named with letters from a to m.

The colors used by the printer are recorded in a control string.
For example a "good" control string would be aaabbbbhaijjjm meaning that the printer used three times color a,
four times color b, one time color h then one time color a...

Sometimes there are problems: lack of colors, technical malfunction and a "bad" control string
is produced e.g. aaaxbbbbyyhwawiwjjjwwm with letters not from a to m.

You have to write a function printer_error which given a string will return the error rate of the printer as a string
representing a rational whose numerator is the number of errors and the denominator the length of the control string.
Don't reduce this fraction to a simpler expression.

The string has a length greater or equal to one and contains only letters from a to z.


*Examples*:

```
s="aaabbbbhaijjjm"
printer_error(s) => "0/14"

s="aaaxbbbbyyhwawiwjjjwwm"
printer_error(s) => "8/22"
```


## Pete, The Baker ##

*Description*:

Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths. Can you help him to find out, how many cakes he could bake considering his recipes?

Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and
returns the maximum number of cakes Pete can bake (integer).
For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200).
Ingredients that are not present in the objects, can be considered as 0.


*Examples*:

```
# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})
```


## Greed is Good ##

*Description*:

Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a throw according to these rules. You will always be given an array with five six-sided dice values.

```
 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point
```

A single die can only be counted once in each roll. For example, a given "5" can only count as part of a triplet (contributing to the 500 points) or as a single 50 points, but not both in the same roll.

Example scoring
```
 Throw       Score
 ---------   ------------------
 5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
 1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
 2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)
```
