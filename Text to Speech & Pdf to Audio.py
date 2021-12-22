import pyttsx3
import PyPDF2
from tkinter import *
from tkinter.messagebox import *


engine = pyttsx3.init()
root = Tk()
root.title("virtual agent")
engine = pyttsx3.init()

#  rate
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)

#  volume
volume = engine.getProperty('volume')
engine.setProperty('volume', 1)


# def Text to Audio
def TexttoAudio():
    root = Tk()
    root.title("virtual agent")
    e = Entry(root, width=50, borderwidth=5, font=("arial", 13))
    e.grid(row=0, column=0, columnspan=3, padx=50, pady=30)

    def click_fun():
         e.delete(0, END)

    def male():
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)

    def female():
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)

    def speak():
        engine = pyttsx3.init()
        speaker = e.get()
        engine.say(speaker)
        engine.runAndWait()
        engine.stop()

    def listen():
        engine = pyttsx3.init()
        audio_listner = e.get()
        engine.save_to_file(audio_listner, "test.mp3")
        engine.runAndWait()
        engine.stop()
        showinfo("python says", "audio is saved ")
    def stop():
        root.destroy()

    Label(root, text="choose the voice", bg="black", fg="white", font="Arial 12 underline").grid(row=1, column=0)
    # creating buttons
    buttonMALE = Button(root, text="MALE", command=male, fg="white", bg="black", padx=30, pady=10, font=("arial", 13))

    buttonFEMALE = Button(root, text="FEMALE", command=female, fg="white", bg="black", padx=30, pady=10,
                          font=("arial", 13))

    buttonSAY = Button(root, text="Say", command=speak, fg="white", bg="black", padx=30, pady=10, font=("arial", 13))

    buttonSAVE = Button(root, text="Save", command=listen, fg="white", bg="black", padx=30, pady=10, font=("arial", 13))

    buttonCLEAR = Button(root, text="Clear", command=click_fun, fg="white", bg="black", padx=30, pady=10,font=("arial", 13))

    buttonEXIT = Button(root, text="EXIT", command=stop, fg="white", bg="black", padx=30, pady=10, font=("arial", 13))


    buttonMALE.grid(row=1, column=1)
    buttonFEMALE.grid(row=1, column=2)
    buttonSAY.grid(row=2, column=0)
    buttonSAVE.grid(row=2, column=1)
    buttonCLEAR.grid(row=2, column=2)
    buttonEXIT.grid(row=3, column=1)

def PDFtoAudio():
     root = Tk()
     root.title("PDF TO AUDIO")
     def readPDF():
         book = open("English.pdf", "rb")
         pdfReader = PyPDF2.PdfFileReader(book)
         pages = pdfReader.numPages
         print(pages)
         for num in range(0, pages):
             speaker = pyttsx3.init()
             page = pdfReader.getPage(num)
             text = page.extractText()
             print(text)
             speaker.say(text)
             speaker.runAndWait()

     def male():
         voices = engine.getProperty('voices')
         engine.setProperty('voice', voices[0].id)

     def female():
         voices = engine.getProperty('voices')
         engine.setProperty('voice', voices[1].id)

     Label(root, text="choose the voice", bg="black", fg="white", font="Arial 12 underline").grid(row=1, column=0)
     # creating buttons
     buttonMALE = Button(root, text="MALE", command=male, fg="white", bg="black", padx=30, pady=10, font=("arial", 13))

     buttonFEMALE = Button(root, text="FEMALE", command=female, fg="white", bg="black", padx=30, pady=10,
                           font=("arial", 13))
     buttonREAD =Button(root, text=" ReadPDF  ",command=readPDF, fg="white", bg="black", padx=30, pady=10, font=("arial", 13))


     buttonMALE.grid(row=1, column=1)
     buttonFEMALE.grid(row=1, column=2)
     buttonREAD.grid(row=2, column=1)

def EXIT():
    root.destroy()


# creating buttons T TO S & PDF TO S

button1 =Button(root, text=" Text to Audio  ",command=TexttoAudio, fg="white", bg="black", padx=30, pady=10, font=("arial", 13))
button2 =Button(root, text=" PDF TO Audio   ",command=PDFtoAudio, fg="white", bg="black", padx=30, pady=10, font=("arial", 13))
button3 =Button(root, text="  CLOSE ",command=EXIT, fg="white", bg="black", padx=30, pady=10, font=("arial", 13))

button1.grid(row=1,column=0)
button2.grid(row=1,column=2)
button3.grid(row=2,column=1)

root.mainloop()
