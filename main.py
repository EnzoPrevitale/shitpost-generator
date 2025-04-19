import random
import os

prompt = input("Digite uma palavra: ")

match = []
data = []
output = [prompt.capitalize()]

for file in os.listdir('data/'):
    text = open(f"data/{file}", 'r')
    for i in text:
        paragraph = i.split(" ")
        for j in paragraph:
            data.append(j)

for i in range(len(data)):
    if prompt.upper() == data[i].upper():
        match.append(data[i + 1])

try:
    current = random.choice(match)
except IndexError:
    current = '.'

while True:
    match = []
    for i in range(len(data)):
        if current == data[i]:
            match.append(data[i + 1])

    try:
        output.append(current)
    except AttributeError:
        break

    for char in current:
        if char == ".":
            output = " ".join(output)

    try:
        current = random.choice(match)
    except IndexError:
        output = "Termo não encontrado."

print(output)