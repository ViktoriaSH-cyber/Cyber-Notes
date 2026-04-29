Мета роботи:
Ознайомитися з принципами роботи моноалфавітних криптосистем на прикладі шифру Цезаря та загальної моноалфавітної підстановки. 
Набути практичних навичок проведення криптоаналізу зашифрованих повідомлень за допомогою методу частотного аналізу, 
а також реалізувати програмні засоби для автоматизації цих процесів.

Суть методу:
1.	У зашифрованому тексті підраховується частота появи кожного символу.
2.	Отриманий розподіл порівнюється з еталонною гістограмою частот мови, якою написано текст.
3.	Символи, що зустрічаються найчастіше, замінюються на найчастіші літери мови (наприклад, символ з частотою 10% ймовірно є літерою «О»).
4.	Ефективність методу зростає пропорційно довжині криптотексту.

Завдання 1: 
Варіанти повідомлень	Відкритий текст
28	Двоє дивляться вниз. Один бачить калюжу, другий – зорі. Що кому. Олексадр Довженко

Для шифрування обераю ключ S = 4.
Д (6) -> (6+4) = 10 (З)
В (3) -> (3+4) = 7 (Е)
О (19) -> (19+4) = 23 (Т)
Є (8) -> (8+4) = 12 (І)
…
Пробіл (34) -> (34+4) (mod 34) = 4 (Г)

Відкритий текст: ДВОЄ ДИВЛЯТЬСЯ ВНИЗ. ОДИН БАЧИТЬ КАЛЮЖУ, ДРУГИЙ - ЗОРІ. ЩО КОМУ. ОЛЕКСАДР ДОВЖЕНКО

Шифротекст: ЗЕОІГЗЙЕПЯЦЬЯГЕПЙНВ.ГТЗЙПГЕДЩИХЯГНДОАМЗ.ГЗТЦЖЙВГ–ГЗТТІ.ГЫТГНСРЗ.ГТПИОФГЖТВЖТЗКЙПНС

Завдання 2: 
Варіанти повідомлень	Відкритий текст
28(4)	ZRTFT IH PQFTHZ IQ ZRT XBGBOZIO HTQBZT. HTWTFBG ZRLPHBQV HLGBF HYHZTSH RBWT VTOGBFTV ZRTIF IQZTQZILQH ZL GTBWT ZRT FTEPKGIO. ZRIH HTEBFBZIHZ SLWTSTQZ, PQVTF ZRT GTBVTFHRIE LD ZRT SYHZTFILPH OLPQZ VLLAP, RBH SBVT IZ VIDDIOPGZ DLF ZRT GISIZTV QPSKTF LD CTVI AQIXRZH ZL SBIQZBIQ ETBOT BQV LFVTF IQ ZRT XBGBJY. HTQBZLF BSIVBGB, ZRT DLFSTF NPTTQ LD QBKLL, IH FTZPFQIQX ZL ZRT XBGBOZIO HTQBZT ZL WLZT LQ ZRT OFIZIOBG IHHPT LD OFTBZIQX BQ BFSY LD ZRT FTEPKGIO ZL BHHIHZ ZRT LWTFMRTGSTV CTVI...

Проведено підрахунок частоти появи символів у шифротексті. Найбільшу частоту мають:
•	T (зустрічається 38 разів)
•	Z (28 разів)
•	I (22 рази)
•	R (21 раз)

Найчастіше трилітерне слово у тексті - ZRT. В англійській мові найпоширенішим словом з трьох літер є THE.

Звідси випливає перші гіпотези підстановок:
•	Z -> T
•	R -> H
•	T -> E
Далі IQ:
Враховуючи контекст IN THE, робимо припущення:
•	I -> I
•	Q -> N
Далі IH:
H -> S

Поступово підставляючи знайдені літери та вгадуючи слова за контекстом:
Шифр	Z	R	T	F	I	H	P	Q	X	B	G	O
Текст	T	H	E	R	I	S	U	N	G	A	L	C

Розшифрований текст:
THERE IS UNREST IN THE GALACTIC SENATE. SEVERAL THOUSAND SOLAR SYSTEMS HAVE DECLARED THEIR INTENTIONS TO LEAVE THE REPUBLIC. THIS SEPARATIST MOVEMENT, UNDER THE LEADERSHIP OF THE MYSTERIOUS COUNT DOOKU, HAS MADE IT DIFFICULT FOR THE LIMITED NUMBER OF JEDI KNIGHTS TO MAINTAIN PEACE AND ORDER IN THE GALAXY. SENATOR AMIDALA, THE FORMER QUEEN OF NABOO, IS RETURNING TO THE GALACTIC SENATE TO VOTE ON THE CRITICAL ISSUE OF CREATING AN ARMY OF THE REPUBLIC TO ASSIST THE OVERWHELMED JEDI...

Висновок: 
Під час виконання лабораторної роботи було досліджено моноалфавітні шифри та методи їхнього зламу. На практиці реалізовано шифр Цезаря, що підтвердило його простоту, але низьку стійкість через обмежену кількість ключів. За допомогою частотного аналізу англомовного тексту вдалося успішно відновити повідомлення, ідентифікувавши статистичні закономірності. Робота довeлa, що моноалфавітні підстановки не приховують частотність літер мови, тому вони є вразливими до статистичних атак і непридатними для надійного захисту даних у сучасній кібербезпеці.
