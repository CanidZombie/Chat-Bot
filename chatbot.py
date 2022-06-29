from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
bot = ChatBot("My bot")
convo =[ 'hello',
    'hi there !',
    'what is your name ?',
    'My name is Bot , i am created by Avijit',
    'how are you ?',
    'I am doing great these days',
    'thank you',
    'In which city you live ?',
    'I live in lucknow',
    'In which language you talk?',
    ' I mostly talk in english',
    'Thank You',
    'Welcome',
    'Its ok']
trainer = ListTrainer(bot)
trainer.train(convo)

main = Tk()

main.geometry("500x650")

main.title("Chat Bot")
img = PhotoImage(file="chatrobo.png")

photoL = Label(main, image=img)

photoL.pack(pady=5)

def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "You : " + query)
    print(type(answer_from_bot))
    msgs.insert(END, "Bot : " + str(answer_from_bot))
    textF.delete(0, END)

frame = Frame(main)

sc = Scrollbar(frame)
msgs = Listbox(frame, width=80, height=20, yscrollcommand=sc.set)

sc.pack(side=RIGHT, fill=Y)

msgs.pack(side=LEFT, fill=BOTH, pady=10)

frame.pack()

textF = Entry(main, font=("Verdana", 20))
textF.pack(fill=X, pady=10)

btn = Button(main, text="Click Here", font=("Verdana", 20), command=ask_from_bot)
btn.pack()


main.mainloop()
