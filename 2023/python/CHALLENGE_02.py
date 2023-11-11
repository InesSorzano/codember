with open("message_02.txt") as f:
    text = f.read()

# "#" Incrementa el valor numérico en 1.
def increment(n):
    return n + 1
# "@" Decrementa el valor numérico en 1.
def decrement(n):
    return n - 1
# "*" Multiplica el valor numérico por sí mismo.
def multiplySelf(n):
    return n * n
# "&" Imprime el valor numérico actual.

finalString = ""
currentNumber = 0
for chara in text:
    if chara == "#":
        currentNumber = increment(currentNumber)
    elif chara == "@":
        currentNumber = decrement(currentNumber)
    elif chara == "*":
        currentNumber = multiplySelf(currentNumber)
    elif chara == "&":
        finalString += str(currentNumber)

print(finalString)

