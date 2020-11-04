#Libraries used: Python Turtle, Speech recognition, word2number, Tkinter
import tkinter as tk
from tkinter import *
import speech_recognition as sr
import turtle
from word2number import w2n

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
colors = ['red','black','blue','green']
keywords=['if','for','while','forward','backward','dot','shape','left','right','penup','pen','up','down','go','move','comma','and','stamp','value']
#function for button click (Mic_Button)
def funct():
    #taking voice input on mouse click(mic Button)
    T0.insert(END , "\nSpeak Anything...:)")
    global textcode
    with sr.Microphone() as source:
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
      textcode+=text

#function for converting the input to code: function for convert button
def functcon():
      global textcode
      #splitting into tokens
      tot_words=textcode.split()
      size=len(tot_words)
      i=0
      #checking whether the token is a keyword or lower case words
      words=[]
      while i<size:
          if(tot_words[i] in keywords or isnumeric(tot_words[i]) or tot_words[i] in colors ):
              words.append(tot_words[i].lower())
          i+=1
      print(words)
      i=0
      #loop over all the tokens to convert into code statemnts
      while i<size:
          if(words[i]=='forward'):
              i+=1
              if(words[i]=='by' or words[i]=='to'):
                  i+=1;
              if(words[i].isnumeric()):
                   number1=int(words[i])
                   i+=1
              else:
                  s=''
                  number1=100
              skk.forward(number1)
              file.write("skk.forward({})\n".format(number1))
              T1.insert(END,"skk.forward({})\n".format(number1))
          elif(words[i]=='backward'):
              i+=1
              if(not words[i].isnumeric()):
                  i+=1
              if(words[i].isnumeric()):
                   number1=int(words[i])
                   i+=1
              else:
                  number1=100
              skk.backward(number1)
              file.write("skk.backward({})\n".format(number1))
              T1.insert(END,"skk.backward({})\n".format(number1))
          elif(words[i]=='left' or words[i]=='lift'):
              i+=1
              if(i>=size):
                  number1=90
              elif(words[i].isnumeric()):
                   number1=int(words[i])
                   i+=1
              else:
                  number1=90
              skk.left(number1)
              file.write("skk.left({})\n".format(number1))
              T1.insert(END,"skk.left({})\n".format(number1))
          elif(words[i]=='right' or words[i]=='write'):
              i+=1
              if(i>=size or not words[i].isnumeric()):
                  number1=90
              elif(words[i].isnumeric()):
                   number1=int(words[i])
                   i+=1
              else:
                  number1=90
                  number1=w2n.word_to_num(s)
              skk.right(number1)
              file.write("skk.right({})\n".format(number1))
              T1.insert(END,"skk.right({})\n".format(number1))
          elif(words[i]=='pen'):
              i+=1
              if(words[i]=='up'):
                  skk.penup()
                  file.write("skk.penup()\n")
                  T1.insert(END,"skk.penup()\n")
              elif(words[i]=='down'):
                  skk.pendown()
                  file.write("skk.pendown()\n")
                  T1.insert(END,"skk.pendown()\n")
          elif(words[i]=='colour' or words[i]=='color'):
              i+=1
              if(words[i]=='to' or words[i]=='it'):
                  i+=1;
              if(words[i] not in colors):
                  skk.color("black")
                  file.write('skk.color("black")\n')
                  T1.insert(END,'skk.color("black")\n')
                  i+=1
              else:
                  skk.color(words[i])
                  file.write('skk.color("{}")\n'.format(words[i]))
                  T1.insert(END,'skk.color("{}")\n'.format(words[i]))
          elif(words[i]=='go' or (words[i]=='move' and words[i+1]=='to')):
              if(words[i+1]=='to'):
                   i+=2
              else:
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
                  while(i<size and not words[i].isnumeric()):
                      i+=1
              skk.dot(int(words[i]),cur_cul)
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
          elif(words[i]=='end' or words[i]=='and'):
              break
          else:
              i+=1
      textcode=""
#-----------------------          skk.stamp()
def pressed():
    print("Button Pressed!")

textcode=" "
#Designing GUI
MainLabel=Label(root,text="This application helps you to generator Python code from your voice :)",anchor=CENTER,
                height=5).pack(side=TOP,fill='x')
mainframe=Frame(root,bg='white',width=100,height=50)
mainframe.pack(side=TOP)


T0= Text(mainframe,bg='gray40',width=50,height=38,fg='white')
T0.pack(side= LEFT,fill=BOTH)
#T0.config(state="normal")
T0.insert(END, "Please say something: ")
#T0.config(state="disabled")
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
                          command = root.destroy)
Bclear.place(relx=0.53,rely=0.5)

turtle.done()
mainloop()
