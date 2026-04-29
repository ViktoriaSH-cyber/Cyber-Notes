e = 3
d = 187
n = 319

word_indices = [29, 20, 0, 14]
encrypted_word = []
decrypted_word = []

print("Шифрування слова 'ШПАК'")
for m in word_indices:
    c = pow(m, e, n)  # C = M^e mod n
    encrypted_word.append(c)
    print(f"Літера ({m}): {m}^{e} mod {n} = {c}")

print("\nДешифрування")
for c in encrypted_word:
    m = pow(c, d, n)  # M = C^d mod n
    decrypted_word.append(m)
    print(f"Криптотекст ({c}): {c}^{d} mod {n} = {m}")
