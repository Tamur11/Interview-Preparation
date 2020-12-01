mag = "This is a list of words."
msg = "List of words."

def anon_note_checker(mag, msg):
    for word in msg.split():
        if word.lower() not in mag.lower():
            return False
    return True

print(anon_note_checker(mag, msg))