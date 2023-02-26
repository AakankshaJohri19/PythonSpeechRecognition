_author_ = 'Aakanksha Johri'

import pdb
from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("Speech Recognition")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        self.quitButton = Button(self, text="Record Voice", command=self.google_voice)
        self.quitButton.grid(row =1, column=0 , sticky =W)

        # creating a text instance
        self.Label2 = Text(self,width =50, height =2, wrap =WORD)
        # placing the text on my window
        self.Label2.grid(row=2, column=0,columnspan=2, sticky =W)

        # creating a text instance
        self.Label1 = Text(self,width =50, height =5, wrap =WORD)
        # placing the text on my window
        self.Label1.grid(row=4, column=0,columnspan=5, sticky =W)               
        

    def  google_voice(self):
        #clear text
        self.Label1.delete(0.0, END)
        self.Label2.delete(0.0, END)
        import speech_recognition as sr
        #microphone is being recognized
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        # recognize speech using Google Speech Recognition
        try:
            text_out = r.recognize_google(audio_data=audio, key=None, language="en-IN", show_all=False)
            print(text_out+"\n")
            self.Label1.insert(0.0,  "You spoke: " + text_out )
            #write to file
            text_file = open("gvtxt.txt", 'a')
            text_file.write(text_out +"\n")
            text_file.close()
            #insert data into webapp
           
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            self.Label2.insert(0.0,  "Google Speech Recognition could not understand audio" )
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            self.Label2.insert(0.0,  "Could not request results from Google Speech Recognition service; {0}".format(e) )


root = Tk()
#size of the window
root.geometry("500x200")
app = Window(root)


root.mainloop()  





