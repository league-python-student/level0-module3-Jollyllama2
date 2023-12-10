from tkinter import simpledialog, messagebox, Tk
if __name__ == '__main__':
    # TODO Tell the user a story, but give them options so they can decide the
    messagebox.showinfo(title='hello',message='It was just supposed to be a normal day, but mario appeared at your door. He askes you to follow him, OR ELSE. Something seems off, but it is Mario, so you follow him anyway(for this adventure answer yes or no only, lowercase)')
    sus = simpledialog.askstring(title='well,well,well',prompt='There is a fork in the path. This your chace to escape this somewhat distrubing Mario.Do you follow him or not?')
    if sus == "no":
        messagebox.showinfo(title='hi',message='Mario teleports in front of you, calls you a biga monke,then slaps you, and then it all becomes black and you are dead')
    if sus == "yes":
        messagebox.showinfo(title='hi',message='Mario quickly debriefs you on your mission to find the lost tressure of the Kongs(He owes them some bananas)')
    ayo = simpledialog.askstring(title='well hello there',prompt='You are attacked  dny a wild Grant. do you help mario fight the evil Grant, or run., yes or no')
