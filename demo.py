status="start"
while status=="start":
    user=input("user input:")
    if "hello" in user:
        print("AI output: hello sir")
    elif "who are you?" == user:
        print("AI output: i am AI")
    elif "bye" == user:
        status="stop"
