import random, string
print('Roblox Game Generator by standdouble1')
letters = int(input('Amountofnumbers: '))
value = 1
while value <= letters:
 games = "https://roblox.com/games/" + ('').join(
  random.choices(string.digits, k=letters))
 f = open('Generatedgames.txt', "a+")
 f.write(f'{games}\n')
 print(f'[Generated!] {games}/')
