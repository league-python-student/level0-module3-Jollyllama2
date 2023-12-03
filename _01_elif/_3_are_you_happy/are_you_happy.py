from tkinter import Tk, simpledialog, messagebox


if __name__ == '__main__':
    # TODO: Look at the AreYouHappy.png image
    #       Use pop-ups to recreate the chart using if and elif statements
    window = Tk()
    window.withdraw()
    happy = simpledialog.askstring(title='hi', prompt= 'are you happy? Yes or No only')
    if happy == "Yes":
        messagebox.showinfo(title='hi',message='keep doing whatever you are doing')
    if happy == "No":
        happy_two = simpledialog.askstring(title="hi", prompt='Do you want to be happy?')
        if happy_two == "No":
            messagebox.showinfo(title="hi", message="keep doing what ever you are doing")
        if happy_two == "Yes":
            messagebox.showinfo(title="hi",message="Change something")

    pass
