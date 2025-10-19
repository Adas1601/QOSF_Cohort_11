# n Dimensional Qubit State Preparation — README

A small utility to prepare, display and validate normalized quantum state vectors (kets)

This repository contains a compact Python implementation to create, display and test normalized quantum states for n qubits.
It has a State_Preparation class helps construct a 2^n-dimensional state vector for n qubits from a list of complex amplitudes and shows the state both as a column vector and in Dirac (ket) notation. It also includes a test suite demonstrating the intended correctness checks (normalization, correct dimensionality, and error cases).

## Features
* Accepts complex amplitudes for 2^n basis states and arranges them into a column vector.
* Displays the state vector and a human-friendly Dirac (ket) representation (e.g. (0.707+0.000j)|00⟩ + (0.707+0.000j)|01⟩ ...).
* Validation checks:
  * Ensures the number of amplitudes equals 2^n.
  * Ensures not all amplitudes are zero.
  * Also ensures normalization.
* Included unit tests that assert normalization, dimensionality and error conditions.

## Files

* Qubit_State_Prep.py — implementation of State_Preparation.
* Tests_Qubit_State_Prep.py — unit tests covering normalization, shape and error handling.

## Pre-requisites
* Python 3.8+ (works on 3.8, 3.9, 3.10, 3.11)
* NumPy — used for numeric arrays and normalization: install using ``` pip install numpy ```

## Installation

Clone the repository (or copy files) and install the dependency:
```
git clone <repo-url>
cd <repo-directory>
pip install numpy
```
No packaging needed — the module is single-file and importable.

## Usage examples

Programmatic usage:
```
from Qubit_State_Prep import State_Preparation

# Prepare a 2-qubit equal superposition (unnormalised input is accepted and the class will normalize)
amps = [1, 1, 1, 1]  # four amplitudes for 2 qubits
qs = State_Preparation(2, amps)
psi = qs.prepare()           # returns a (4,1) numpy column vector
print(qs.dirac_notation())   # human-friendly ket notation
qs.show()                    # prints vector, dirac form and normalization check
```

Interactive CLI (run the file directly):

```
python Qubit_State_Prep.py
```

You will be prompted for:
* Number of qubits (integer)
* Space-separated complex amplitudes (e.g. 1+0j 0 1j 0)

Example interactive input for 1 qubit:

```
Enter number of qubits: 2
Enter 2 complex amplitudes (space-separated, e.g. 1+0j 0):
1 1 1j 0

```

## Usage examples

Example 1: Create and print a Bell-like vector (programmatically)

```
from Qubit_State_Prep import State_Preparation
amps = [1, 0, 0, 1]   # corresponds to |00> + |11> (unnormalized)
qs = State_Preparation(2, amps)
psi = qs.prepare()
qs.show()
```

Expected printed output (illustrative):

```
Normalized 2-qubit state vector (column form):
[[0.70710678+0.j]
 [0.        +0.j]
 [0.        +0.j]
 [0.70710678+0.j]]

State in Dirac notation:
|ψ⟩ = (0.707+0.000j)|00⟩ + (0.707+0.000j)|11⟩

Normalization check: 1.0
```
Example 2: Using complex amplitudes

```
amps = [0.6+0.8j, 0, 0, 0]   # single nonzero complex amplitude
qs = State_Preparation(2, amps)
qs.prepare()
print(qs.dirac_notation())

```
