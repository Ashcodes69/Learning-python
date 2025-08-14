import random
import string


def get_random():
    return "".join(random.choice(string.ascii_lowercase) for _ in range(3))


def code_message(message):
    message_arr = message.split()
    coded_msg = []

    for msg in message_arr:
        if len(msg) >= 3:
            msg_array = list(msg)
            msg_array.append(msg_array.pop(0))
            msg_array.insert(0, get_random())
            msg_array.append(get_random())
            coded_msg.append("".join(msg_array))
        if len(msg) < 3:
            msg_array = list(msg)
            msg_array.reverse()
            coded_msg.append("".join(msg_array))

    coded_msg = " ".join(coded_msg)
    return coded_msg


def decode_message(message):
    message_arr = message.split()
    decoded_msg = []

    for msg in message_arr:
        if len(msg) >= 3:
            msg_array = list(msg)
            msg_array = msg_array[3:-3]
            msg_array.insert(0, msg_array.pop())
            decoded_msg.append("".join(msg_array))

        if len(msg) < 3:
            msg_array = list(msg)
            msg_array.reverse()
            decoded_msg.append("".join(msg_array))

    decoded_msg = " ".join(decoded_msg)
    return decoded_msg


request = str(input("Enter c to code a message or d for decode a message: "))

message = str(input("Enter your message: "))

if request == "c":
    print(code_message(message))

elif request == "d":
    print(decode_message(message))
else:
    print("bad request")
