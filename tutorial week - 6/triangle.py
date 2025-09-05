# utils.py

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def is_even(n):
    return n % 2 == 0

def triangle_area(b, h=1):
    area = 0.5 * b * h
    return area

# Example usage
if __name__ == "__main__":
    # Fahrenheit to Celsius
    temp_f = 98.6
    temp_c = fahrenheit_to_celsius(temp_f)
    print(f"{temp_f}°F is equal to {temp_c:.2f}°C")

    # Even check
    number = 42
    print(f"Is {number} even? {is_even(number)}")

    # Triangle area
    base = 10
    print(f"Area of triangle with base {base} and default height: {triangle_area(base)}")
    print(f"Area of triangle with base {base} and height 5: {triangle_area(base, 5)}")
