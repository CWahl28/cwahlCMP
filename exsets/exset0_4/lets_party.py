attendees = []
y = 'temp'

while y != '':
    y = input("Enter invitee's name (or just enter to finish): ")
    if y != '':
        attendees.append(y)
else:
    for i in attendees:
        print(i + ", please attend our party this Saturday!")
