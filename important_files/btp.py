import speech_recognition as sr
import turtle
from word2number import w2n

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

#list for colors and numbers in text
colors = ['red','black','blue','green']
num_rep=['one','two','three','four','five','six','seven','eight','nine','zero',
         'eleven','twelve','thrteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen',
         'twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety'
         'hundred','thousand']

#taking voice input in loop
while(1):
  with sr.Microphone() as source:
    text=''
    print("Speak Anything :")
    audio = r.listen(source, phrase_time_limit=10)
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize what you said")

    words=text.split()
    size=len(words)
    i=0
    while i<size:
        words[i]=words[i].lower()
        i+=1
    print(words)
    i=0
    while i<size:
        if(words[i]=='forward' and i<size):
            i+=1
            #if(not words[i].isnumeric() and not words[i] in num_rep):
                #continue
            if(words[i]=='by' or words[i]=='to'):
                i+=1;
            if(words[i].isnumeric()):
                 number1=int(words[i])
                 i+=1
            else:
                s=''
                if(words[i] in num_rep):
                    i+=1
                while(i<size and words[i] in num_rep):
                     s.append(words[i]+' ')
                     i+=1
                i-=1
                if(s==''):
                     continue
                number1=w2n.word_to_num(s)
            skk.forward(number1)
            file.write("skk.forward({})\n".format(number1))
        elif(words[i]=='backward'):
            i+=1
            if(not words[i].isnumeric()):
                i+=1
            if(words[i].isnumeric()):
                 number1=int(words[i])
                 i+=1
            else:
                i-=1
                s=''
                if(words[i] not in num_rep):
                    i+=1
                while(i<size and words[i] in num_rep):
                     s.append(words[i]+' ')
                     i+=1
                i-=1
                number1=w2n.word_to_num(s)
            skk.backward(number1)
            file.write("skk.backward({})\n".format(number1))
        elif(words[i]=='left' or words[i]=='lift'):
            i+=1
            if(i>=size):
                number1=90
            elif(not words[i].isnumeric()):
                number1=90
            elif(words[i].isnumeric()):
                 number1=int(words[i])
                 i+=1
            else:
                s=''
                if(words[i] in num_rep):
                    i+=1
                while(i<size and words[i] in num_rep):
                     s.append(words[i]+' ')
                     i+=1
                i-=1
                number1=w2n.word_to_num(s)
            skk.left(number1)
            file.write("skk.left({})\n".format(number1))
        elif(words[i]=='right' or words[i]=='write'):
            i+=1
            if(i>=size or (words[i] not in num_rep and not words[i].isnumeric())):
                number1=90
            elif(words[i].isnumeric()):
                 number1=int(words[i])
                 i+=1
            else:
                s=''
                number1=0
                if(words[i] in num_rep):
                    i+=1
                while(i<size and words[i] in num_rep):
                     s.append(words[i]+' ')
                     i+=1
                i-=1
                number1=w2n.word_to_num(s)
            skk.right(number1)
            file.write("skk.right({})\n".format(number1))
        elif(words[i]=='pen'):
            i+=1
            if(words[i]=='up'):
                skk.penup()
                file.write("skk.penup()\n")
            elif(words[i]=='down'):
                skk.pendown()
                file.write("skk.pendown()\n")
        elif(words[i]=='colour' or words[i]=='color'):
            i+=1
            if(words[i]=='to' or words[i]=='it'):
                i+=1;
            if(words[i] not in colors):
                skk.color("black")
                file.write('skk.color("black")\n')
                i+=1
            else:
                skk.color(words[i])
                file.write('skk.color("{}")\n'.format(words[i]))
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
        elif(words[i]=='stamp'):
                skk.stamp()
                file.write('skk.stamp()\n')
        elif(words[i]=='shape' or words[i]=='make' or words[i]=='change'):
            i+=1
            while(words[i]=='to' or words[i]=='it'):
                i+=1;
            skk.shape(words[i])
            file.write('skk.shape("{}")\n'.format(words[i]))
        elif(words[i]=='end' or words[i]=='and'):
            break
        else:
            i+=1
  if(i<size):
      file.close()
      break
turtle.done()
