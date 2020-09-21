#  Introduction

**pyttsx3** is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline and is compatible with both Python 2 and 3. An application invokes the pyttsx3.init() factory function to get a reference to a pyttsx3. Engine instance. it is a very easy to use tool which converts the entered text into speech.
The pyttsx3 module supports two voices first is female and the second is male which is provided by “sapi5” for windows.
It supports three TTS engines :

- *sapi5* – SAPI5 on Windows
- *nsss* – NSSpeechSynthesizer on Mac OS X
- *espeak* – eSpeak on every other platform

**Installataion**
To install the pyttsx3 module, first of all, you have to open the terminal and write

```
pip install pyttsx3
```

![Click to enlarge](https://media.geeksforgeeks.org/wp-content/uploads/20190822185833/Screenshot-3114.png)
If you receive errors such as No module named win32com.client, No module named win32, or No module named win32api, you will need to additionally install pypiwin32.
It can work on any platform. Now we are all set to write a program for conversion of text to speech.

**Code : Python program to convert text to speech**

```
# Import the required module for text 
# to speech conversion 
import pyttsx3 
# init function to get an engine instance for the speech synthesis engine = pyttsx3.init() 
# say method on the engine that passing input text to be spoken engine.say('Hello sir, how may I help you, sir.')
# run and wait method, it processes the voice commands. engine.runAndWait() 
```
Output :
The output of the above program would be a voice saying,
```
'Hello sir, how may I help you, sir.'
```

## More

Now we are all set to write a sample program that converts text to speech.

```
# Python program to show 
# how to convert text to speech 
import pyttsx3
# Initialize the converter 
converter =pyttsx3.init()
# Set properties before adding 
# Things to say 
# Sets speed percent 
# Can be more than 100 
converter.setProperty('rate',150) 
# Set volume 0-1 
converter.setProperty('volume',0.7)
# Queue the entered text 
# There will be a pause between 
# each one like a pause in 
# a sentence 
converter.say("Hello World") 
converter.say("I'm also a nerd")
# Empties the say() queue 
# Program will not continue 
# until all speech is done talking 
converter.runAndWait() 
```

**Output:**

> The output of the above program will be a voice saying, “Hello world” and “I’m also a nerd”.

## Changing Voice

Suppose, you want to change the voice generated from male to female. How do you go about it? Let us see.
As you will notice, when you run the above code to bring about the text to speech conversion, the voice that responds is a male voice. To change the voice you can get the list of available voices by getting `voices `properties from the engine and you can change the voice according to the voice available in your system.

To get the list of voices, write the following code.

```
voices = converter.getProperty('voices')
for voice in voices: 
	# to get the info. about various voices in our PC   		print("Voice:")
	print("ID: %s"`%voice.id)
	print("Name: %s"%voice.name)
	print("Age: %s"%voice.age)
	print("Gender: %s"%voice.gender)
	print("Languages Known: %s"%voice.languages) 
```

**Output:**
![Click to enlarge](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20191016160940/text-to-speech-python1.png)

To change the voice, set the voice using `setProperty()` method. Voice Id found above is used to set the voice.
Below is the implementation of changing voice.

```
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
# Use female voice 
converter.setProperty('voice', voice_id)
converter.runAndWait() 
```

Now you’ll be able to switch between voices as and when you want. You can try out running a for loop to assign different statements to different voices. Run the code and enjoy the result.