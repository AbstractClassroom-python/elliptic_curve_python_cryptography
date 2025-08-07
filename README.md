# Elliptic Curve Cryptography (Weierstrass Form) – Assignment

This assignment requires you to implement **Elliptic Curve Cryptography (ECC)** using the short **Weierstrass form** of elliptic curves over a finite prime field (GF(p)). The code is structured into a Python class with stubs for you to implement.

You are provided with:

- ✅ A partially implemented `EllipticCurve` class (method stubs only)
- ✅ A `curves.json` file with parameters for two common NIST elliptic curves
- ✅ A `test.py` driver script
- ✅ A `test2.py` similar to `test.py` but private keys are provided and not generated
- ✅ A `test_output.txt` file containing the expected output for driver script
- ✅ A `test2_output.txt` file containing the expected output for `test2.py`

---

## 📁 Files Overview

| File             | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| `EllipticCurve.py` | Class definition you must complete                                         |
| `curves.json`     | Stores elliptic curve parameters in decimal format                         |
| `test.py`         | Driver script that loads curves, generates keys, signs, verifies, and derives shared keys |
| `test2.py`       | Similar to `test.py` but uses provided private keys                       |
| `test_output.txt` | Reference output from a correct implementation                             |
| `test2_output.txt` | Reference output from a correct implementation of `test2.py`             |

---

## 📐 Curve Format

The curves are in **short Weierstrass form**:


## 📏 Implementation Details

1. **EllipticCurve Class**: Implement the methods for key generation, signing, and verification. It must be in a single file called `EllipticCurve.py` (already present).
2. **Finite Field Arithmetic**: Ensure all operations are performed in the finite field GF(p) (p is a prime defined in the curve parameters).
3. **Testing**: Use the provided `test.py` and `test2.py` scripts to validate your implementation against the expected outputs. These scripts will test key generation, signing, verification, and shared key derivation. They should run without errors or warnings and should have a run time of less than 1 second each.
4. **JSON Loading**: Your implementation should be able to load curve parameters from the `curves.json` file, which contains the curve ID and its parameters in decimal format.
5. **External Libraries**: You may not change the imports in `test.py` or `test2.py`. You can use libraries like `Crypto` for AES encryption, but the core ECC implementation must be done manually.  The EllipticCurve class should not import any libraries other than `hashlib` (for computing SHA256 hashes) and `random` (for generating random integers).
6. **Documentation**: Create a `README2.md` file that details all the methods you implemented, their purpose, and any important notes about your implementation.
7. **Video Walkthrough**: Create a video walkthrough of your implementation, explaining how each part works and demonstrating the tests passing. The video should be at least 10 minutes long and no longer than 20 minutes.
8. **Code Comments**: Ensure your code is well-commented, explaining the purpose of each function and any complex logic. This will help others (and your future self) understand your code more easily.
9. **NO Generative AI**: Given that this assignment is Python-based, you are not allowed to use any generative AI tools to write or assist in writing the code. The implementation must be done manually by you.
10. **Successive Addition**: In order to perform scalar multiplication quickly, you will need to implement a method for successive addition of points on the elliptic curve. This is known as the double-and-add method, which is a common technique for efficiently computing multiples of a point on an elliptic curve.   
11. **Virtual Environment**: In order to use the `Crypto` library, you will need to create a virtual environment and install the `pycryptodome` package. You can do this by running the following commands in your terminal:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    pip install pycryptodome
    ```
12. **Linux Coder Environment**: Feel free to use the Linux Coder environment for this assignment. Given that this assignment is Python-based, you may not need to use the Coder environment since pip is available on most systems.

## Full Assignment

Below are the items you need to complete to receive full credit for this assignment:
- ✅ Implement the `EllipticCurve` class methods in `EllipticCurve.py`.
- ✅ Ensure the class can load curve parameters from `curves.json`.
- ✅ Implement key generation, signing, verification, and shared key derivation methods.
- ✅ Validate your implementation using the provided `test.py` and `test2.py` scripts.
- ✅ Ensure the output matches the expected outputs in `test_output.txt` and `test2_output.txt`.
- ✅ Ensure the implementation runs without errors or warnings and completes in less than 1 second for each test script.
- ✅ Create a file called `README2.md` that details all the methods you implemented, their purpose, and any important notes about your implementation.
- ✅ Create a video walkthrough of your implementation, explaining how each part works and demonstrating the tests passing. The video should be at least 10 minutes long and no longer than 20 minutes.

## Comment About Randomness
For testing purposes, the `random` module is used to generate private keys. In a production environment, you should use a cryptographically secure random number generator to ensure the security of the keys. The `secrets` module in Python is a good choice for this purpose.  The `test.py` script will generate different private keys each time it is run, leading to different outputs. This is expected behavior and you can compare the output with known Elliptic Curve implementations (online calculators).  The `test2.py` script uses fixed private keys to ensure consistent output for testing purposes.