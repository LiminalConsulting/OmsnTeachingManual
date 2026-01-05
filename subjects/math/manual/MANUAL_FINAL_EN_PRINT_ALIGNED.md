# Mathematics Manual: Grades 5-9
## Thematic Organization

This manual presents essential mathematics content for grades 5-9, organized by mathematical themes rather than by grade level. This approach provides an integrated view of conceptual progression, facilitating understanding of the natural evolution of concepts throughout the five years.

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

### DATA ORGANIZATION AND TREATMENT
- Data Representation
- Statistics
- Probability


\cleardoublepage

# NUMBERS

# Natural Numbers

### NATURAL NUMBERS

#### SET OF NATURAL NUMBERS

The set of natural numbers is represented by ℕ and begins with: 1, 2, 3, 4, 5, 6, …

ℕ = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, …}

**Important note:** the set of natural numbers is infinite.

### MULTIPLES AND DIVISORS

#### Divisible numbers, multiples and divisors

A number is **divisible** by another if the division results in zero remainder.

**Examples:**
- 10 : 2 = 5 (remainder 0) → 10 is divisible by 2
- 10 : 3 = 3 (remainder 1) → 10 is not divisible by 3

If a number is divisible by another, it is also its **multiple**.
If a number divides another exactly, it is its **divisor**.

**From the division 10 : 2 = 5 (remainder 0):**
- 10 is divisible by 2 and by 5
- 10 is a multiple of 2 and of 5
- 2 and 5 are divisors of 10

#### Divisibility Criteria

A number is divisible by:

**2** if it is even (ends in 0, 2, 4, 6 or 8)
- 4565 is not divisible by 2
- 6548 is divisible by 2

**3** if the sum of its digits is a multiple of 3
- 548 (5+4+8=17) is not divisible by 3
- 85461 (8+5+4+6+1=24) is divisible by 3

**4** if it ends in 00 or the last two digits form a multiple of 4
- 45425 (ends in 25) is not divisible by 4
- 54536 (ends in 36, a multiple of 4) is divisible by 4
- 454500 (ends in 00) is divisible by 4

**5** if it ends in 0 or 5
- 5648 is not divisible by 5
- 5640 (ends in 0) is divisible by 5
- 8465 (ends in 5) is divisible by 5

**6** if it is divisible by both 2 and 3
- 491 is not divisible by 6
- 4624 is even but 4+6+2+4=16 (not a multiple of 3), not divisible by 6
- 1596 is even and 1+5+9+6=21 (a multiple of 3), is divisible by 6

**9** if the sum of its digits is a multiple of 9
- 548 (5+4+8=17) is not divisible by 9
- 85464 (8+5+4+6+4=27) is divisible by 9

**10** if it ends in 0
- 154 is not divisible by 10
- 450 is divisible by 10

#### Determining Multiples and Divisors

**Multiples:** multiply the number by 0, 1, 2, 3, 4, …

**Multiples of 4:**
- 4 × 0 = 0
- 4 × 1 = 4
- 4 × 2 = 8
- 4 × 3 = 12
- 4 × 4 = 16
- 4 × 5 = 20
- 4 × 6 = 24
- 4 × 7 = 28

Multiples of 4 = {0, 4, 8, 12, 16, 20, 24, 28, …}

**Notes:**
- The set of multiples is infinite
- The number 0 is a multiple of any number

**Divisors:** divide the number by 1 up to itself, checking for zero remainder.

**Divisors of 10:**
- 10 : 1 = 10 (remainder 0) ✓
- 10 : 2 = 5 (remainder 0) ✓
- 10 : 3 = 3 (remainder 1) ✗
- 10 : 4 = 2 (remainder 2) ✗
- 10 : 5 = 2 (remainder 0) ✓
- 10 : 6 = 1 (remainder 4) ✗
- 10 : 7 = 1 (remainder 3) ✗
- 10 : 8 = 1 (remainder 2) ✗
- 10 : 9 = 1 (remainder 1) ✗
- 10 : 10 = 1 (remainder 0) ✓

Divisors of 10 = {1, 2, 5, 10}

**Notes:**
- The set of divisors is finite
- The number 1 is a divisor of any number

#### Properties of Divisors

**Property 1:** In a product, a divisor of one factor is also a divisor of the product.
- 15 × 4 = 60
- 3 is a divisor of 15, therefore it is a divisor of 60
- 2 is a divisor of 4, therefore it is a divisor of 60

**Property 2:** If a number divides two numbers, it also divides their sum and difference.
- 14 + 10 = 24 | 14 – 10 = 4
- 2 divides 14 and 10, therefore it divides 24 and 4

**Property 3:** In an integer division, if a number divides the divisor and the remainder, it also divides the dividend.
- 14 : 10 = 1 (remainder 4)
- 2 divides 10 and 4, therefore it divides 14

**Property 4:** In an integer division, if a number divides the dividend and the divisor, it also divides the remainder.
- 14 : 10 = 1 (remainder 4)
- 2 divides 14 and 10, therefore it divides 4

### LEAST COMMON MULTIPLE AND GREATEST COMMON DIVISOR

#### Least Common Multiple (LCM)

The **least common multiple** is the smallest number that is a multiple of two or more numbers (not counting zero).

**Least common multiple of 4 and 10:**
- Multiples of 10 = {0, 10, **20**, …}
- Multiples of 4 = {0, 4, 8, 12, 16, **20**, …}

LCM (4, 10) = **20**

#### Greatest Common Divisor (GCD)

The **greatest common divisor** is the largest number that divides two or more numbers.

**Greatest common divisor of 4 and 10:**
- Divisors of 10 = {1, **2**, 5, 10}
- Divisors of 4 = {1, **2**, 4}

GCD (4, 10) = **2**

#### Euclidean Algorithm

Method for determining the greatest common divisor of two numbers:

1. Divide the larger number by the smaller one
2. Make a new division: the previous divisor becomes the dividend, the previous remainder becomes the divisor
3. Repeat until remainder 0 is obtained; that divisor is the GCD

**Greatest common divisor of 30 and 50:**
- 50 : 30 = 1 (remainder 20)
- 30 : 20 = 1 (remainder 10)
- 20 : 10 = 2 (remainder 0) ← **10 is the GCD**

GCD (30, 50) = **10**

#### Finding Common Divisors using GCD

Determine the GCD, then find all divisors of the GCD.

**Common divisors of 30 and 50:**
- GCD (30, 50) = 10
- Divisors of 10 = {1, 2, 5, 10}

Common divisors of 30 and 50 = {1, 2, 5, 10}

#### Relationship between LCM and GCD

**a × b = GCD (a, b) × LCM (a, b)**

#### Problems with LCM and GCD

**Problem type 1 - When asking for maximum number of divisions:**

*Maria has 24 daisies, 16 tulips and 20 roses. What is the maximum number of equal bouquets? What is the composition?*

- Divisors of 24 = {1, 2, 3, **4**, 6, 8, 24}
- Divisors of 16 = {1, 2, **4**, 8}
- Divisors of 20 = {1, 2, **4**, 5, 10}
- GCD (24, 16, 20) = **4**

Maximum number of bouquets = **4**

Composition of each bouquet:
- Daisies: 24 : 4 = **6**
- Tulips: 16 : 4 = **4**
- Roses: 20 : 4 = **5**

**Problem type 2 - When asking for coincidence of events:**

*The Octopus Festival occurs every 6 years; the Sardine Festival every 8 years. Both in 2010. When will they repeat together?*

- Multiples of 6 = {0, 6, 12, 18, **24**, …}
- Multiples of 8 = {0, 8, 16, **24**, …}
- LCM (6, 8) = **24**

They repeat every 24 years: 2010 + 24 = **2034**

### RELATIVELY PRIME NUMBERS

#### Prime Numbers and Composite Numbers

**Prime number:**
- Has only two divisors: 1 and itself
- 5 is prime (divisors: 1, 5)

**Composite number:**
- Has more than two divisors
- 6 is composite (divisors: 1, 2, 3, 6)

**Note:** The number 1 has only one divisor, therefore it is neither prime nor composite.

#### Relatively Prime Numbers

Two numbers are **relatively prime** if their GCD equals 1.

**Are the numbers 8 and 21 relatively prime?**
- Divisors of 21 = {**1**, 3, 7, 21}
- Divisors of 8 = {**1**, 2, 4, 8}
- GCD (8, 21) = **1**

**Yes**, 8 and 21 are relatively prime.

**Important notes:**
- Dividing two numbers by their GCD yields two relatively prime numbers
- A fraction with numerator and denominator that are relatively prime is irreducible

### MATERIALS AND RESOURCES

**Summary available in PDF file (pages 3 and 4)**
Video summary and PDF file provided by RjasMatemática.

### CURRICULUM COMPETENCIES - 5TH GRADE

**DOMAIN: NUMBERS AND OPERATIONS**

**SUBDOMAIN: NATURAL NUMBERS**

Know and apply properties of divisors:
1. Divisibility criteria by 3, 4 and 9
2. Identify GCD by inspection of divisors
3. In a product, a divisor of one factor is a divisor of the product
4. If a number divides two numbers, it divides their sum and difference
5. Integer division: if it divides the divisor and remainder, it divides the dividend
6. Integer division: if it divides the dividend and divisor, it divides the remainder
7. Use Euclidean algorithm for common divisors and GCD
8. Designate as "relatively prime" two numbers with GCD = 1
9. Dividing two numbers by their GCD yields relatively prime numbers
10. An irreducible fraction has numerator and denominator that are relatively prime
11. Identify LCM by inspection of multiples
12. Product of two numbers = GCD × LCM; use to determine one knowing the other

Solve problems:
- Involving calculation of GCD and LCM of two or more natural numbers

### NATURAL NUMBERS

#### DECOMPOSITION OF NUMBERS INTO PRIME FACTORS

##### Prime numbers and composite numbers

**Composite numbers**
- Have more than two divisors

**Prime numbers**
- Have only two divisors (1 and themselves)

*Note: the number 1 has only one divisor (itself), therefore it is neither composite nor prime.*

**Practical examples:**

The number 10:
- Divisors of 10 = {1, 2, 5, 10}
- Has four divisors, therefore it is **composite**

The number 11:
- Divisors of 11 = {1, 11}
- Has only two divisors, therefore it is **prime**

##### Sieve of Eratosthenes

"The Sieve of Eratosthenes is a practical method for finding prime numbers."

Procedure to discover prime numbers up to 100:

1. Write in a table the numbers from 1 to 100
2. Cross out 1
3. Cross out all multiples of 2 greater than 2 (4, 6, 8,…)
4. Cross out all multiples of 3 greater than 3 (3, 6, 9,…)
5. Cross out all multiples of 5 greater than 5 (5, 10, 15,…)
6. Cross out all multiples of 7 greater than 7 (7, 14, 21,…)

The numbers that were not crossed out are the prime numbers up to 100.

##### Fundamental theorem of arithmetic

"Given a natural number greater than 1, there exists a unique increasing sequence of prime numbers whose product equals that number."

**Example:**
90 = 2 × 3 × 3 × 5

When there are repeated prime factors, exponentiation can be used:
- 3 × 3 = 3²
- Therefore: 90 = 2 × 3² × 5

##### Decomposition of a number into prime factors

Practical method:

1. Divide the number by its smallest prime divisor
2. Divide the quotient by its smallest prime divisor, successively until quotient 1 is obtained
3. The initial number equals the product of the divisors used

**Example - Decomposition of the number 630:**
630 = 2 × 3 × 3 × 5 × 7 = 2 × 3² × 5 × 7

**Finding divisors through prime factorization**

1. Decompose the number into prime factors
2. Multiply the prime factors together in all possible ways
3. The number 1, the prime factors, and the results are all divisors

**Example - Divisors of 90:**
90 = 2 × 3 × 3 × 5

Possible multiplications:
- 2 × 3 = 6
- 2 × 5 = 10
- 3 × 3 = 9
- 3 × 5 = 15
- 2 × 3 × 3 = 18
- 2 × 3 × 5 = 30
- 3 × 3 × 5 = 45
- 2 × 3 × 3 × 5 = 90

Divisors of 90 = {1, 2, 3, 5, 6, 9, 10, 15, 18, 30, 45, 90}

#### GREATEST COMMON DIVISOR AND LEAST COMMON MULTIPLE

##### Greatest common divisor (GCD)

To determine the greatest common divisor of two or more numbers:

1. Decompose the numbers into prime factors
2. "The GCD will equal the product of the common prime factors with the smallest exponent"

**Example:**
- 630 = 2 × 3² × 5 × 7
- 100 = 2² × 5²
- GCD (630, 100) = 2 × 5 = 10

**Using Venn diagram:**

1. Decompose the numbers into prime factors
2. Arrange the factors in the diagram (common factors in the intersection)
3. "The GCD will equal the product of the factors that are inside the intersection"

**Example with diagram:**
- 630 = 2 × 3 × 3 × 5 × 7
- 100 = 2 × 2 × 5 × 5
- GCD (630, 100) = 2 × 5 = 10

**Simplifying fractions with greatest common divisor**

1. Determine the GCD between numerator and denominator
2. Divide both by the GCD to obtain an irreducible fraction

*Note: if GCD = 1, the numbers are relatively prime and the fraction is already irreducible.*

**Example:**
- 24 = 2 × 2 × 2 × 3
- 36 = 2 × 2 × 3 × 3
- GCD (24, 36) = 2 × 2 × 3 = 12
- 24 : 12 = 2
- 36 : 12 = 3
- Therefore: 24/36 = 2/3

##### Least common multiple (LCM)

Determination through prime factorization:

1. Decompose the numbers into prime factors
2. "The LCM will equal the product of the common prime factors with the largest exponent and the non-common factors"

**Example:**
- 630 = 2 × 3² × 5 × 7
- 100 = 2² × 5²
- LCM (630, 100) = 2² × 5² × 3² × 7 = 4 × 25 × 9 × 7 = 6300

**Using Venn diagram:**

1. Decompose the numbers into prime factors
2. Arrange the factors in the diagram
3. "The LCM will equal the product of all factors arranged in both circles"

**Example:**
- 630 = 2 × 3 × 3 × 5 × 7
- 100 = 2 × 2 × 5 × 5
- LCM (630, 100) = 2 × 5 × 3 × 3 × 7 × 2 × 5 = 6300

##### Problems with LCM and GCD

**When asking to divide by the maximum number**

The greatest common divisor is used for problems that ask for the maximum number of something through division.

**Practical example:**

"Maria has 24 daisies, 16 tulips and 20 roses. What is the maximum number of equal bouquets can she make? What is the composition of each bouquet?"

- GCD (24, 16, 20) = 4
- Maximum number of bouquets: 4
- Composition: 6 daisies, 4 tulips, 5 roses per bouquet

**When asking after how much time events will happen simultaneously again**

The least common multiple is used.

**Practical example:**

"In a village, the Octopus Festival is held every 6 years, and the Sardine Festival every 8 years. They were held in 2010. When will they be held in the same year again?"

- LCM (6, 8) = 24
- Answer: 2010 + 24 = 2034

### EDUCATIONAL RESOURCES

**Summary in PDF file:** available for download

**Video summary and PDF:** provided by RjasMatemática (www.matexplica.pt)

### EXERCISES

**Worksheet 1** - problems and solutions (www.matexplica.pt)

**Worksheet 2** - problems and solutions (www.matexplica.pt)

**Online exercises:**
- Sieve of Eratosthenes (hypatiamat.com)
- Decomposition into prime factors (hypatiamat.com)

**Other resources:**
- Prime factorization calculator (matematicadidatica.com.br)

### COMPETENCIES ACCORDING TO PROGRAM AND CURRICULUM GOALS

**DOMAIN: NUMBERS AND OPERATIONS (NO6)**
**SUBDOMAIN: NATURAL NUMBERS**

**Know and apply properties of prime numbers:**

1. Identify a prime number as a natural number greater than 1 that has exactly two divisors: 1 and itself.

2. Use the Sieve of Eratosthenes to determine prime numbers less than a given natural number.

3. "Know, given a natural number greater than 1, that there exists a unique increasing sequence of prime numbers whose product equals that number" - Fundamental theorem of arithmetic. Decompose natural numbers into a product of prime factors.

4. Use prime factorization to: simplify fractions, determine the divisors of a natural number, and calculate the greatest common divisor and least common multiple of two natural numbers.

# Integers

**Title:** Mathematics 6th grade | Positive and negative rational numbers

**Modification Date:** August 21, 2016
**Description:** Mathematics summary - 6th grade according to the new curriculum and learning goals

### POSITIVE AND NEGATIVE RATIONAL NUMBERS

**DOMAIN:** NUMBERS AND OPERATIONS (NO6)
**SUBDOMAIN:** RATIONAL NUMBERS

### What you need to know in this chapter

#### Representing and Comparing Positive and Negative Numbers

1. Recognize pairs of points on the number line equidistant from the origin: a positive rational and its corresponding negative (–a)

2. Identify symmetric numbers: a and –a are symmetric to each other; 0 is symmetric to itself

3. Use "+a" correctly to designate the number a itself; understand "sign of a number"

4. Identify everyday quantities expressed in positive and negative numbers

5. Define "half-line with positive direction" associated with a point on the number line

6. Compare rational numbers using the half-line with positive direction

7. Recognize that 0 > any negative and 0 < any positive

8. Define "absolute value" or "modulus" of number a as distance to the origin: |a|

9. For positive numbers: greater absolute value = greater number; for negative numbers: smaller absolute value = greater number

10. Symmetric numbers: same absolute value with opposite signs

11. Identify the set of "relative integers" (ℤ) formed by 0, natural numbers and their symmetric counterparts

12. Identify the set of "rational numbers" (ℚ) formed by 0, positive rationals and their symmetric counterparts

### Review the material/mathematics summary/synthesis here

### EXERCISES

**Note:** The sections for summary material and exercises were not yet available at the publication date.

**Title:** Mathematics 7th grade | Integers - addition and subtraction

**Modification Date:** February 12, 2024

### INTEGERS - ADDITION AND SUBTRACTION

### Sets of Integer Numbers

- **Natural Numbers:** N = {0, 1, 2, 3, 4, 5, …}
- **Integers:** Z = {…, -3, -2, -1, 0, 1, 2, 3, …}
- **Positive Integers:** Z+ = {1, 2, 3, 4, 5, …}
- **Negative Integers:** Z– = {…, -5, -4, -3, -2, –1}
- **Non-Positive Integers:** Z0– = {…, -5, -4, -3, -2, -1, 0}
- **Non-Negative Integers:** Z0+ = {0, 1, 2, 3, 4, 5, …}

### Number Line, Absolute Value and Symmetric Numbers

Each point on the line corresponds to a unique number (the abscissa of the point), with the origin at zero.

**Absolute Value:** Corresponds to the distance from the point to the origin on the number line. The absolute value is always positive or zero.

**Examples:**
- |5| = 5
- |-5| = 5
- |0| = 0

**Symmetric Numbers:** Have equal absolute value but opposite signs.

**Example:** The symmetric of 5 is -5

### Algebraic Addition

#### Addition with Same Signs
The result has the same sign; add the absolute values.

**Examples:**
- (+2) + (+4) = (+6)
- (-1) + (-3) = (-4)

#### Addition with Different Signs
The result has the sign of the term with greater absolute value; subtract the absolute values.

**Example:**
- (-6) + (+4) = (-2)

### Properties of Addition

**Commutative Property:**
- 4 + 2 = 2 + 4

**Associative Property:**
- (4 + 2) + 5 = 2 + (4 + 5)

**Identity Element:**
- 4 + 0 = 4

**Symmetric Element:**
- (+4) + (-4) = 0

### Subtraction of Integers

To subtract integers, add to the first number the symmetric of the second number.

**Examples:**
- (+3) – (+5) = (+3) + (-5)
- (+3) – (-5) = (+3) + (+5)

### Numerical Expressions

Simplifying numerical expressions follows rules for consecutive signs:
- Same signs: positive result
- Different signs: negative result

### Available Resources

**Exercise Worksheets:**
- Number line and algebraic addition
- Integer exercises

**#StudyAtHome Classes:**
- Videos about integers (addition and subtraction)
- Worksheets accompanying RTP classes

**Essential Learning:**
List of learning objectives including:
- Comparison and ordering of integers
- Problem solving with integers
- Understanding properties of operations

# Rational Numbers

**Title:** Mathematics Grade 5 | Non-negative Rational Numbers

### NON-NEGATIVE RATIONAL NUMBERS

#### SET OF RATIONAL NUMBERS

The set of rational numbers is represented by the symbol ℚ. A number is rational if it can be expressed as a fraction. This chapter works exclusively with non-negative numbers.

#### FRACTIONS

**What is a fraction?**

A fraction represents parts of a whole. In the fraction 3/5:
- Numerator: 3
- Denominator: 5
- Reading: "three-fifths"

**Simplifying fractions**

Both terms are divided by the same number. When it's not possible to simplify further, it's called an "irreducible fraction."

**Equivalent fractions**

Both terms are multiplied by the same number to obtain equivalent fractions.

**Ordering fractions**

- Same denominator: the greater one has the greater numerator
- Same numerator: the greater one has the smaller denominator
- Different: make the denominators equal

**Proper and improper fractions**

Proper: denominator greater than numerator (less than 1)
Improper: numerator greater than denominator (greater than 1)

**Decimal fractions**

Denominators 10, 100, 1000, etc. Conversion to decimals: write the numerator with decimal places according to the zeros in the denominator.

