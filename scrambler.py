__author__ = 'Stephen'

import csv
from random import randint

contacts = []
with open("contacts.csv", newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    for row in reader:
        contact = {"name": row[0], "number": row[1], "email": row[2]}
        contacts.append(contact)

#### Scramble Names ###
names = []
for contact in contacts:
    firstname = contact["name"].split()[0]
    lastname = contact["name"].split()[1]
    names.append([firstname, lastname])

# Mix 100 Times
for i in range(0, 100):
    # Mix First Names
    for j in range(len(names)):
        # Random Place to put 'j'
        random = randint(0, (len(names)-1))
        firstname = names[j][0]
        names[j][0] = names[random][0]
        names[random][0] = firstname

    # Mix Last Names
    for j in range(len(names)):
        # Random Place to put 'j'
        random = randint(0, (len(names)-1))
        lastname = names[j][1]
        names[j][1] = names[random][1]
        names[random][1] = lastname

for i in range(len(contacts)):
    contacts[i]["name"] = names[i][0] + " " + names[i][1]

### Scramble Numbers ###
numbers = []
for contact in contacts:
    partition1 = contact["number"].split()[0]
    partition2 = contact["number"].split()[1].split("-")[0]
    partition3 = contact["number"].split()[1].split("-")[1]
    numbers.append([partition1, partition2, partition3])

# Mix 100 Times
for i in range(0, 100):
    # Mix First Partition
    for j in range(len(numbers)):
        # Random Place to put 'j'
        random = randint(0, (len(numbers)-1))
        partition1 = numbers[j][0]
        numbers[j][0] = numbers[random][0]
        numbers[random][0] = partition1

    # Mix Second Partition
    for j in range(len(numbers)):
        # Random Place to put 'j'
        random = randint(0, (len(numbers)-1))
        partition2 = numbers[j][1]
        numbers[j][1] = numbers[random][1]
        numbers[random][1] = partition2

    # Mix Third Partition
    for j in range(len(numbers)):
        # Random Place to put 'j'
        random = randint(0, (len(numbers)-1))
        partition3 = numbers[j][2]
        numbers[j][2] = numbers[random][2]
        numbers[random][2] = partition3

for i in range(len(contacts)):
    contacts[i]["number"] = numbers[i][0] + " " + numbers[i][1] + "-" + numbers[i][2]

### Scramble Emails ###
emails = []
for contact in contacts:
    partition1 = contact["email"].split("@")[0]
    partition2 = contact["email"].split("@")[1]
    emails.append([partition1, partition2])

# Mix 100 Times
for i in range(0, 100):
    # Mix First Partition
    for j in range(len(emails)):
        # Random Place to put 'j'
        random = randint(0, (len(emails)-1))
        partition1 = emails[j][0]
        emails[j][0] = emails[random][0]
        emails[random][0] = partition1

    # Mix First Partition
    for j in range(len(emails)):
        # Random Place to put 'j'
        random = randint(0, (len(emails)-1))
        partition2 = emails[j][1]
        emails[j][1] = emails[random][1]
        emails[random][1] = partition2

### Privatize Emails ###
for i in range(len(emails)):
    AMOUNT_TO_SHOW = 1
    partition1 = emails[i][0]
    star_amount = "*" * (len(partition1) - AMOUNT_TO_SHOW*2)
    private_partion = partition1[:AMOUNT_TO_SHOW] + star_amount + partition1[-AMOUNT_TO_SHOW:]
    emails[i][0] = private_partion

for i in range(len(contacts)):
    contacts[i]["email"] = emails[i][0] + "@" + emails[i][1]

with open("contacts_scrambled.csv", "w") as csvfile:
    writer = csv.writer(csvfile, lineterminator="\n")
    for contact in contacts:
        row = [contact["name"], contact["number"], contact["email"]]
        writer.writerow(row)