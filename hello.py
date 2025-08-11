import random
import string

request = str(input("Enter c to code a message or d for decode a message: "))
message = str(input("Enter your massege: "))

if request == "c":

    def get_random():
        return "".join(random.choice(string.ascii_lowercase) for _ in range(3))

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
    print(coded_msg)
elif request == "d":
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
    print(decoded_msg)

else:
    print("bad request")
