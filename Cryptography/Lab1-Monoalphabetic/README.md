# Lab 1: Monoalphabetic Substitution & Frequency Analysis

## Overview
This project implements the classical Caesar Cipher and demonstrates a frequency analysis attack.

## Objectives
* Learn the principles of monoalphabetic systems.
* Implement Caesar Cipher for Ukrainian and English languages.
* Practice frequency analysis to decrypt unknown texts.

## Theoretical Background
A monoalphabetic cipher replaces each character of the plaintext with a fixed character of the ciphertext. 
The mathematical model for Caesar Cipher: $E_i = (M_i + S) \pmod L$.

## Analysis Results
### Frequency Analysis (Ukrainian)
During the lab, I analyzed a ciphertext encrypted with shift S=4. The character frequency distribution remained identical to the language's distribution, making the cipher weak[cite: 1].

### Frequency Analysis (English)
I successfully decrypted a text about the Galactic Senate by identifying common English patterns (e.g., 'ZRT' -> 'THE')[cite: 1].

## Conclusion
Monoalphabetic ciphers are insecure because they do not hide language statistics, making them vulnerable to frequency analysis attacks[cite: 1].
