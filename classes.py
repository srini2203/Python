import math

class ComplexNumber:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.img + other.img)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.img - other.img)

    def __mul__(self, other):
        real_part = self.real * other.real - self.img * other.img
        imag_part = self.real * other.img + self.img * other.real
        return ComplexNumber(real_part, imag_part)

    def __truediv__(self, other):
        denom = other.real ** 2 + other.img ** 2
        real_part = (self.real * other.real + self.img * other.img) / denom
        imag_part = (self.img * other.real - self.real * other.img) / denom
        return ComplexNumber(real_part, imag_part)

    def mod(self):
        return ComplexNumber(math.sqrt(self.real ** 2 + self.img ** 2), 0)

    @staticmethod
    def parse_Complex(input_string):
        real, img = map(float, input_string.strip().split())  # Converts to float
        return ComplexNumber(real, img)

    def __str__(self):
        if self.img >= 0:
            return f"{self.real:.2f}+{self.img:.2f}i"
        else:
            return f"{self.real:.2f}{self.img:.2f}i"


z1_input = input("Enter first complex number (real and imaginary parts separated by space): ")
z2_input = input("Enter second complex number (real and imaginary parts separated by space): ")

z1 = ComplexNumber.parse_Complex(z1_input)
z2 = ComplexNumber.parse_Complex(z2_input)

print("Addition:", z1 + z2)  
print("Subtraction:", z1 - z2)
print("Multiplication:", z1 * z2)
print("Division:", z1 / z2)
print("Modulus of z1:", z1.mod())
print("Modulus of z2:", z2.mod())
