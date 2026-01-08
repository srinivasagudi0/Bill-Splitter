# Bill Splitter 💸

A simple Python command-line program that splits a bill among a group of friends.  
It also includes a fun **"Who is lucky?"** feature that randomly selects one person who doesn’t have to pay.

---

## 📌 Features

- Accepts the number of participants
- Collects names of all friends
- Splits the total bill equally
- Optional **"Who is lucky?"** mode to exclude one person from paying
- Handles invalid inputs gracefully

---

## ▶️ How It Works

1. Enter the number of friends (including yourself)
2. Enter each friend’s name
3. Enter the total bill amount
4. Choose whether to enable the **"Who is lucky?"** feature
5. The program prints how much each person should pay

---

## 🧪 Example Output

```text
Enter the number of friends joining (including you):
3
Enter the name of every friend (including you), each on a new line:
Alice
Bob
Charlie
Enter the total bill value:
150
Do you want to use the "Who is lucky?" feature? Write Yes/No:
Yes
Bob is the lucky one!
{'Alice': 75.0, 'Bob': 0, 'Charlie': 75.0}
```
Thanks for reading.
