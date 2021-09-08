import pyttsx3

"""# Create a string
string = "My name is kunal"

# Initialize the Pyttsx3 engine
engine = pyttsx3.init()

# We can use file extension as mp3 and wav, both will work
engine.save_to_file(string, 'music/speech2.mp3')

# Wait until above command is not finished.
engine.runAndWait()"""


def text_to_speech(text):
    string = text
    engine = pyttsx3.init()
    engine.save_to_file(string, f'music/{text}.wav')
    engine.runAndWait()

