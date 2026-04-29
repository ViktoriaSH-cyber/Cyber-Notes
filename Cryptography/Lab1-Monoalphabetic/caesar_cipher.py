from collections import Counter
class MonoCipher:
    def __init__(self):
        self.alphabet = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ "
        self.L = len(self.alphabet)

    def caesar(self, text, s, mode='enc'):
        #Шифр Цезаря
        res = ""
        shift = s if mode == 'enc' else -s
        for char in text.upper():
            if char in self.alphabet:
                idx = (self.alphabet.find(char) + shift) % self.L
                res += self.alphabet[idx]
            else:
                res += char
        return res

    def frequency_report(self, text):
        #Розрахунок частоти
        chars = [c for c in text.upper() if c in self.alphabet]
            
        total = len(chars)
        counts = Counter(chars)
        
        print(f"\n{'Символ':^10} | {'Кількість':^10} | {'Частота (%)':^12}")
        print("-" * 38)
        
        for char, count in counts.most_common():
            freq = (count / total) * 100
            print(f"  {char:^6}   | {count:^10} | {freq:^12.2f}%")

tool = MonoCipher()
message = "ШПАК ВІКТОРІЯ ОЛЕКСАНДРІВНА" 
shift_value = 5

encrypted = tool.caesar(message, shift_value)
print(f"Зашифрований текст: {encrypted}")

print("\nРЕЗУЛЬТАТИ ЧАСТОТНОГО АНАЛІЗУ:")
tool.frequency_report(encrypted)

decrypted = tool.caesar(encrypted, shift_value, mode='dec')
print(f"Розшифрований текст: {decrypted}")
