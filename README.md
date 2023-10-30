# anzan_training

This is a simple training programm for multiplication of (up to) two digits integers.

[]()
<img src="Screenshot 2023-10-30 at 09.48.26.png" alt="screenshot" title="サンプル">

This is probably not for anzan (mental arithmetic) per se, but still helps.

It has three courses:

1. Genral
2. Indian
3. Mixed

In the Indian course (2), probelms are designed to work with so called Indian calculations.

There are three types.
1. The tens place of a and b　match and the sum of the units place of a and b is 10 (eg. $97 \times 93$)
2. The tens place of a and b　match and the sum of the units place of a and b is **NOT** 10 (eg. $78 \times 76$)
3. the units place of a and b match and the sum of the tens place of a and b is 10 (eg. $79 \times 39$)

In case 1,
1. Multiply the tens place of **a** with the sum of the tens place of **b** and 1 ($9 \times (9 + 1)= 90$)
2. Join this value with the product of the units place of **a** and that **b** ($7 \times 3$)

eg. $97 \times 93 = 9021$ as $9 \times (9 + 1) = 90$ is followed by $7 \times 3 = 21$

$$
\begin{align}
(10p  + q) \times (10p + (10-q)) &= 100 \cdot p^2 + 10  p  (q + 10 - q) + q(10-q) \\
&= 100  p^2  + q(10-q)
\end{align}
$$


In case 2, 
1. Add the unit place of **b** to **a** to gain **c** ($78 + 6 = 84$) 
2. Multiply this value **c** ($84$) with the tens place of **b** (9) ($84 \times 7 = 588$)
3. Obain the product of the units place of **a** and **b** ($8 \times 6$) to 10-fold of the product above ($588 \times 10$)

eg. $78 \times 76 = 5928$ as $(78 + 6) \times 7 = 588$ and add $8 \times 6$ to $588\times10$

$$
\begin{align}
(10p  + q) \times (10p + r) &= 100  p^2 + 10  p  (q + r) + qr \\
&= (10 p + q + r)  10  p + qr
\end{align}
$$


In case 3, 
1. Add the unit places of **b** to the product of the tens place of **a** and **b** ($7 \times 3 + 9$)
2. Join the product of the units place of **a** and **b**.

eg. $79 \times 39 = 3081$ as $7 \times 3 + 9 = 30$ is followed by $9 \times 9 = 81$


$$
\begin{align}
(10p  + q) \times (10(10-p) + q) &= 100  p(10-p) + 10q (p + (10-p)) + q^2 \\
&= 1000p -100p^2 + 100q + q^2\\
&= (10p -p^2 + q)*100 + q^2\\
&= (p(10-p) + q)*100 + q^2\\
\end{align}
$$



In general,
1. Join the product of the tens place of **a** and **b** and that of the units place of **a** and **b**
2. Obtain the sum of the product of the tens place of **a** and the units place of **a** and **b**
 and that of the units place of **a** and the tens place of **b**
3. Add the numbers by adjusting the digits

eg. $56 \times 79 = 4424$ as $7\times5$ is joined with $6 \times 9$ to obtain $3554$, and $(5 \times 9 + 6 * 7) \times 10 = 87 \times 10$ is added.


$$
\begin{align}
(10p  + q) \times (10r + s) &= 100  pr + qs + 10(ps +qr)  \\
\end{align}
$$

