# #DAY 23 — FUNCTION ARGUMENTS IN PYTHON

---

## 1. Introduction to Function Arguments

**Arguments** are values that we pass to a function when calling it.

They allow functions to work with different inputs.

Example:

```python
def greet(name):
print("Hello",name)

greet("Rahul")
```

Here `"Rahul"` is an **argument**.

---

## 2. Types of Function Arguments

Python provides different types of arguments:

1. Positional Arguments
2. Keyword Arguments
3. Default Arguments
4. Variable-Length Arguments

---

## 3. Positional Arguments

Arguments are passed in the same order as parameters.

```python
def add(a,b):
print(a+b)

add(5,3)
```

Here:

- `a = 5`
- `b = 3`

---

## 4. Keyword Arguments

Arguments are passed using parameter names.

```python
def greet(name,age):
print(name,age)

greet(age=20,name="Aarav")
```

Order does not matter here.

---

## 5. Default Arguments

We can give default values to parameters.

```python
def greet(name="Guest"):
print("Hello",name)

greet()
greet("Devansh")
```

Output:

```
Hello Guest
Hello Devansh
```

---

## 6. Variable-Length Arguments (`args`)

Used when we don’t know how many arguments will be passed.

```python
def add(*numbers):
print(sum(numbers))

add(1,2,3)
add(5,10,15,20)
```

---

## 7. Variable-Length Keyword Arguments (`*kwargs`)

Used to pass multiple keyword arguments.

```python
def info(**data):
print(data)

info(name="Rahul",age=20)
```

Output:

```
{'name': 'Rahul', 'age': 20}
```

---

## 8. Important Points

- Arguments are values passed to functions
- Parameters are variables in function definition
- Order matters in positional arguments
- Keyword arguments remove order dependency
- `args` and `*kwargs` handle multiple inputs

---

# 📝 SUMMARY — FUNCTION ARGUMENTS

- Positional → order matters
- Keyword → order doesn’t matter
- Default → provides default value
- `args` → multiple values
- `*kwargs` → multiple key-value pairs

---

## One-Line Concept

> Function arguments allow us to pass different values to a function, making it flexible and reusable.
>
