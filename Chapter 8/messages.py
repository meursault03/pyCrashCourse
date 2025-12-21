
def show_messages(short_messages):
    for message in short_messages:
        print(message)

my_short_messages = ["Iuri Vale", "wowmao", "2 + 2 = 5", "melon melon lemon cookie", "take me out tonight, to a place where theresmwommwoamoem"]
sent_messages = []
show_messages(my_short_messages)

def send_messages(short_messages, move_messages):
    while short_messages:
        popped_short_messages = short_messages.pop()
        move_messages.append(popped_short_messages)

send_messages(my_short_messages, sent_messages)

print(sent_messages)
print(my_short_messages)