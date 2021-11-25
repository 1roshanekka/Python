# Discussions

The following is the transncript of some the discussions that we had as a part of the open session on `10th of September`.

## D-0

Introduction to Replit, Replit Teams

If you want to run another file from within Replit, say `week_1.py`, add this in `main.py`.

```python
import week_1
```

## D-1

How to accept input from the console?

```python
x = input()
```

You can also prompt the user, by providing an argument to the `input` command.

```python
x = input('Enter a number')
```

Please avoid having strings inside the `input` command.

## D-2

How to accept an integer as input from the console?

`input` always returns string. If you want to accept an integer as input then, do the following:

```python
x = int(input())
```

## D-3

How does indexing work in strings?

- Zero-based indexing; it starts from `0` and goes upto `len(string) - 1`
- Exceed the index, it will throw `IndexError`.
- Python supports negative indexing.
- Integers cannot be indexed.

## D3-Problem

```python
x = input()
y = int(input())
print(len(x) == 10)
z = x[y]
```

Data given to you:
- This program runs without any error.
- It outputs True.

> How many possible values are there for the second input?

## D-4

How does slicing work in strings?

[Online Textbook](https://pypod.github.io/chapter-1/lesson-1.6.html)

## D-5

What does string concatenation mean?

## D-6

How does the programming assignment interface work in the portal?

## D-7

What are public test cases? What are private test cases? Why do we need them?

## D-8

Importance of the sequence in which you consume the content.