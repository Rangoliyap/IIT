# Laboratory - Week 5
# Temperature Conversions and Vowel Counting

# =========================
# Temperature Conversions
# =========================
print("Celsius\tFahrenheit")

celsius = 10
while celsius <= 30:
    fahrenheit = (9/5 * celsius) + 32
    print(f"{celsius}\t{int(fahrenheit)}")
    celsius += 5

# =========================
# Vowels Counting
# =========================
phrase = input("\nEnter a phrase: ")
vowels = "aeiouAEIOU"
count = 0

for char in phrase:
    if char in vowels:
        count += 1

print(f"The phrase contains {count} vowels.")