**Operations with fractions**

Addition/subtraction: make denominators equal, then add or subtract numerators.
Multiplication: multiply numerators and denominators.
Division: three possible methods (inverting the second fraction is common).

#### MIXED NUMBERS

Representation of improper fractions with whole part and fractional part.

Conversion fraction → mixed number: decomposition into complete units.
Conversion mixed number → fraction: (whole part × denominator + numerator) / denominator

**Operations with mixed numbers**

Addition: add whole parts and fractional parts separately.
Subtraction: subtract whole parts and fractional parts separately.

#### APPROXIMATE VALUES AND ROUNDING

**Fraction as quotient**

Fractions represent divisions: 4/2 = 4÷2

**Approximations**

By defect: write up to certain decimal places without changing
By excess: write up to decimal places, adding one to the last digit
By rounding: considering whether the next digit is less than or greater/equal to 5

**Representations of infinite periodic decimals**

Exact form with repeated digit in parentheses: 0,(3)

#### PROBLEMS

**Fraction of a whole**

Replace "of" with multiplication: "2/5 of 30" = 2/5 × 30 = 12

**Percentages**

Fractions with denominator 100 convert directly: 25/100 = 25%
Other fractions: convert to decimal and multiply by 100.

#### Curricular Goals

The program covers: simplifying fractions, equivalence, ordering, operations (addition, subtraction, multiplication, division), mixed numbers, approximations, rounding, and solving problems with fractions, decimals, percentages.

**Title:** Mathematics Grade 7 | Rational numbers – addition, subtraction, percentage, and scientific notation

### RATIONAL NUMBERS

#### Meaning of Rational Number

A rational number is a number that can be represented in the form of a fraction.

**Notation:**
- Q = rational numbers
- Q+ = positive rational numbers
- Q– = negative rational numbers
- Q0+ = non-negative rational numbers
- Q0– = non-positive rational numbers

**Relationship between sets:** All natural numbers and integers are rational (N ⊂ Z ⊂ Q)

#### Representation on the Number Line

The denominator indicates divisions of the unit.
The numerator indicates how many parts to traverse from the origin.

#### Addition and Subtraction of Rational Numbers

The same rules as integers apply.

**Example:**
(+4/2) + (–3/5) = +7/5

(After finding common denominators)

#### Percentage

A percentage is a quotient where the divisor is 100.

**Example:**
25% = 25 ÷ 100 = 25/100

**Calculations with percentages:**
- Finding a part: percentage × whole
- Finding the whole: 100 × part / percentage

#### Scientific Notation

Numbers are expressed in the format: a × 10ⁿ, where 1 ≤ a < 10 and n is a positive integer.

**Example:**
37000 = 3,7 × 10⁴

**Comparison between numbers in scientific notation:**
- Equal exponents: greater coefficient = greater number
- Different exponents: greater exponent = greater number

#### Essential Learning

This material covers the definition and representation of rational numbers, addition and subtraction operations, calculations with percentages, and expressing numbers in scientific notation.

### Part 1: Representation of Rational Numbers

**Title:** Mathematics Grade 8 | Representation of rational numbers – Finite and infinite periodic decimals

#### NUMERICAL SETS

- Natural numbers (N)
- Integers (Z)
- Fractional numbers
- Rational numbers (Q)

"Rational numbers can be integers or fractional numbers" - rational numbers include both integer and fractional types.

#### FINITE DECIMALS

Finite decimals are numbers whose decimal part has an end.

"Decimal fractions (whose denominator is 10, 100, 1000, …, 10n)" always correspond to finite decimals.

#### INFINITE PERIODIC DECIMALS

These present "an infinite sequence of digits, where a group of one or more digits repeats."

**Types:**
- Simple or pure periodic decimals (such as 1,(14))
- Compound periodic decimals with "anti-period" (such as 2,8(3))

#### APPROXIMATE VALUES

**Three approximation methods:**
- Values by defect (rounding down)
- Values by excess (rounding up)
- Standard rounding based on the first eliminated digit

### Part 2: Operations with Rational Numbers

**Title:** Mathematics Grade 8 | Operations with rational numbers

## EXPLANATION OF THE MATERIAL

### 2. Operations with rational numbers

#### 2.1. Addition and subtraction

##### **Addition**

To add rational numbers it is important to first recall the rules for adding integers.

**Addition of integers with the same signs**

If the numbers we want to add have the same sign, then the result has that sign and we add the absolute values of the addends.

(+) + (+) = (+)
(-) + (-) = (-)

(+2) + (+4) = (+6) → positive result because both addends are positive and 6 because 2 + 4 = 6

(–1) + (–3) = (–4) → negative result because both addends are negative and 4 because 1 + 3 = 4

**Addition of integers with different signs**

If the numbers we want to add have different signs, then the result has the sign of the addend with the greater absolute value and we subtract the absolute values of the addends (the larger by the smaller).

(+) + (-) = (sign of the addend with greater absolute value)
(-) + (+) = (sign of the addend with greater absolute value)

(–6) + (+4) = (–2) → negative result because the addend with greater absolute value is negative ( |-6| > |+4| ) and 2 because 6 – 4 = 2

(–3) + (+5) = (+2) → positive result because the addend with greater absolute value is positive ( |-3| < |+5| ) and 2 because 5 – 3 = 2

**Addition with fractions**

To add fractions we must have the same denominator and add only the numerators according to the same rules for adding integers, keeping the denominator the same.

(-2/3) + (+5/4) = → different denominators, so we must find equivalent fractions
= (-8/12) + (+15/12) = → addition of numbers with different signs
= (+7/12) → positive result because the addend with greater absolute value was positive ( |(+15/12)| > |(-8/12)| ) and 7 because 15 – 8 = 7

##### **Subtraction**

As with addition, to subtract rational numbers it is important to first recall the rules for subtracting integers.

**Subtraction of integers**

To subtract integers we can transform subtraction into addition by adding to the additive the opposite of the subtractive. Then, we follow the rules of addition.

a – (+) = a + (-)
a – (-) = a + (+)

(+3) – (+5) =
= (+3) + (-5) = → we change subtraction to addition and place the opposite of (+5)
= (-2) → we follow the rules of addition (in this case, with different signs, result with the sign of the addend with greater value (-5) and subtraction of the absolute values of the addends (5 – 3) )

**Subtraction with fractions**

To subtract fractions we must have the same denominator and subtract only the numerators according to the same rules for subtracting integers, keeping the denominator the same.

(-2/3) – (+5/4) = → different denominators, so we must find equivalent fractions
= (-8/12) – (+15/12) = → change to addition by placing the opposite of the subtractive
= (-8/12) + (-15/12) = → addition of numbers with the same signs
= (-23/12) → negative result because the addends are negative and 23 because 8 + 15 = 23

##### **Ways to simplify expressions**

There are ways to simplify expressions to perform fewer steps, which can be very useful especially when there are several operations in the same expression.

**Simplification of notation**

In an expression we can replace two consecutive equal signs with a single + sign.

+ (+) = +
– (-) = +

4 + (+3) = 4 + 3 → "plus with plus gives plus"
4 – (-3) = 4 + 3 → "minus with minus gives plus"

Two consecutive different signs can be replaced with a single – sign.

+ (-) = –
– (+) = –

4 + (-3) = 4 – 3 → "plus with minus gives minus"
4 – (+3) = 4 – 3 → "minus with plus gives minus"

**Opposite of the sum and opposite of the difference**

When we have the opposite of a sum, we can add the opposites of the addends.

– (a + b) = (-a) + (-b) = – a – b

– (2 + 4) = – 2 – 4

When we have the opposite of a subtraction, we can subtract the opposites of the terms.

– (a – b) = (-a) – (-b) = – a + b

– (2 – 4) = – 2 + 4

#### 2.2. Multiplication and division

##### **Multiplication**

The multiplication of rational numbers presents different rules from addition and subtraction, nor is it possible to apply the same notation simplification rules. That is, it has its own rules and properties.

**Multiplication with the same signs**

In a multiplication with factors with the same sign, the result is positive and we multiply the absolute values of the factors.

(+) × (+) = (+)
(-) × (-) = (+)

(+2) × (+4) = (+8) → positive result because both factors have the same sign and 8 because 2 × 4 = 8

(-1) × (-3) = (+3) → positive result because both factors have the same sign and 3 because 1 × 3 = 3

**Multiplication with different signs**

In a multiplication with factors with different signs, the result is negative and we multiply the absolute values of the factors.

(+) × (-) = (-)
(-) × (+) = (-)

(+2) × (-4) = (-8) → negative result because both factors have different signs and 8 because 2 × 4 = 8

(-1) × (+3) = (-3) → negative result because both factors have different signs and 3 because 1 × 3 = 3

**Multiplication with fractions**

To multiply fractions it is not necessary to have the same denominator. Multiply numerator with numerator and denominator with denominator and the result has the sign according to the same rules for multiplying integers.

(-2/3) × (+5/4) = → multiply the numerators (2×5) and the denominators (3×4)
= (-10/12) → the result is negative because both factors have different signs

**Properties of multiplication**

Commutative property of multiplication: we can change the order of the factors in a multiplication.

a × b = b × a

5 × 3 = 3 × 5

Associative property of multiplication: we can associate the factors of a multiplication differently.

(a × b) × c = a × (b × c)

(5 × 3) × 1 = 5 × (3 × 1)

Existence of the neutral element of multiplication: the multiplication of a number by 1 is equal to that number.

a × 1 = a

5 × 1 = 5

A negative integer is equal to the product of its opposite by -1, that is, the multiplication of a number by -1 gives the opposite of that number.

a × (-1) = – a

5 × (-1) = -5

Existence of the absorbing element of multiplication: the multiplication of a number by 0 is always equal to 0.

a × 0 = 0

5 × 0 = 0

Existence of the inverse element of multiplication: the multiplication of a number (except 0) by its inverse is equal to 1.

a × (1/a) = 1

5 × (1/5) = 1

Distributive property of multiplication over addition: the multiplication of a number with an addition can be transformed into an addition of two multiplications.

a × (b + c) = a × b + a × c

5 × (4 + 1) = 5 × 4 + 5 × 1

Distributive property of multiplication over subtraction: the multiplication of a number with a subtraction can be transformed into a subtraction of two multiplications.

a × (b – c) = a × b – a × c

5 × (4 – 1) = 5 × 4 – 5 × 1

##### **Division**

The rules for dividing integers are quite similar to those for multiplication, and division between fractions can be transformed into multiplication, since division is the inverse operation of multiplication.

**Division of integers with the same signs**

In a division with dividend and divisor with the same sign, the result is positive and the dividend is divided by the divisor.

(+) : (+) = (+)
(-) : (-) = (+)

(+8) : (+4) = (+2) → positive result because dividend and divisor have the same sign and 2 because 8 : 4 = 2 since 2 × 4 = 8

(-15) : (-5) = (+3) → positive result because dividend and divisor have the same sign and 3 because 15 : 5 = 3 since 3 × 5 = 15

**Division of integers with different signs**

In a division with dividend and divisor with different signs, the result is negative and the dividend is divided by the divisor.

(+) : (-) = (-)
(-) : (+) = (-)

(+8) : (-4) = (-2) → negative result because dividend and divisor have different signs and 2 because 8 : 4 = 2 since 2 × 4 = 8

(-15) : (+5) = (-3) → negative result because dividend and divisor have different signs and 3 because 15 : 5 = 3 since 3 × 5 = 15

**Division with fractions**

To divide fractions it is not necessary to have the same denominator. Divide numerator by numerator and denominator by denominator and the result has the sign according to the same rules for dividing integers.

(-16/6) : (+4/3) = → divide the numerators (16 : 4) and the denominators (6 : 3)
= (-4/2) → the result is negative because both factors have different signs

When dividing the numerator of the first fraction by the numerator of the second, or denominator by denominator, the result is not always an integer. In these cases, in order to obtain a result in the form of a fraction, it is possible to transform the division into a multiplication, multiplying the first fraction by the inverse of the second fraction.

(-2/3) : (+4/5) = → change to multiplication by placing the inverse of the second fraction
= (-2/3) × (+5/4) = → multiply the numerators (2×5) and the denominators (3×4)
= (-10/12) → the result is negative because both factors have different signs

#### 2.3. Numerical expressions

##### **Numerical expressions with additions, subtractions, multiplications and divisions**

Numerical expressions can present additions, subtractions, multiplications and divisions mixed together, and there are rules for the priority of operations to be performed.

**Priorities of operations in numerical expressions**

First we must perform the operations inside parentheses, then multiplications and divisions in the order they appear and, finally, additions and subtractions in the order they appear.

2 + 3 – (3 + 5 × 3) : 2 = → multiplication inside parentheses
= 2 + 3 – (3 + 15) : 2 = → addition inside parentheses
= 2 + 3 – 18 : 2 = → division since it has priority over addition and subtraction
= 2 + 3 – 9 = → addition since it appears before subtraction
= 5 – 9 =
= – 4

## SUMMARY

**2. Operations with rational numbers**

### 2.1. Addition and subtraction

• **Addition with the same signs**
  - has the same sign
  - add the absolute values of the addends
  - (+2) + (+4) = (+6)
  - (-1) + (-3) = (-4)

• **Addition with different signs**
  - has the sign of the addend with greater absolute value
  - subtract the absolute values of the addends (the larger by the smaller)
  - (-6) + (+4) = (-2)
  - (-3) + (+5) = (+2)

• **Addition with fractions**
  - fractions must have the same denominator
  - add the numerators, denominator stays the same
  - (-2/3) + (+5/4) = (-8/12) + (+15/12) = (+7/12)

• **Subtraction of integers**
  - add to the additive the opposite of the subtractive
  - (+3) – (+5) = (+3) + (-5) = (-2)
  - (+3) – (-5) = (+3) + (+5) = (+8)

• **Subtraction with fractions**
  - fractions must have the same denominator
  - subtract the numerators, denominator stays the same
  - (-2/3) – (+5/4) = (-8/12) – (+15/12) = (-8/12) + (-15/12) = (-23/12)

• **Simplification of notation**
  - + (+) = +
  - – (-) = +
  - + (-) = –
  - – (+) = –

• **Opposite of the sum and opposite of the difference**
  - – (a + b) = – a – b
  - – (a – b) = – a + b

### 2.2. Multiplication and division

• **Multiplication with the same signs**
  - is positive
  - multiply the factors
  - (+2) × (+4) = (+8)
  - (-1) × (-3) = (+3)

• **Multiplication with different signs**
  - is negative
  - multiply the factors
  - (-2) × (+4) = (-8)
  - (-1) × (+3) = (-3)

• **Multiplication with fractions**
  - fractions don't need to have the same denominator
  - multiply numerator with numerator and denominator with denominator
  - (-2/3) × (+5/4) = (-10/12)

• **Properties of multiplication**
  - Commutative property → a × b = b × a
  - Associative property → (a × b) × c = a × (b × c)
  - Neutral element → a × 1 = a
  - Multiplication by -1 → a × (-1) = – a
  - Absorbing element → a × 0 = 0
  - Inverse element → a × (1/a) = 1
  - Distributive property → a × (b + c) = a × b + a × c | a × (b – c) = a × b – a × c

• **Division with the same signs**
  - is positive
  - divide dividend by divisor
  - (+8) : (+4) = (+2)
  - (-15) : (-5) = (+3)

• **Division with different signs**
  - is negative
  - divide dividend by divisor
  - (-8) : (+4) = (-2)
  - (-15) : (+5) = (-3)

• **Division with fractions**
  - fractions don't need to have the same denominator
  - it's possible to turn it into a multiplication by placing the inverse of the second fraction
  - (-2/3) : (+4/5) = (-2/3) × (+5/4) = (-10/12)

### 2.3. Numerical expressions

• **Priorities of operations**
  - 1st: operations inside parentheses
  - 2nd: multiplications and divisions in the order they appear
  - 3rd: additions and subtractions in the order they appear
  - Example: 2 + 3 – (3 + 5 × 3) : 2 = 2 + 3 – (3 + 15) : 2 = 2 + 3 – 18 : 2 = 2 + 3 – 9 = 5 – 9 = – 4

## ESSENTIAL LEARNING (Grade 8)

- Recognize a negative rational number as the product of its opposite by -1.
- Multiply and divide rational numbers.
- Recognize the properties of multiplication and division of rational numbers.
- Interpret situations involving operations with rational numbers, whether the answers to be given are exact values or approximate values, and solve associated problems.

# Real Numbers

**Topic:** Square root and cube root

### Page Title
Mathematics 8th grade | Square root and cube root - O Bichinho do Saber

### Main Navigation
- HOME
- SUMMARIES AND EXERCISES
- TESTS AND EXAMS
- Archive
- Calendar
- HIGHER EDUCATION ACCESS
- OUR PROJECT AND CONTACTS

### Article Header
**Mathematics 8th grade | Square root and cube root**

by Luis Carrilho · October 25, 2023

### Content Navigation Links
- Explanation of the material
- Summary
- Interactive exercises
- To print – summaries and exercises
- More resources

## EXPLANATION OF THE MATERIAL

### 4. Square root and cube root

#### 4.1. Perfect squares and square root

##### **Perfect square**

A perfect square is a natural number that results from a power whose base is a natural number and which has exponent number 2, that is, it is a number equal to the square of a natural number.

**Perfect squares**

The perfect square formula is represented by:

n² = a (where n is a natural number and a is a perfect square)

4² = 16 , therefore 16 is a perfect square

First perfect squares:

1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, …

##### **Square root**

The square root of a number is the factor which, when squared, equals that number.

**Square roots**

The square root formula is represented by:

√a = b , if b² = a

√16 = 4   → because 4² = 16

√0 = 0   → because 0² = 0

The square roots of positive integers that are not perfect squares correspond to infinite non-periodic decimals.

√20 = 4.47213595…   → 20 is not a perfect square

**Square of the square root**

The square of the square root of a number equals that number.

(√a)² = a

(√15)² = 15

**Relationship between the side of a square and its area**

The side of a square equals the square root of its area.

l = √A

A square with area 50 has side √50

#### 4.2. Perfect cubes and cube root

##### **Perfect cube**

A perfect cube is a natural number that results from a power whose base is a natural number and which has exponent number 3, that is, it is a number equal to the cube of a natural number.

**Perfect cubes**

The perfect cube formula is represented by:

n³ = a (where n is a natural number and a is a perfect cube)

4³ = 64 , therefore 64 is a perfect cube

First perfect cubes:

1, 8, 27, 64, 125, …

##### **Cube root**

The cube root of a number is the factor which, when cubed, equals that number.

**Cube roots**

The cube root formula is represented by:

∛a = b , if b³ = a

∛27 = 3   → because 3³ = 27

∛0 = 0   → because 0³ = 0

The cube roots of positive integers that are not perfect cubes correspond to infinite non-periodic decimals.

∛20 = 2.7144176…   → 20 is not a perfect cube

**Cube of the cube root**

The cube of the cube root of a number equals that number.

(∛a)³ = a

(∛15)³ = 15

**Relationship between the edge of a cube and its volume**

The edge of a cube equals the cube root of its volume.

a = ∛V

A cube with volume 50 has edge ∛50

## SUMMARY

### 4. Square root and cube root

#### 4.1. Perfect squares and square root

• **Perfect squares**
  - ⤷ n² = a ( n natural number and a perfect square)
    - ⤷ 4² = 16
  - ⤷ First perfect squares
    - ⤷ 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, …

• **Square roots**
  - ⤷ √a = b , if b² = a
  - ⤷ √16 = 4   → because 4² = 16
    ⤷ √20 = 4.47213595…  → 20 is not a perfect square

• **Square of the square root**
  - ⤷ (√a)² = a
  - ⤷ (√15)² = 15

• **Relationship between the side of a square and its area**
  - ⤷ l = √A
  - ⤷ A square with area 50 has side √50

#### 4.2. Perfect cubes and cube root

• **Perfect cubes**
  - ⤷ n³ = a ( n natural number and a perfect cube)
    - ⤷ 4³ = 64
  - ⤷ First perfect cubes
    - ⤷ 1, 8, 27, 64, 125, …

• **Cube roots**
  - ⤷ ∛a = b , if b³ = a
  - ⤷ ∛27 = 3   → because 3³ = 27
  - ⤷ ∛20 = 2.7144176…  → 20 is not a perfect cube

• **Cube of the cube root**
  - ⤷ (∛a)³ = a
  - ⤷ (∛15)³ = 15

• **Relationship between the edge of a cube and its volume**
  - ⤷ a = ∛V
  - ⤷ A cube with volume 50 has edge ∛50

## INTERACTIVE EXERCISES

[Interactive exercises section - h5p id="21"]

## TO PRINT

**Review of the material**

4. Square root and cube root | summary · synthesis

4.1. Perfect squares and square root | sheet 4.1. a » correction
4.2. Perfect cubes and cube root | sheet 4.2. a » correction

4. Square root and cube root | test 4. a » correction

4. Square root and cube root | various exercises

## MORE RESOURCES

### POWERPOINTS

### VIDEOS

### CLASSES AND WORKSHEETS #ESTUDOEMCASA

**#EstudoEmCasa 2020/2021**

1 | Square root » see class · worksheet

2 | Cube root » see class · worksheet

### ESSENTIAL LEARNING OUTCOMES

