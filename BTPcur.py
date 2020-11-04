#Libraries used: Python Turtle, Speech recognition, word2number, Tkinter
import tkinter as tk
from tkinter import *
import speech_recognition as sr
import turtle
from word2number import w2n


#----------------------example input -------------------
"""
Key words implemneted and example input:
forward backward: move forward by 100 (default 100 units)
right left: take/trun left by 80 degrees (default 90 degrees)
penup pendown: lift/put the pen up/down
colour: change colour to red (default black)
move to: move to 10 comma 20
dot: keep red dot of size 60 (default size 60 clour black)
stamp:
import: import library_name
if: if CONDITIONS then STATEMENTS end indentation
while: while CONDITIONS then STATEMENTS end indentation

All the key words implemented:
forward     backward    left    right     penup     pendown
colour      moveto      stamp   dot       import    if
while       shape
"""
#----------------------example input ends------------------

#initialising speech recgnition python turtle and Tkinter GUI
root = Tk()
root.title("Python code Generator")
root.geometry("800x800")
r = sr.Recognizer()
skk = turtle.Turtle()

#Opening file and including basic libraries
file = open('output.py','w')
file.write("import turtle\n")
file.write("skk = turtle.Turtle()\n")
skk.pensize(5)
file.write("skk.pensize(5)\n")
skk.shape('turtle')
file.write("skk.shape('turtle')\n")

#useful lists
#list of colors
colors = ['red','black','blue','green']
#list of key words
keywords=['if','for','while','forward','backward','dot','shape','left','right','penup','pen','up','down','go','move','comma','and','or','stamp','value','import','kinter'
          'speech','turtle','colour']
#logical operators
logical_operators=['and','or','xor','not']
compare_operators=['greater','less','greaterequal','notequal','lessequal']
#list of Libraries
libraries=['tkinter','speech_recognition','word2number']
#list of variables declared
variables=[]


#function to return compare_operators
def operator(str):
    if(str=='greaterequal'):
        return '>='
    elif(str=='lessequal'):
        return '<='
    elif(str=='notequal'):
        return '!='
    elif(str=='equal'):
        return '='
    elif(str=='greater'):
        return '>'
    elif(str=='less'):
        return '<'
    elif(str=='plus'):
        return '+'
    elif(str=='minus'):
        return '-'
    elif(str=='times'):
        return '*'
    elif(str=='upon'):
        return '/'
    elif(str=='power'):
        return '**'
    else:
        return ' '

#function for getting condition
def condition(words,i):
    while(words[i]!='then'):
        if words[i]+words[i+1] in compare_operators:
            T1.insert(END,' {} '.format(operator(words[i]+words[i+1])))
            i+=1
        elif(words[i] in variables or words[i] in logical_operators):
            T1.insert(END,' {} '.format(words[i]))
        elif(words[i]=='equal'):
            T1.insert(END,' {} '.format('=='))
        elif(words[i] in comapare_operators):
            T1.insert(END,' {} '.format(operator(words[i])))
        i+=1
    return i+1

#function for button click (Mic_Button)
def funct():
    #taking voice input on mouse click(mic Button
    global textcode
    global text_prev
    with sr.Microphone() as source:
      print("\nSpeak Anything...:)")
      T0.insert(END , "\nSpeak Anything...:)")
      text=''
      audio = r.listen(source, phrase_time_limit=20)
      try:
          text = r.recognize_google(audio)
          print("You said : {}".format(text))
          T0.insert(END,"\nYou said : \n{}".format(text))
      except:
          print("Sorry could not recognize what you said")
          T0.insert(END,"Sorry could not recognize what you said")
      #adding input to string
      text_prev=textcode
      textcode+=text

#function for last line taken
def clear():
    global text_prev
    global textcode
    textcode=text_prev
