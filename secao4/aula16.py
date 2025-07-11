# dir, hasattr e getattr em Python

string_ = "luiz"

print(string_)

# exemplo 1
if hasattr(string_, "upper"):
    print("Existe upper")
    print(string_.upper())

metodo = "upper"

# exemplo 2
if hasattr(string_, "upper"):
    print("Existe upper")
    print(getattr(string_, metodo)())
