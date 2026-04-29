# Lab 5: Diffie-Hellman Key Exchange Protocol

## Objective
To understand key distribution schemes, specifically the Diffie-Hellman (DH) algorithm for generating a shared secret key over an insecure communication channel.

## Theoretical Background
The Diffie-Hellman protocol was the first practical method to allow two parties to establish a shared secret without ever transmitting the key itself.
* **Mathematical Basis:** The security relies on the **Discrete Logarithm Problem**. While it is easy to calculate $g^a \pmod p$, it is computationally infeasible to find $a$ given the result if the numbers are sufficiently large[cite: 5].
* **Public Parameters:** Both parties agree on a large prime number $p$ (modulus) and a generator $g$[cite: 5].

## Protocol Workflow
1. **Private Keys:** Alice chooses a private random number $a$; Bob chooses $b$[cite: 5].
2. **Public Keys:** 
   * Alice calculates $A = g^a \pmod p$ and sends it to Bob[cite: 5].
   * Bob calculates $B = g^b \pmod p$ and sends it to Alice[cite: 5].
3. **Shared Secret Calculation:**
   * Alice computes $K = B^a \pmod p$[cite: 5].
   * Bob computes $K = A^b \pmod p$[cite: 5].
   * Result: Both parties arrive at the same key $K$ because $(g^b)^a \equiv (g^a)^b \pmod p$[cite: 5].

## Practical Example (Variant 28)
* **System Parameters:** $p = 47, g = 5$[cite: 5].
* **Alice's Keys:** Private $a=10$, Public $A=12$[cite: 5].
* **Bob's Keys:** Private $b=15$, Public $B=26$[cite: 5].
* **Established Shared Secret:** $K = 4$[cite: 5].

## Security & Vulnerabilities
* **Passive Eavesdropping:** Protected by the complexity of discrete logarithms[cite: 5].
* **Active Attacks:** The basic DH protocol is vulnerable to **Man-in-the-Middle (MitM)** attacks because it lacks authentication. In practice, it is combined with digital signatures or certificates[cite: 5].

## Conclusion
The Diffie-Hellman protocol is essential for building secure connections in modern networks. While mathematically sound, it requires additional authentication layers to prevent active interception[cite: 5].
