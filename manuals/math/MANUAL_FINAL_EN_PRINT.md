# Mathematics Manual: 5th to 9th Grade
## Thematic Organization

This manual presents the essential mathematics content for school years 5th through 9th grade, organized by mathematical themes rather than by school year. This approach allows for an integrated view of conceptual progression, facilitating understanding of the natural evolution of concepts over the five years.

---

## Table of Contents

### NUMBERS
- Natural Numbers
- Integers
- Rational Numbers
- Real Numbers
- Powers and Scientific Notation

### ALGEBRA
- Algebraic Expressions
- Sequences and Patterns
- Equations and Inequalities
- Functions

### GEOMETRY
- Basic Elements
- Plane Figures
- Geometric Transformations
- Geometric Solids
- Trigonometry

### MEASUREMENT
- Area
- Volume

### DATA ORGANIZATION AND PROCESSING
- Data Representation
- Statistics
- Probability

---

# NUMBERS

## Natural Numbers

### Set of Natural Numbers

The set of natural numbers is represented by $\mathbb{N}$ and begins with: $1, 2, 3, 4, 5, 6, \ldots$

$\mathbb{N} = \{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, \ldots\}$

**Important note:** the set of natural numbers is infinite.

---

### Multiples and Divisors

#### Divisible numbers, multiples and divisors

A number is **divisible** by another if the division results in zero remainder.

**Examples:**

- $10 \div 2 = 5$ (remainder $0$) $\rightarrow$ $10$ is divisible by $2$
- $10 \div 3 = 3$ (remainder $1$) $\rightarrow$ $10$ is not divisible by $3$

If a number is divisible by another, it is also its **multiple**.
If a number divides another exactly, it is its **divisor**.

**From the division $10 \div 2 = 5$ (remainder $0$):**

- $10$ is divisible by $2$ and by $5$
- $10$ is a multiple of $2$ and of $5$
- $2$ and $5$ are divisors of $10$

---

#### Divisibility Criteria

A number is divisible by:

**2** if it is even (ends in 0, 2, 4, 6 or 8)

- $4565$ is not divisible by $2$
- $6548$ is divisible by $2$

**3** if the sum of its digits is a multiple of 3

- $548$ ($5+4+8=17$) is not divisible by $3$
- $85461$ ($8+5+4+6+1=24$) is divisible by $3$

**4** if it ends in 00 or the last two digits form a multiple of 4

- $45425$ (ends in $25$) is not divisible by $4$
- $54536$ (ends in $36$, multiple of $4$) is divisible by $4$
- $454500$ (ends in $00$) is divisible by $4$

**5** if it ends in 0 or 5

- $5648$ is not divisible by $5$
- $5640$ (ends in $0$) is divisible by $5$
- $8465$ (ends in $5$) is divisible by $5$

**6** if it is divisible by 2 and by 3

- $491$ is not divisible by $6$
- $4624$ is even but $4+6+2+4=16$ (not a multiple of $3$), is not divisible by $6$
- $1596$ is even and $1+5+9+6=21$ (multiple of $3$), is divisible by $6$

**9** if the sum of its digits is a multiple of 9

- $548$ ($5+4+8=17$) is not divisible by $9$
- $85464$ ($8+5+4+6+4=27$) is divisible by $9$

**10** if it ends in 0

- $154$ is not divisible by $10$
- $450$ is divisible by $10$

---

#### Determining Multiples and Divisors

**Multiples:** multiply the number by $0, 1, 2, 3, 4, \ldots$

**Multiples of 4:**

- $4 \times 0 = 0$
- $4 \times 1 = 4$
- $4 \times 2 = 8$
- $4 \times 3 = 12$
- $4 \times 4 = 16$
- $4 \times 5 = 20$

Multiples of $4 = \{0, 4, 8, 12, 16, 20, 24, 28, \ldots\}$

**Notes:**

- The set of multiples is infinite
- The number $0$ is a multiple of any number

**Divisors:** divide the number by $1$ up to itself, checking for zero remainder.

**Divisors of 10:**

- $10 \div 1 = 10$ (remainder $0$) ✓
- $10 \div 2 = 5$ (remainder $0$) ✓
- $10 \div 5 = 2$ (remainder $0$) ✓
- $10 \div 10 = 1$ (remainder $0$) ✓

Divisors of $10 = \{1, 2, 5, 10\}$

**Notes:**

- The set of divisors is finite
- The number $1$ is a divisor of any number

---

#### Properties of Divisors

**Property 1:** In a product, a divisor of a factor is also a divisor of the product.

- $15 \times 4 = 60$
- $3$ is a divisor of $15$, so it is a divisor of $60$
- $2$ is a divisor of $4$, so it is a divisor of $60$

**Property 2:** If a number divides two numbers, it also divides their sum and difference.

- $14 + 10 = 24$ | $14 - 10 = 4$
- $2$ divides $14$ and $10$, so it divides $24$ and $4$

**Property 3:** In an integer division, if a number divides the divisor and the remainder, it also divides the dividend.

- $14 \div 10 = 1$ (remainder $4$)
- $2$ divides $10$ and $4$, so it divides $14$

**Property 4:** In an integer division, if a number divides the dividend and the divisor, it also divides the remainder.

- $14 \div 10 = 1$ (remainder $4$)
- $2$ divides $14$ and $10$, so it divides $4$

---

### Least Common Multiple and Greatest Common Divisor

#### Least Common Multiple (l.c.m.)

The **least common multiple** is the smallest number that is a multiple of two or more numbers (not counting zero).

**Least common multiple of 4 and 10:**

- Multiples of $10 = \{0, 10, \mathbf{20}, \ldots\}$
- Multiples of $4 = \{0, 4, 8, 12, 16, \mathbf{20}, \ldots\}$

$\text{l.c.m.}(4, 10) = 20$

---

#### Greatest Common Divisor (g.c.d.)

The **greatest common divisor** is the largest number that divides two or more numbers.

