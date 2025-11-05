# Natural Numbers

**Source:** O Bichinho do Saber
**Grades:** 5, 6
**Extraction Date:** 2025-10-29

---

## Grade 5

**Source URL:** https://www.obichinhodosaber.com/2016/08/18/matematica-5o-ano-numeros-naturais/

### NATURAL NUMBERS

#### SET OF NATURAL NUMBERS

The set of natural numbers is represented by ℕ and begins with: 1, 2, 3, 4, 5, 6, …

ℕ = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, …}

**Important note:** the set of natural numbers is infinite.

---

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

---

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

---

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

---

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

---

### LEAST COMMON MULTIPLE AND GREATEST COMMON DIVISOR

#### Least Common Multiple (LCM)

The **least common multiple** is the smallest number that is a multiple of two or more numbers (not counting zero).

**Least common multiple of 4 and 10:**
- Multiples of 10 = {0, 10, **20**, …}
- Multiples of 4 = {0, 4, 8, 12, 16, **20**, …}

LCM (4, 10) = **20**

---

#### Greatest Common Divisor (GCD)

The **greatest common divisor** is the largest number that divides two or more numbers.

**Greatest common divisor of 4 and 10:**
- Divisors of 10 = {1, **2**, 5, 10}
- Divisors of 4 = {1, **2**, 4}

GCD (4, 10) = **2**

---

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

---

#### Finding Common Divisors using GCD

Determine the GCD, then find all divisors of the GCD.

**Common divisors of 30 and 50:**
- GCD (30, 50) = 10
- Divisors of 10 = {1, 2, 5, 10}

Common divisors of 30 and 50 = {1, 2, 5, 10}

---

#### Relationship between LCM and GCD

**a × b = GCD (a, b) × LCM (a, b)**

---

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

---

### RELATIVELY PRIME NUMBERS

#### Prime Numbers and Composite Numbers

**Prime number:**
- Has only two divisors: 1 and itself
- 5 is prime (divisors: 1, 5)

**Composite number:**
- Has more than two divisors
- 6 is composite (divisors: 1, 2, 3, 6)

**Note:** The number 1 has only one divisor, therefore it is neither prime nor composite.

---

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

---

### MATERIALS AND RESOURCES

**Summary available in PDF file (pages 3 and 4)**
Video summary and PDF file provided by RjasMatemática.

---

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

---

## Grade 6

**Source URL:** https://www.obichinhodosaber.com/2016/08/20/matematica-6o-ano-numeros-naturais-numeros-primos-decomposicao-fatores-primos/

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
