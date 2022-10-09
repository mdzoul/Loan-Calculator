# Common Errors

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

## Invalid Syntax
👉 This program will add all the numbers from 0 to 99 and continually print out the total. Why is it not working?

```python
total = 0
for number in range 100:
  total += number
  print(total)
```

<details> <summary> 👀 Answer </summary> 

We forgot the `()` with the range. The brackets are important because `range` is a function (like the exit function). What `range` is doing is creating a list of numbers between 0 and the number we put in the brackets. If there are no `()`, it won't work.

```python
for number in range (100):
```

</details>

## Name Error
👉 In this program, the computer should be printing out day + numbers 1-6. Why is it saying 'day is not defined'?

```python
for days in range(7):
  print("Day", day)
```

<details> <summary> 👀 Answer </summary> 

The variable name is wrong inside the code. If you want to refer to a created variable in a `for` loop, you have to spell it the same way each time.

```python
  print("Day", days)
```

</details>