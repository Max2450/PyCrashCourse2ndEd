# pg. 42-43 Guest List Exercises
# 3-4, list of 3+ people to invite to dinner
guest_list = ["Sgt. Johnson", "Brent Hinds", "Aubrey Plaza"]
print(f'{guest_list[0]}, you are being cordially invited to dinner.')
print(f'{guest_list[1]}, you are being cordially invited to dinner.')
print(f'{guest_list[2]}, you are being cordially invited to dinner.')

# 3-5 one guest cannot make it, print their name, replace it in the list, print 2nd set
print(f'\n{guest_list[0]} cannot make it.')
del guest_list[0]
for guest in guest_list:
    print(f"{guest} you are cordially invited to dinner.")

# 3-6 bigger table, add 3 new guests, 1 to beginning, 1 to middle, 1 to end, print new invs
print("\nWe got a bigger table! 5 can fit.")
guest_list.insert(0, "Kratos")
guest_list.insert(2, "Solaire")
guest_list.append("Squidward")
for guest in guest_list:
    print(f"{guest}, please RSVP to this thing ASAP.")

# 3-7 bigger table won't arrive, only 2 guests will be able to come. Pop list and print oops msg
print("\nDang, bigger table won't arrive on time. Only 2 guests will fit.")
while(len(guest_list) > 2):
    print(f"Dear {guest_list.pop()}, regretfully our small table will not have room for you.")
for guest in guest_list:
    print(f"{guest}, you are not the weakest link.")
while len(guest_list) > 0:
    del guest_list[0]
print(guest_list)
