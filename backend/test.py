
"""
users = {}

id = "1234"

if id not in users:
    users[id] = {'emoticon1': 0, 'emoticon2': 0, 'emoticon3': 0, 'emoticon4': 0, 'emoticon5': 0, 'emoticon6': 0}

# Increase count of emoticon2 for user1
users[id]['emoticon2'] += 1 

users[id]['emoticon3'] += 9 

if '3669' in users:
    del (users['3669'])
print (len(users))
# Print the updated counts
for user, emoticons in users.items():
    print(f"{user}: {emoticons}")
"""

