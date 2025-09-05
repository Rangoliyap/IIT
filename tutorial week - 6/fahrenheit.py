# fahrenheit_to_celsius.py

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

# Example usage
if __name__ == "__main__":
    temp_f = 98.6
    temp_c = fahrenheit_to_celsius(temp_f)
    print(f"{temp_f}°F is equal to {temp_c:.2f}°C")
