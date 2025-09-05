# utils.py

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def is_even(n):
    return n % 2 == 0

# Example usage
if __name__ == "__main__":
    # Fahrenheit to Celsius
    temp_f = 98.6
    temp_c = fahrenheit_to_celsius(temp_f)
    print(f"{temp_f}°F is equal to {temp_c:.2f}°C")

    # Even check
    number = 42
    print(f"Is {number} even? {is_even(number)}")
