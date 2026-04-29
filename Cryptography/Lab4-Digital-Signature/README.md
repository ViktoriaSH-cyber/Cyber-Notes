# Lab 4: Digital Signature Algorithms (DSA)

## Objective
To explore the mechanisms of Digital Signature Schemes (DSS), master key generation, and the procedures for creating and verifying digital signatures to ensure data integrity and authenticity.

## Theoretical Background
A Digital Signature (DS) is a cryptographic tool added to a document to confirm its integrity, the author's authenticity, and non-repudiation[cite: 4].
* **Hash Function:** Converts a message $M$ into a fixed-length digest $m = h(M)$[cite: 4].
* **Asymmetric Keys:** Uses a private key for signing and a public key for verification[cite: 4].

## DSA Components & Process
The implementation follows the Discrete Logarithm problem complexity:
1. **System Parameters:** $(p, q, g)$ define the mathematical field[cite: 4].
2. **Key Generation:** Private key $x$ (random) and Public key $y = g^x \pmod p$[cite: 4].
3. **Signing:** Generates a pair of numbers $(r, s)$ using a unique random $k$ for each signature[cite: 4].
4. **Verification:** Validates the signature by checking if the calculated value $v$ matches $r$[cite: 4].

## Practical Example (Variant 28)
* **Parameters:** $p=23, q=11, g=4$[cite: 4].
* **User Keys:** Private $x=8$, Public $y=13$[cite: 4].
* **Message Hash:** $m=9$[cite: 4].
* **Generated Signature:** $(r=7, s=7)$[cite: 4].

## Security Analysis
The reliability of the digital signature is guaranteed by the impossibility of calculating the private key from the public key within a reasonable time and the resistance of the hash function to collisions[cite: 4].

## Conclusion
Digital signatures are fundamental for electronic document management, providing non-repudiation and proof of integrity based on the complexity of discrete logarithms[cite: 4].
