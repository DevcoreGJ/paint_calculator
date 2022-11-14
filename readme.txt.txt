Set up:
Hi so I made this in Pythons tkinter.
As far as I am aware that is the only dependency you will need.

You can install tkinker in your terminal with following pip:

pip install tk

After that in your terminal (I use gitbash)
navigate to your folder the file is in.

in terminal enter:
python paint_calculator.py

on mac/unix it may be:
python3 paint_calculator.py

So to outline what I did:

I used a previous piece of work as a base as you can see on my initial
commit.
I tore it apart and started retooling.
In hindsight this may have cost me more time than it was worth because
The buttons and functions the original calculator were using were scrapped
in my final design.

My design was focussed on ease of use. I scrapped the buttons for entry
boxes so users didn't feel compelled to use the mouse.

I made the tool functional.
You can enter the raw values of what you want in the little boxes.
The appropriately labeled big box gives your answer.

For all intents and purposes this is a functional piece of software.

What I would do to improve it:

There is evidence that I began using classes in the comments but time
constraints and fiddliness prevented me from successfully implementing
the more dynamic usage of the program.

I would focus on making output boxes read-only.
I did experiment with this in the perimeter box box whenever read-only
was active it overwrote/made the output disappear.
It would be cool to add a clear all feature.

A ambitious stretch goal would be to have a second frame open and graphically
represent the wall with labels 3 dimensionally/isometrically.

What obstacles did I encouter?

I think what took up a good chunk of my time in a direct sense was the 
taking a string assign the string to a stringVar() and inputting it as
a float. I didn't expect Entry widgets to be as restrictive as they 
are.

Indirectly/not skilled related - I began having power problems at about
an hour in. My electric would shut on/off and eventually had no power
so I had to get a call out for that causing me to lose flow.