- Know the perfect squares up to 144 and relate them to their respective pictorial representation.
- Estimate and frame square roots, using technology.
- Calculate square roots of perfect squares and approximate values of other square roots, using technology.
- Know the perfect cubes up to 125.
- Solve problems that involve calculating cube roots of perfect cubes and approximate values of other cube roots, using technology.

## Related Content Navigation

**SUMMARIES AND EXERCISES | 8TH GRADE | MATHEMATICS**

- Representations of rational numbers (finite decimals and infinite periodic decimals)
- Operations with rational numbers
- Rules of powers
- Square root and cube root (current page)
- Scientific notation
- Polynomials
- First-degree equations
- Literal equations
- Affine functions
- Statistical study
- Probabilities
- Pythagorean theorem
- Vectors, isometries and symmetries
- Geometric solids

**Topic:** Real numbers – Number intervals, order relation and approximate values

### Page Title and Header
"Mathematics 9th grade | Real numbers - O Bichinho do Saber"

### Main Heading
"Mathematics 9th grade | Real numbers"

### Section: Real numbers – Number intervals, order relation and approximate values

Navigation anchors available:
- SUMMARY
- POWERPOINTS
- VIDEOS
- CLASSES AND WORKSHEETS #ESTUDOEMCASA
- EXERCISES
- ESSENTIAL LEARNING OUTCOMES

## SUMMARY Section

### _**REAL NUMBERS**_

#### _Set of real numbers_

**›  _From natural numbers to real numbers_**
"see video"

**›  _Scientific notation_**
"see video"

**›  _Intervals of real numbers_**

» _Representation of real number intervals_
"see video"

» _Intersection and union of intervals_
"see video 1"
"see video 2"

#### _Order relation_
"see video"

#### _Approximate values_
"see video"

## POWERPOINT PRESENTATION

## YOUTUBE VIDEOS

## CLASSES AND WORKSHEETS #ESTUDOEMCASA

### #EstudoEmCasa 2020/2021

