# Python-AI-assistant
#Assistant Name - Monkey

What is the Agenda?
The main objective of this model is to enable automated task using speech recognition.

What can this A.I. assistant do for you?
It can send emails on your behalf.
It can do Wikipedia searches for you.
It is capable of opening websites like Google, Youtube, etc., in a web browser.

- The functions included in the model are following :

1.  Wish me Function :  Wishme() function that will make our AI assistant named Monkey wish or greet the user according to the time of computer or pc.

2.  Take command Function  : The important thing for our A.I. assistant is that it should take command with the help of the microphone of the user's system. So, for that we made a takeCommand() function.  With the help of the takeCommand() function, our A.I. assistant will return a string output by taking microphone input from the user.

3.  Speak Function : The first and foremost thing for an A.I. assistant is that it should be able to speak. To make our AI assistant (i.e., Monkey) talk, we will make a function called speak(). This function will take audio as an argument, and then it will pronounce it.Now, the next thing we need is audio. We must supply audio so that we can pronounce it using the speak() function we made. We are going to install a module called pyttsx3.

What is pyttsx3?
A python library that will help us to convert text to speech. In short, it is a text-to-speech library.
It works offline, and it is compatible with Python 2 as well as Python 3.

Installation:
pip install pyttsx3

In case you receive such errors: 
No module named win32com.client
No module named win32
No module named win32api

Then, install pypiwin32 by typing the below command in the terminal :
pip install pypiwin32.
After successfully installing pyttsx3, import this module into your program.

What is sapi5?
Microsoft developed speech API.
Helps in synthesis and recognition of voice.

What Is VoiceId?
Voice id helps us to select different voices.
voice[0].id = Male voice 
voice[1].id = Female voice

Recapitulate : 

First of all, we have created a wishme() function that gives the greeting functionality according to our A.I system time.
After wishme() function, we have created a takeCommand() function, which helps our A.I to take command from the user. This function is also responsible for returning the user's query in a string format.
We developed the code logic for opening different websites like google, youtube, and stack overflow.
At last, we added functionality to send emails.

Is it an A.I.?
Many people will argue that the virtual assistant that we have created is not an A.I, but it is the output of a bunch of the statement. But, if we look at the fundamental level, the sole purpose of A.I develop machines that can perform human tasks with the same effectiveness or even more effectively than humans.
It is a fact that our virtual assistant is not a very good example of A.I., but it is an A.I.!
