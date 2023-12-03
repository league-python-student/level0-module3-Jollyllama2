from tkinter import simpledialog, messagebox, Tk
import webbrowser


# Use this function to play a video from the internet
def play_video(url):
    webbrowser.open(url)

# =================== DO NOT MODIFY THE CODE ABOVE ===========================


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    number = simpledialog.askstring(title="hi",prompt="how many cats do you have?")
    number = int(number)
    if number >= 3:
        messagebox.showinfo(title="hi",message="You're a crazy cat person")
    if number >0 and number <3:
        messagebox.showinfo(title="hi",message="hmm,ok")
    if number == 0:
        messagebox.showinfo(title="hi",message="Yay, no cats!")

    #      5) If they have less than 3 cats AND more than 0 cats, call the
    #         play_video function below to show them a cat video
    #      6) If they have 0 cats, show them a video of A Frog Sitting on a
    #         Bench Like a Human

    pass
