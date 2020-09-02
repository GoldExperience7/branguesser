from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as Soup
import random
import sys

lives = 15

my_url = 'http://www.autocarbrands.com/car-brands-information-list/'
uClient = ureq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = Soup(page_html, "html.parser")
containers = page_soup.findAll("div", {"style": "width: 134px"})

brand_names = []

for container in containers:
    brand = container.findAll("p", {"class": "wp-caption-text"})
    brand1 = brand[0].text.replace(' ', '-')
    brand_names.append(brand1)

# print(brand_names)
name = brand_names[random.randint(0, 111)]
# print(len(brand_names))
name = name.lower()
name_list = list(name)
guess = []
for i in range(len(name)-1):
    guess.append("_")

print("Welcome to the Guessing Game! enter '-' for a space")

pos1 = random.randint(0, (len(name_list)-1))
initial = name_list[pos1]
guess.insert(pos1, initial)

used = [initial]
print(''.join(guess))

while lives > 0:
    letter = input("Enter a letter.")
    if letter in name_list:
        for i in range(0, len(name_list)):
            if name_list[i] == letter:
                guess[i] = name_list[i]
            else:
                continue
        if guess == name_list:
            print("You found the brand! The brand was", name)
            sys.exit()
        else:
            print(''.join(guess))
    elif letter not in used:
        print("Letter not in word!")
        lives -= 1
        print("lives:", lives)
    else:
        print("letter already entered!")
    used.append(letter)

print("You ran out of lives! The brand is :", name)
