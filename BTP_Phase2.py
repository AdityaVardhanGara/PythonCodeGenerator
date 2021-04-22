#Libraries used: Python Turtle, Speech recognition, word2number, Tkinter
import tkinter as tk
from tkinter import *
import speech_recognition as sr
import turtle
from time import sleep
from word2number import w2n
import os


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
root.geometry("870x1000")
r = sr.Recognizer()
#skk = turtle.Turtle()

#Opening file and including basic libraries
file = open('output.py','w')
file.write("import turtle\n\n")
file.write("skk = turtle.Turtle()\n")
#skk.pensize(5)
file.write("skk.pensize(5)\n")
#skk.shape('turtle')
file.write("skk.shape('turtle')\n\n")

#useful lists
#list of colors
colors = ['red','black','blue','green']
#list of shapes:
shapes = ['turtle','arrow']
#list of key words
keywords=['if','for','while','forward','front','backward','back','dot','shape','left','right','penup','pen','up','down','go','move','comma','and','or','stamp','value','import','kinter'
          ,'speech','turtle','colour','greater','equal','less','then','indentation','indent','increment','decrement','range','in','per','where','go','dot','declare'
          ,'program','end', 'loop','mod','block','times']
#logical operators
logical_operators=['and','or','xor','not']
compare_operators=['greater','less','greaterequal','notequal','lessequal']
#list of Libraries
libraries=['tkinter','speech_recognition','word2number']
#list of variables declared
variables=['skk','y']


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
    elif(str=='mod'):
        return '%'
    else:
        return ' '

#function for getting condition
def condition(words,i):
    size=len(words)
    while(i<size and words[i]!='then'):
        if (i+1<size and words[i]+words[i+1] in compare_operators):
            T1.insert(END,' {} '.format(operator(words[i]+words[i+1])))
            i+=1
        elif(words[i] in variables or words[i] in logical_operators or words[i].isnumeric()):
            T1.insert(END,' {} '.format(words[i]))
        elif(words[i]=='equal'):
            T1.insert(END,' {} '.format('=='))
        elif(words[i] in compare_operators):
            T1.insert(END,' {} '.format(operator(words[i])))
        i+=1
    return i+1

# declaring a help function
def help_function():
    T00.delete("1.0","end")
    T00.insert(END , "Speak Anything   :)")
    sleep(2)
#function for button click (Mic_Button)
def funct():
    #taking voice input on mouse click(mic Button
    help
    global textcode
    help_function()
    #global text_prev
    with sr.Microphone() as source:
      #print("\nSpeak Anything...:)")
      text=''
      audio = r.listen(source, phrase_time_limit=20)
      T00.delete("1.0","end")
      T00.insert(END , "You said   :)")
      try:
          text = r.recognize_google(audio)
          #print("\n\nYou said : \n{}".format(text))
          T01.insert(END,"{}\n".format(text))
      except:
          #print("Sorry could not recognize what you said")
          T01.insert(END,"Sorry could not recognize what you said")
      #adding input to string
      #text_prev=textcode
      #textcode+=text

#function for last line taken
def clear():
    #global text_prev
    #global textcode
    #textcode=text_prev
    T01.delete("1.0","end")
    file.write("\nturtle.done()")
    file.close()
    os.system('python3 output.py')
