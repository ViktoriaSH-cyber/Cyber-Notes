# Lab 3: Asymmetric Cryptography - RSA Algorithm

## Objective
To explore asymmetric cryptography, specifically key generation and the RSA encryption/decryption processes, and to assess the algorithm's security[cite: 3].

## Mathematical Foundations
RSA security relies on the computational difficulty of factoring large composite numbers[cite: 3].
* **Modulus:** $n = p \times q$[cite: 3].
* **Euler's Totient:** $\phi(n) = (p-1)(q-1)$[cite: 3].
* **Exponents:** Public exponent $e$ and private exponent $d$ (modular inverse of $e$)[cite: 3].

## Calculations (Variant 28)
* **Prime Factors:** $p=29, q=11 \implies n=319, \phi(n)=280$[cite: 3].
* **Keys:** Public $(e=3, n=319)$, Private $(d=187, n=319)$[cite: 3].
* **Example:** Encrypting the letter `Ш` (index 29): $29^3 \pmod{319} = 145$[cite: 3].

## Security Assessment
The resistance to brute force depends on the difficulty of factoring $n$[cite: 3]. While $n=319$ is easily factored in this demonstration, real-world applications utilize 2048-bit or larger keys, making it impossible to calculate $d$ without knowing the prime factors[cite: 3].

## Conclusion
Asymmetric cryptography ensures confidentiality and integrity without requiring the secure exchange of a secret key over open channels[cite: 3].
