import random
import string

# Ask user for action: code or decode
request = str(input("Enter c to code a message or d for decode a message: "))
# Ask user for the message
message = str(input("Enter your massege: "))

if request == "c":
    # Function to generate a random 3-letter string
    def get_random():
        return "".join(random.choice(string.ascii_lowercase) for _ in range(3))

    message_arr = message.split()  # Split message into words
    coded_msg = []
    for msg in message_arr:
        if len(msg) >= 3:
            # For words with 3 or more letters:
            msg_array = list(msg)
            msg_array.append(msg_array.pop(0))  # Move first letter to the end
            msg_array.insert(0, get_random())  # Add random 3 letters at the start
            msg_array.append(get_random())  # Add random 3 letters at the end
            coded_msg.append("".join(msg_array))
        if len(msg) < 3:
            # For words with less than 3 letters, reverse the word
            msg_array = list(msg)
            msg_array.reverse()
            coded_msg.append("".join(msg_array))

    coded_msg = " ".join(coded_msg)  # Join coded words into a string
    print(coded_msg)
elif request == "d":
    message_arr = message.split()  # Split message into words
    decoded_msg = []

    for msg in message_arr:
        if len(msg) >= 3:
            # For words with 3 or more letters:
            msg_array = list(msg)
            msg_array = msg_array[3:-3]  # Remove first and last 3 letters
            msg_array.insert(0, msg_array.pop())  # Move last letter to the front
            decoded_msg.append("".join(msg_array))

        if len(msg) < 3:
            # For words with less than 3 letters, reverse the word
            msg_array = list(msg)
            msg_array.reverse()
            decoded_msg.append("".join(msg_array))

    decoded_msg = " ".join(decoded_msg)  # Join decoded words into a string
    print(decoded_msg)

else:
    print("bad request")
