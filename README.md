# Number Checker v1.3

Number Checker is a Python-based tool for analyzing numbers. The program can:

- Check if a number is a **Fibonacci number**.
- Display the **index in the Fibonacci sequence** (F0-based).
- Check if a number is a **prime number** (practical for smaller numbers).
- Display the **prime number’s index** in the prime series (for small numbers).

This tool is intended for educational, experimental, and mathematical purposes.

---

## Features

1. **Fibonacci Check**  
   Uses the mathematical square test:  
   > A number `n` is Fibonacci if and only if `5*n^2 + 4` or `5*n^2 - 4` is a perfect square.

2. **Prime Check**  
   Simple prime checking via `is_prime()`. Note: very large numbers (>10^9) may take a long time.

3. **Dynamic Input**  
   Users can input any number at runtime via the terminal.

4. **Large Number Support**  
   Python handles large integers exactly using `math.isqrt`, allowing Fibonacci checks with hundreds of digits.

---

## Installation

1. Clone the repository:  
```bash
git clone https://github.com/FEUE256/Number-Checker.git
cd Number-Checker