#function for converting the input to code: function for convert button
def functcon():
      global textcode

      global indent_string
      global indent
      #splitting into tokens
      #textcode=textcode.lower()
      textcode=T01.get("1.0",END)
      T01.delete("1.0","end")
      T0.insert(END,"{}\n".format(textcode))
      tot_words=textcode.split()
      size=len(tot_words)
      i=0
      #checking whether the token is a keyword or lower case words
      words=[]
      while i<size:
          if(tot_words[i] in keywords or tot_words[i].isnumeric() or tot_words[i] in colors or tot_words[i] in variables):
              words.append(tot_words[i].lower())
          elif(i>0 and (tot_words[i-1]=='for' or tot_words[i-1]=='variable')):
              words.append(tot_words[i].lower())
          i+=1
      print(words)
      print(variables)
      size=len(words)
      i=0
      #loop over all the tokens to convert into code statemnts
      while i<size:
          if(words[i]=='forward' or words[i]=='front'):
              i+=1
              if(i<size and words[i].isnumeric()):
                   number1=int(words[i])
                   i+=1
              else:
                  s=''
                  number1=100
              #skk.forward(number1)
              file.write("skk.forward({})\n".format(number1)+indent_string)
              T1.insert(END,"skk.forward({})\n".format(number1)+indent_string)
          elif(words[i]=='backward' or words[i]=='back'):
              i+=1
              if(i<size and words[i].isnumeric()):
                   number1=int(words[i])
                   i+=1
              else:
                  number1=100
              #skk.backward(number1)
              file.write("skk.backward({})\n".format(number1)+indent_string)
              T1.insert(END,"skk.backward({})\n".format(number1)+indent_string)
          elif(words[i]=='left' or words[i]=='lift'):
              i+=1
              if(i<size and words[i].isnumeric()):
                   number1=int(words[i])
                   i+=1
              else:
                  number1=90
              #skk.left(number1)
              file.write("skk.left({})\n".format(number1)+indent_string)
              T1.insert(END,"skk.left({})\n".format(number1)+indent_string)
          elif(words[i]=='right' or words[i]=='write'):
              i+=1
              if(i<size and words[i].isnumeric()):
                   number1=int(words[i])
                   i+=1
              else:
                  number1=90
              #skk.right(number1)
              file.write("skk.right({})\n".format(number1)+indent_string)
              T1.insert(END,"skk.right({})\n".format(number1)+indent_string)
          elif(words[i]=='pen'):
              i+=1
              if(i<size and words[i]=='up'):
                  #skk.penup()
                  file.write("skk.penup()\n"+indent_string)
                  T1.insert(END,"skk.penup()\n"+indent_string)
              elif(i<size and words[i]=='down'):
                  #skk.pendown()
                  file.write("skk.pendown()\n"+indent_string)
                  T1.insert(END,"skk.pendown()\n"+indent_string)
          elif(words[i]=='colour' or words[i]=='color'):
              i+=1
              if(i<size and words[i] not in colors):
                  #skk.color("black")
                  file.write('skk.color("black")\n'+indent_string)
                  T1.insert(END,'skk.color("black")\n'+indent_string)
                  i+=1
              else:
                  #skk.color(words[i])
                  file.write('skk.color("{}")\n'.format(words[i])+indent_string)
                  T1.insert(END,'skk.color("{}")\n'.format(words[i])+indent_string)
          elif((words[i]=='move'  and words[i+1]=='to') or words[i]=='go'):
              i+=1
              number1=0
              number2=0
              if(words[i].isnumeric()):
                   number1=int(words[i])
                   i+=1
              if(words[i]=='comma' or words[i]=='and'):
                  i+=1;
              if(words[i].isnumeric()):
                   number2=int(words[i])
                   i+=1
              T1.insert(END,'skk.goto('+number1+','+number2+')\n'+indent_string)
              file.write('skk.goto('+number1+','+number2+')\n'+indent_string)
          elif(words[i]=='dot'):
              if(i>0 and words[i-1] in colors):
                  cur_cul=words[i-1]
                  i+=1
                  if(i<size and words[i].isnumeric()):
                      number1=int(words[i])
                  else:
                      number1=60
                  i+=1
              else:
                  i+=1
                  cur_cul="black"
                  number1=60
              #skk.dot(number1,cur_cul)
              file.write('skk.dot({},"{}")\n'.format(number1,cur_cul)+indent_string)
              T1.insert(END,'skk.dot({},"{}")\n'.format(number1,cur_cul)+indent_string)
          elif(words[i]=='stamp'):
                file.write('skk.stamp()\n'+indent_string)
                T1.insert(END,'skk.stamp()\n'+indent_string)
                i+=1
          elif(words[i]=='shape' or words[i]=='make' or words[i]=='change'):
              i+=1
              shape=words[i]
              if(words[i] not in shapes):
                  shape='arrow'
              #skk.shape(shape)
              file.write('skk.shape("{}")\n'.format(words[i])+indent_string)
              T1.insert(END,'skk.shape("{}")\n'.format(shape)+indent_string)
          elif(words[i]=='import'):
              i+=1
              if(words[i]=='kinter'):
                  T1.insert(END,'import tkinter\n'+indent_string)
                  file.write('import tkinter\n'+indent_string)
              elif(words[i]=='speech'):
                  T1.insert(END,'import speech_recognition\n'+indent_string)
                  file.write('import speech_recognition\n'+indent_string)
              elif(words[i]=='speech'):
                  T1.insert(END,'import turtle\n')
                  file.write('import turtle\n')
          #if condition
          elif(words[i]=='if'):
              T1.insert(END,'if(')
              file.write('if(')
              i+=1
              i=condition(words,i)
              indent+=3
              indent_string=' '*indent
              T1.insert(END,'):\n'+indent_string)
              file.write('):\n'+indent_string)

          #while condition
          elif(words[i]=='while'):
              T1.insert(END,'while(')
              file.write('while(')
              i+=1
              i=condition(words,i)
              indent+=3
              indent_string=' '*indent
              T1.insert(END,'):\n'+indent_string)
              file.write('):\n'+indent_string)

          elif(words[i]=='for' or words[i] =='per' or words[i]=='where'):
              T1.insert(END,'for ')
              file.write('for ')
              i+=1
              while(words[i] not in keywords or words[i]=='in'):
                  T1.insert(END,' {} '.format(words[i]))
                  file.write(' {} '.format(words[i]))
                  i+=1
              if(words[i]=='range'):
                  T1.insert(END,' range(')
                  file.write(' range(')
                  i+=1
                  while(words[i].isnumeric() or words[i]=='comma'):
                      T1.insert(END,'{}'.format(words[i]))
                      file.write('{}'.format(words[i]))
                      i+=1
                  T1.insert(END,')')
                  file.write(')')
              indent+=3
              indent_string=' '*indent

              T1.insert(END,':\n'+indent_string)
              file.write(':\n'+indent_string)
          #elif(words[i]=='times'):
          elif(words[i]=='block'):
              i+1
              num10='4'
              if(words[i+1]=='times' and words[i].isnumeric() ):
                  num10=words[i]
                  i+=2
              indent+=3
              indent_string=' '*indent
              T1.insert(END,'for i in range('+num10+'):\n'+indent_string)
              file.write('for i in range('+num10+'):\n'+indent_string)
          elif(words[i]=='loop'):
               i+=1
               num10='4'
               if(words[i].isnumeric() ):
                  num10=words[i]
                  i+=1
               indent+=3
               indent_string=' '*indent
               T1.insert(END,'for i in range('+num10+'):\n'+indent_string)
               file.write('for i in range('+num10+'):\n'+indent_string)
               """
          elif(words[i]+words[i+1]=='openbracket'||words[i]+words[i+1]=='bracketopen'):
              T1.insert(END,'(')
          elif(words[i]+words[i+1]=='openbracket'||words[i]+words[i+1]=='bracketopen'):
              T1.insert(END,')')
              """
          elif(words[i]=='declare'):
              i+=1
              if(i<size-2 and (words[i+1]=='equal' or words[i+1]=='value') and words[i+2].isnumeric()):
                 T1.insert(END,words[i].lower()+' = '+words[i+2]+'\n'+indent_string)
                 file.write(END,words[i].lower()+' = '+words[i+2]+'\n'+indent_string)
                 variables.append(words[i].lower())
                 i+=3
          elif(words[i]=='increment'):
              i+=1
              if(i<size and words[i] in variables):
                  T1.insert(END,'{}+=1\n'.format(words[i])+indent_string)
                  file.write('{}+=1\n'.format(words[i])+indent_string)
                  i+=1
              else:
                  i+=1
          elif(words[i]=='decrement'):
              i+=1
              if(i<size and words[i] in variables):
                  T1.insert(END,'{}-=1\n'.format(words[i])+indent_string)
                  file.write('{}-=1\n'.format(words[i])+indent_string)
                  i+=1
              else:
                  i+=1
          elif(words[i] in variables):
              T1.insert(END,'{} '.format(words[i]))
              file.write('{} '.format(words[i]))
              i+=1
              while(i<size-1 and operator(words[i])!=' '):
                  T1.insert(END,'{} {}'.format(operator(words[i]),words[i+1]))
                  file.write('{} {}'.format(operator(words[i]),words[i+1]))
                  i+=2
              T1.insert(END,'\n'+indent_string)
              file.write('\n'+indent_string)
          elif(words[i]=='end' or words[i]=='and'):
              i+=1
              if(i<size and (words[i]=='indent' or words[i]=='indentation' or words[i]=='block') ):
                  if(indent>=3):
                      indent-=3
                      indent_string=' '*indent
                      T1.insert(END,'\n'+indent_string)
                      file.write('\n'+indent_string)

              elif(i<size and words[i]=='program'):
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
mainframe=Frame(root,bg='white',height=50,width=80)
mainframe.pack(fill = BOTH, expand = True,side=TOP)