**Greatest common divisor of 4 and 10:**

- Divisors of $10 = \{1, \mathbf{2}, 5, 10\}$
- Divisors of $4 = \{1, \mathbf{2}, 4\}$

$\text{g.c.d.}(4, 10) = 2$

---

#### Euclidean Algorithm

Method to determine the greatest common divisor of two numbers:

1. Divide the larger number by the smaller
2. Make a new division: previous divisor becomes dividend, previous remainder becomes divisor
3. Repeat until obtaining remainder $0$; that divisor is the g.c.d.

**Greatest common divisor of 30 and 50:**

- $50 \div 30 = 1$ (remainder $20$)
- $30 \div 20 = 1$ (remainder $10$)
- $20 \div 10 = 2$ (remainder $0$) ← **$10$ is the g.c.d.**

$\text{g.c.d.}(30, 50) = 10$

---

#### Relationship between l.c.m. and g.c.d.

$$a \times b = \text{g.c.d.}(a, b) \times \text{l.c.m.}(a, b)$$

---

### Prime Numbers

#### Prime Numbers and Composite Numbers

**Prime number:**

- Has only two divisors: $1$ and itself
- $5$ is prime (divisors: $1, 5$)

**Composite number:**

- Has more than two divisors
- $6$ is composite (divisors: $1, 2, 3, 6$)

**Note:** The number $1$ has only one divisor, so it is neither prime nor composite.

---

#### Sieve of Eratosthenes

The sieve of Eratosthenes is a practical method for finding prime numbers.

Procedure to discover prime numbers up to 100:

1. Write in a table the numbers from $1$ to $100$
2. Cross out $1$
3. Cross out all multiples of $2$ greater than $2$ ($4, 6, 8, \ldots$)
4. Cross out all multiples of $3$ greater than $3$ ($6, 9, 12, \ldots$)
5. Cross out all multiples of $5$ greater than $5$ ($10, 15, 20, \ldots$)
6. Cross out all multiples of $7$ greater than $7$ ($14, 21, 28, \ldots$)

The numbers that were not crossed out are the prime numbers up to 100.

---

#### Fundamental Theorem of Arithmetic

Given a natural number greater than $1$, there exists a unique increasing sequence of prime numbers whose product equals that number.

**Example:**
$90 = 2 \times 3 \times 3 \times 5$

When there are repeated prime factors, powers can be used:
- $3 \times 3 = 3^2$
- Therefore: $90 = 2 \times 3^2 \times 5$

---

#### Decomposition of a Number into Prime Factors

Practical method:

1. Divide the number by its smallest prime divisor
2. Divide the quotient by its smallest prime divisor, successively until obtaining quotient $1$
3. The initial number equals the product of the divisors used

**Example - Decomposition of number 630:**
$630 = 2 \times 3 \times 3 \times 5 \times 7 = 2 \times 3^2 \times 5 \times 7$

---

#### Relatively Prime Numbers

Two numbers are **relatively prime** if their g.c.d. equals $1$.

**Are the numbers 8 and 21 relatively prime?**

- Divisors of $21 = \{\mathbf{1}, 3, 7, 21\}$
- Divisors of $8 = \{\mathbf{1}, 2, 4, 8\}$
- $\text{g.c.d.}(8, 21) = 1$

**Yes**, $8$ and $21$ are relatively prime.

**Important notes:**

- Dividing two numbers by their g.c.d. yields two relatively prime numbers
- A fraction with numerator and denominator relatively prime is irreducible

---

## Integers

### Sets of Integer Numbers

- **Natural Numbers:** $\mathbb{N} = \{0, 1, 2, 3, 4, 5, \ldots\}$
- **Integer Numbers:** $\mathbb{Z} = \{\ldots, -3, -2, -1, 0, 1, 2, 3, \ldots\}$
- **Positive Integer Numbers:** $\mathbb{Z}^+ = \{1, 2, 3, 4, 5, \ldots\}$
- **Negative Integer Numbers:** $\mathbb{Z}^- = \{\ldots, -5, -4, -3, -2, -1\}$
- **Non-Positive Integer Numbers:** $\mathbb{Z}_0^- = \{\ldots, -5, -4, -3, -2, -1, 0\}$
- **Non-Negative Integer Numbers:** $\mathbb{Z}_0^+ = \{0, 1, 2, 3, 4, 5, \ldots\}$

---

### Number Line, Absolute Value and Opposite Numbers

To each point on the line corresponds a unique number (abscissa of the point), with the origin at zero.

**Absolute Value:** Corresponds to the distance from the point to the origin on the number line. The absolute value is always positive or zero.

**Examples:**

- $|5| = 5$
- $|-5| = 5$
- $|0| = 0$

**Opposite Numbers:** Have equal absolute value but opposite signs.

**Example:** The opposite of $5$ is $-5$

---

### Algebraic Addition

#### Addition with Same Signs
The result has the same sign; add the absolute values.

**Examples:**

- $(+2) + (+4) = (+6)$
- $(-1) + (-3) = (-4)$

#### Addition with Different Signs
The result has the sign of the term with larger absolute value; subtract the absolute values.

**Example:**

- $(-6) + (+4) = (-2)$

---

### Properties of Addition

**Commutative Property:**

- $4 + 2 = 2 + 4$

**Associative Property:**

- $(4 + 2) + 5 = 2 + (4 + 5)$

**Identity Element:**

- $4 + 0 = 4$

**Opposite Element:**

- $(+4) + (-4) = 0$

---

### Subtraction of Integer Numbers

To subtract integer numbers, add to the first number the opposite of the second number.

**Examples:**

- $(+3) - (+5) = (+3) + (-5) = (-2)$
- $(+3) - (-5) = (+3) + (+5) = (+8)$

---

## Rational Numbers

### Set of Rational Numbers

The set of rational numbers is represented by the symbol $\mathbb{Q}$. A number is rational if it can be expressed as a fraction.

