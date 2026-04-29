# Параметри (p, q, g), хеш (m), секретне k та ключ (x)
p, q, g = 23, 11, 4
m, k, x = 9, 3, 8

#Відкритий ключ: y = g^x mod p
y = pow(g, x, p)

print(f"Публічні дані: p={p}, q={q}, g={g}, y={y}")

#ПІДПИСАННЯ
# r = (g^k mod p) mod q
r = pow(g, k, p) % q

# s = k^-1 * (m + x*r) mod q (pow(k, -1, q) зворотне число)
s = (pow(k, -1, q) * (m + x * r)) % q

print(f"ЕЦП створено: (r={r}, s={s})")

#ПЕРЕВІРКА
# w = s^-1 mod q
w = pow(s, -1, q)

# u1 = m*w mod q, u2 = r*w mod q
u1 = (m * w) % q
u2 = (r * w) % q

# v = ((g^u1 * y^u2) mod p) mod q
v = (pow(g, u1, p) * pow(y, u2, p) % p) % q

print(f"Перевірка: v={v} (має дорівнювати r={r})")
print("Результат: ПІДПИС ДІЙСНИЙ" if v == r else "ПІДПИС НЕВІРНИЙ")
