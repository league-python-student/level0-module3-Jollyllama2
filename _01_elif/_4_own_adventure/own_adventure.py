from tkinter import simpledialog, messagebox, Tk
if __name__ == '__main__':
    # TODO Tell the user a story, but give them options so they can decide the
    messagebox.showinfo(title='hello',message='It was just supposed to be a normal day, but mario appeared at your door. He askes you to follow him, OR ELSE. Something seems off, but it is Mario, so you follow him anyway(for this adventure answer yes or no only, lowercase)')
    sus = simpledialog.askstring(title='well,well,well',prompt='There is a fork in the path. This your chance to escape this somewhat disturbing Mario.Do you follow him or not?')
    if sus == "no":
        messagebox.showinfo(title='hi',message='Mario teleports in front of you, calls you a biga monke,then slaps you, and then it all becomes black and you are dead')
    if sus == "yes":
        messagebox.showinfo(title='hi',message='Mario quickly debriefs you on your mission to find the lost treasure of the Kongs(He owes them some bananas)')
        wow = simpledialog.askstring(title='well hello there',prompt='You are attacked  by a wild Grant. Do you help mario fight the evil Grant?')
        if wow == "no":
            messagebox.showinfo(title='hi',message='You run away and here the battle continue. You see mario flung into the sky before death, angrily yelling at you')
            dead_mario = simpledialog.askstring(title='hi',prompt='You see the mine Mario told you the treasure was in. All of a sudden you hear the wild Grant grunt as it searches for you. You may have enough time to run into the mine. Do you do it?')
            if dead_mario == 'no':
                simpledialog.askstring(title='hi',prompt='You quickly hide in the shrub. However the wild Grants sense of smell is too keen, and it finds and ends you')
            if dead_mario == 'yes':
                messagebox.showinfo(title='aDFDFGHGJK', message= 'You run as fast as you can towards the mine, whilst hearing the beast behind you. You just barely make it in, as the wild Grant is stuck at the entrance. However this also means it is going to take a while to get out.You deceide to start searching,and use the matches You had in your pocket, (Which you never knew you had) light them, and start searching')
                the_sign = simpledialog.askstring(title='Almost there',prompt=' You see an ancient sign that says "Both riches and dnager lie ahead". All of a sudden you here a noise coming from withen the cavern , and it is very close. Do you jump and hide?')
                if the_sign == 'yes':
                    messagebox.showinfo(title='hi',message='The mystery figure hears you jump and out of fright throws the spear it has right at you, ad I think you know how that goes' )
                if the_sign == 'no':
                    messagebox.showinfo(title='hi',message='you slowly advance towards the figure, who sees your light and calms down, knowing your another explorer, and annoces that he is luigi, tells oyu there is no treasure, and you and him head back to your house, chill, and then he is your roommate! ')
        if wow == 'yes':
            messagebox.showinfo(title='ayyyyyyoooooooooo tra-s furry', message= 'You try to help mario, but he starts running and abandons you to the grant, who ends you...')