# Lab 2: Polyalphabetic Ciphers & Vigenere Cryptanalysis

## Overview
Implementation of the Vigenere Cipher and advanced cryptanalysis techniques: Kasiski examination and Friedman test.

## Objectives
* Understand polyalphabetic substitution mechanics.
* Determine key length using statistical methods.
* Recover the secret key using "reading in columns" frequency analysis.

## Technical Implementation
The Vigenere cipher masks language frequency by using a periodic key (gamma).
Formula: $E_i = (M_i + K_{i \pmod u}) \pmod L$[cite: 2].

## Cryptanalysis Workflow
1. **Kasiski Examination:** Found repeating patterns like `ГҐИГШҐАГГ` with a distance of 12[cite: 2].
2. **Friedman Test (Index of Coincidence):** Calculated IC to confirm key length periodicity[cite: 2].
3. **Column Analysis:** Split the text into $u$ columns and applied frequency analysis to each to find the key "СОВА"[cite: 2].

## Conclusion
The main vulnerability of the Vigenere cipher is its periodicity. By determining the key length, the task reduces to breaking several Caesar ciphers[cite: 2].