#function for converting the input to code: function for convert button
def functcon():
      global textcode

      global indent_string
      global indent
      #splitting into tokens
      tot_words=textcode.split()
      size=len(tot_words)
      i=0
      #checking whether the token is a keyword or lower case words
      words=[]
      while i<size:
          if(tot_words[i] in keywords or tot_words[i].isnumeric() or tot_words[i] in colors ):
              words.append(tot_words[i].lower())
          elif(i>0 and (tot_words[i-1]=='for' or tot_words[i-1]=='variable')):
              words.append(tot_words[i].lower())
          i+=1
      print(words)
      size=len(words)
      i=0
      #loop over all the tokens to convert into code statemnts
      while i<size:
          if(words[i]=='forward'):
              i+=1
              if(i<size and words[i].isnumeric()):
                   number1=int(words[i])
                   i+=1
              else:
                  s=''
                  number1=100
              skk.forward(number1)
              file.write("skk.forward({})\n".format(number1)+indent_string)
              T1.insert(END,"skk.forward({})\n".format(number1))
          elif(words[i]=='backward'):
              i+=1
              if(i<size and words[i].isnumeric()):
                   number1=int(words[i])
                   i+=1
              else:
                  number1=100
              skk.backward(number1)
              file.write("skk.backward({})\n".format(number1))
              T1.insert(END,"skk.backward({})\n".format(number1))
          elif(words[i]=='left' or words[i]=='lift'):
              i+=1
              if(i<size and words[i].isnumeric()):
                   number1=int(words[i])
                   i+=1
              else:
                  number1=90
              skk.left(number1)
              file.write("skk.left({})\n".format(number1))
              T1.insert(END,"skk.left({})\n".format(number1))
          elif(words[i]=='right' or words[i]=='write'):
              i+=1
              if(i<size and words[i].isnumeric()):
                   number1=int(words[i])
                   i+=1
              else:
                  number1=90
              skk.right(number1)
              file.write("skk.right({})\n".format(number1))
              T1.insert(END,"skk.right({})\n".format(number1))
          elif(words[i]=='pen'):
              i+=1
              if(i<size and words[i]=='up'):
                  skk.penup()
                  file.write("skk.penup()\n")
                  T1.insert(END,"skk.penup()\n")
              elif(i<size and words[i]=='down'):
                  skk.pendown()
                  file.write("skk.pendown()\n")
                  T1.insert(END,"skk.pendown()\n")
          elif(words[i]=='colour' or words[i]=='color'):
              i+=1
              if(i<size and words[i] not in colors):
                  skk.color("black")
                  file.write('skk.color("black")\n')
                  T1.insert(END,'skk.color("black")\n')
                  i+=1
              else:
                  skk.color(words[i])
                  file.write('skk.color("{}")\n'.format(words[i]))
                  T1.insert(END,'skk.color("{}")\n'.format(words[i]))
          elif(words[i]=='move'):
              i+=1
              if(words[i].isnumeric()):
                   number1=int(words[i])
                   i+=1
              if(words[i]=='comma' or words[i]=='and'):
                  i+=1;
              if(words[i].isnumeric()):
                   number2=int(words[i])
                   i+=1
              skk.goto(number1,number2)
          elif(words[i]=='dot'):
              if(i>0 and words[i-1] in colors):
                  cur_cul=words[i-1]
                  if(i<size and words[i].isnumeric()):
                      number1=int(words[i])
                  else:
                      number1=60
                  i+=1
              skk.dot(number1,cur_cul)
              file.write('skk.dot()\n')
              T1.insert(END,'skk.dot()\n')
          elif(words[i]=='stamp'):
                file.write('skk.stamp()\n')
                T1.insert(END,'skk.stamp()\n')
          elif(words[i]=='shape' or words[i]=='make' or words[i]=='change'):
              i+=1
              while(words[i]=='to' or words[i]=='it'):
                  i+=1;
              skk.shape(words[i])
              file.write('skk.shape("{}")\n'.format(words[i]))
              T1.insert(END,'skk.shape("{}")\n'.format(words[i]))
          elif(words[i]=='import'):
              i+=1
              if(words[i]=='kinter'):
                  T1.insert(END,'import tkinter\n')
              elif(words[i]=='speech'):
                  T1.insert(END,'import speech_recognition\n')
              elif(words[i]=='speech'):
                  T1.insert(END,'import turtle\n')
          #if condition
          elif(words[i]=='if'):
              T1.insert(END,'if(')
              i+=1
              i=condition(words,i)
              T1.insert(END,'):\n')
              indent+=3
              indent_string=' '*indent
          #while condition
          elif(words[i]=='while'):
              T1.insert(END,'while(')
              i+=1
              i=condition(words,i)
              T1.insert(END,'):\n')
              indent+=3
              indent_string=' '*indent
          elif(words[i]=='for'):
              T1.insert(END,'for ')
              i+=1
              while(words[i] in variables or words[i]=='in'):
                  T1.insert('{}'.format(words[i]))
                  i+=1
              if(words[i]=='range'):
                  T1.insert(END,' range(')
                  i+=1
                  while(words[i].isnumeric() or words[i]=='comma'):
                      T1.insert(END,'{}'.format(words[i]))
                      i+=1

          elif(words[i]=='declare'):
              i+=1
              if(i<size-2 and words[i+1]=='equal' and words[i+2].isnumeric()):
                 T0.insert(END,''+words[i]+' = '+words[i+2])
          elif(words[i]=='end' or words[i]=='and'):
              i+=1
              if(i<size and words[i]=='indent'):
                  if(indent>=3):
                      indent-=3
                      indent_string=' '*indent

              else:
                  break
          else:
              i+=1
      textcode=""
#-----------------------          convert function ends --------------------------------
def pressed():
    print("Button Pressed!")


#-------------------------------   GUI part     ----------------------------------------
textcode=" "
text_prev=" "
indent=0
indent_string=''
#Designing GUI
MainLabel=Label(root,text="This application helps you to generator Python code from your voice :)",anchor=CENTER,
                height=5).pack(side=TOP,fill='x')
mainframe=Frame(root,bg='white',width=100,height=50)
mainframe.pack(side=TOP)


T0= Text(mainframe,bg='gray40',width=50,height=38,fg='white')
T0.pack(side= LEFT,fill=BOTH)
T0.insert(END, "Please say something: ")
T1= Text(mainframe,bg='gray40',width=50,height=38,fg='white')
T1.pack(side= RIGHT,fill=BOTH)
T1.insert(END, "import turtle\nskk = turtle.Turtle()\nskk.pensize(5)\nskk.shape('turtle')\n")

#function declaration
Fmic=PhotoImage(file='./mic.png')
Fmic= Fmic.subsample(3,3)
funcframe=Frame(root,bg='seashell4',height=60)
funcframe.pack(side=BOTTOM,fill='x')

Bmic=Button(funcframe, image=Fmic,command=funct)
Bmic.pack(side=BOTTOM)

Bconvert = Button(funcframe, text = 'Convert',
                          command = functcon)
Bconvert.place(relx=0.37,rely=0.5)
Bclear = Button(funcframe, text = 'Clear',
                          command = clear)
Bclear.place(relx=0.53,rely=0.5)

turtle.done()
mainloop()
#---------------------------      GUI part ends      -----------------------------
