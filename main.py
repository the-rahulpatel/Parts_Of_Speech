from tkinter import *
import anthropic
import os

print('this is the master branch')

root = Tk()
root.title("PoS AI")
root.geometry("700x500")
root.resizable(0,0)
welcome_text = Label(root,text='Parts Of Speech',font=("Arial",25)).pack(pady=50)

user = StringVar()
user_input = Entry(root,textvariable=user,bd=2)
user_input.pack(pady=100)
labels = []
def submit():
    use = user.get()
    global labels
    if labels:
        for i in labels:
            i.pack_forget()
        labels = []
    client = anthropic.Anthropic(
        # defaults to os.environ.get("ANTHROPIC_API_KEY")
        api_key=os.environ.get("CLAUDE_API"),
    )
    message = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": f"You are now an expert at identifying parts of speech. You are a British grammar master, and all kinds of people come to you irrespective of their proficiency in the English langauge. You are asked to only state the part of speech. In the following sentence accurately identify the part of speech for each word in British English:{use}"}
        ]
    )
    answer = message.content[0].text.split('\n')
    for i in answer:
        label = Label(root,text=i)
        labels.append(label)
    for l in labels:
        l.pack()
    
    # Label(root,text=message.content[0].text).pack(pady=20)
b = Button(root,text="Press",width=10,command=submit)
b.pack()



# message = client.messages.create(
    # model="claude-3-opus-20240229",
    # max_tokens=1024,
    # messages=[
        # {"role": "user", "content": f"You are now an expert at identifying parts of speech. You are a British grammar master, and all kinds of people come to you irrespective of their proficiency in the English langauge. In the following sentence accurately identify the technical grammar terms for each word in British English:{user_input}"}
    # ]
# )

root.mainloop()