subframe=Frame(mainframe,bg='white',height=35,width=40)
subframe.pack(fill = BOTH, expand = True,side=LEFT)
T0= Text(subframe,bg='gray20',fg='ghost white',font=("Helvetica", 15),
         width=40,height=25)
T0.pack(side = TOP, fill = BOTH)
T0.insert(END, "Text input so far:\n ")

T00= Text(subframe,bg='black',fg='ghost white',font=("Helvetica", 15),
         width=40,height=2)
T00.pack(side = TOP, fill = BOTH)
T00.insert(END, "You said: ")

T01= Text(subframe,bg='gray20',fg='ghost white',font=("Helvetica", 15),
         width=40,height=10)
T01.pack(side = BOTTOM,fill = BOTH)

T1= Text(mainframe,bg='gray20',fg='ghost white',font=("Helvetica", 15),
         width=40,height=35)
T1.pack(side = RIGHT, fill = BOTH)
T1.insert(END, "import turtle\n\nskk = turtle.Turtle()\nskk.pensize(5)\nskk.shape('turtle')\n\n")

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
Bclear = Button(funcframe, text = 'Execute',
                          command = clear)
Bclear.place(relx=0.53,rely=0.5)

#turtle.done()
mainloop()
#---------------------------      GUI part ends      -----------------------------
