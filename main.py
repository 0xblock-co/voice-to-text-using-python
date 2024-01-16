
from manage_audio import manage_audio

if __name__ == "__main__":
    while True:
        text = manage_audio()
        if text == "bye":
            print("bye")
            break
        print(text)