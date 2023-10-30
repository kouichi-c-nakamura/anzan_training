# anzan_training

This is a simple training programm for multiplication of (up to) two digits integers.

It has three courses:

1. Genral
2. Indian
3. Mixed

In the Indian course (2), probelms are designed to work with so called Indian calculations.

There are three types.
1. The tens place of a and b　match and the sum of the units place of a and b is 10 (eg. 97 * 93)
2. The tens place of a and b　match and the sum of the units place of a and b is **NOT** 10 (eg. 78 * 76)
3. the units place of a and b match and the sum of the tens place of a and b is 10 (eg. 79 * 39)

In case 1,
1. Multiply the tens place of **a** with the sum of the tens place of **b** and 1 (9 * (9 + 1)= 90)
2. Join this value with the product of the units place of **a** and that **b** (7 * 3)

eg. 97 * 93 = 9021 as 9 * (9 + 1) = 90 is followed by 7 * 3 = 21

In case 2, 
1. Add the unit place of **b** to **a** to gain **c** (78 + 6 = 84) 
2. Multiply this value **c** (84) with the tens place of **b** (9) (84 * 7 = 588)
3. Obain the product of the units place of **a** and **b** (8 * 6) to 10-fold of the product above (588 * 10)

eg. 78 * 76 = 5928 as (78 + 6) * 7 = 588 and add 8 * 6 to 588*10


In case 3, 
1. Add the unit places of **b** to the product of the tens place of **a** and **b** (7 * 3 + 9)
2. Join the product of the units place of **a** and **b**.

eg. 79 * 39 = 3081 as 7 * 3 + 9 = 30 is followed by 9 * 9 = 81


In general,
1. Join the product of the tens place of **a** and **b** and that of the units place of **a** and **b**
2. Obtain the sum of the product of the tens place of **a** and the units place of **a** and **b**
 and that of the units place of **a** and the tens place of **b**
3. Add the numbers by adjusting the digits

eg. 56 * 79 = 4424 as 7*5 is joined with 6 * 9 to obtain 3554, and (5 * 9 + 6 * 7) *10 = 87 * 10 is added.