**Notation:**

- $\mathbb{Q}$ = rational numbers
- $\mathbb{Q}^+$ = positive rational numbers
- $\mathbb{Q}^-$ = negative rational numbers
- $\mathbb{Q}_0^+$ = non-negative rational numbers
- $\mathbb{Q}_0^-$ = non-positive rational numbers

**Relationship between sets:** All natural numbers and integer numbers are rational ($\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q}$)

---

### Fractions

**What is a fraction?**

A fraction represents parts of a whole. In the fraction $\frac{3}{5}$:
- Numerator: $3$
- Denominator: $5$
- Reading: "three fifths"

**Simplification of fractions**

Divide both terms by the same number. When it's not possible to simplify further, it is an "irreducible fraction".

**Equivalent fractions**

Multiply both terms by the same number to obtain equivalent fractions.

**Ordering fractions**

- Same denominator: larger the one with larger numerator
- Same numerator: larger the one with smaller denominator
- Different: make the denominators equal

**Proper and improper fractions**

Proper: denominator greater than numerator (less than $1$)
Improper: numerator greater than denominator (greater than $1$)

**Decimal fractions**

Denominators $10, 100, 1000$, etc. Conversion to decimals: write the numerator with decimal places according to zeros in the denominator.

---

### Operations with Rational Numbers

#### Addition and Subtraction with Fractions

To add or subtract fractions:
- The fractions must have the same denominator
- Add or subtract the numerators
- The denominator stays the same

**Example:**
$$\frac{-2}{3} + \frac{+5}{4} = \frac{-8}{12} + \frac{+15}{12} = \frac{+7}{12}$$

---

#### Multiplication with Fractions

To multiply fractions:
- It is not necessary to have the same denominator
- Multiply numerator with numerator and denominator with denominator

**Example:**
$$\frac{-2}{3} \times \frac{+5}{4} = \frac{-10}{12}$$

**Sign rules:**

- $(+) \times (+) = (+)$
- $(-) \times (-) = (+)$
- $(+) \times (-) = (-)$
- $(-) \times (+) = (-)$

---

#### Division with Fractions

To divide fractions:
- Transform the division into a multiplication
- Multiply the first fraction by the reciprocal of the second fraction

**Example:**
$$\frac{-2}{3} \div \frac{+4}{5} = \frac{-2}{3} \times \frac{+5}{4} = \frac{-10}{12}$$

---

### Percentage

A percentage is a quotient in which the divisor is $100$.

**Example:**
$25\% = 25 \div 100 = \frac{25}{100}$

**Calculations with percentages:**

- Discover a part: percentage $\times$ whole
- Discover the whole: $100 \times \frac{\text{part}}{\text{percentage}}$

---

### Decimal Expansions

#### Terminating Decimals

Terminating decimals are numbers whose decimal part has an end.

Decimal fractions (whose denominator is $10, 100, 1000, \ldots$) always correspond to terminating decimals.

#### Infinite Repeating Decimals

Present an infinite sequence of digits, where a group of one or more digits repeats.

**Types:**

- Simple or pure repeating decimals: $1,\overline{14}$
- Composite repeating decimals with pre-period: $2,8\overline{3}$

---

### Scientific Notation

Numbers are expressed in the format: $a \times 10^n$, where $1 \leq a < 10$ and $n$ is an integer.

**Example:**
$37000 = 3,7 \times 10^4$

**Comparison between numbers in scientific notation:**

- Equal exponents: larger coefficient = larger number
- Different exponents: larger exponent = larger number

---

## Real Numbers

### Perfect Squares and Square Root

#### Perfect Square

A perfect square is a natural number that results from a power whose base is a natural number and whose exponent is the number $2$.

**Formula:** $n^2 = a$ (where $n$ is a natural number and $a$ is a perfect square)

**Example:** $4^2 = 16$, so $16$ is a perfect square

**First perfect squares:**
$1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, \ldots$

---

#### Square Root

The square root of a number is the factor that squared equals that number.

**Formula:** $\sqrt{a} = b$, if $b^2 = a$

**Examples:**

- $\sqrt{16} = 4 \rightarrow$ because $4^2 = 16$
- $\sqrt{0} = 0 \rightarrow$ because $0^2 = 0$

Square roots of positive integers that are not perfect squares correspond to infinite non-repeating decimals.

**Square of the square root:**
$(\sqrt{a})^2 = a$

**Relationship with square area:**
The side of a square equals the square root of its area: $l = \sqrt{A}$

---

### Perfect Cubes and Cube Root

#### Perfect Cube

A perfect cube is a natural number that results from a power whose base is a natural number and whose exponent is the number $3$.

**Formula:** $n^3 = a$ (where $n$ is a natural number and $a$ is a perfect cube)

**Example:** $4^3 = 64$, so $64$ is a perfect cube

**First perfect cubes:**
$1, 8, 27, 64, 125, \ldots$

---

#### Cube Root

The cube root of a number is the factor that cubed equals that number.

**Formula:** $\sqrt[3]{a} = b$, if $b^3 = a$

**Examples:**

- $\sqrt[3]{27} = 3 \rightarrow$ because $3^3 = 27$
- $\sqrt[3]{0} = 0 \rightarrow$ because $0^3 = 0$

**Cube of the cube root:**
$(\sqrt[3]{a})^3 = a$

**Relationship with cube volume:**
The edge of a cube equals the cube root of its volume: $a = \sqrt[3]{V}$

---

### Real Numbers – Intervals and Order Relation

#### Set of Real Numbers

Real numbers include all rational and irrational numbers.

**Progression of number sets:**
$\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$

**Irrational numbers:** Square roots of numbers that are not perfect squares, cube roots of numbers that are not perfect cubes, and other numbers with infinite non-repeating decimals.

---

#### Intervals of Real Numbers

