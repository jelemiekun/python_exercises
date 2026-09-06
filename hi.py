name = input("What is your name? (Should be 8 characters and above) ")

name_len = len(name)
passed = False


def dontKnow():
    print("Who the fuck are you?")


if name_len >= 8:
    print("PASS")
    passed = True
else:
    passed = False
    dontKnow()

if passed:
    is_name_Jason = "Jason" in name or "jason" in name

    if is_name_Jason:
        print("Hello, Jason!")
    else:
        dontKnow()
