# n Dimensional Qubit State Preparation — README

A small utility to prepare, display and validate normalized quantum state vectors (kets)

This repository contains a compact Python implementation to create, display and test normalized quantum states for n qubits.
It has a State_Preparation class helps construct a 2^n-dimensional state vector for n qubits from a list of complex amplitudes and shows the state both as a column vector and in Dirac (ket) notation. It also includes a test suite demonstrating the intended correctness checks (normalization, correct dimensionality, and error cases).

## Features
* Accepts complex amplitudes for 2^n basis states and arranges them into a column vector.
* Displays the state vector and a human-friendly Dirac (ket) representation (e.g. (0.707+0.000j)|00⟩ + (0.707+0.000j)|01⟩ ...).
* Validation checks:
** Ensures the number of amplitudes equals 2^n.
** Ensures not all amplitudes are zero.
** Also ensures normalization
* Included unit tests that assert normalization, dimensionality and error conditions.

## Files

* Qubit_State_Prep.py — implementation of State_Preparation.
* Tests_Qubit_State_Prep.py — unit tests covering normalization, shape and error handling.

## Pre-requisites
* Python 3.8+ (works on 3.8, 3.9, 3.10, 3.11)
* NumPy — used for numeric arrays and normalization: install using pip install numpy