Intervals can be represented in several ways:
- Interval notation: $[a, b]$, $]a, b[$, $[a, b[$, $]a, b]$
- Representation on the real line
- Set-builder notation: $\{x \in \mathbb{R} : a \leq x \leq b\}$

---

#### Approximate Values

**Three approximation methods:**

- Values by defect (rounding down)
- Values by excess (rounding up)
- Standard rounding based on the first eliminated digit

---

## Powers and Scientific Notation

### Powers with Integer Exponent

#### Powers with Negative Base

**Even exponent:**

- $(-a)^n = a^n$ (when $n$ is even)
- Example: $(-3)^2 = 9$

**Odd exponent:**

- $(-a)^n = -a^n$ (when $n$ is odd)
- Example: $(-3)^3 = -27$

---

#### Special Rules

**Power with exponent 1:**
$a^1 = a$

**Power with exponent 0:**
$a^0 = 1$

**Power with negative exponent:**
$a^{-n} = \left(\frac{1}{a}\right)^n$

**Power with base 1:**
$1^n = 1$

**Power of a power:**
$(a^m)^n = a^{m \times n}$

---

#### Power Rules in Multiplication

**Same base:**
$a^m \times a^n = a^{m + n}$

**Same exponent:**
$a^n \times b^n = (a \times b)^n$

---

#### Power Rules in Division

**Same base:**
$a^m \div a^n = a^{m - n}$

**Same exponent:**
$a^n \div b^n = (a \div b)^n$

---

### Scientific Notation

#### Representation in Scientific Notation

Scientific notation is a way of writing numbers using the power of base $10$.

**Format:** $a \times 10^n$, where $1 \leq a < 10$ and $n$ is an integer

**Conversion process:**
1. Write "$a$" by moving the decimal point so that $1 \leq a < 10$
2. Multiply by the power of base $10$ with exponent equal to the number of moves
   - Positive exponent: decimal point moved to the left
   - Negative exponent: decimal point moved to the right

**Examples:**

- $25600000 = 2,56 \times 10^7$
- $0,00054897 = 5,4897 \times 10^{-4}$

---

#### Comparison and Operations

**Comparison:**

- With different exponents: larger number has larger exponent
- With equal exponents: larger number has larger "$a$" value

**Multiplication:**
$(a_1 \times 10^{n_1}) \times (a_2 \times 10^{n_2}) = (a_1 \times a_2) \times 10^{n_1+n_2}$

**Division:**
$(a_1 \times 10^{n_1}) \div (a_2 \times 10^{n_2}) = (a_1 \div a_2) \times 10^{n_1-n_2}$

---

# ALGEBRA

## Algebraic Expressions

### Fundamental Concepts

**Algebraic expression:**
Expression with letters and numbers related by operations.

**Example:** $2n + 1$

**Terms of an algebraic expression:**

- Are separated by $+$ and $-$ signs
- Are constituted by a coefficient and may have a literal part
- Example: in $2n + 1$:
  - The term $2n$ has coefficient $2$ and literal part $n$
  - The term $1$ has only coefficient $1$

---

### Simplification of Algebraic Expressions

**Simplify an algebraic expression:**
Reduce like terms (that have the same literal part)

**Example:**
$3b + 2b + 5 + 4m - 3 + 4n - 3m = 5b + 2 + m + 4n$

---

### Properties of Operations

#### Properties of Addition and Multiplication

**Commutative Property:**

- Addition: $a + b = b + a$
- Multiplication: $a \times b = b \times a$

**Associative Property:**

- Addition: $(a + b) + c = a + (b + c)$
- Multiplication: $(a \times b) \times c = a \times (b \times c)$

**Identity Element:**

- Addition: $a + 0 = a$
- Multiplication: $a \times 1 = a$

**Absorbing Element:**

- Multiplication: $a \times 0 = 0$

**Inverse Element:**

- Multiplication: $a \times \frac{1}{a} = 1$

**Distributive Property:**

- $a \times (b + c) = a \times b + a \times c$
- $a \times (b - c) = a \times b - a \times c$

---

## Sequences and Patterns

### Basic Concepts

**Numerical Sequence:**
An ordered list of numbers. Each number represents a term; the position is called order.

**Example:** $1, 3, 5, 7$
- $1$ is order $1$
- $3$ is order $2$
- $5$ is order $3$
- $7$ is order $4$

**Succession:**
Infinite sequence – sequence with infinite terms.
Represented as: $1, 3, 5, 7, \ldots$

---

### General Term

**Concept:**
Algebraic expression that relates each term to its order.

**Example:**
For the sequence $1, 3, 5, 7$: the general term is $2n - 1$

**Method to discover the general term:**

When the difference between consecutive terms is constant:
1. Multiply this constant difference by $n$
2. Then adjust as necessary

**Examples:**

*Sequence $2, 4, 6, 8$*

- Constant difference: $2$
- General term: $2n$

*Sequence $3, 5, 7, 9$*

- Constant difference: $2$
- General term: $2n + 1$

---

### Finding Terms from the General Term

**Method:** Substitute $n$ by the order of the desired term

**Examples** (using general term $2n - 1$):

- Order $1$: $2(1) - 1 = 1$
- Order $2$: $2(2) - 1 = 3$
- Order $5$: $2(5) - 1 = 9$

---

## Equations and Inequalities

### Linear Equations

#### Meaning of Equation

**Equation:**
Equality between two numerical expressions in which there exists at least one unknown (letter).

**Example:** $3b + 5 = 11$

---

#### Solution of an Equation

**Solution of an equation:**
Numerical value of the unknown that transforms the equation into a true statement.

**Example:** $3b + 5 = 11$
- $3 \times 2 + 5 = 11 \rightarrow 2$ is a solution

**Solution set:**
Set of solutions of an equation.

**Equivalent equations:**
Have the same solution set.

---

#### Elements of an Equation

- **1st member:** expression to the left of the equals sign
- **2nd member:** expression to the right of the equals sign
- **Unknowns:** letters present in the equation
- **Dependent terms:** terms with unknown
- **Independent terms:** terms without unknown

---

#### Solving Linear Equations

**Addition equivalence principle:**
Adding or subtracting the same expression to both members yields an equivalent equation.

**Multiplication equivalence principle:**
Multiplying or dividing both members by a number different from zero yields an equivalent equation.

**Practical rule:**
Any term can be moved from one member to another by changing its sign.

**Example:**
\begin{align*}
3x + 4 &= x + 10 \Leftrightarrow \\
3x - x &= 10 - 4 \Leftrightarrow \\
2x &= 6 \Leftrightarrow \\
x &= 3
\end{align*}

---

#### Classification of Equations

- **Determinate possible:** $x = 5$ ; S.S. $= \{5\}$
- **Indeterminate possible:** $0x = 0$ ; S.S. $= \mathbb{R}$
- **Impossible:** $0x = 5$ ; S.S. $= \{\}$

---

### Quadratic Equations

#### Solving Quadratic Equations

**Incomplete equations:**
Can be solved through simplification and extraction of square root.

**Completing the square:**
Method to transform the equation into a form where the square root can be extracted.

**Quadratic formula:**
General method to solve any complete quadratic equation.

---

#### Discriminant

The discriminant allows discovering the number of solutions of a quadratic equation without completely solving it.

---

### Inequalities

**Inequality:**
Inequality between two numerical expressions in which there exists at least one unknown.

**Solving inequalities:**
A process similar to equations is applied, but with attention to the direction of inequality when multiplying or dividing by a negative number.

**Conjunction and disjunction of inequalities:**

- Conjunction: intersection of solutions
- Disjunction: union of solutions

---

## Functions

### Concept of Function

**Definition:**
Correspondence between two sets in which to each element of the domain set corresponds one and only one element of the range set.

**Terminology:**

- **Objects:** elements of the domain set
- **Images:** elements of the range set with correspondence
- **Domain ($D$):** set of objects
- **Range ($D'$):** set of images
- **Independent variable:** represents the objects (usually $x$)
- **Dependent variable:** represents the images (usually $y$)

---

### Forms of Representation

Functions can be represented through:
- Arrow diagram
- Table
- Algebraic expression
- Graph
- Cartesian coordinate system

---

### Variation of Functions

- **Increasing:** the dependent variable increases when the independent variable increases
- **Constant:** the dependent variable remains unchanged
- **Decreasing:** the dependent variable decreases when the independent variable increases

---

### Direct Proportionality Function

**Directly proportional quantities:** have a constant ratio.

**Form:** $f(x) = kx$, where $k$ is the constant of direct proportionality.

**The constant $k$:**

- Equals $f(1)$
- Is calculated as $k = f(x) \div x$
- If $k > 0$: the function is increasing
- If $k < 0$: the function is decreasing

**Graphical Representation:**
Line that passes through the origin of the coordinate system.

---

### Linear Function

**Form:** $f(x) = ax + b$

**Special cases:**

- Linear function: $b = 0$, that is, $f(x) = ax$
- Constant function: $a = 0$, that is, $f(x) = b$

**Elements:**

- **Slope ($a$):** angular coefficient
- **Y-intercept ($b$):** linear coefficient

**Graphical representation:**
Non-vertical line.

---

### Inverse Proportionality Function

**Form:** $f(x) = \frac{k}{x}$, where $k$ is the constant of inverse proportionality.

**Characteristics:**

- Graph: hyperbola
- Domain: $\mathbb{R} \setminus \{0\}$

---

### Quadratic Function

**Form:** $f(x) = ax^2$, where $a \neq 0$

**Characteristics:**

- Graph: parabola
- If $a > 0$: parabola with concavity facing upward
- If $a < 0$: parabola with concavity facing downward

---

# GEOMETRY

## Basic Elements

### Angles

#### Classification of Angles by Amplitude

- **Acute:** between $0°$ and $90°$
- **Right:** $90°$
- **Obtuse:** between $90°$ and $180°$
- **Straight:** $180°$
- **Full rotation:** $360°$

---

#### Pairs of Angles

- **Complementary:** whose sum is $90°$
- **Supplementary:** whose sum is $180°$
- **Alternate interior/exterior:** formed by a transversal on two lines, on opposite sides
- **Vertically opposite:** have the same vertex and the sides of one are in the extension of the sides of the other

**Properties:**

- Vertically opposite angles are equal
- Alternate interior angles are equal when the lines are parallel

---

#### Angle Measurement

**Unit of measurement:**

- Degree $(°)$
- The full rotation angle has amplitude equal to $360$ degrees

**Subdivisions:**

- $1$ degree $= 60$ minutes $(')$
- $1$ minute $= 60$ seconds $(")$

---

### Parallelism and Perpendicularity

**Parallel lines:**
Lines that do not intersect.

**Perpendicular lines:**
Lines that form right angles.

**Properties:**

- Corresponding angles are equal when the lines are parallel
- Alternate interior and exterior angles are equal when the lines are parallel

---

## Plane Figures

### Triangles

#### Classification by Sides

- **Equilateral:** three equal sides
- **Isosceles:** two equal sides
- **Scalene:** three different sides

---

#### Classification by Angles

- **Acute-angled:** three acute angles
- **Right-angled:** one right angle
- **Obtuse-angled:** one obtuse angle

---

#### Properties of Triangles

**Sum of interior angles:**
The sum of the interior angles of a triangle equals $180°$.

**Elements of a right triangle:**

- **Hypotenuse:** side opposite the right angle
- **Legs:** sides adjacent to the right angle

**Triangle inequality:**
The measure of the length of any side is less than the sum of the measures of the lengths of the other two and greater than their respective difference.

---

#### Criteria for Congruence of Triangles

- **SSS:** Three equal sides
- **SAS:** Two sides and the angle formed by them equal
- **ASA:** Two angles and the side between them equal

---

### Quadrilaterals

#### Types of Quadrilaterals

**Parallelogram:**
Opposite sides parallel and equal; opposite angles equal.

**Rhombus:**
Parallelogram quadrilateral; all sides equal.

**Rectangle:**
Parallelogram quadrilateral; all angles equal (right).

**Square:**
All sides equal; all angles equal (right).

**Kite:**
Two pairs of consecutive equal sides.

**Trapezoid:**
Quadrilateral with at least two parallel sides.

---

#### Properties of Diagonals

- **Parallelogram:** bisect each other
- **Rhombus:** bisect each other and are perpendicular
- **Rectangle:** bisect each other and are equal
- **Square:** bisect each other, are perpendicular and equal
- **Kite:** are perpendicular

---

### Polygons

#### Angles of a Convex Polygon

**Formulas:**

- $S_i = (n - 2) \times 180°$ (sum of interior angles)
- $S_e = 360°$ (sum of exterior angles)
- $a_i = \frac{(n - 2) \times 180°}{n}$ (interior angle)
- $a_e = \frac{360°}{n}$ (exterior angle)
- $a_i + a_e = 180°$

---

### Circumference and Circle

**Elements of the circumference:**

- **Center:** fixed point
- **Radius:** distance from the center to any point on the circumference
- **Diameter:** segment that passes through the center and has endpoints on the circumference
- **Chord:** segment with endpoints on the circumference
- **Arc:** part of the circumference between two points

**Properties:**

- Diameter $= 2 \times$ radius
- Perimeter of the circumference $= \pi \times$ diameter $= 2 \times \pi \times$ radius
- $\pi \approx 3,1416$

---

#### Angles in the Circumference

**Central angle:**
Angle with vertex at the center.

**Inscribed angle:**
Angle with vertex on the circumference.

**Circular sector:**
Intersection of a central angle with the circle.

---

### Loci

**Circumference:**
Locus of points that are at a fixed distance from a point (center).

**Circle:**
Locus of points that are at a distance less than or equal to a fixed value from a point (center).

**Perpendicular bisector:**
Locus of points equidistant from the endpoints of a segment.

**Angle bisector:**
Locus of points equidistant from two sides of an angle.

---

## Geometric Transformations

### Isometries

**Isometry:**
Geometric transformation that preserves distances.

---

#### Central Reflection

A point $M'$ is the image of $M$ in a central reflection with center $O$ when $O$ is the midpoint of segment $[MM']$.

**Properties:**

- Preserves segment lengths
- Preserves angle measures

---

#### Axial Reflection

A point $M'$ is the image of $M$ in an axial reflection with axis $r$ when $r$ is the perpendicular bisector of segment $[MM']$.

**Properties:**

- Preserves segment lengths
- Preserves angle measures

**Axis of symmetry:**
Line that divides a figure into two parts that are images of each other by axial reflection.

---

#### Rotation

A point $M'$ is the image of $M$ by a rotation with center $O$ and angle $\alpha$ when:

- The segments $[OM]$ and $[OM']$ have equal length
- The angle $M\hat{O}M'$ has measure $\alpha$

**Properties:**

- Preserves segment lengths
- Preserves angle measures

---

#### Translation

A translation is defined by a vector that indicates:

- Direction
- Sense
- Length

**Properties:**

- Preserves segment lengths
- Preserves angle measures
- Preserves parallelism

---

### Similarities

**Similar figures:**

- Have the same shape
- Distances between pairs of corresponding points are directly proportional

---

#### Similar Polygons

**Properties:**

- Corresponding angles equal
- Corresponding sides directly proportional

**Similarity ratio ($r$):**
Constant of proportionality between the length of corresponding sides.

**Classification:**

- **Enlargement:** $r > 1$
- **Reduction:** $0 < r < 1$
- **Isometry:** $r = 1$

---

#### Relationship between Perimeters and Areas

**Perimeters:**
Perimeter of similar figure $=$ Original perimeter $\times r$

**Areas:**
Area of similar figure $=$ Original area $\times r^2$

---

#### Criteria for Similarity of Triangles

**AA Criterion (Angle-Angle):**
Two equal corresponding angles determine similarity.

**SSS Criterion (Side-Side-Side):**
Three directly proportional sides determine similarity.

**SAS Criterion (Side-Angle-Side):**
Two directly proportional sides and the corresponding angle equal determine similarity.

---

## Geometric Solids

### Polyhedra

**Polyhedron:**
Solid with only flat faces.

**Elements:**

- **Faces:** polygons that bound the polyhedron
- **Edges:** segments of intersection of two faces
- **Vertices:** points of intersection of three or more edges

---

#### Regular Polyhedra (Platonic)

Solid whose faces are equal regular polygons and each vertex is common to the same number of faces.

**Five regular polyhedra:**

- **Tetrahedron:** $4$ triangular faces
- **Cube:** $6$ quadrangular faces
- **Octahedron:** $8$ triangular faces
- **Dodecahedron:** $12$ pentagonal faces
- **Icosahedron:** $20$ triangular faces

---

#### Euler's Formula

$$V + F = A + 2$$

Where:

- $V =$ number of vertices
- $F =$ number of faces
- $A =$ number of edges

---

### Prisms

**Prism:**
Polyhedron with two geometrically equal faces (bases) situated in parallel planes.

**In a prism with base of $n$ sides:**

- Number of vertices $= 2n$
- Number of edges $= 3n$
- Number of faces $= n + 2$

**Right prism:**
Lateral edges perpendicular to the bases.

**Regular prism:**
Right prism with bases that are regular polygons.

---

### Pyramids

**Pyramid:**
Polyhedron determined by a polygon (base) and a point exterior to the plane of the base (vertex).

**In a pyramid with base of $n$ sides:**

- Number of vertices $= n + 1$
- Number of edges $= 2n$
- Number of faces $= n + 1$

**Regular pyramid:**
Base is a regular polygon and lateral edges are all equal.

---

### Cylinders

**Cylinder:**
Solid determined by two circles with equal radius in parallel planes.

**Elements:**

- **Bases:** the two circles
- **Axis:** segment that joins the centers of the bases
- **Generators:** segments that join points of the circumferences of the bases
- **Lateral surface:** union of all generators

**Right cylinder:**
Axis perpendicular to the radii of the bases.

---

### Cones

**Cone:**
Solid determined by a circle (base) and a point exterior to the plane of the base (vertex).

**Elements:**

- **Base:** circle
- **Vertex:** point exterior to the plane of the base
- **Axis:** segment that joins the vertex to the center of the base
- **Generators:** segments that join the vertex to points of the circumference of the base
- **Lateral surface:** union of all generators

**Right cone:**
Axis perpendicular to the radius of the base.

---

### Sphere

**Sphere:**
Solid constituted by all points in space that are at a distance less than or equal to a fixed value (radius) from a point (center).

**Spherical surface:**
Set of points in space that are at a distance equal to the radius from the center.

---

## Trigonometry

### Pythagorean Theorem

**Statement:**
In a right triangle, the square of the hypotenuse equals the sum of the squares of the legs.

**Formula:**
$$a^2 + b^2 = c^2$$

Where:

- $c =$ hypotenuse
- $a, b =$ legs

---

#### Converse of the Pythagorean Theorem

If in a triangle the square of one side equals the sum of the squares of the other two sides, then the triangle is right-angled.

---

#### Pythagorean Triples

Set of three natural numbers $(a, b, c)$ that satisfy $a^2 + b^2 = c^2$.

**Examples:**

- $(3, 4, 5)$
- $(5, 12, 13)$
- $(8, 15, 17)$

---

#### Pythagorean Theorem in Space

Application of the Pythagorean Theorem to the calculation of space diagonals in geometric solids.

---

### Trigonometric Ratios

#### Definitions

In a right triangle with an acute angle $\alpha$:

**Sine:**
$$\sin \alpha = \frac{\text{opposite leg}}{\text{hypotenuse}}$$

**Cosine:**
$$\cos \alpha = \frac{\text{adjacent leg}}{\text{hypotenuse}}$$

**Tangent:**
$$\tan \alpha = \frac{\text{opposite leg}}{\text{adjacent leg}}$$

---

#### Relations between Trigonometric Ratios

**Fundamental relation:**
$$\sin^2\alpha + \cos^2\alpha = 1$$

**Tangent:**
$$\tan \alpha = \frac{\sin \alpha}{\cos \alpha}$$

**Complementary angles:**

- $\sin \alpha = \cos (90° - \alpha)$
- $\cos \alpha = \sin (90° - \alpha)$

---

#### Exact Values

**Angle of $30°$:**

- $\sin 30° = \frac{1}{2}$
- $\cos 30° = \frac{\sqrt{3}}{2}$
- $\tan 30° = \frac{\sqrt{3}}{3}$

**Angle of $45°$:**

- $\sin 45° = \frac{\sqrt{2}}{2}$
- $\cos 45° = \frac{\sqrt{2}}{2}$
- $\tan 45° = 1$

**Angle of $60°$:**

- $\sin 60° = \frac{\sqrt{3}}{2}$
- $\cos 60° = \frac{1}{2}$
- $\tan 60° = \sqrt{3}$

---

# MEASUREMENT

## Area

### Fundamental Concepts

**Area:**
Measure of the surface of a plane figure.

**Units of measurement:**

- $\text{m}^2$ (square meter)
- $\text{cm}^2$ (square centimeter)
- $\text{mm}^2$ (square millimeter)
- $\text{km}^2$ (square kilometer)

---

### Area Formulas

#### Basic Figures

**Triangle:**
$$A = \frac{\text{base} \times \text{height}}{2}$$

**Square:**
$$A = \text{side} \times \text{side} = \text{side}^2$$

**Rectangle:**
$$A = \text{length} \times \text{width}$$

**Parallelogram:**
$$A = \text{base} \times \text{height}$$

---

#### Special Quadrilaterals

**Rhombus and Kite:**
$$A = \frac{\text{Major diagonal} \times \text{minor diagonal}}{2}$$

**Trapezoid:**
$$A = \frac{\text{Major base} + \text{minor base}}{2} \times \text{height}$$

---

#### Regular Polygons and Circle

**Regular polygon:**
$$A = \frac{\text{Perimeter}}{2} \times \text{apothem}$$

**Circle:**
$$A = \pi \times \text{radius}^2$$

**Circular sector:**
$$A = \frac{\pi \times \text{radius}^2 \times \text{angle measure}}{360°}$$

---

### Construction of Formulas

**Area of rectangle:**
Recognize that the area of a rectangle with sides $q$ and $r$ equals $q \times r$ square units.

**Area of parallelogram:**
Recognize that a parallelogram with base $b$ and height $a$ has area $= b \times a$.

**Area of triangle:**
Recognize that a triangle with base $b$ and height $a$ has area $= \frac{b \times a}{2}$.

---

## Volume

### Fundamental Concepts

**Volume:**
Measure of the space occupied by a solid.

**Units of measurement:**

- $\text{m}^3$ (cubic meter)
- $\text{cm}^3$ (cubic centimeter)
- $\text{mm}^3$ (cubic millimeter)
- $\text{L}$ (liter) $= \text{dm}^3$

---

### Volume Formulas

#### Prisms

**Prism (general):**
$$V = \text{base area} \times \text{height}$$

**Rectangular parallelepiped:**
$$V = \text{length} \times \text{width} \times \text{height}$$

**Cube:**
$$V = \text{edge}^3$$

---

#### Pyramids

**Pyramid:**
$$V = \frac{\text{base area} \times \text{height}}{3}$$

---

#### Cylinders

**Cylinder:**
$$V = \text{base area} \times \text{height} = \pi \times \text{radius}^2 \times \text{height}$$

---

#### Cones

**Cone:**
$$V = \frac{\text{base area} \times \text{height}}{3} = \frac{\pi \times \text{radius}^2 \times \text{height}}{3}$$

---

#### Sphere

**Sphere:**
$$V = \frac{4 \times \pi \times \text{radius}^3}{3}$$

---

### Surface Areas of Solids

#### Prisms and Pyramids

**Prism:**
Total area $=$ area of two bases $+$ lateral surface area

**Pyramid:**
Total area $=$ base area $+$ lateral surface area

---

#### Cylinders and Cones

**Cylinder:**
$$\text{Total area} = 2 \times \pi \times \text{radius}^2 + 2 \times \pi \times \text{radius} \times \text{height}$$

**Cone:**
$$\text{Total area} = \pi \times \text{radius}^2 + \pi \times \text{radius} \times \text{slant height}$$

---

#### Sphere

**Spherical surface:**
$$A = 4 \times \pi \times \text{radius}^2$$

---

# DATA ORGANIZATION AND PROCESSING

## Data Representation

### Basic Concepts

**Statistical population:**
Set of elements about which one or more common characteristics are to be studied.

**Statistical sample:**
Part of the population about which data are collected; must be representative of the population.

**Statistical variable:**
Characteristic that takes different values.

---

### Types of Variables

**Quantitative variable:**

- **Discrete:** counting (number of siblings)
- **Continuous:** measurement (height)

**Qualitative variable:**

- **Nominal:** categories without order (eye color)
- **Ordinal:** categories with order (qualifications)

---

### Data Collection and Organization

**Census:**
Statistical study that involves the observation of all elements of the population.

**Survey:**
Statistical study that involves the observation of elements of a sample.

**Data organized in classes:**
When there is great variability of values, they are grouped into classes with a certain range.

---

### Forms of Representation

**Tables:**

- Table of absolute and relative frequencies

**Graphs:**

- Cartesian graphs
- Pictograms
- Stem-and-leaf diagram
- Bar graph
- Pie chart
- Line graph/graphs
- Juxtaposed bar graph
- Stacked bar graph
- Histograms

---

## Statistics

### Measures of Central Location

**Arithmetic mean ($\bar{x}$):**
Calculated by adding all values of a data set and dividing that sum by the number of elements in that set.

**Mode ($M_o$):**
Value with highest frequency.

**Median ($M_e$):**

- If the number of data is odd: data in the central position, with data placed in order
- If the number of data is even: arithmetic mean of the data in the two central positions

---

### Measures of Dispersion

**Range:**
Difference between the maximum value and the minimum value.

---

### Example

Data: $1, 1, 2, 3, 3, 4$

- $\bar{x} = (2 \times 1 + 2 + 2 \times 3 + 4) \div 6 = 14 \div 6 \approx 2,3$
- $M_o = 1$ and $3$
- $M_e = (2 + 3) \div 2 = 2,5$
- Range $= 4 - 1 = 3$

---

### Histograms

**Characteristics:**

- Classes on the abscissa axis
- Frequencies on the ordinate axis
- Juxtaposed rectangular bars
- Area proportional to absolute frequency

**Modal class:**
Class with highest absolute frequency.

---

## Probability

### Random Experiments

**Deterministic experiment:**
Allows predicting the result, having only one possible case.

**Random experiment:**
Depends on luck and chance, presenting a set of possible cases called the outcome space or sample space ($\Omega$).

**Example:**
Roll a die: $\Omega = \{1, 2, 3, 4, 5, 6\}$ with $\#\Omega = 6$

---

### Events

**Event:**
Subset of the outcome space.

**Classification:**

- **Elementary:** constituted by a single element
- **Compound:** constituted by two or more elements
- **Certain:** contains all elements of the outcome space
- **Impossible:** does not contain any element ($\emptyset$)

---

### Operations with Events

**Union ($A \cup B$):**
Outcomes that belong to at least one of events $A$ or $B$.

**Intersection ($A \cap B$):**
Outcomes that belong simultaneously to $A$ and $B$.

**Compatible events:**
Have at least one element in common ($A \cap B \neq \emptyset$).

**Incompatible events:**
Have no elements in common ($A \cap B = \emptyset$).

**Complementary or contrary events:**
$A \cap B = \emptyset \land A \cup B = \Omega$

The complement of $A$ is represented by $\bar{A}$.

---

### Probability

**Probability scale:**
The probability of an event varies between $0$ and $1$ (or $0\%$ and $100\%$).

$$0 \leq P(A) \leq 1 \text{ or } 0\% \leq P(A) \leq 100\%$$

**Classification:**

- **Certain event:** $P(A) = 1$ (or $100\%$)
- **Impossible event:** $P(A) = 0$ (or $0\%$)
- **Equally likely events:** have the same probability

---

### Calculating Probability

**Laplace's Law:**

$$P(A) = \frac{\text{number of favorable cases to } A}{\text{number of possible cases}}$$

**Example:**
Roll a die. Event $A$ "face with multiple of $5$ appears" $= \{5\}$

$$P(A) = \frac{1}{6} \approx 0,167 \approx 16,7\%$$

---

### Probability of Compound Events

The probability of a compound event equals the sum of the probabilities of the elementary events that compose it.

**Example:**
"Multiple of $3$ appears" when rolling a die $= \{3, 6\}$

$$P = \frac{1}{6} + \frac{1}{6} = \frac{2}{6} = \frac{1}{3}$$

---

### Auxiliary Counting Schemes

**Venn diagram:**
Useful for experiments with a single action and for visualizing union and intersection.

**Two-way table:**
Useful for experiments with two actions.

**Tree diagram:**
Useful for experiments with two or more actions.

---

### Law of Large Numbers

When an experiment is repeated a high number of times, the relative frequency of an event tends to approach the probability value of that event:

$$F_r(A) \approx P(A)$$

The greater the number of repetitions, the closer the value of relative frequency will be to the probability.

---

**Content adapted from O Bichinho do Saber (www.obichinhodosaber.com)**
