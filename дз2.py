class ClassA:
    def __init__(self):
        self.attribute_a = "Атрибут класу A"

    def method_a(self):
        return "Метод класу A"

class ClassB:
    def __init__(self):
        self.attribute_b = "Атрибут класу B"

    def method_b(self):
        return "Метод класу B"

class ResultClass(ClassA, ClassB):
    def __init__(self):
        ClassA.__init__(self)
        ClassB.__init__(self)
        self.attribute_result = "Атрибут дочірнього класу"

    def method_result(self):
        return f"Використовує {self.method_a()} та {self.method_b()}"

result = ResultClass()
print(result.attribute_a)
print(result.attribute_b)
print(result.attribute_result)
print(result.method_result())

# Обробка виключень
result = []

def divider(a, b):
    if a < b:
        raise ValueError("Ділене менше за дільник")
    if b > 100:
        raise IndexError("Значення дільника занадто велике")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except (ValueError, IndexError, TypeError, ZeroDivisionError) as e:
        print(f"Помилка: {e}")

print(result)