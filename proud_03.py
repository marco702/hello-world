'''
check input against list
'''

friends = ["Mario","Giuseppe", "Michael"]

question = input("Enter a name: ")

if question in  friends:
    print("Yes, in the list")
else:
    print("No")