**Class 1** | "The man who counted. Identify, recognize and compare real numbers" » [see class](https://www.rtp.pt/play/estudoemcasa/p7823/e500032/matematica-9-ano) · [worksheet](https://estudoemcasa-2020-2021.s3.eu-west-3.amazonaws.com/resources/1a9e1c1ad4e7352140811fef12a36d92/01_Matem%C3%A1tica_9%C2%BA%20ano_O%20homem%20que%20calculava.pdf)

**Class 2** | "A matter of order" » [see class](https://www.rtp.pt/play/estudoemcasa/p7823/e500886/matematica-9-ano) · [worksheet](https://estudoemcasa-2020-2021.s3.eu-west-3.amazonaws.com/resources/8556550a2e93e0d1a053d15821ddb74a/02_Matem%C3%A1tica_9%C2%BA%20ano_Uma%20quest%C3%A3o%20de%20ordem.pdf)

**Class 3** | "Approximate values and framings" » [see class](https://www.rtp.pt/play/estudoemcasa/p7823/e501579/matematica-9-ano) · [worksheet](https://estudoemcasa-2020-2021.s3.eu-west-3.amazonaws.com/resources/927bc03bc7d41ae7013c645f9bfe7462/03_Matem%C3%A1tica_9%C2%BA%20ano_Valores%20aproximados%20e%20enquadramentos.pdf)

**Class 4** | "Exact values" » [see class](https://www.rtp.pt/play/estudoemcasa/p7823/e502344/matematica-9-ano) · [worksheet](https://estudoemcasa-2020-2021.s3.eu-west-3.amazonaws.com/resources/400718d6a3c99165891ec85c5b78fcf5/04_Matem%C3%A1tica_9%C2%BA%20ano_Valores%20exatos.pdf)

**Class 5** | "Problem solving with real numbers" » [see class](https://www.rtp.pt/play/estudoemcasa/p7823/e503085/matematica-9-ano) · [worksheet](https://estudoemcasa-2020-2021.s3.eu-west-3.amazonaws.com/resources/b2e5d3d008651b900f21d144cf9b087c/05_Matem%C3%A1tica_9%C2%BA%20ano_Resolu%C3%A7%C3%A3o%20de%20problemas%20com%20n%C3%BAmeros%20reais.pdf)

**Class 6** | "Intervals of real numbers" » [see class](https://www.rtp.pt/play/estudoemcasa/p7823/e503945/matematica-9-ano) · [worksheet](https://estudoemcasa-2020-2021.s3.eu-west-3.amazonaws.com/resources/0aceeb89e9d7ff1571a39002b5eb67f2/06_Matem%C3%A1tica_9%C2%BA%20ano_Intervalos%20de%20n%C3%BAmeros%20reais.pdf)

**Class 7** | "Intersection of real number intervals" » [see class](https://www.rtp.pt/play/estudoemcasa/p7823/e504690/matematica-9-ano) · [worksheet](https://estudoemcasa-2020-2021.s3.eu-west-3.amazonaws.com/resources/2df675722d00575e953df7db25a9509c/07_Matem%C3%A1tica_9%C2%BA%20ano_Interse%C3%A7%C3%A3o%20de%20intervalos%20de%20n%C3%BAmeros%20reais.pdf)

**Class 8** | "Union of real number intervals. Disjunction of conditions" » [see class](https://www.rtp.pt/play/estudoemcasa/p7823/e505543/matematica-9-ano) · [worksheet](https://estudoemcasa-2020-2021.s3.eu-west-3.amazonaws.com/resources/f46b63ee69df227f1daaf27d896181f3/08_Matem%C3%A1tica_9%C2%BA%20ano_Reuni%C3%A3o%20de%20intervalos%20de%20n%C3%BAmeros%20reais.%20Disjun%C3%A7%C3%A3o%20de%20condi%C3%A7%C3%B5es.pdf)

### #EstudoEmCasa 2019/2020

**Class 1** | "A journey through numbers" » [see class](https://www.rtp.pt/play/estudoemcasa/p7134/e467839/matematica-9-ano) · [worksheet](https://estudoemcasa.s3.eu-west-3.amazonaws.com/resources/97cdac04a90817e830943f9ae0d2957c/Uma%20viagem%20pelos%20n%C3%BAmeros.pdf)

**Class 2** | "Numbers in family" » [see class](https://www.rtp.pt/play/estudoemcasa/p7134/e467848/matematica-9-ano) · [worksheet](https://estudoemcasa.s3.eu-west-3.amazonaws.com/resources/dcae7056d3dc5eb20e23411fcba9ccca/N%C3%BAmeros%20em%20fam%C3%ADlia.pdf)

**Class 3** | "A trip to the stadium" » [see class](https://www.rtp.pt/play/estudoemcasa/p7134/e469320/matematica-9-ano) · [worksheet](https://estudoemcasa.s3.eu-west-3.amazonaws.com/resources/f6a5596c1449c960d85c3a51095b3580/Ativ.%20Compl.%20Aula3_EstudoEmCasa.pdf)

## EXERCISES

## ESSENTIAL LEARNING OUTCOMES

**ELO – ESSENTIAL LEARNING OUTCOMES:**

- "Recognize integers, rational and real numbers in their different representations, including scientific notation, in mathematical and non-mathematical contexts."

- "Compare real numbers, in diverse contexts, with and without recourse to the real line."

- "Calculate, with and without calculator, with real numbers using exact and approximate values and in different representations, evaluate the effects of operations and make plausible estimates."

- "Recognize that the properties of operations in ℚ are maintained in IR, and use them in situations involving calculation."

## CURRICULAR REFERENCE DOCUMENTS

› [Essential Learning Outcomes](http://www.dge.mec.pt/sites/default/files/Curriculo/Aprendizagens_Essenciais/3_ciclo/matematica_3c_9a_ff_18julho_rev.pdf)

› [Student Profile (at the end of compulsory schooling)](https://www.dge.mec.pt/sites/default/files/Curriculo/Projeto_Autonomia_e_Flexibilidade/perfil_dos_alunos.pdf)

› [Curricular Program and Goals](http://www.dge.mec.pt/sites/default/files/Basico/Metas/Matematica/programa_matematica_basico.pdf) – revoked

## Additional Mathematics Topics for 9th Grade

**SUMMARIES AND EXERCISES**
**9TH GRADE | MATHEMATICS**

- › Real numbers
- › Geometric Figures
- › Areas and Volumes
- › Trigonometry
- › Sequences and regularities
- › Equations
- › Inequalities
- › Functions
- › Statistical planning and Data processing
- › Probability

## Metadata
- Published: July 11, 2021
- Modified: February 13, 2024
- Author: Luis Carrilho
- Website: O Bichinho do Saber

## Footer Information

**O Bichinho do Saber © 2025. All rights reserved.**

Powered by WordPress. Theme by Alx.

Social Media Links:
- Facebook
- Twitter
- LinkedIn
- RSS Feed

Footer Navigation:
- About
- Contacts
- Site Map
- Partners

# Powers and Scientific Notation

### Mathematics Grade 6 | Powers with Natural Exponents

#### Page Metadata
- **URL:** https://www.obichinhodosaber.com/matematica-6o-ano-potencias-expoente-natural/
- **Title:** Mathematics Grade 6 | Powers with natural exponents - O Bichinho do Saber
- **Publication Date:** August 21, 2016
- **Author:** Luis Carrilho
- **Description:** "Summary of Mathematics - 6th grade according to the new curriculum and goals | Powers with natural exponents"

#### Navigation and Breadcrumbs
- Home > Mathematics 6th > Subject summaries and exercises

#### Main Structure

##### Section: POWERS WITH NATURAL EXPONENTS

**Areas to cover:**

#### Mandatory Curriculum Competencies

**Domain:** ALGEBRA (ALG6)
**Subdomain:** POWERS WITH NATURAL EXPONENTS

##### Perform operations with powers

1. Identify a^n (where n is a natural number > 1 and a is a non-negative rational number) as the product of n factors equal to a
2. Correctly use the terms "power", "base" and "exponent"
3. Identify a^1 as the number a itself
4. Product of two powers with the same base = power with the same base and exponent equal to the sum of exponents
5. Power of a power: (a^n)^m = a^(n×m)
6. Recognize the difference between a^(n^m) and (a^n)^m
7. Product of powers with the same exponent = power with that exponent and base equal to the product of the bases
8. Quotient of powers with the same base (different exponents) = power with the same base and exponent = difference of exponents
9. Quotient of powers with the same exponent (divisor base ≠ 0) = power with the same exponent and base = quotient of bases
10. Priority of exponentiation in arithmetic operations
11. Simplify and calculate numerical expressions with the four operations, powers and parentheses

##### Solve problems

1. Translate statements between natural language and symbolic language

#### Related Navigation
- Return to complete list of 6th grade content – Mathematics

#### Social Networks
- Facebook
- Twitter
- LinkedIn
- RSS Feed

### Mathematics Grade 8 | Rules of Powers

#### Page Metadata
- **URL**: https://www.obichinhodosaber.com/matematica-8o-ano-regras-das-potencias/
- **Published**: October 18, 2023
- **Modified**: February 13, 2024
- **Author**: Luis Carrilho
- **Language**: Portuguese (pt-PT)
- **Image**: mat8_03_regras_das_potencias.jpg (800x420px)

#### Navigation
**Breadcrumbs**: Home > Mathematics Grade 8 | Rules of powers

**Main Menu**:
- HOME
- SUMMARIES AND EXERCISES
- TESTS AND EXAMS
- ACCESS TO HIGHER EDUCATION
- OUR PROJECT AND CONTACTS

#### Main Content

##### Title
**Mathematics Grade 8 | Rules of Powers**

##### Table of Contents
- Explanation of the material
- Summary
- Interactive exercises
- To print – summaries and exercises
- More resources

#### EXPLANATION OF THE MATERIAL

##### 3. Rules of Powers

###### 3.1. Powers with integer exponents

**Simplification rules for powers**

Powers have several simplification rules that help in solving operations with powers.

**Powers with negative base**

**Even exponent:**
- (- a)ⁿ = aⁿ (when n is even)
- Example: (- 3)² = 9 (because (- 3) × (- 3) = (+ 9))

**Important note**: The negative sign must be within parentheses. Otherwise:
- – aⁿ = – aⁿ (when n is even)
- Example: – 3² = – 9 (because – (3 × 3) = – 9)

**Odd exponent:**
- (- a)ⁿ = – aⁿ (when n is odd)
- Example: (- 3)³ = – 27 (because (- 3) × (- 3) × (- 3) = (- 27))

If the exponent is odd and the "-" sign is outside the parentheses:
- – aⁿ = – aⁿ (when n is odd)
- Example: – 3³ = – 27 (because – (3 × 3 × 3) = – 27)

**Power with exponent 1**

"Powers with exponent 1 are always equal to the value of the power's base"

- a¹ = a
- Example: 3¹ = 3

**Power with exponent 0**

"Powers with exponent 0 are always equal to 1"

- a⁰ = 1
- Example: 3⁰ = 1

**Power with negative exponent**

When a power has a negative exponent, it is possible to transform it into a power with a positive exponent by inverting the base.

- (a)⁻ⁿ = (1/a)ⁿ
- Example: (3)⁻² = (1/3)²

**Power with base 1**

"Powers with base 1 are always equal to 1, whatever the exponent"

- 1ⁿ = 1
- Example: 1³ = 1 (because 1 × 1 × 1 = 1)
- Example: 1⁻³ = 1 (because 1⁻³ = 1/1³, and the inverse of 1 equals 1)

**Power of a power**

It is possible to apply a simplification rule by multiplying the exponents.

- (aᵐ)ⁿ = aᵐ ˣ ⁿ
- Example: (3²)⁻⁴ = 3⁻⁸

**Rules of powers in multiplication**

**Same base:**
Add the exponents.

- aᵐ × aⁿ = aᵐ ⁺ ⁿ
- Example: 3² × 3⁴ = 3⁶
- Example: (1/3)² × (1/3)⁴ = (1/3)⁶

**Same exponent:**
Multiply the bases.

- aⁿ × bⁿ = (a × b)ⁿ
- Example: 3² × 5² = 15²
- Example: (1/3)² × (5/4)² = (5/12)²

**Rules of powers in division**

**Same base:**
Subtract the exponents.

- aᵐ : aⁿ = aᵐ ⁻ ⁿ
- Example: 3² : 3⁴ = 3⁻²
- Example: (1/3)² : (1/3)⁴ = (1/3)⁻²

**Same exponent:**
Divide the bases.

- aⁿ : bⁿ = (a : b)ⁿ
- Example: 3² : 5² = (3/5)²
- Example: (1/3)² : (5/4)² = (1/3)² × (4/5)² = (4/15)²

#### SUMMARY

##### 3. Rules of Powers

###### 3.1. Powers with integer exponents

**Powers with negative base**
- Even exponent → (- a)ⁿ = aⁿ
  - (- 3)² = 9
- Odd exponent → (- a)ⁿ = – aⁿ
  - (- 3)³ = – 27

**Power with exponent 1**
- a¹ = a
- 3¹ = 3

**Power with exponent 0**
- a⁰ = 1
- 3⁰ = 1

**Power with negative exponent**
- (a)⁻ⁿ = (1/a)ⁿ
- (3)⁻² = (1/3)²

**Power with base 1**
- 1ⁿ = 1
- 1⁻³ = 1

**Power of a power**
- (aᵐ)ⁿ = aᵐ ˣ ⁿ
- (3²)⁻⁴ = 3⁻⁸

**Rules of powers in multiplication**
- aᵐ × aⁿ = aᵐ ⁺ ⁿ
  - (1/3)² × (1/3)⁴ = (1/3)⁶
- aⁿ × bⁿ = (a × b)ⁿ
  - (1/3)² × (5/4)² = (5/12)²

**Rules of powers in division**
- aᵐ : aⁿ = aᵐ ⁻ ⁿ
  - (1/3)² : (1/3)⁴ = (1/3)⁻²
- aⁿ : bⁿ = (a : b)ⁿ
  - (1/3)² : (5/4)² = (4/15)²

#### INTERACTIVE EXERCISES

[Interactive exercises integrated into the page - details not specified in HTML]

#### TO PRINT

##### Material review
**3. Rules of powers**
- Summary (PDF)
- Synopsis (PDF)

##### Exercise sheets
**3.1. Powers with integer exponents**

##### Tests
**3. Rules of powers**

##### Item bank
**3. Rules of powers**

#### MORE RESOURCES

##### Powerpoints

##### Videos

##### Classes and Worksheets #EstudoEmCasa

**#EstudoEmCasa 2020/2021**

1. **Powers with natural exponent and rational base**
   - Watch class: https://www.rtp.pt/play/estudoemcasa/p7829/e506602/matematica-7-e-8-anos
   - Worksheet: Available on EstudoEmCasa server

2. **Powers with integer exponent and rational base**
   - Watch class: https://www.rtp.pt/play/estudoemcasa/p7829/e507829/matematica-7-e-8-anos
   - Worksheet: Available on EstudoEmCasa server

3. **Numerical expressions**
   - Watch class: https://www.rtp.pt/play/estudoemcasa/p7829/e508182/matematica-7-e-8-anos
   - Worksheet: Available on EstudoEmCasa server

#### ESSENTIAL LEARNINGS

- Understand the meaning of a power with rational base and integer exponent.
- Recognize and apply the operational rules of powers with rational base and integer exponent.
- Simplify and calculate numerical expressions involving powers.
- Compare and order powers with rational base and integer exponent.
- Conjecture or generalize regularities in the multiplication and division of powers and justify.
- Interpret mathematical situations involving powers with rational base and integer exponent and solve associated problems.
- Operate with powers with rational base and integer exponent, presenting and explaining ideas and reasoning.

#### RELATED TOPICS (GRADE 8 - MATHEMATICS)

- Representations of rational numbers (finite decimals and periodic infinite decimals)
- Operations with rational numbers
- Rules of powers
- Square root and cube root
- Scientific notation
- Polynomials
- First-degree equations
- Literal equations
- Affine functions
- Statistical study
- Probabilities
- Pythagorean theorem
- Vectors, isometries and symmetries
- Geometric solids

#### SOCIAL SHARING

Available options:
- Facebook
- Messenger
- WhatsApp
- Instagram
- Copy link

#### FOOTER

**Social Networks**:
- Facebook: O Bichinho do Saber
- Twitter: @bichinhodosaber
- LinkedIn: Luis Carrilho
- RSS Feed

**Useful Links**:
- About
- Contacts
- Site Map
- Partners

**Copyright**: O Bichinho do Saber © 2025. All rights reserved.

**Powered by**: WordPress | Theme: Alx

### Mathematics Grade 8 | Scientific Notation

#### Page Metadata
- **Title**: Mathematics Grade 8 | Scientific notation - O Bichinho do Saber
- **URL**: https://www.obichinhodosaber.com/matematica-8o-ano-notacao-cientifica/
- **Publication Date**: November 29, 2023
- **Modification Date**: February 13, 2024
- **Author**: Luis Carrilho
- **Language**: Portuguese (Portugal)

#### Navigation and Breadcrumbs
- Home > Mathematics Grade 8 | Scientific notation
- Section: SUMMARIES AND EXERCISES > GRADE 8 > MATHEMATICS GRADE 8

#### Table of Contents
- Explanation of the material
- Summary
- Interactive exercises
- To print – summaries and exercises
- More resources

#### EXPLANATION OF THE MATERIAL

##### 5. Scientific Notation

###### 5.1. Representation and comparison of numbers in scientific notation

**Numbers written in scientific notation**

"Scientific notation is a way of writing numbers using powers of base 10."

**Format of a number written in scientific notation**

A number in scientific notation is presented as: **a × 10ⁿ**

Where: 1 ≤ a < 10 and n is an integer

**Conversion process:**

1st → Write "a" by moving the decimal point as many times as necessary so that 1 ≤ a < 10
2nd → Multiply by the power of base 10 with exponent equal to the number of moves
   - Positive exponent: decimal point moved to the left
   - Negative exponent: decimal point moved to the right

**Example 1**: 25600000 in scientific notation
- a = 2.56
- n = 7 (7 moves to the left)
- Result: 2.56 × 10⁷

**Example 2**: 0.00054897 in scientific notation
- a = 5.4897
- n = -4 (4 moves to the right)
- Result: 5.4897 × 10⁻⁴

**Example 3**: 138.7 × 10⁶ in scientific notation
- a = 1.387
- Result: 1.387 × 10⁸

**Comparison of numbers in scientific notation**

- With different exponents: larger number has larger exponent
  - 1.387 × 10⁸ > 5.4897 × 10⁻⁴
- With equal exponents: larger number has larger value "a"
  - 1.387 × 10⁶ < 5.4897 × 10⁶

###### 5.2. Operations with numbers in scientific notation

**Multiplication of numbers in scientific notation**

General formula: b × a × 10ⁿ = (b × a) × 10ⁿ

- Double of 1.38 × 10⁶ = 2.76 × 10⁶
- Half of 1.38 × 10⁶ = 0.69 × 10⁶
- 75% of 1.38 × 10⁶ = 1.035 × 10⁶

For two numbers in scientific notation:
(a₁ × 10ⁿ¹) × (a₂ × 10ⁿ²) = (a₁ × a₂) × 10ⁿ¹⁺ⁿ²

Example: (1.38 × 10⁶) × (2.45 × 10³) = 3.8088 × 10⁹

**Division of numbers in scientific notation**

General formula: (a₁ × 10ⁿ¹) ÷ (a₂ × 10ⁿ²) = (a₁ ÷ a₂) × 10ⁿ¹⁻ⁿ²

Example: (6.78 × 10⁴) ÷ (3.2 × 10³) = 2.11875 × 10³

#### SUMMARY

##### 5. Scientific Notation

**5.1. Representation and comparison**
- Format: a × 10ⁿ (1 ≤ a < 10, n ∈ ℤ)
- Comparison by exponent (if different) or by "a" (if exponents equal)

**5.2. Operations**
- Multiplication: multiply "a" and add exponents
- Division: divide "a" and subtract exponents

#### INTERACTIVE EXERCISES

Included interactive h5p content (exercise type not specified in text)

#### TO PRINT

**Material review**
- 5. Scientific notation | summary · synopsis

**Exercise sheets**
- 5.1. Representation and comparison | sheet 5.1.a » correction
- 5.2. Operations | sheet 5.2.a » correction

#### MORE RESOURCES

**CLASSES #ESTUDOEMCASA 2020/2021**

1. Scientific notation
   - Class: https://www.rtp.pt/play/estudoemcasa/p7829/e509284/
   - PDF worksheet

2. Scientific notation. Ordering and operating with rational numbers
   - Class: https://www.rtp.pt/play/estudoemcasa/p7829/e509618/
   - PDF worksheet

3. Scientific notation. Operating with rational numbers
   - Class: https://www.rtp.pt/play/estudoemcasa/p7829/e510640/
   - PDF worksheet

**CLASSES #ESTUDOEMCASA 2019/2020**

1. Around with numbers 4
   - Class: https://www.rtp.pt/play/estudoemcasa/p7133/e472361/
   - PDF worksheet

#### ESSENTIAL LEARNINGS

- Analyze real situations involving numbers very close to zero
- Recognize advantages of scientific notation
- Represent and compare positive rational numbers in scientific notation
- Operate with numbers in scientific notation in simple cases (percentages, double, triple, half)

#### RELATED CONTENT (GRADE 8 - MATHEMATICS)

- Representations of rational numbers
- Operations with rational numbers
- Rules of powers
- Square root and cube root
- Polynomials
- First-degree equations
- Literal equations
- Affine functions
- Statistical study
- Probabilities
- Pythagorean theorem
- Vectors, isometries and symmetries
- Geometric solids

#### FOOTER

**O Bichinho do Saber © 2025. All rights reserved.**

Powered by WordPress. Theme by Alx.

**Social Networks**: Facebook · Twitter · LinkedIn · RSS Feed


\cleardoublepage

# ALGEBRA

# Algebraic Expressions

### ALGEBRAIC EXPRESSIONS AND PROPERTIES OF OPERATIONS

#### Video Content

Review the material/math summary/synthesis here:

_Note: watch up to 4 minutes._

_Video synthesis provided by [RjasMatemática](https://www.facebook.com/rjasmatematica/) ([www.matexplica.pt](http://www.matexplica.pt/))_

#### EXERCISES

#### Mandatory Content according to Curriculum Program and Goals

**DOMAIN: ALGEBRA (ALG5)**

**SUBDOMAIN: ALGEBRAIC EXPRESSIONS AND PROPERTIES OF OPERATIONS**

##### Know and apply the properties of operations

1. Master the conventional priorities of addition, subtraction, multiplication, and division operations, correctly using parentheses.

2. Recognize the associative and commutative properties of addition and multiplication, as well as the distributive properties of multiplication with respect to addition and subtraction, representing them algebraically.

3. Identify 0 as the additive identity and 1 as the multiplicative identity for non-negative rational numbers; recognize 0 as the absorbing element of multiplication.

4. Use the fraction bar to represent the quotient of two rational numbers, designating it as "ratio".

5. Identify two positive rational numbers as "inverses" when their product equals 1; recognize that the inverse of a positive rational number *q* equals 1/q.

6. Recognize that the inverse of a/b is b/a (where a and b are natural numbers); recognize that dividing by a positive rational number is equivalent to multiplying by its inverse.

7. Recognize that the inverse of the product (or quotient) of two positive rational numbers equals the product (or quotient) of the inverses.

8. Recognize that for positive rational numbers q, r, s and t: (q/r) × (s/t) = (q×s)/(r×t); conclude that the inverse of q/r is r/q.

9. Recognize that for positive rational numbers q, r, s and t: (q/r)/(s/t) = (q×t)/(r×s).

10. Simplify and calculate the value of numerical expressions involving the four arithmetic operations and use of parentheses.

11. Translate mathematical statements expressed in natural language into symbolic language and vice versa, knowing that the multiplication sign can be omitted between numbers and letters and between letters, and a dot can be used in this place.

**Modification Date:** August 26, 2016

### RATIONAL NUMBERS: ADDITION AND SUBTRACTION

#### Math Summary/Synthesis
Available soon

#### Exercises
Available soon

#### Learning Objectives - Curriculum Program and Goals

**Domain:** NUMBERS AND OPERATIONS (NO6)
**Subdomain:** RATIONAL NUMBERS

##### ADDITION OF RATIONAL NUMBERS

**1. Identify oriented segment**
- Definition: "line segment in which an origin is chosen from one of the two endpoints"
- Notation: [A,B] represents the oriented segment with origin A and endpoint B

**2. Segment Orientation**
- **Positively oriented:** when the first number is less than the second
- **Negatively oriented:** when the first number is greater than the second

**3. Sum of Rational Numbers**
- The sum a + b is the abscissa of the endpoint of a segment with origin at A
- The segment has length and orientation of segment [0,B]
- Extends the definition of addition of non-negative numbers to all rationals

**4. Sum with Same Sign**
- The sum has the same sign as the addends
- Absolute value of sum = sum of absolute values of addends

**5. Sum with Opposite Signs (not symmetric)**
- The result has the sign of the addend with greater absolute value
- Absolute value = difference between the greater and lesser of the absolute values

**6. Properties of Addition**
- Any number + 0 = the number itself
- Sum of symmetric numbers = 0

##### SUBTRACTION OF RATIONAL NUMBERS

**1. Difference between Rational Numbers**
- The difference a – b is "the number whose sum with b equals a"
- Extension from non-negative rationals to all rationals

**2. Relationship between Subtraction and Addition**
- a – b = a + (–b), that is, subtraction is equivalent to addition of the opposite
- General term: "algebraic sum" for sum and difference

**3. Subtraction by Zero**
- 0 – q = –q (opposite of number q)

**4. Opposite of the Opposite**
- –(–q) = q

**5. Absolute Value of Rational Number**
- If q > 0: |q| = q
- If q < 0: |q| = –q

**6. Distance between Points**
- Measure of distance between points with abscissas a and b = |b – a| = |a – b|

**Modification Date:** August 21, 2016

### FIRST DEGREE EQUATIONS

#### SUMMARY

##### 4. First degree equations

###### 4.1. Algebraic expressions

**Meaning of algebraic expression**

- **Algebraic expression**
  - expression with letters and numbers related by operations
  - Example: 2n + 1

- **Terms of an algebraic expression**
  - are separated by + and – signs
  - consist of a coefficient and may have a literal part
  - Example: 2n + 1
    - the term 2n has coefficient 2 and literal part n
    - the term 1 has only coefficient 1

**Reduced algebraic expression**

- **Simplify an algebraic expression**
  - reduce like terms (that have the same literal part)
  - Example: 3b + 2b + 5 + 4m – 3 + 4n – 3m = 5b + 2 + m + 4n

###### 4.2. Equations

**Meaning of equation**

- **Equation**
  - equality between two numerical expressions in which there is at least one unknown (letter)
  - Example: 3b + 5 = 11

**Solution of an equation and equivalent equations**

- **Solution of an equation**
  - numerical value of the unknown that transforms the equation into a true statement
  - Example: 3b + 5 = 11
    - 3 × 2 + 5 = 11 → 2 is a solution

- **Solution set of an equation**
  - set of solutions of an equation
  - Example: |2 + c| = 4
    - |2 + 2| = 4 → 2 is a solution
    - |2 + (-6)| = 4 → -6 is also a solution
    - S.S. = (-6, 2)

- **Equivalent equations**
  - have the same solution set

**Elements of an equation**

- **1st member**
  - expression to the left of the equals sign

- **2nd member**
  - expression to the right of the equals sign

- **Unknowns**
  - letters present in the equation

- **Dependent terms**
  - terms with unknown

- **Independent terms**
  - terms without unknown

**Solving first degree equations with one unknown**

- **Addition equivalence principle**
  - adding or subtracting the same expression to both members yields an equivalent equation
  - Example: 2x + 4 = x + 10 ⇔ 2x + 4 – x = x + 10 – x ⇔ x + 4 = 10 ⇔ x + 4 – 4 = 10 – 4 ⇔ x = 6

- **Multiplication equivalence principle**
  - multiplying or dividing both members by a number different from zero yields an equivalent equation
  - Example: 2x = 6 ⇔ 2x : 2 = 6 : 2 ⇔ x = 3

- **Practical rule**
  - any term can be moved from one member to another by changing its sign
  - Example: 3x + 4 = x + 10 ⇔ 3x – x = 10 – 4 ⇔ 2x = 6 ⇔ x = 6 : 2 ⇔ x = 3

**Classification of equations**

- **Equation**
  - possible determinate → x = 5 ; S.S. = {5}
  - possible indeterminate → 0x = 0 ; S.S. = ℝ
  - impossible → 0x = 5 ; S.S. = {}

#### INTERACTIVE EXERCISES

#### TO PRINT

**Material review**

**Exercise sheets**

**Tests**

#### MORE RESOURCES

##### LESSONS AND WORKSHEETS #ESTUDOEMCASA

**#EstudoEmCasa 2020/2021**

- **23** | Equations (1) — [watch lesson](https://www.rtp.pt/play/estudoemcasa/p7829/e518433/matematica-7-e-8-anos) · [worksheet](https://estudoemcasa-2020-2021.s3.eu-west-3.amazonaws.com/resources/cf80e8e6744013ae12f2743735175273/23_Matem%C3%A1tica_7%C2%BA%20e%208%C2%BA%20anos_Equa%C3%A7%C3%B5es%20%281%29.pdf?v8GfMweX.a7PnAvcDu.JTewmQ4GG0uXw)

- **24** | Equations (2) — [watch lesson](https://www.rtp.pt/play/estudoemcasa/p7829/e518997/matematica-7-e-8-anos) · [worksheet](https://estudoemcasa-2020-2021.s3.eu-west-3.amazonaws.com/resources/ff4d2f911063b10a36856d5b050fec0e/24_Matem%C3%A1tica_7%C2%BA%20e%208%C2%BA%20anos_Equa%C3%A7%C3%B5es%20%282%29.pdf?2zoK89DgFEAshR2G3bHhi9a5CGZEEWHF)

- **25** | Equations (3) — [watch lesson](https://www.rtp.pt/play/estudoemcasa/p7829/e519970/matematica-7-e-8-anos) · [worksheet](https://estudoemcasa-2020-2021.s3.eu-west-3.amazonaws.com/resources/23f6e43995491f97b2ae503a2d35032c/25_Matem%C3%A1tica_7%C2%BA%20e%208%C2%BA%20anos_Equa%C3%A7%C3%B5es%20%283%29.pdf)

- **26** | Equations (4) — [watch lesson](https://www.rtp.pt/play/estudoemcasa/p7829/e520409/matematica-7-e-8-anos) · [worksheet](https://estudoemcasa-2020-2021.s3.eu-west-3.amazonaws.com/resources/28d7ca731b2704c27e20e80881832fb3/26_Matem%C3%A1tica_7%C2%BA%20e%208%C2%BA%20anos_Equa%C3%A7%C3%B5es%20%284%29.pdf)

- **27** | Equations (5) — [watch lesson](https://www.rtp.pt/play/estudoemcasa/p7829/e521463/matematica-7-e-8-anos) · [worksheet](https://estudoemcasa-2020-2021.s3.eu-west-3.amazonaws.com/resources/de079a38ccdb62dfba7a583c4f7aca3d/27_Matem%C3%A1tica_7%C2%BA%20e%208%C2%BA%20anos_Equa%C3%A7%C3%B5es%20%285%29.pdf?oa2a3c2Jp0KE7VCrzZndrxN049LA64Wt)

- **28** | Equations (6) — [watch lesson](https://www.rtp.pt/play/estudoemcasa/p7829/e522047/matematica-7-e-8-anos) · [worksheet](https://estudoemcasa-2020-2021.s3.eu-west-3.amazonaws.com/resources/057f7d8ada53f71c36bccae15807c677/28_Matem%C3%A1tica_7%C2%BA%20e%208%C2%BA%20anos_Equa%C3%A7%C3%B5es%20%286%29.pdf?5lhZDfYKlh.RKgk311sBvf.FHe.Zvh0C)

**#EstudoEmCasa 2019/2020**

- **9** | Equations 1 — [watch lesson](https://www.rtp.pt/play/estudoemcasa/p7133/e473669/matematica-7-e-8-anos) · [worksheet](https://estudoemcasa.s3.eu-west-3.amazonaws.com/resources/23eb4676066841fe285a00afec69ef65/Equacoes_1.pdf)

- **10** | Equations 2 — [watch lesson](https://www.rtp.pt/play/estudoemcasa/p7133/e474274/matematica-7-e-8-anos) · [worksheet](https://estudoemcasa.s3.eu-west-3.amazonaws.com/resources/80eabb5cf1701e55f95e7377d7f912b4/Equacoes_2.pdf)

- **11** | Equations 3 — [watch lesson](https://www.rtp.pt/play/estudoemcasa/p7133/e475203/matematica-7-e-8-anos) · [worksheet](https://estudoemcasa.s3.eu-west-3.amazonaws.com/resources/190b77c5222c4589062f023c7c3b4eb2/Equa%C3%A7%C3%B5es_3.pdf)

#### ESSENTIAL LEARNING

- Recognize equations and distinguish between terms with unknown and independent terms.
- Translate situations in mathematical and non-mathematical contexts through a first degree equation and vice versa.
- Present and explain ideas and processes involving first degree equations with one unknown.
- Solve first degree equations with one unknown (without parentheses and denominators).
- Justify the equivalence of two equations.
- Solve problems involving first degree equations with one unknown, particularly from students' daily lives, analyzing the adequacy of the solution obtained in the problem's context.

#### RELATED TOPICS - MATHEMATICS 7TH GRADE

- [Integer numbers – addition and subtraction](https://www.obichinhodosaber.com/matematica-7o-ano-numeros-inteiros-adicao-e-subtracao/)
- [Rational numbers – addition, subtraction, percentage and scientific notation](https://www.obichinhodosaber.com/matematica-7o-numeros-racionais/)
- [Sequences and successions](https://www.obichinhodosaber.com/matematica-7o-ano-sequencias-e-sucessoes/)
- [Functions and direct proportionality](https://www.obichinhodosaber.com/matematica-7o-ano-funcoes-e-proporcionalidade-direta/)
- [Statistical study](https://www.obichinhodosaber.com/matematica-7o-ano-estudo-estatistico/)
- [Probabilities](https://www.obichinhodosaber.com/matematica-7o-ano-probabilidades/)
- [Plane figures – angles, quadrilaterals and areas](https://www.obichinhodosaber.com/matematica-7o-ano-figuras-planas-angulos-quadrilateros-e-areas/)
- [Operations with figures – similarities](https://www.obichinhodosaber.com/matematica-7o-ano-operacoes-com-figuras-semelhancas/)
- [Figures in space – regular polyhedra, prisms and pyramids](https://www.obichinhodosaber.com/matematica-7o-ano-figuras-no-espaco-solidos-geometricos/)

# Sequences and Patterns

### Mathematics 6th grade | Sequences and regularities

#### Introduction

This is an educational resource page from "O Bichinho do Saber" focused on 6th grade mathematics, specifically on the topic of sequences and regularities.

- Main material/summary
- Exercise materials

#### Curriculum Requirements

The page presents the official curriculum standards under **Domain: Algebra (ALG6)**, **Subdomain: Sequences and Regularities**.

Students should develop skills in three problem-solving areas:

1. **Determination of sequence terms** using generating expressions or formation rules based on preceding terms

2. **Formulas for generating expressions** for sequences defined by formation laws that depend on previous elements

3. **Identification of formation laws** for partially known sequences, expressed in natural and symbolic language

#### Navigation Context

The page is positioned within the broader 6th grade mathematics curriculum structure on the website, with links to other mathematical topics and grade levels.

### Mathematics 7th grade | Sequences and successions

This is an educational resource page from "O Bichinho do Saber" covering sequences and successions for 7th grade mathematics students.

#### Main Content Structure

**Main Topics Covered:**

##### 1. Formation Law of a Sequence or Succession

**Numerical Sequence**
- Definition: an "ordered list of numbers"
- Each number represents a term; the position is called order
- Example: 1, 3, 5, 7 where 1 is order 1, 3 is order 2, etc.
- Finite sequence with a limited number of terms

**Succession**
- Defined as an infinite sequence
- Sequence with infinite terms
- Represented as: "1, 3, 5, 7, …"

##### 2. General Term

**Concept:**
- Algebraic expression that relates each term to its order
- For the sequence 1, 3, 5, 7: the general term is 2n – 1
- The algebraic expression connects each term to its position

**Method to Discover the General Term:**

When the difference between consecutive terms is constant:
- Multiply that constant difference by n
- Then adjust as needed

**Examples:**

*Example 1:* Sequence 2, 4, 6, 8
- Constant difference: 2
- General term: 2n

*Example 2:* Sequence 3, 5, 7, 9
- Constant difference: 2
- If the first term differs, add the corresponding difference
- General term: 2n + 1

##### 3. Finding Terms from the General Term

**Method:**
- Replace n with the order of the desired term

**Calculation examples** (using general term 2n – 1):
- Order 1: 2(1) – 1 = 1
- Order 2: 2(2) – 1 = 3
- Order 5: 2(5) – 1 = 9

#### Available Resources

**For Printing:**
- Exercise worksheets on regularities and sequences (two levels available)

**Interactive Content:**
- Video tutorials referenced throughout the page
- Lessons for home study (#EstudoEmCasa) from 2020/2021 and 2019/2020
- Links to RTP educational broadcasts

**Related Topics in the Series:**
Nine additional 7th grade mathematics units covering integers, equations, functions, statistics, geometry and more.

### Mathematics 9th grade | Sequences and regularities

**Title:** Mathematics 9th grade | Sequences and regularities - O Bichinho do Saber

**Main Topic:** Educational resource page for 9th grade mathematics focusing on sequences and regularities.

#### Page Content

This is a summary and educational resources page from the "O Bichinho do Saber" website about sequences and regularities for 9th grade students.

#### Main Structure

The page is organized into several sections:

##### SUMMARY

The page indicates there is a summary section with a video reference for "Sequences and regularities," although the detailed content indicates "(see video)" - with the actual summary content not fully displayed.

Presents the concept of "Sequences and regularities" with reference to a video (not visible in the extracted content).

##### POWERPOINT PRESENTATION

##### YOUTUBE VIDEOS

##### LESSONS AND WORKSHEETS #ESTUDOEMCASA

The page provides lessons from the Portuguese distance education initiative:

**2020/2021 Program:**
- **Lesson 21:** "Sequences (1)" with video and worksheet
- **Lesson 22:** "Sequences (2)" with video and worksheet
- **Lesson 23:** "Sequences (3)" with video and worksheet

References to three study sessions (Lessons 21-23) on "Sequences" with accompanying worksheets via the RTP educational platform.

**2019/2020 Program:**
- **Lesson 9:** "Regularities" with video and supplementary material

##### EXERCISES

##### APRENDIZAGENS ESSENCIAIS (Essential Learning Outcomes)

The page defines as a fundamental objective:

**Students should:** "Recognize regularities and determine a formation law for a sequence of rational numbers and an algebraic expression (including second-degree ones) that represents it."

Translation: Recognize patterns and determine formation rules for sequences of rational numbers and algebraic expressions, including second-degree expressions.

##### REFERENCE DOCUMENTS

Includes links to official curriculum documents:
- Essential Learning Outcomes
- Student Profile
- Mathematics Program

#### Related Topics

Links to other 9th grade mathematics units including:
- Real Numbers
- Geometric Figures
- Areas and Volumes
- Trigonometry
- Equations
- Inequalities
- Functions
- Statistical Planning
- Probability

#### Thematic Navigation

Presents other 9th Grade Mathematics units: Real Numbers, Geometric Figures, Areas and Volumes, Trigonometry, Equations, Inequalities, Functions, Statistical Planning and Probability.

# Equations and Inequalities

### Mathematics 7th grade | First-degree equations

## SUMMARY

### **4. First-degree equations**

#### **4.1. Algebraic expressions**

**Meaning of algebraic expression**

• **Algebraic expression**
  - expression with letters and numbers related by operations
  - example: 2n + 1

• **Terms of an algebraic expression**
  - are separated by the + and – signs
  - consist of a coefficient and may have a literal part
  - example: 2n + 1
    - the term 2n has coefficient 2 and literal part n
    - the term 1 has only coefficient 1

**Reduced algebraic expression**

• **Simplifying an algebraic expression**
  - reduce like terms (that have the same literal part)
  - example: 3b + 2b + 5 + 4m – 3 + 4n – 3m = 5b + 2 + m + 4n

(see video)

#### **4.2. Equations**

**Meaning of equation**

• **Equation**
  - equality between two numerical expressions in which there is at least one unknown (letter)
  - example: 3b + 5 = 11

**Solution of an equation and equivalent equations**

• **Solution of an equation**
  - numerical value of the unknown that transforms the equation into a true statement
  - example: 3b + 5 = 11
    - 3 × 2 + 5 = 11 → 2 is a solution

• **Solution set of an equation**
  - set of solutions of an equation
  - example: |2 + c| = 4
    - |2 + 2| = 4 → 2 is a solution
    - |2 + (-6)| = 4 → -6 is also a solution
    - S.S. = (-6, 2)

• **Equivalent equations**
  - have the same solution set

**Elements of an equation**

• **1st member**
  - expression to the left of the equal sign

• **2nd member**
  - expression to the right of the equal sign

• **Unknowns**
  - letters present in the equation

• **Dependent terms**
  - terms with unknown

• **Independent terms**
  - terms without unknown

**Solving first-degree equations with one unknown**

• **Addition equivalence principle**
  - adding or subtracting the same expression to both members yields an equivalent equation
  - example: 2x + 4 = x + 10 ⇔
  - ⇔ 2x + 4 – x = x + 10 – x ⇔
  - ⇔ x + 4 = 10 ⇔
  - ⇔ x + 4 – 4 = 10 – 4 ⇔
  - ⇔ x = 6

• **Multiplication equivalence principle**
  - multiplying or dividing both members by a number different from zero yields an equivalent equation
  - example: 2x = 6 ⇔
  - ⇔ 2x : 2 = 6 : 2 ⇔
  - ⇔ x = 3

• **Practical rule**
  - any term can be moved from one member to another by changing its sign
  - example: 3x + 4 = x + 10 ⇔
  - ⇔ 3x – x = 10 – 4 ⇔
  - ⇔ 2x = 6 ⇔
  - ⇔ x = 6 : 2 ⇔
  - ⇔ x = 3

**Classification of equations**

• **Equation**
  - possible determinate → x = 5 ; S.S. = {5}
  - possible indeterminate → 0x = 0 ; S.S. = ℝ
  - impossible → 0x = 5 ; S.S. = {}

## INTERACTIVE EXERCISES

## TO PRINT

**Review of content**

**Exercise worksheets**

**Tests**

## MORE RESOURCES

### POWERPOINTS
(No content listed)

### VIDEOS
(No content listed)

### LESSONS AND WORKSHEETS #ESTUDOEMCASA

**#EstudoEmCasa 2020/2021**

**23 | Equations (1)** » see lesson · worksheet

**24 | Equations (2)** » see lesson · worksheet

**25 | Equations (3)** » see lesson · worksheet

**26 | Equations (4)** » see lesson · worksheet

**27 | Equations (5)** » see lesson · worksheet

**28 | Equations (6)** » see lesson · worksheet

**#EstudoEmCasa 2019/2020**

**9 | Equations 1** » see lesson ⋅ worksheet

**10 | Equations 2** » see lesson ⋅ worksheet

**11 | Equations 3** » see lesson ⋅ worksheet

### ESSENTIAL LEARNING

- Recognize equations and distinguish between terms with unknowns and independent terms.
- Translate situations in mathematical and non-mathematical contexts through a first-degree equation and vice versa.
- Present and explain ideas and processes involving first-degree equations with one unknown.
- Solve first-degree equations with one unknown (without parentheses and denominators).
- Justify the equivalence of two equations.
- Solve problems involving first-degree equations with one unknown, particularly from students' daily lives, analyzing the adequacy of the solution obtained in the context of the problem.

## RELATED TOPICS (7TH GRADE | MATHEMATICS)

- Integer numbers – addition and subtraction
- Rational numbers – addition, subtraction, percentage and scientific notation
- Sequences and progressions
- First-degree equations
- Functions and direct proportionality
- Statistical study
- Probability
- Plane figures – angles, quadrilaterals and areas
- Operations with figures – similarities
- Figures in space – regular polyhedra, prisms and pyramids

### Part 1: Second-degree equations

**Mathematics 9th grade | Second-degree equations**

## SUMMARY | MATHEMATICS 9TH GRADE

### **EQUATIONS**

#### First-degree equations

**›  Solving first-degree equations with parentheses and denominators (review)**
_see video_

#### Second-degree equations

**›  Solving incomplete second-degree equations (review)**
_see video_

**›  Completing the square**
_see video_

**›  Solving complete second-degree equations**

»  Solution by completing the square
_see video_

»  Solution using the quadratic formula
_see video_

**›  Discriminant binomial**

»  Finding the number of solutions of a second-degree equation
_see video_

»  Finding the value of an unknown knowing the number of solutions
_see video_

## POWERPOINT PRESENTATION

## YOUTUBE VIDEOS

## LESSONS AND WORKSHEETS #ESTUDOEMCASA

### #EstudoEmCasa 2020/2021

**Lesson 24** | "Second-Degree Equations (1)" » [see lesson](https://www.rtp.pt/play/estudoemcasa/p7823/e520918/matematica-9-ano) · [worksheet](https://estudoemcasa-2020-2021.s3.eu-west-3.amazonaws.com/resources/9b5bf5956a8eff8850be167a3f03035c/24_Matem%C3%A1tica_9%C2%BA%20ano_Equa%C3%A7%C3%B5es%20do%202.%C2%BA%20Grau%20%281%29.pdf)

**Lesson 25** | "Second-Degree Equations (2)" » [see lesson](https://www.rtp.pt/play/estudoemcasa/p7823/e521753/matematica-9-ano) · [worksheet](https://estudoemcasa-2020-2021.s3.eu-west-3.amazonaws.com/resources/a87f2c689496d9dc5b977ad9a71a13d1/25_Matem%C3%A1tica_9%C2%BA%20ano_Equa%C3%A7%C3%B5es%20do%202.%C2%BA%20grau%20%282%29.pdf?qQo7umc4FpCFwpRUBJo4Cu0gi_eNSPj4)

**Lesson 26** | "Second-Degree Equations (3)" » [see lesson](https://www.rtp.pt/play/estudoemcasa/p7823/e522546/matematica-9-ano) · [worksheet](https://estudoemcasa-2020-2021.s3.eu-west-3.amazonaws.com/resources/dd8a9ad2da34e5bdd38b3f608949b46c/26_Matem%C3%A1tica_9%C2%BA%20ano_Equa%C3%A7%C3%B5es%20do%202.%C2%BA%20Grau%20%283%29.pdf?mGB_d3MhTvSX7wPH_OP7B_xw1f_cEqhm)

**Lesson 27** | "Solving complete second-degree equations. Quadratic formula" » [see lesson](https://www.rtp.pt/play/estudoemcasa/p7823/e523349/matematica-9-ano) · [worksheet](https://estudoemcasa-2020-2021.s3.eu-west-3.amazonaws.com/resources/72a2e7cf1f5a5e4b839da95e92a6885c/27_Matem%C3%A1tica_9%C2%BA%20ano_Resolu%C3%A7%C3%A3o%20de%20equa%C3%A7%C3%B5es%20do%202.%C2%BA%20grau%20completas.%20F%C3%B3rmula%20resolvente.pdf?FRZbcX.niIFA_CQC4ZODM1WUbXrw6CG7)

**Lesson 28** | "Number of solutions of a second-degree equation​" » [see lesson](https://www.rtp.pt/play/estudoemcasa/p7823/e523947/matematica-9-ano) · [worksheet](https://estudoemcasa-2020-2021.s3.eu-west-3.amazonaws.com/resources/55b3cd13532705dcb441e37617a4a257/28_Matem%C3%A1tica_9%C2%BA%20ano_N%C3%BAmero%20de%20solu%C3%A7%C3%B5es%20de%20uma%20equa%C3%A7%C3%A3o%20do%202.%C2%BA%20grau%E2%80%8B.pdf?Jdb8BnOFrEqVmkgVyoZ9xLoxMUFm15jx)

**Lesson 29** | "Solving problems involving second-degree equations" » [see lesson](https://www.rtp.pt/play/estudoemcasa/p7823/e525390/matematica-9-ano) · [worksheet](https://estudoemcasa-2020-2021.s3.eu-west-3.amazonaws.com/resources/4ac3d37ce30acef6df061ebc4b1184c8/29_Matem%C3%A1tica_9%C2%BA%20ano_Resolu%C3%A7%C3%A3o%20de%20problemas%20envolvendo%20equa%C3%A7%C3%B5es%20do%202.%C2%BA%20grau.pdf?XIcH93mAp6S7xjvtjP3o030BmolTyM9c)

**Lesson 30** | "Solving problems involving second-degree equations" » [see lesson](https://www.rtp.pt/play/estudoemcasa/p7823/e526099/matematica-9-ano) · [worksheet](https://estudoemcasa-2020-2021.s3.eu-west-3.amazonaws.com/resources/68c00acdff989d8af2d996e18374c6d2/30_Matem%C3%A1tica_9%C2%BA%20ano_Resolu%C3%A7%C3%A3o%20de%20problemas%20envolvendo%20equa%C3%A7%C3%B5es%20do%202.%C2%BA%20grau.pdf?brZtzeFyOT3tLL73.vUJhpOSWqZ5OO8X)

### #EstudoEmCasa 2019/2020

**Lesson 10** | "More than one solution" » [see lesson](https://www.rtp.pt/play/estudoemcasa/p7134/e473221/matematica-9-ano) · [worksheet](https://estudoemcasa.s3.eu-west-3.amazonaws.com/resources/442188f2169e7899a55c634c00a26a87/Mais%20do%20que%20uma%20solu%C3%A7%C3%A3o.pdf)

**Lesson 11** | "A special formula" » [see lesson](https://www.rtp.pt/play/estudoemcasa/p7134/e474524/matematica-9-ano) · [worksheet](https://estudoemcasa.s3.eu-west-3.amazonaws.com/resources/ef7506e8f08f58417c659dd2bb0863e2/Ativ_Complemento_aula_11.pdf)

## EXERCISES

## ESSENTIAL LEARNING

- "Recognize, interpret and solve first- and second-degree equations with one unknown and use them to" represent situations in mathematical and non-mathematical contexts.

## CURRICULAR REFERENCE DOCUMENTS

›    Essential Learning
›    Student Profile (upon leaving compulsory schooling)
›    Program and Curricular Standards – revoked

### Part 2: Inequalities

**Mathematics 9th grade | Inequalities**

## SUMMARY | MATHEMATICS 9TH GRADE

**INEQUALITIES**

**Topics:**
1. Inequalities
2. Solving inequalities (see video)
3. Conjunction and disjunction of inequalities (see video)

## POWERPOINT PRESENTATION

## YOUTUBE VIDEOS

## LESSONS AND WORKSHEETS #ESTUDOEMCASA

### #EstudoEmCasa 2020/2021

**Lesson 9** | "Inequalities" » see lesson · worksheet

**Lesson 10** | "Body Mass Index" » see lesson · worksheet

**Lesson 11** | "A place with history" » see lesson · worksheet

**Lesson 12** | "Conjunction and disjunction of inequalities" » see lesson · worksheet

**Lesson 13** | "Solving problems involving inequalities" » see lesson · worksheet

### #EstudoEmCasa 2019/2020

**Lesson 3** | "A trip to the stadium" » see lesson · worksheet

## ESSENTIAL LEARNING

"Recognize, interpret and solve first-degree inequalities with one unknown" and use them to represent situations in mathematical and non-mathematical contexts.

## CURRICULAR REFERENCE DOCUMENTS

- Essential Learning
- Student Profile (upon leaving compulsory schooling)
- Program and Curricular Standards – revoked

## RELATED TOPICS (9TH GRADE | MATHEMATICS)

- Real numbers
- Geometric figures
- Areas and volumes
- Trigonometry
- Sequences and patterns
- Equations
- Inequalities
- Functions
- Statistical planning and data processing
- Probability

# Functions

### Mathematics Grade 6 | Direct proportionality

### Content Status

- Topic summary/review
- Exercises

### Curriculum Learning Objectives

The page describes what students should know according to Portuguese curriculum standards in the **ALGEBRA domain (ALG6), subdomain DIRECT PROPORTIONALITY**:

#### Relating directly proportional quantities:

- Identify when one quantity is directly proportional to another
- Recognize constant ratios in proportional relationships
- Understand mutual proportionality and inverse constants
- Define proportions, extremes, means, and terms
- Apply the property that "the product of the means equals the product of the extremes"
- Solve proportions using the rule of three or other calculation methods
- Understand scale relationships on maps

#### Problem-solving competencies:

- Distinguish dependent quantities and identify proportional relationships
- Solve problems involving direct proportionality

### Mathematics Grade 7 | Functions and direct proportionality

This page provides comprehensive content on functions and direct proportionality for 7th grade mathematics students, aligned with the Portuguese national curriculum.

### SUMMARY | MATHEMATICS GRADE 7

#### 5.1 Functions

**Function Definition:**

"correspondence between two sets in which each element of the domain set corresponds to one and only one element of the codomain set"

**Key Terminology:**

- **Objects:** elements of the domain set
- **Images:** elements of the codomain set with correspondence
- **Domain (D):** set of objects
- **Codomain (D'):** set of images
- **Independent variable:** represents the objects (usually x)
- **Dependent variable:** represents the images (usually y)

**Forms of Representation:**

Functions can be represented through:
- Arrow diagram
- Table
- Algebraic expression
- Graph
- Cartesian coordinate system

**Working with Algebraic Expressions:**

Functions use notation such as:
- y = 2x or f(x) = 2x

relating independent and dependent variables.

To find images: substitute x with the value of the object
To find objects: substitute y with the value of the image and solve the equation

**Function Variation:**

- **Increasing:** the dependent variable increases when the independent variable increases
- **Constant:** the dependent variable remains unchanged
- **Decreasing:** the dependent variable decreases when the independent variable increases

#### 5.2 Direct Proportionality Function

**Directly proportional quantities:** have a constant ratio.

A direct proportionality function has the form **f(x) = kx**, where k represents the direct proportionality constant.

**The constant k:**

- Is equal to f(1)
- Is calculated as k = f(x) ÷ x
- If k > 0: the function is increasing
- If k < 0: the function is decreasing

**Graphical Representation:**

Graphically, direct proportionality functions appear as "a line passing through the origin of the coordinate system", with steeper slopes for larger absolute values of k.

### Additional Resources

### Mathematics Grade 8 | Graphs of affine functions

This educational resource page from "O Bichinho do Saber" presents study materials for 8th grade mathematics, specifically focused on "Graphs of affine functions".

### Main Content

**Topic:** Affine function (Função Afim)

The page features an embedded educational presentation from SlideShare titled "Gráficos de funções afim – Matemática 8º ano – Resumo da matéria" (Graphs of affine functions – Mathematics Grade 8 – Summary of the Material).

### Associated Tags and Topics

The page includes multiple topic tags:

- **declive da reta** (slope of the line)
- **equação da reta não vertical** (equation of a non-vertical line)
- **equação da reta vertical** (equation of a vertical line)
- **função afim** (affine function)
- **função constante** (constant function)
- **função linear** (linear function)
- **gráfico de uma função afim** (graph of an affine function)
- **ordenada na origem** (y-intercept)
- **retas paralelas** (parallel lines)

### SlideShare Presentation Content

**Title:** "Gráficos de funções afim - Matemática 8º ano - Resumo da matéria"

**Platform:** SlideShare

**Format:** PowerPoint presentation (PPTX)

**Language:** Portuguese

#### Content Covered in the Presentation:

1. **Graphical representation of constant functions** - functions where the value remains invariable

2. **Linear functions** - functions that pass through the origin

3. **Affine functions** - functions of the type f(x) = ax + b

4. **Associated equations**, including:
   - Vertical lines
   - Parallel lines

5. **Determining parameters:**
   - Slope (angular coefficient)
   - Y-intercept (linear coefficient)

6. **Practical examples** with corresponding equations and graphical representations

The material works as a structured summary for 8th grade mathematics students, focusing on visualization and understanding of fundamental concepts related to affine functions.

### Learning Objectives

According to the Portuguese curriculum, students should:
- Recognize affine functions
- Represent them using multiple formats (graphs, algebraic expressions, tables)
- Apply them to model real situations
- Linear functions are presented as a special case of affine functions

### Mathematics Grade 9 | Functions

**Modification Date:** February 14, 2024

### Main Structure

The page is organized around **"Functions (affine, direct proportionality, and quadratic)"** with the following sections:

### SUMMARY | MATHEMATICS GRADE 9

#### Inverse proportionality function

**Topics:**
- Direct proportionality vs inverse proportionality
- Representation of an inverse proportionality function

**Note:** The topics show the indication "_see video_" but are not functional links.

#### Quadratic function

**Topics:**
- Affine functions, direct proportionality function, and quadratic function
- Representation of a quadratic function

**Note:** The topics show the indication "_see video_" but are not functional links.

### LESSONS AND WORKSHEETS #ESTUDOEMCASA

#### #EstudoEmCasa 2020/2021

**Lesson 14:** "Directly proportional quantities. Direct proportionality function"

**Lesson 15:** "Inversely proportional quantities"

**Lesson 16:** "Inverse proportionality as a function"

**Lesson 17:** "Problem solving involving inverse proportionality"

**Lesson 18:** "Graphical representation of functions of the type f(x)=ax², with a≠0"

**Lesson 19:** "Problem solving involving functions (1)"

**Lesson 20:** "Problem solving involving functions (2)"

#### #EstudoEmCasa 2019/2020

**Lesson 12:** "Constant products"

**Lesson 13:** "Everything in reverse"

**Lesson 14:** "The curve of squares"

**Lesson 15:** "Miscellany of functions"

**Note:** These lessons include links to RTP broadcasts and PDFs of worksheets available in cloud storage (estudoemcasa-2020-2021.s3.eu-west-3.amazonaws.com).

### ESSENTIAL LEARNING

Students should be able to:

"Recognize a function in various representations, and interpret it as a relationship between variables and as a one-to-one correspondence between two sets, and use functions" for diverse contexts.

"Represent and interpret graphically a function (including inverse proportionality and of the type 𝑦 = 𝑎𝑥², 𝑎 ≠ 0), and relate the graphical representation with the algebraic one."

### Additional Content

### Related Topics in Grade 9 Curriculum

- Real numbers – intervals, order relations, and approximate values
- Geometric Figures (Circumference and geometric loci)
- Areas and Volumes
- Trigonometry
- Sequences and regularities
- Equations (2nd degree equations)
- Inequalities
- Statistical planning and Data treatment (Statistical study - histograms and box plots)
- Probability

## Progression Through the Years

### Grade 6: Foundations
- Introduction to direct proportionality
- Recognition of constant ratios
- Rule of three and solving proportions

### Grade 7: Function Concept
- Formal definition of function
- Multiple representations (diagrams, tables, algebraic expressions, graphs)
- Increasing, decreasing, and constant functions
- Direct proportionality function f(x) = kx

### Grade 8: Affine Functions
- Extension to affine functions f(x) = ax + b
- Linear functions as a special case
- Constant functions
- Slope and y-intercept
- Equations of lines (vertical and non-vertical)
- Parallel lines

### Grade 9: Expanding the Repertoire
- Review of affine functions and direct proportionality
- Introduction to inverse proportionality
- Quadratic functions f(x) = ax², a ≠ 0
- Interpretation and graphical representation of multiple types of functions
- Problem solving with various types of functions


\cleardoublepage

# GEOMETRY

# Basic Elements

**Source URLs:**
- https://www.obichinhodosaber.com/2016/08/20/matematica-5o-ano-angulos-paralelismo-perpendicularidade/
- https://www.obichinhodosaber.com/2016/08/20/matematica-5o-ano-medida-amplitude-angulos/

### Mathematics 5th Grade | Angles, Parallelism and Perpendicularity

**GEOMETRIC PROPERTIES:**

**ANGLES, PARALLELISM AND PERPENDICULARITY**

Review the material/summary/synthesis here:

_Video synthesis provided by RjasMatemática (www.matexplica.pt)_

**EXERCISES**

**What you need to know in this chapter, according to the Mathematics curriculum and learning goals – 5th grade:**

**DOMAIN: GEOMETRY AND MEASUREMENT (GM5)**

**SUBDOMAIN: GEOMETRIC PROPERTIES**

**ANGLES, PARALLELISM AND PERPENDICULARITY**

- Recognize properties involving angles, parallelism and perpendicularity

1. Identify a non-complete angle _a_ as the sum of two angles _b_ and _c_ if _a_ is equal to the union of two adjacent angles _b'_ and _c'_ respectively equal to _b_ and _c_.
2. Identify a complete angle as equal to the sum of two other angles if these are equal respectively to two non-coincident angles with the same sides.
3. Construct an angle equal to the sum of two other angles using a straightedge and compass.
4. Designate as the "bisector" of a given angle the half-line contained within it, originating from the vertex and forming equal angles with each side, and construct it using a straightedge and compass.
5. Identify two angles as "supplementary" when their sum is equal to a straight angle.
6. Identify two angles as "complementary" when their sum is equal to a right angle.
7. Recognize that vertically opposite angles are equal.
8. Identify two half-lines with the same supporting line as having "the same direction" if one contains the other.
9. Identify two half-lines with distinct supporting lines as having "the same direction" if they are parallel and contained in the same half-plane determined by their respective origins.
10. Use correctly the expressions "directly parallel half-lines" and "inversely parallel half-lines".
11. Identify, given two half-lines _OA_ and _VC_ contained on the same line and with the same direction, and two points _B_ and _D_ belonging to the same half-plane defined by line _OV_, the angles _AOB_ and _CVD_ as "corresponding" and know that they are equal when (and only when) lines _OB_ and _VD_ are parallel.
12. Construct parallel line segments using a straightedge and set square, utilizing any pair of sides of the set square.
13. Identify, given two lines _r_ and _s_ intersected by a transversal, "interior angles" and "exterior angles" and pairs of "alternate interior" and "alternate exterior" angles, and recognize that the angles of each of these pairs are equal when (and only when) _r_ and _s_ are parallel.
14. Recognize that two coplanar convex angles with sides that are pairwise directly parallel or pairwise inversely parallel are equal.
15. Recognize that two coplanar convex angles that have two sides directly parallel and the other two inversely parallel are supplementary.
16. Know that two coplanar convex angles with sides that are pairwise perpendicular are equal if they are "of the same type" (both acute or both obtuse) and are supplementary if they are "of different types".

### Mathematics 5th Grade | Measurement: Angle Amplitude

**MEASUREMENT:**

**ANGLE AMPLITUDE**

**Review the material/summary/synthesis here:**

**EXERCISES**

**What you need to know in this chapter, according to the Mathematics curriculum and learning goals – 5th grade:**

**DOMAIN: GEOMETRY AND MEASUREMENT (GM5)**

**SUBDOMAIN: MEASUREMENT**

**ANGLE AMPLITUDE**

- **Measure angle amplitudes**

1. Identify, with a fixed (non-null) angle as a unit, the measure of the amplitude of a given angle as 1/b (where b is a natural number) when the unit angle is equal to the sum of b angles equal to that one.

2. Identify, with a fixed (non-null) angle as a unit, the measure of the amplitude of a given angle θ as a/b (where a and b are natural numbers) when it is equal to the sum of a angles of amplitude units.

3. Identify the "degree" as the unit of measurement for angle amplitude such that a complete angle has an amplitude equal to 360 degrees and use the symbol "º" correctly.

4. Know that one degree is divided into 60 minutes (of a degree) and one minute into 60 seconds (of a degree) and use the symbols "'" and '"' correctly.

5. Use a protractor to measure angle amplitudes and construct angles of a given amplitude expressed in degrees.

- **Solve problems**

1. Solve problems involving additions, subtractions and conversions of amplitude measurements expressed in complex and simple forms.

# Plane Figures

**Title:** Mathematics Grade 5 | Geometric Properties: Triangles and Quadrilaterals

### Content Status

### Domain and Subdomain

**Domain:** Geometry and Measurement (GM5)
**Subdomain:** Geometric Properties

### Curriculum and Curricular Goals - 24 Performance Descriptors

1. "Use correctly the terms «internal angle», «external angle» and «angles adjacent to a side» of a polygon."

2. "Recognize that the sum of the internal angles of a triangle equals a straight angle."

3. "Recognize that in a right or obtuse triangle, two of the internal angles are acute."

4. "Designate as «hypotenuse» of a right triangle the side opposite the right angle and as «legs» the sides adjacent to it."

5. "Recognize that an external angle of a triangle equals the sum of the non-adjacent internal angles."

6. "Recognize that in a triangle the sum of three external angles with distinct vertices equals a full angle."

7. "Identify parallelograms as quadrilaterals with sides parallel two by two and recognize that two opposite angles are equal."

8. "Use correctly the terms «right triangle», «acute triangle» and «obtuse triangle»."

9. "Construct triangles given the lengths of the sides, recognize that the various possible constructions lead to congruent triangles and use correctly the «SSS criterion for triangle congruence»."

10. "Construct triangles given the lengths of two sides and the measure of the angle formed by them and use correctly the «SAS criterion for triangle congruence»."

11. "Construct triangles given the length of one side and the measures of the angles adjacent to that side and use correctly the «ASA criterion for triangle congruence»."

12. "Recognize that in a triangle, equal sides are opposite equal angles and vice versa."

13. "Recognize that in congruent triangles, equal sides are opposite equal angles and vice versa."

14. "Classify triangles according to their sides using the measures of their respective internal angles."

15. "Know that in a triangle the longest side is opposite the largest angle and the shortest side is opposite the smallest angle, and vice versa."

16. "Recognize that in a parallelogram opposite sides are equal."

17. "Know that in a triangle the measure of the length of any side is less than the sum of the measures of the lengths of the other two and greater than their difference, and designate the first as the «triangle inequality»."

18. "Know, given a line r and a point P not belonging to r, that there exists a line perpendicular to r passing through P, recognize that it is unique and construct the intersection of this line with r."

19. "Know, given a line r and a point P belonging to it, that there exists in each plane containing r, a line perpendicular to r passing through P, recognize that it is unique and construct it using ruler and set square."

20. "Identify the distance from a point P to a line r as the distance from P to the foot of the perpendicular drawn from P to r."

21. "Identify, given a triangle and one of its respective sides, the «height» of the triangle relative to that side as the line segment joining the vertex opposite the base with the foot of the perpendicular."

22. "Recognize that the line segments joining two parallel lines and perpendicular to them are equal and designate the length of these segments as the «distance between parallel lines»."

23. "Identify, given a parallelogram, a «height» relative to a side as a line segment joining a point on the opposite side to the line containing the base and perpendicular to it."

24. "Use deductive reasoning to recognize geometric properties."

**Title:** Mathematics Grade 6 | Plane Geometric Figures

### Content Status

### Domain and Subdomain

**Domain:** Geometry and Measurement (GM6)
**Subdomain:** Plane Geometric Figures

### Curriculum and Curricular Goals - Relating Circles with Angles, Lines and Polygons

The curriculum requires students to master seven key competencies:

1. "Designate, given a circle, as «central angle» an angle with vertex at the center."

2. "Designate, given a circle, as «circular sector» the intersection of a central angle with the circle."

3. "Identify a polygon as «inscribed» in a given circle when its respective vertices are points on the circle."

4. "Recognize that a line passing through a point P on a circle with center O and perpendicular to the radius [OP] intersects the circle only at P and designate it as a «line tangent to the circle»."

5. "Identify a line segment as tangent to a given circle if it intersects it and its respective supporting line is tangent to the circle."

6. "Identify a polygon as «circumscribed» about a given circle when its respective sides are tangent to the circle."

7. "Recognize, given a regular polygon inscribed in a circle, that the segments joining the center of the circle to the feet of the perpendiculars drawn from the center to the sides of the polygon are all equal and designate them as «apothems»."

**Title:** Mathematics Grade 7 | Plane figures - angles, quadrilaterals and areas

This educational resource from "O Bichinho do Saber" provides comprehensive coverage of 7th grade mathematics focused on plane figures, angles, quadrilaterals and areas.

### 8.1. Angles

**Classification of angles according to measure:**
- acute → between 0º and 90º
- right → 90º
- obtuse → between 90º and 180º
- straight → 180º
- full → 360º

**Pairs of angles:**
- complementary → whose sum is 90º
- supplementary → whose sum is 180º
- alternate interior/exterior → formed by a transversal on two lines, on opposite sides
- vertically opposite → have the same vertex and the sides of one are in the extension of the sides of the other

**Angles of a convex polygon:**
- Si = (n – 2) × 180º
- Se = 360º
- ai = ((n – 2) × 180º)/n
- ae = 360º/n
- ai + ae = 180º

### 8.2. Quadrilaterals

**Parallelogram:** opposite sides parallel and equal; opposite angles equal; two consecutive angles supplementary

**Rhombus:** parallelogram quadrilateral; all sides equal

**Rectangle:** parallelogram quadrilateral; all angles equal (right angles)

**Square:** all sides equal; all angles equal (right angles)

**Kite:** two pairs of consecutive sides equal

**Properties of diagonals:**
- Parallelogram: bisect each other
- Rhombus: bisect each other and are perpendicular
- Rectangle: bisect each other and are equal
- Square: bisect each other, are perpendicular and equal
- Kite: are perpendicular

**Trapezoid:** quadrilateral with at least two parallel sides

### 8.3. Areas of plane figures

- Triangle: A = (base × height)/2
- Square: A = side × side
- Rectangle: A = length × width
- Parallelogram: A = base × height
- Rhombus and kite: A = (Major diagonal × minor diagonal)/2
- Trapezoid: A = ((Major base + minor base)/2) × height
- Regular polygon: A = (Perimeter/2) × apothem
- Circle: A = π × (radius)²

### Essential Learning

"Identify internal and external angles of a convex polygon. Generalize and justify the sum of the measures of the internal and external angles of a convex polygon. Solve problems that include angles of a convex polygon."

"Recognize the equality of the measures of alternate interior angles in pairs of parallel lines intersected by a transversal. Recognize and justify the equality of the measures of vertically opposite angles."

"Identify the diagonals of a quadrilateral. Describe the properties of the diagonals of a quadrilateral and apply them to solve problems. Formulate conjectures, generalizations and justifications, from the identification of regularities common to objects under study."

"Explain the hierarchical classification of quadrilaterals, including the cases of trapezoid and kite, presenting and explaining reasoning and representations. Identify properties and classify quadrilaterals."

"Communicate mathematically articulating knowledge of the properties of quadrilaterals with their visualization. Generalize and justify the formulas for the areas of trapezoid, rhombus and kite, using those of other figures."

### Classes and Worksheets #EstudoEmCasa

Two resources are available with links to view classes and worksheets in PDF:

1. "Around with areas"
2. "Still around with areas"

### Available Resources

- Interactive exercises (pending)
- Printable worksheets and tests (pending)
- Educational videos from the #EstudoEmCasa program 2019/2020 with links to RTP classes about areas

**Title:** Mathematics Grade 9 | Geometric Figures

### Main Topic: Circles and Geometric Loci

### SUMMARY

**GEOMETRIC FIGURES**

#### Circle

**Elements of the circle**
- Reference to available explanatory video

**Arc length and circular sector area**
- Arc length (with video reference)
- Circular sector area (with video reference)

**Arc measure**
- Central angle (with video reference)
- Inscribed angle (with video reference)

**Properties**

#### Geometric loci

**Circle, disk, perpendicular bisector and angle bisector**
- Reference to available video

**Circumcenter, incenter, orthocenter and barycenter**
- Reference to available video

### Available Content Sections:

### Essential Learning

According to the page, students should be able to:

- "Analyze plane and three-dimensional geometric figures, including the circle, disk and sphere"
- "Relate the measure of a central angle and an inscribed angle in a circle"
- "Identify and construct geometric loci (circle, disk, perpendicular bisector and angle bisector)"

### Classes and Worksheets #EstudoEmCasa (2020/2021)

| Class | Title | Links |
|------|--------|-------|
| 31 | Geometric loci: circle, disk, perpendicular bisector and angle bisector | [view class](https://www.rtp.pt/play/estudoemcasa/p7823/e526901/matematica-9-ano) · [worksheet](https://estudoemcasa-2020-2021.s3.eu-west-3.amazonaws.com/resources/446917046539eb55b10508a26ea179e4/31_Matem%C3%A1tica_9%C2%BA%20ano_Lugares%20geom%C3%A9tricos%20-%20circunfer%C3%AAncia%2C%20c%C3%ADrculo%2C%20mediatriz%20e%20bissetriz.pdf) |
| 32 | Circle inscribed and circumscribed to the triangle | [view class](https://www.rtp.pt/play/estudoemcasa/p7823/e527640/matematica-9-ano) · [worksheet](https://estudoemcasa-2020-2021.s3.eu-west-3.amazonaws.com/resources/12958c7329abb27ec3d8f262bb27b6cf/32_Matem%C3%A1tica_9%C2%BA%20ano_Circunfer%C3%AAncia%20inscrita%20num%20tri%C3%A2ngulo%20%28incentro%29%20e%20circunfer%C3%AAncia%20circunscrita%20ao%20tri%C3%A2ngulo%20%28circuncentro%29.pdf) |
| 33 | Altitudes, orthocenter, medians and barycenter | [view class](https://www.rtp.pt/play/estudoemcasa/p7823/e528504/matematica-9-ano) · [worksheet](https://estudoemcasa-2020-2021.s3.eu-west-3.amazonaws.com/resources/6b00ce8d03a6813225325eb526cac5c5/33_Matem%C3%A1tica_9%C2%BA%20ano_Alturas%20de%20um%20tri%C3%A2ngulo%20e%20ortocentro.%E2%80%8B%20Medianas%20de%20um%20tri%C3%A2ngulo%20e%20baricentro.pdf) |
| 34 | Problem solving involving geometric loci | [view class](https://www.rtp.pt/play/estudoemcasa/p7823/e529245/matematica-9-ano) · [worksheet](https://estudoemcasa-2020-2021.s3.eu-west-3.amazonaws.com/resources/f4d911f383b80d5c5e047193e65b8baa/34_Matem%C3%A1tica_9%C2%BA%20ano_Resolu%C3%A7%C3%A3o%20de%20problemas%20envolvendo%20lugares%20geom%C3%A9tricos.pdf) |
| 35 | Circle. Symmetries in the circle | [view class](https://www.rtp.pt/play/estudoemcasa/p7823/e530152/matematica-9-ano) · [worksheet](https://estudoemcasa-2020-2021.s3.eu-west-3.amazonaws.com/resources/853ef9c25df9621d6ad2a0a0b8049a66/35_Matem%C3%A1tica_9%C2%BA_Circunfer%C3%AAncia.%20Simetrias%20na%20circunfer%C3%AAncia.pdf) |
| 36 | Angles in the circle: central and inscribed angle | [view class](https://www.rtp.pt/play/estudoemcasa/p7823/e531113/matematica-9-ano) · [worksheet](https://estudoemcasa-2020-2021.s3.eu-west-3.amazonaws.com/resources/e4342feec9e86ac7a44df5a4a67574f4/36_Matem%C3%A1tica_9%C2%BA%20ano_%C3%82ngulos%20na%20circunfer%C3%AAncia%20-%20%C3%A2ngulo%20ao%20centro%20e%20%C3%A2ngulo%20inscrito.%C2%A0Propriedades.pdf) |
| 37 | Angles in the circle. Properties | [view class](https://www.rtp.pt/play/estudoemcasa/p7823/e531708/matematica-9-ano) · [worksheet](https://estudoemcasa-2020-2021.s3.eu-west-3.amazonaws.com/resources/da35eee71ab5b9bf0626dfe89d6a3200/37_Matem%C3%A1tica_9%C2%BA%20ano_%C3%82ngulos%20na%20circunfer%C3%AAncia.%C2%A0Propriedades.pdf) |
| 38 | Circular sector area and arc length | [view class](https://www.rtp.pt/play/estudoemcasa/p7823/e532452/matematica-9-ano) · [worksheet](https://estudoemcasa-2020-2021.s3.eu-west-3.amazonaws.com/resources/87b48b1339b3ebae1a72dd6a940f5880/38_Matem%C3%A1tica_9_%C3%81rea%20de%20um%20sector%20circular%20e%20comprimento%20de%20um%20arco%20de%20circunfer%C3%AAncia.pdf) |
| 39 | Inscribed regular polygon. Sum of angles | [view class](https://www.rtp.pt/play/estudoemcasa/p7823/e535199/matematica-9-ano) · [worksheet](https://estudoemcasa-2020-2021.s3.eu-west-3.amazonaws.com/resources/5a641a2b42a4ed1b14ea72df119eaacb/39_Matem%C3%A1tica_9_Pol%C3%ADgono%20regular%20inscrito%20numa%20circunfer%C3%AAncia.%C2%A0Soma%20das%20amplitudes%20dos%20%C3%A2ngulos%20internos%20e%20dos%20%C3%A2ngulos%20externos%20de%20um%20pol%C3%ADgono%20convexo.pdf) |

### Related Topics in Mathematics Grade 9

Real numbers, Areas and Volumes, Trigonometry, Sequences and regularities, Equations, Inequalities, Functions, Statistical planning, Probability

### Reference Curriculum Documents

The page references curriculum documents with available PDF links.

# Geometric Transformations

**Topic:** Plane Isometries – Rotation and Reflection

### Content Status

### Domain and Subdomain

**Domain:** Geometry and Measurement (GM6)
**Subdomain:** Plane Isometries

### Fundamental Definitions

#### Perpendicular Bisector
The **perpendicular bisector** is described as "the line perpendicular to that segment at the midpoint." Points on this line maintain equidistance from the endpoints of the segment.

#### Central Reflection
For **central reflection**, a point M' is the image of M when a center O is the midpoint of segment [MM']. This transformation preserves segment lengths and angle measures.

#### Axial Reflection
In **axial reflection** (or reflection), the axis r functions as the perpendicular bisector of segment [MM'], maintaining the same isometric properties.

#### Rotation
Regarding **rotation**, M' is defined as the image of M by a rotation with center O and angle α when segments [OM] and [OM'] have equal length and the corresponding angles have identical measure.

### Curricular Objectives - Constructing and Recognizing Properties of Plane Isometries

The curriculum establishes 24 specific learning objectives in this area:

#### Central Reflection (Objectives 1-3)
- Understand the properties of central reflection
- Identify image points
- Recognize that central reflection preserves segment lengths and angle measures

#### Perpendicular Bisector and Constructions (Objectives 4-7)
- Understand the definition of perpendicular bisector
- Construct perpendicular bisectors using ruler and compass
- Recognize that points on the perpendicular bisector are equidistant from the segment endpoints

#### Axial Reflection and Axes of Symmetry (Objectives 8-13)
- Identify axial reflection and its properties
- Recognize axes of symmetry in figures
- Understand angle bisectors
- Construct images of figures by axial reflection

#### Rotation (Objectives 14-20)
- Understand rotation with specified center, angle, and direction
- Recognize rotational symmetries in figures
- Identify rotation angles and directions
- Construct images by rotation

#### Constructive Skills (Objectives 21-24)
- Construct images of figures by central reflection, axial reflection, and rotation
- Use ruler, compass, and protractor in geometric constructions
- Identify symmetries in existing figures
- Apply properties of isometries through deductive reasoning

### Competencies to Develop

Students should develop capabilities to:
- Construct perpendicular bisectors using ruler and compass
- Create images of figures by central reflection, axial reflection, and rotation
- Identify symmetries in existing figures
- Solve problems applying properties of isometries through deductive reasoning
- Work with figures containing rotational and reflection symmetries

**Topic:** Operations with Figures – Similarities (Similar Figures and Similarity Criteria)

### Main Content

This educational resource addresses similar figures, similar polygons, and triangle similarity criteria for 7th grade students.

### Definitions of Similar Figures

Similar figures possess two fundamental properties:
- **"have the same shape"**
- **"distances between pairs of corresponding points are directly proportional"**

#### Similar Polygons

For polygons specifically, the properties include:
- **Equal corresponding angles**
- **Directly proportional corresponding sides**

### Similarity Ratio (r)

The **similarity ratio** is the "constant of proportionality between the lengths of corresponding sides."

The similarity ratio classifies transformations into three categories:

- **Enlargement**: r > 1
- **Reduction**: 0 < r < 1
- **Isometry**: r = 1

### Formulas for Perimeters and Areas

#### Relationship between Perimeters
"The ratio between perimeters of similar figures [is] equal to the similarity ratio"

**Formula:** Perimeter of similar figure = Original perimeter × r

#### Relationship between Areas
The ratio between areas is "equal to the square of the similarity ratio"

**Formula:** Area of similar figure = Original area × r²

### Worked Example - Similar Rectangles

#### Rectangle A (Original)
- Length: 2
- Width: 1
- Perimeter: 6
- Area: 2

#### Rectangle B (Enlargement with r = 2)
- Length: 4
- Width: x
- Perimeter: y
- Area: z

#### Calculations with r = 2:

**Width (x):**
x = 1 × 2 = 2

**Perimeter (y):**
y = 6 × 2 = 12

**Area (z):**
z = 2 × 2² = 2 × 4 = 8

#### Verification:
- Rectangle B: length 4, width 2, perimeter 12, area 8
- The formulas applied were: side × r, perimeter × r, and area × r²

### Triangle Similarity Criteria

Three methods for identifying similar triangles:

#### AA Criterion (Angle-Angle)
Two equal corresponding angles are sufficient to determine triangle similarity.

#### SSS Criterion (Side-Side-Side)
Three directly proportional sides determine triangle similarity.

#### SAS Criterion (Side-Angle-Side)
Two directly proportional sides and the equal corresponding angle (between those sides) determine triangle similarity.

### Learning Objectives

Students should be able to:

1. Recognize similar figures as shapes obtained by enlargement or reduction
2. Identify similar figures in everyday life
3. Identify similar polygons by recognizing equal corresponding angles and proportional corresponding sides
4. Determine similarity ratios in polygons
5. Construct images of figures through homothety
6. Understand scale relationships in maps and plans
7. Apply triangle similarity criteria (AA, SSS, SAS)
8. Relate perimeters and areas of similar figures
9. Solve problems involving perimeters and areas of similar figures
10. Solve problems with similarity in various contexts

### Practical Applications

- Recognition of similar figures in everyday contexts
- Working with scales in maps and representations
- Problem solving using triangle similarity criteria
- Calculating perimeters and areas of similar figures

**Topic:** Vectors, Translations, and Isometries (Vectors, Isometries, and Symmetries)

### Description

Summary of 8th grade Mathematics according to the new program and curricular goals | Oriented line segments, vectors, translations, and isometries

### Content Format

The page presents a summary about **Vectors, Translations, and Isometries** for 8th grade Mathematics through a **SlideShare presentation** created by O Bichinho do Saber.

The main content is delivered through a visual presentation (SlideShare), suggesting a visual and interactive pedagogy.

### Topics Covered in the Presentation

The presentation "Vectors, Translations, and Isometries" covers the following themes:

#### Vectors
- **Oriented line segments**
- **Characterization of a vector**
- **Direction and sense of vectors**
- **Equipollent oriented segments**
- **Null vector**
- **Collinear vectors**
- **Symmetric vectors**

#### Operations with Vectors
- **Addition of vectors**
- **Triangle rule**

#### Geometric Transformations
- **Translations**
- **Reflection**
- **Rotation**
- **Isometries** (general concept)

### Key Concepts

#### Understanding the Meaning of Vector
The program emphasizes understanding the concept of vector, including:
- Mathematical characterization
- Direction and sense properties
- Relationships between oriented segments

#### Addition of Vectors
- Vector addition techniques
- Application of the triangle rule

#### Translations
- Understanding translations as geometric transformations
- Relationship between vectors and translations

#### Reflections and Symmetries
- Identification of reflections
- Recognition of translational symmetries
- Identification of glide reflection symmetries

### Tags Associated with Content

vector addition | characterization of a vector | direction and sense of vectors | reflection | triangle rule | rotation | oriented line segment | equipollent oriented segments | translation | null vector | vectors | collinear vectors | symmetric vectors

### Page Features

The page offers:
- Visual presentation of content through SlideShare
- Social media sharing links
- Access to related 8th grade Mathematics content
- Reference to support materials
- Navigation to other 8th grade Mathematics topics

### Curricular Integration

The material is organized within the 8th grade Mathematics section of the site, with connection to the main "Mathematics 8th" content hub, allowing easy navigation between related topics.

## Notes on Extraction

**Grade 7:** Substantive content available with definitions, formulas, worked examples, and similarity criteria.

**Grade 8:** The main content is presented through an embedded SlideShare presentation. The page lists the topics covered and provides metadata, but the detailed content is in the visual presentation.

**Extraction Limitation:** The WebFetch tool provided summaries of the content rather than complete verbatim transcriptions. For Grade 8 especially, the complete content would require direct access to the embedded SlideShare presentation.

# Geometric Solids

### Mathematics 6th Grade | Geometric Solids and Properties

**Metadata:**
- **Author:** Luis Carrilho
- **Published:** August 20, 2016
- **Modified:** August 21, 2016
- **Website:** O Bichinho do Saber
- **Language:** Portuguese (pt-PT)

### Page Heading
"Mathematics 6th Grade | Geometric Solids and Properties"

### Content Sections

**Section 1: GEOMETRIC SOLIDS AND PROPERTIES**

**Section 2: Learning Material**
Header: "Review here the material/mathematics summary/synthesis:"

**Section 3: Exercises**
Header: "EXERCISES"

### Curriculum Requirements

**Domain:** GEOMETRY AND MEASUREMENT (GM6)
**Subdomain:** GEOMETRIC SOLIDS AND PROPERTIES

#### Learning Objectives - "Identify Geometric Solids"

1. **Prisms:** Students should recognize a "prism" as a polyhedron with two geometrically equal faces ("prism bases") located respectively in two parallel planes. The text distinguishes between oblique prisms, regular right prisms, and lateral faces.

2. **Pyramids:** Defined as a "pyramid" as a polyhedron determined by a polygon ("pyramid base"), with a vertex exterior to the base plane. Regular pyramids feature regular polygon bases and equal lateral edges.

3. **Cylinders:** Two circles with identical radius in parallel planes define a cylinder, with the "cylinder axis" connecting their centers. "Cylinder generators" and "lateral surface of the cylinder" are key terminology. Right cylinders have axes perpendicular to base radii.

4. **Cones:** Formed from a circle C and a point P exterior to the plane, the cone features "cone generators," "cone axis," and "lateral surface of the cone." Right cones maintain perpendicular axes to base radii.

#### Learning Objectives - "Recognize Properties of Geometric Solids"

1. **Edge Properties:**
   - Prism edges = 3 × base edges
   - Pyramid edges = 2 × base edges

2. **Vertex Properties:**
   - Prism vertices = 2 × base vertices
   - Pyramid vertices = base vertices + 1

3. **Convex Polyhedra:** Definition states "convex" when any line segment that connects two points of the polyhedron is contained within it.

4. **Euler's Formula:** Applicability verified for prisms, pyramids, and other convex polyhedra.

5. **Spatial Visualization:** Students identify solids from perspective drawings.

#### Learning Objectives - "Solve Problems"

Problem-solving involving geometric solids and their nets (planifications).

### Reference Navigation
"Return to 6th Grade Mathematics Content List"

### Mathematics 7th Grade | Figures in Space – Regular Polyhedra, Prisms and Pyramids

**Page Metadata:**
- **Title:** Mathematics 7th Grade | Figures in Space - Regular Polyhedra, Prisms and Pyramids - O Bichinho do Saber
- **Published:** November 3, 2022
- **Modified:** February 12, 2024
- **Author:** Luis Carrilho
- **Site:** O Bichinho do Saber

### Navigation Structure

**Primary Menu:**
- HOME
- SUMMARIES AND EXERCISES
- TESTS AND EXAMS
- ACCESS TO HIGHER EDUCATION
- OUR PROJECT AND CONTACTS

**Breadcrumb:**
7TH GRADE > Mathematics 7th > Material Summaries and Exercises

### Main Content

#### Page Heading
"Mathematics 7th Grade | Figures in Space – Regular Polyhedra, Prisms and Pyramids"

#### Section Navigation
- SUMMARY
- INTERACTIVE EXERCISES
- TO PRINT
- MORE RESOURCES

### Educational Content Summary

#### 10. Figures in Space – Regular Polyhedra, Prisms and Pyramids

##### 10.1. Geometric Solids – Polyhedra

**Polyhedra Definition:**
- "solid with only flat faces"

**Regular Polyhedron (Platonic):**
- "solid whose faces are equal regular polygons and each vertex is common to the same number of faces"

**Types Listed:**
- tetrahedron → 4 triangular faces
- cube → 6 quadrilateral faces
- octahedron → 8 triangular faces
- dodecahedron → 12 pentagonal faces
- icosahedron → 20 triangular faces

##### Faces, Edges and Vertices in Prisms

**In a prism with base of n sides:**
- number of vertices = 2n
- number of edges = 3n
- number of faces = n + 2

##### Faces, Edges and Vertices in Pyramids

**In a pyramid with base of n sides:**
- number of vertices = n + 1
- number of edges = 3n
- number of faces = n + 1

##### Euler's Formula
- "V + F = A + 2"

### Section: Interactive Exercises

### Section: To Print

**Material Review:**

**Exercise Worksheets:**

**Tests:**

### Section: More Resources

**Categories:**
- POWERPOINTS
- VIDEOS
- CLASSES AND WORKSHEETS #STUDYATHOME
- Note: "No classes on this subject."

### Learning Objectives (Essential Learnings)

- Distinguish regular and irregular polyhedra and explain the differences
- Build three-dimensional models of regular polyhedra and some planifications
- Visualize polyhedra and their planifications
- Identify which regular polyhedra exist and justify the non-existence of others
- Establish relationships between the number of elements of solid classes
- Infer Euler's formula from the analysis of a broad set of polyhedra
- Relate elements of polyhedra with properties of integers
- Validate previous experiences through recognition of Euler's formula

### Related Topics (7th Grade Mathematics)

1. Integers – addition and subtraction
2. Rational numbers – addition, subtraction, percentage and scientific notation
3. Sequences and successions
4. First-degree equations
5. Functions and direct proportionality
6. Statistical study
7. Probabilities
8. Plane figures – angles, quadrilaterals and areas
9. Operations with figures – similarities
10. Figures in space – regular polyhedra, prisms and pyramids (current)

### Footer Information

**Links:**
- About
- Contacts
- Site Map
- Partners

**Copyright:** O Bichinho do Saber © 2025. All rights reserved.

**Powered by:** WordPress. Theme by Alx

**Social Media:**
- Facebook
- Twitter
- LinkedIn
- RSS Feed

# Trigonometry

**Last Modified Date:** February 13, 2024

### Mathematics 8th Grade | Pythagorean Theorem

#### Main Navigation
- Home
- Summaries and Exercises
- Tests and Exams
- Access to Higher Education
- Blog

#### Breadcrumb
- 8TH GRADE
- Mathematics 8th
- Summaries of content and exercises

### Main Content

**Title:** Mathematics 8th | Pythagorean Theorem

### Topics Covered

The page addresses several related mathematical concepts:

- The Pythagorean Theorem
- Decomposition of a right triangle by its height
- The converse of the Pythagorean Theorem
- Pythagorean triples
- The Pythagorean Theorem in space (spatial applications)
- The height with respect to the hypotenuse
- Spatial diagonals

### Main Learning Resource

**Embedded SlideShare Presentation:**
- **Title:** "Pythagorean Theorem – Mathematics 8th grade – Summary of content"
- **Source:** O Bichinho do Saber's SlideShare Account
- **Location:** Embedded directly on the page

The main educational material consists of an embedded SlideShare presentation that provides comprehensive summarized material aligned with Portuguese curricular standards.

### Associated Tags

The page includes the following thematic tags:
- height with respect to the hypotenuse
- spatial diagonal
- converse of the pythagorean theorem
- pythagorean theorem
- pythagorean theorem in space
- pythagorean triple

### Related Navigation Links

The page provides access to comprehensive 8th grade mathematics content:

- **Main Mathematics Hub:** "Return to 8th grade content – Mathematics" links to broader 8th grade mathematics materials
- **Subject Portal:** Links to "Summaries and exercises for 8th grade mathematics"

### Features

The page offers a link to return to "8th grade content – Mathematics" and includes social sharing features (Facebook, WhatsApp, Instagram).

### Navigation Context

The resource connects to broader 8th grade mathematics materials on the website and provides access to related content covering the complete curriculum.

### Mathematics 9th Grade | Trigonometry

**SUMMARY | MATHEMATICS 9TH GRADE**

### TRIGONOMETRY

#### Trigonometric ratios

**› Sine, cosine and tangent**
- Determine the measure of an acute angle in a right triangle (knowing the length of two sides)
- Determine the length of a side of a right triangle (knowing the measure of an angle and the length of another side)

**› Relationships between trigonometric ratios**
- Of an acute angle
- Of complementary angles

**› Exact values of trigonometric ratios for angles of 30º, 45º and 60º**

## AVAILABLE RESOURCES

### Study Materials

## CLASSES AND WORKSHEETS #ESTUDOEMCASA

### #EstudoEmCasa 2020/2021

**Class 40: "Trigonometric ratios of an acute angle"**
- RTP Video: https://www.rtp.pt/play/estudoemcasa/p7823/e536027/matematica-9-ano
- Worksheet (PDF): https://estudoemcasa-2020-2021.s3.eu-west-3.amazonaws.com/resources/681e0a684b364615501aef80d3a000bf/40_Matem%C3%A1tica_9_Raz%C3%B5es%20trigonom%C3%A9tricas%20de%20um%20%C3%A2ngulo%20agudo.pdf

**Class 41: "Calculating trigonometric ratios. Trigonometric tables and calculator"**
- RTP Video: https://www.rtp.pt/play/estudoemcasa/p7823/e536746/matematica-9-ano
- Worksheet (PDF): https://estudoemcasa-2020-2021.s3.eu-west-3.amazonaws.com/resources/eb55a8c0221dff2216337a3c5d16f408/41_Matem%C3%A1tica_9_C%C3%A1lculo%20de%20raz%C3%B5es%20trigonom%C3%A9tricas.%20Tabelas%20trigonom%C3%A9tricas%20e%20calculadora.pdf

**Class 42: "Trigonometric formulas. Relationship between sine and cosine of complementary angles"**
- RTP Video: https://www.rtp.pt/play/estudoemcasa/p7823/e537571/matematica-9-ano
- Worksheet (PDF): https://estudoemcasa-2020-2021.s3.eu-west-3.amazonaws.com/resources/58caecc9dd6fd126a3512887730add2c/42_Matem%C3%A1tica_9_F%C3%B3rmulas%20trigonom%C3%A9tricas.%20Rela%C3%A7%C3%A3o%20entre%20o%20seno%20e%20o%20cosseno%20de%20%C3%A2ngulos%20complementares.pdf

**Class 43: "Approximate values of the measure of an angle, given known trigonometric ratios. Trigonometric ratios of angles of 30º, 45º and 60º"**
- RTP Video: https://www.rtp.pt/play/estudoemcasa/p7823/e538286/matematica-9-ano
- Worksheet (PDF): https://estudoemcasa-2020-2021.s3.eu-west-3.amazonaws.com/resources/d7eccfc02fa8123e7c325eb825ad801f/43_Matem%C3%A1tica_9_Valores%20aproximados%20da%20amplitude%20de%20um%20%C3%A2ngulo%2C%20conhecidas%20raz%C3%B5es%20trigonom%C3%A9tricas.%C2%A0Raz%C3%B5es%20trigonom%C3%A9tricas%20de%20%C3%A2ngulos%20de%2030%C2%BA%2C%2045%C2%BA%20e%2060%C2%BA.pdf

**Class 44: "Problem solving involving distances and trigonometric ratios"**
- RTP Video: https://www.rtp.pt/play/estudoemcasa/p7823/e539151/matematica-9-ano
- Worksheet (PDF): https://estudoemcasa-2020-2021.s3.eu-west-3.amazonaws.com/resources/c792923de7a9e61f2091391bd5bcc054/44_Matem%C3%A1tica_9_Resolu%C3%A7%C3%A3o%20de%20problemas%20envolvendo%20dist%C3%A2ncias%20e%20raz%C3%B5es%20trigonom%C3%A9tricas.pdf

**Class 45: "Problem solving involving distances and trigonometric ratios"**
- RTP Video: https://www.rtp.pt/play/estudoemcasa/p7823/e539849/matematica-9-ano
- Worksheet (PDF): https://estudoemcasa-2020-2021.s3.eu-west-3.amazonaws.com/resources/41c83d5f998e7137345c8ffff4ee00c5/45_Matem%C3%A1tica_9%C2%BA_Resolu%C3%A7%C3%A3o%20de%20problemas%20envolvendo%20dist%C3%A2ncias%20e%20raz%C3%B5es%20trigonom%C3%A9tricas.pdf

### #EstudoEmCasa 2019/2020

**Class 7: "Constant ratios"**
- RTP broadcasts available at: https://www.rtp.pt/play/estudoemcasa/
- Worksheets available for download

**Class 8: "Inaccessible distances"**
- RTP broadcasts available at: https://www.rtp.pt/play/estudoemcasa/
- Worksheets available for download

## ESSENTIAL LEARNINGS

- Recognize the trigonometric ratios of an acute angle (sine, cosine and tangent) as ratios between the measures of sides of a right triangle and establish relationships between these ratios (sin²α + cos²α = 1, tan α = sin α/cos α).

- Use trigonometric ratios and their relationships in solving problems in mathematical and non-mathematical contexts.

## RELATED TOPICS (9TH GRADE | MATHEMATICS)

- Real numbers
- Geometric Figures
- Areas and Volumes
- Sequences and regularities
- Equations
- Inequalities
- Functions
- Statistical planning and Data processing
- Probability

## Notes on Resources

### Grade 8
- The main content is in an embedded SlideShare presentation that contains the complete summary of the material
- The presentation covers: Pythagorean Theorem, applications in space, Pythagorean triples, and related concepts

### Grade 9
- The available educational content consists mainly of the #EstudoEmCasa classes with RTP videos and PDF worksheets
- All classes include both video and PDF support materials
- The resources cover from basic concepts (trigonometric ratios) to practical applications (problem solving with distances)


\cleardoublepage

# MEASUREMENT

# Area

### Mathematics 5th Grade | Measurement: Area

#### Page Title & Navigation
"Mathematics 5th Grade | Measurement: Area - O Bichinho do Saber"

#### Main Headings
- MEASUREMENT
- AREA

#### Key Curriculum Section

**DOMAIN: GEOMETRY AND MEASUREMENT (GM5)**
**SUBDOMAIN: MEASUREMENT**

##### Learning Objectives - AREA

**Measuring areas of plane figures:**

1. Construct unit squares decomposed into a × b rectangles with side measurements 1/a and 1/b
2. Recognize that the area of a rectangle with sides q and r = q × r square units
3. Express the rule for calculating the area of a rectangle in symbolic language
4. Express the rule for calculating the area of a square, designating it as "c squared" (c²)
5. Recognize that a parallelogram with base b and height a has area = b × a
6. Recognize that a triangle with base b and height a has area = (b × a)/2
7. Express rules for calculating areas of parallelograms and triangles in symbolic language

**Solving problems:**
Solve problems involving calculation of areas of plane figures

#### Navigation Links
"Return to the list of 5th grade contents – Mathematics"

### Mathematics 6th Grade | Measurement: Area

#### Main Headings
- Mathematics 6th Grade | Measurement: Area
- MEASUREMENT: AREA

#### Key Sections Status
- Content/summary of mathematics/synthesis
- Exercises

#### Curriculum Learning Objectives

**DOMAIN: GEOMETRY AND MEASUREMENT (GM6)**
**SUBDOMAIN: MEASUREMENT - AREA**

**Measuring the perimeter and area of regular polygons and circles:**

1. Recognize that circle perimeter and area can be approximated using inscribed and circumscribed regular polygon perimeters and areas
2. Understand circle perimeters and diameters are directly proportional; π (pi) ≈ 3.1416
3. The perimeter of a circle equals the product of π times the diameter
4. Decompose regular polygons inscribed in circles into isosceles triangles; polygon area equals semiperimeter times apothem length
5. Circle area equals π times radius squared

**Solving problems:** Calculate perimeters and areas of polygons and circles

#### Navigation Elements
Site includes sections for grades 1-11, subjects, national exams, and higher education access information.

### Mathematics 7th Grade | Plane figures – angles, quadrilaterals and areas

#### Section 8.1: Angles

**Classification of angles by amplitude:**
- acute → between 0º and 90º
- right → 90º
- obtuse → between 90º and 180º
- straight → 180º
- full rotation → 360º

**Pairs of angles:**
- complementary → whose sum is 90º
- supplementary → whose sum is 180º
- alternate interior/exterior → formed by a transversal line crossing two lines, on opposite sides
- vertically opposite → have the same vertex and the sides of one are the extension of the sides of the other

**Angles of a convex polygon:**
- Si = (n – 2) × 180º
- Se = 360º
- ai = ((n – 2) × 180º) / n
- ae = 360º / n
- ai + ae = 180º

#### Section 8.2: Quadrilaterals

**Parallelogram, Rhombus, Rectangle, Square, Kite** definitions provided with properties.

**Properties of diagonals:**
- Parallelogram: bisect each other
- Rhombus: bisect each other and are perpendicular
- Rectangle: bisect each other and are equal
- Square: bisect each other, are perpendicular and equal
- Kite: are perpendicular

#### Section 8.3: Areas

- Triangle: A = (base × height) / 2
- Square: A = side × side
- Rectangle: A = length × width
- Parallelogram: A = base × height
- Rhombus/Kite: A = (Major diagonal × minor diagonal) / 2
- Trapezoid: A = ((Major base + minor base) / 2) × height
- Regular polygon: A = (Perimeter / 2) × apothem
- Circle: A = π × (radius)²

### Mathematics 9th Grade | Areas and volumes - Complete Content Extract

#### Page Title and Metadata
"Mathematics 9th Grade | Areas and volumes - O Bichinho do Saber"

Published: July 11, 2021
Last Modified: February 14, 2024
Author: Luis Carrilho

#### Main Heading
**Mathematics 9th Grade | Areas and volumes**

#### Navigation Sections

**SUMMARY | POWERPOINTS | VIDEOS | #STUDYATHOME LESSONS AND WORKSHEETS | EXERCISES | ESSENTIAL LEARNING**

#### Content Sections

##### SUMMARY | MATHEMATICS 9TH GRADE

###### **AREAS AND VOLUMES**

**_Relative position of lines and planes_**

**› Relative position between two lines**
_see video_

**› Relative position between two planes**
_see video_

**› Relative position between a line and a plane**
_see video_

**_Areas and volumes of geometric solids_**

**› Volumes of solids**
_see video 1_
_see video 2_

**› Surface areas of solids**
_see video_

##### LESSONS AND WORKSHEETS #STUDYATHOME

###### #StudyAtHome 2020/2021

**Lesson 46** | "Relative position of two lines in a plane. Relative position of two planes. Relative position of lines and planes"

**Lesson 47** | "Views and nets of solids"

**Lesson 48** | "Prisms and pyramids. Surface area of prisms and pyramids"

**Lesson 49** | "Volumes of prisms and pyramids"

**Lesson 50** | "Cylinders and cones. Surface area of cylinders and cones"

**Lesson 51** | "Volumes of cylinders and cones"

**Lesson 52** | "Spherical surface and sphere. Spherical surface area and volume of sphere"

**Lesson 53** | "Problem solving involving area and volume of solids (1)"

**Lesson 54** | "Problem solving involving area and volume of solids (2)"

###### #StudyAtHome 2019/2020

**Lesson 5** | "The "Revolution" of solids"

**Lesson 6** | "A matter of capacity"

#### ESSENTIAL LEARNING

"Recognize the meaning of formulas for calculating surface areas and volumes of solids, including the sphere, and use them in problem solving in mathematical and non-mathematical contexts."

#### REFERENCE CURRICULUM DOCUMENTS

- Essential Learning
- Student Profile (at the end of compulsory education)
- Program and Curriculum Goals (revoked)

#### Related Mathematics Topics (9th Year)

- Real numbers
- Geometric figures
- Areas and Volumes
- Trigonometry
- Sequences and regularities
- Equations
- Inequalities
- Functions
- Statistical planning and Data processing
- Probability

# Volume

### Mathematics Grade 6 | Measurement: Volume of Geometric Solids

#### Page Metadata
- **Title:** "Mathematics Grade 6 | Measurement: Volume of geometric solids"
- **Published:** August 21, 2016
- **Author:** Luis Carrilho
- **Website:** O Bichinho do Saber

#### Main Heading
"Mathematics Grade 6 | Measurement: Volume"

#### Content Status
- Material summary/resume
- Exercises

#### Curriculum Standards (Portuguese)

**Domain:** GEOMETRY AND MEASUREMENT (GM6)
**Subdomain:** VOLUME

##### Learning Objectives - Measure Volumes of Solids

1. Understanding unit cube decomposition into a × b × c rectangular parallelepipeds with fractional dimensions
2. Recognizing volume calculation for rectangular parallelepipeds using rational positive numbers
3. Understanding triangular prism volume equals half a parallelogram-based parallelepiped
4. Calculating triangular prism volume using "base area × height" formula
5. Extending volume formula to general right prisms through triangular decomposition
6. Approximating cylinder volume using regular prisms to establish "base area × height"

##### Learning Objectives - Problem Solving
"Solve problems involving solid volume calculations"

#### Navigation Elements

**Main Menu:**
- HOME | SUMMARIES & EXERCISES | EXAMS & TESTS | HIGHER EDUCATION ACCESS | PROJECT & CONTACTS

**Grade Levels:** Pre-K through 11th year with subject-specific subsections

**Breadcrumb Navigation:**
Home > Mathematics Grade 6 | Measurement: Volume

#### Footer Information
- Copyright: "O Bichinho do Saber © 2025"
- Powered by WordPress
- Theme: Alx Media
- Social: Facebook, Twitter, LinkedIn, RSS Feed

### Mathematics Grade 9 | Areas and Volumes - Complete Content Extract

#### Page Metadata
- **URL:** https://www.obichinhodosaber.com/matematica-9o-ano-areas-e-volumes/
- **Title:** Mathematics Grade 9 | Areas and volumes - O Bichinho do Saber
- **Published:** July 11, 2021
- **Last Modified:** February 14, 2024
- **Author:** Luis Carrilho
- **Language:** Portuguese (pt-PT)

#### Main Content Sections

##### SUMMARY | MATHEMATICS GRADE 9

###### Areas and Volumes

**Relative position of lines and planes**
- Relative position between two lines
- Relative position between two planes
- Relative position between a line and a plane

**Areas and volumes of geometric solids**
- Volumes of solids
- Surface areas of solids

#### #EstudoEmCasa Resources (2020/2021)

| Class | Topic | Links |
|------|--------|-------|
| 46 | "Relative position of two lines in a plane. Relative position of two planes..." | see class · worksheet |
| 47 | "Views and nets of solids" | see class · worksheet |
| 48 | "Prisms and pyramids. Surface area of prisms and pyramids" | see class · worksheet |
| 49 | "Volumes of prisms and pyramids" | see class · worksheet |
| 50 | "Cylinders and cones. Surface area of cylinders and cones" | see class · worksheet |
| 51 | "Volumes of cylinders and cones" | see class · worksheet |
| 52 | "Spherical surface and sphere. Surface area and volume of sphere" | see class · worksheet |
| 53 | "Problem solving involving area and volume of solids (1)" | see class · worksheet |
| 54 | "Problem solving involving area and volume of solids (2)" | see class · worksheet |

##### #EstudoEmCasa 2019/2020
- Class 5: "The 'Revolution' of solids"
- Class 6: "A matter of capacity"

#### Essential Learning Outcomes

"Recognize the meaning of formulas for calculating surface areas and volumes of solids, including the sphere, and use them to solve problems in mathematical and non-mathematical contexts."

#### Curriculum Reference Documents

- Essential Learning Outcomes
- Student Profile (at the end of compulsory education)
- Program and Curricular Goals (revoked)

#### Related Topics in Grade 9 Mathematics

- Real numbers
- Geometric figures
- Trigonometry
- Sequences and patterns
- Equations
- Inequalities
- Functions
- Statistical planning and data processing
- Probability

#### Navigation & Site Info

**Site:** O Bichinho do Saber
**Footer Links:** About · Contacts · Site Map · Partners
**Social Media:** Facebook, Twitter, LinkedIn, RSS Feed


\cleardoublepage

# DATA ORGANIZATION AND TREATMENT

# Data Representation

**Page:**
Mathematics 5th grade | Cartesian graphs - O Bichinho do Saber

**Date:** August 20, 2016

**Breadcrumb:** Home > 5th GRADE > 5th Grade Mathematics > Course content summaries and exercises

### Main Content

**CARTESIAN GRAPHS**

**Review the material/mathematics summary/synthesis here:**

**EXERCISES**

### Learning Objectives

**What you need to know in this chapter, according to the Mathematics curriculum and objectives – 5th grade:**

**DOMAIN:** ORGANIZATION AND DATA PROCESSING (OTD5)

**SUBDOMAIN:** CARTESIAN GRAPHS

**Construct Cartesian graphs**

1. Identify a "Cartesian reference system" as a pair of non-coincident number lines that intersect at their respective origins, designate the reference system as "orthogonal" when perpendicular and "monometric" when the unit is equal.

2. Identify the "abscissa" and "ordinate" of a point in a Cartesian reference system, designating them as the "coordinates" of P.

3. Construct the "Cartesian graph" by representing points whose abscissas and ordinates correspond to the associated values.

**Page title:** "Mathematics 5th grade | Data representation and processing - O Bichinho do Saber"

**Date:** August 20, 2016

### Main Content

**DATA REPRESENTATION AND PROCESSING**

### What you need to know in this chapter

**DOMAIN:** ORGANIZATION AND DATA PROCESSING (OTD5)

**SUBDOMAIN:** DATA REPRESENTATION AND PROCESSING

#### Organize and represent data

1. Construct tables of absolute and relative frequencies recognizing that "the sum of absolute frequencies equals the number of data points and the sum of relative frequencies equals 1"

2. Represent a data set in a bar graph

3. Identify a line graph as one that results from connecting points with consecutive abscissas by line segments

#### Process data sets

1. Identify the mean as "the quotient between the sum of the respective values and the number of data points"

#### Solve problems

1. Solve problems involving mean and mode

2. Solve problems involving data analysis in tables, stem-and-leaf diagrams, bar graphs and line graphs

**Page title:** Mathematics 6th grade | Data representation and processing - O Bichinho do Saber

**Date:** August 21, 2016

### Main Content

**DATA REPRESENTATION AND PROCESSING**

**Review the material/mathematics summary/synthesis here:**

**EXERCISES**

### What you need to know in this chapter

**DOMAIN:** ORGANIZATION AND DATA PROCESSING (OTD6)

**SUBDOMAIN:** DATA REPRESENTATION AND PROCESSING

#### Organize and Represent Data

1. Recognize "statistical population" as a set of elements about which data can be collected regarding a common characteristic.

2. Identify "statistical variable" as a characteristic that admits different values (numerical or modal), one for each statistical unit.

3. Classify statistical variables as "quantitative" (measurable or countable) or "qualitative" (non-numerical characteristics).

4. Understand "sample" as a subset of a population and "sample size" as the number of statistical units contained in it.

5. Represent data in a "pie chart" by dividing the circle into adjacent sectors proportional to the relative frequencies of the categories.

6. Use multiple graphical representations selecting the most appropriate one to convey information.

#### Solve Problems

1. Analyze data represented in different graphical formats.

2. Solve problems using mean, mode and range of a data set.

# Statistics

### Mathematics Grade 7 | Statistical Study

#### SUMMARY

##### 6. Statistical study

###### 6.1. Statistical questions, data collection, organization and analysis

**Statistical question, population and sample**

- **Statistical question**: a question whose answer depends on data collection

- **Statistical population**: set of elements (statistical units) about which we want to study one or more common characteristics

- **Statistical sample**: part of the population from which data is collected; must be representative of the population (random and with the characteristics of the population)

- **Sample size**: number of elements in the sample

**Census and survey**

- **Census**: statistical study that involves observation of all elements of the population

- **Survey**: statistical study that involves observation of elements from a sample

**Statistical variables**

- **Statistical variable**: characteristic that takes different values

- **Types of variables**:
  - Quantitative variable:
    - Discrete (counting) → number of siblings
    - Continuous (measurement) → height
  - Qualitative variable:
    - Nominal (categories without order) → eye color
    - Ordinal (categories with order) → qualifications

**Data organization**

- **Data organized in classes**: when there is a large variability of values
  - [0, 10]: class that includes values from 0 to 10; class with amplitude 10 (10 – 0 = 10)

- **Ways to organize and represent data**:
  - Table of absolute and relative frequencies
  - Pictograms
  - Stem-and-leaf diagram
  - Bar chart
  - Pie chart
  - Line graph/graphs
  - Juxtaposed bar chart
  - Stacked bar chart

**Data analysis**

- **Arithmetic mean (x̄)**: calculated by adding all values in a data set and dividing this sum by the number of elements in that set

- **Mode (Mo)**: value with the highest frequency

- **Median (Me)**:
  - If the number of data points is even → the central position value, with data arranged in order
  - If the number of data points is odd → arithmetic mean of the two central position values, with data arranged in order

- **Range**: difference between the maximum value and the minimum value

**Example:**

Data: 1, 1, 2, 3, 3, 4

- x̄ = (2 × 1 + 2 + 2 × 3 + 4) : 6 = (2 + 2 + 6 + 4) : 6 = 14 : 6 ≅ 2.3
- Mo = 1 and 3
- Me = (2 + 3) : 2 = 5 : 2 = 2.5
- Range = 4 – 1 = 3

#### INTERACTIVE EXERCISES

#### TO PRINT

**Review materials**

**Exercise sheets**

**Tests**

#### MORE RESOURCES

##### POWERPOINTS
(Not specified on the page)

##### VIDEOS
(Not specified on the page)

##### LESSONS AND WORKSHEETS #ESTUDOEMCASA

**#EstudoEmCasa 2019/2020**
- Episode 15 | Data Organization and Processing 1 » [watch lesson and worksheet]

#### ESSENTIAL LEARNING OUTCOMES

- Formulate statistical questions about qualitative and quantitative variables
- Classify variables according to their nature: qualitative (nominal versus ordinal) and quantitative (discrete versus continuous)
- Distinguish population from sample
- Identify the population from which data is to be collected and in what circumstances a sample is used
- Plan the selection of the sample from which data will be collected, ensuring its representativeness
- Define which data to collect, select the source and method of data collection, and proceed with its collection and cleaning
- Collect data through a collection method, namely using credible websites on the Internet
- Identify in which cases it is necessary to proceed with grouping discrete data into classes
- Build classes of equal amplitude to group discrete data that have great variability
- Use frequency tables to organize data in classes (including title in the table)
- Represent bivariate data, in which one of the variables is time, through line graphs, including source, title and legend
- Represent two data sets relating to a given characteristic through stacked bar charts, including source, title and legend
- Decide which graphical representation(s) to adopt to represent data sets, including source, title, legend and scales, and justify the choice(s) made
- Analyze and compare different graphical representations from secondary sources, discuss their adequacy and critically conclude about possible effects of graphic manipulations, developing statistical literacy
- Recognize the range of a quantitative data set as a measure of dispersion and calculate it
- Identify the difference between measures that provide information in terms of location (central) and measures that provide information in terms of dispersion
- Recognize and use the median as a measure of location of the center of data distribution and determine it
- Recognize the difference between summary measures obtained through ungrouped data and data grouped in classes
- Critically analyze which summary measure(s) are appropriate to summarize the data, according to its nature
- Read, interpret and discuss data distributions, critically highlighting the most relevant aspects, listening to others, discussing, countering arguments in a substantiated way
- Draw conclusions, substantiate decisions and raise new questions prompted by the conclusions obtained, to be pursued in possible future studies
- Decide to whom to disseminate the study carried out and prepare different communication resources in order to disseminate it in a rigorous, effective and non-misleading way
- Disseminate the study, telling the story behind the data and raising emerging questions for future studies
- Critically analyze the communication of statistical studies carried out in the media, developing statistical literacy

#### RELATED TOPICS (GRADE 7 - MATHEMATICS)

- Integers – addition and subtraction
- Rational numbers – addition, subtraction, percentage and scientific notation
- Sequences and successions
- First-degree equations
- Functions and direct proportionality
- Probabilities
- Plane figures – angles, quadrilaterals and areas
- Operations with figures – similarities
- Figures in space – regular polyhedra, prisms and pyramids

### Mathematics Grade 9 | Histograms

#### COMPLETE SUMMARY

**DATA ORGANIZATION AND PROCESSING - STATISTICAL PLANNING AND DATA PROCESSING**

##### Nature of Statistical Variables

**Qualitative variable:** Data obtained by classification without counting or measurements. Example: eye color (green, blue, brown).

**Discrete quantitative variable:** Data obtained through counting. Example: number of siblings (0, 1, 2, 3).

**Continuous quantitative variable:** Data obtained through measurements. Example: height.

##### Grouping Data in Frequency Table

Data from continuous quantitative variables are grouped into **classes** with a certain **amplitude**. The class with the highest absolute frequency is called the **modal class**.

**Practical example:**
- Variable: height (centimeters)
- Data: 152, 158, 150, 165, 174, 163, 170, 156, 172, 168
- Amplitude: 5cm

**Frequency table:**

| Classes | Absolute frequency | Relative frequency | Percentage |
|---------|-------------------|-------------------|------------|
| [150, 155[ | 2 | 0.2 | 20% |
| [155, 160[ | 2 | 0.2 | 20% |
| [160, 165[ | 1 | 0.1 | 10% |
| [165, 170[ | 2 | 0.2 | 20% |
| [170, 175[ | 3 | 0.3 | 30% |
| Total | 10 | 1 | 100% |

**Modal class:** [170, 175[

##### Histogram Representation

**Characteristics:**
- Classes on the horizontal axis
- Frequencies on the vertical axis
- Juxtaposed rectangular bars
- Area proportional to absolute frequency

##### Essential Learning Outcomes

- Interpret and produce statistical information
- Collect, organize and represent data in histograms
- Analyze appropriate statistical measures
- Conduct statistical studies and compare data sets

# Probabilities

### 7. Probabilities

#### 7.1. Event Probabilities

**Probability Scale**
- The probability of an event is estimated by relative frequency
- Varies between 0 and 1 (0% and 100%)

**Classification of Events by Probability**
- Certain event: has 100% probability
- Impossible event: has 0% probability
- Equally likely events: have the same probability

**Classification of Events by Number of Elements**
- Elementary event: consists of one element from the set of possible outcomes
- Compound event: consists of two or more elements; probability equals the sum of the probabilities of the elementary events that compose it

**Practical Example with Dice:**
Possible outcomes = {1, 2, 3, 4, 5, 6}
- "Rolling a 1" = elementary event: P = 1/6
- "Rolling a multiple of 3" = compound event: P = 1/6 + 1/6 = 2/6

### Sections Available

- Additional Resources (PowerPoints, Videos, #StudyAtHome Classes)

### Essential Learning Outcomes

"Recognize that the probability of an event consisting of more than one outcome is equal to the sum of the probabilities of the events consisting of the outcomes that compose it."

### SUMMARY | MATHEMATICS GRADE 9

#### DATA ORGANIZATION AND PROCESSING - PROBABILITY

##### RANDOM EXPERIMENTS

**Deterministic Experiment vs Random Experiment**

A deterministic experiment allows predicting the result, having only one possible outcome. Example: placing sugar in a glass of water results in the dissolution of the sugar.

A random experiment depends on luck and chance, presenting a set of possible outcomes called the universe of results or sample space (Ω). The number of possible outcomes is represented by #Ω. Example: rolling a die and checking the number on the top face results in Ω = {1, 2, 3, 4, 5, 6} with #Ω = 6.

**Events of a Random Experiment**

An event constitutes a subset of the universe of results and can be represented in comprehension or extension. Favorable outcomes are the elements of an event, represented by #A (number of favorable outcomes for A).

Example: Rolling a die with Ω = {1, 2, 3, 4, 5, 6}. Event A "getting a face with an even number" = {2, 4, 6} in extension, with #A = 3.

**Classification of Events**

An elementary event consists of a single element from the universe of results. A compound event has two or more elements. A certain event contains all elements from the universe of results. An impossible event contains no elements.

Example: With Ω = {1, 2, 3, 4, 5, 6}:
- A "getting a face with a multiple of 5" = {5} (elementary)
- B "getting a face with an even number" = {2, 4, 6} (compound)
- C "getting a face with a natural number" = {1, 2, 3, 4, 5, 6} = Ω (certain)
- D "getting a face with a negative number" = Ø (impossible)

**Union and Intersection of Events**

The union A U B consists of outcomes that belong to at least one of events A or B. The intersection A ∩ B is formed by outcomes that belong simultaneously to A and B.

Example: A = {1, 4, 5, 6} and B = {2, 4, 6} result in A U B = {1, 2, 4, 5, 6} and A ∩ B = {4, 6}.

**Compatible and Incompatible Events**

Compatible events have at least one element in common (P ∩ Q ≠ Ø). Incompatible or disjoint events have no elements in common (P ∩ Q = Ø). Among incompatible events, complementary or contrary events satisfy P ∩ Q = Ø ∧ P U Q = Ω, while non-complementary events verify P ∩ Q = Ø ∧ P U Q ≠ Ω.

The complement of A is represented by Ᾱ.

Example: With Ω = {1, 2, 3, 4, 5, 6}:
- A = {5} and C = {1, 3, 5}: A ∩ C = {5}, being compatible
- B = {2, 4, 6} and C = {1, 3, 5}: B ∩ C = Ø and B U C = Ω, being incompatible complementary
- A = {5} and B = {2, 4, 6}: A ∩ B = Ø and A U B ≠ Ω, being incompatible non-complementary
- A = {5}, then Ᾱ = {1, 2, 3, 4, 6}

##### PROBABILITY OF AN EVENT

**Probability Scale**

Probability can be expressed as an irreducible fraction, decimal, or percentage, satisfying 0 ≤ P(A) ≤ 1 or 0% ≤ P(A) ≤ 100%.

Example: P(A) = 1/2 = 0.5 = 50%

Note: Events with the same probability are called equally likely.

**Calculating the Probability of an Event - Laplace's Law**

P(A) = (number of favorable outcomes for A)/(number of possible outcomes)

Example 1: Rolling a die with Ω = {1, 2, 3, 4, 5, 6}. Event A "getting a face with a multiple of 5" = {5} results in #A = 1, #Ω = 6, P(A) = 1/6 ≅ 0.167 ≅ 16.7%.

Example 2: In a class of 20 students, the probability of choosing a boy is 1/4. The probability of choosing a girl = 1 - 1/4 = 3/4. Thus: (3/4) = x/20, so x = (3×20)/4 = 15 girls.

**Auxiliary Counting Schemes**

**Venn Diagram** is mainly used to count favorable outcomes of events resulting from union or intersection in experiments with a single action.

Example: Choosing a student with passing grades in Mathematics and Portuguese. With 30 students in the class, 2 failed both, 20 passed Portuguese, 17 passed Mathematics:
- Students who passed Portuguese or Mathematics = 30 - 2 = 28
- Students who passed both = (20 + 17) - 28 = 9
- Students who passed only Portuguese = 20 - 9 = 11
- Students who passed only Mathematics = 17 - 9 = 8

**Two-way Table** is applied in experiments consisting of two actions.

Example 1 (with replacement): Drawing two balls from a bag with a blue, green, and black ball, checking colors. Possibilities: (A,A), (A,V), (A,P), (V,A), (V,V), (V,P), (P,A), (P,V), (P,P). Probability of getting at least one blue = 5/9 (5 favorable outcomes out of 9 possible).

Example 2 (without replacement): Drawing two balls without replacement. Valid possibilities: (A,V), (A,P), (V,A), (V,P), (P,A), (P,V). Probability of getting at least one blue = 4/6 = 2/3.

Example 3 (simultaneously): Drawing two balls simultaneously. Possibilities: (V,A), (P,A), (P,V). Probability = 2/3.

**Tree Diagram** is used in experiments with two or more actions.

Example 1: Drawing three balls without replacement from a bag containing blue, green, and black. Probability of getting at least one blue = 6/6 = 1.

Example 2: Drawing two balls without replacement from a bag with 3 blue and 7 green balls. P = (3/10)×(2/9) + (3/10)×(7/9) + (7/10)×(3/9) = 6/90 + 21/90 + 21/90 = 48/90 = 8/15.

**Law of Large Numbers (Frequentist Definition)**

When an experiment is repeated a large number of times, the relative frequency of an event tends to approach the value of the probability of that event: Fr(A) ≈ P(A). The greater the number of repetitions, the closer the value of the relative frequency will be to the probability.

### ESSENTIAL LEARNING OUTCOMES

- Interpret the concept of probability as relative frequency or Laplace's rule
- Calculate and interpret probabilities associated with random experiments

**Content adapted from:** O Bichinho do Saber (www.obichinhodosaber.com)
