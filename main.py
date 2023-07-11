from tkinter import *
from lorem.text import TextLorem


def start_test():
    global canvas
    # When test starts, hide start screen and start button
    canvas.grid_forget()
    start_button.grid_forget()

    def count_down(count):  # Basic timer function
        test_canvas.itemconfig(timer_text, text=f"Time remaining: {count}")
        if count > 0:
            window.after(1000, count_down, count-1)
        if count == 0:
            end_test()

    def end_test():  # Test summary screen
        test_canvas.itemconfig(guide_text, text=f"\n\nYou typed {current_position} characters in 60 seconds."
                                           f"\n\nThis means your characters per minute (cpm) is {current_position}."
                                           f"\n\nThe average cpm for adults is 200."
                                           f"\n\nThe world record is 1060 cpm.",
                               fill="black", font=("Courier", 30)
                               )
        test_canvas.itemconfig(completed_text, text="")
        test_canvas.itemconfig(timer_text, text="Time's up!")
        start_button.grid(row=2, column=0, columnspan=2)

        window.unbind('<KeyPress>')  # Keyboard is no longer listening while user is at test summary screen

    # Create bigger canvas for the test's "guide text" and "completed text" to go
    test_canvas = Canvas(width=1200, height=600, bg="white")
    test_canvas.grid(row=1, column=0, columnspan=2)

    # Generate random paragraph of text
    lorem = TextLorem(srange=(100, 101))
    test_text = lorem.sentence()
    test_text_list = [*test_text]
    current_position = 0  # Both a score counter and a way to track how far the user has gotten through the test text
    user_text = ""

    timer_text = test_canvas.create_text(
        600, 30, text="60", fill="black", font=("Times", 30, "bold")
    )
    guide_text = test_canvas.create_text(
        0, 50, width=1200, text=test_text, justify="center", fill="black", font=("Arial", 20), anchor=NW
    )
    completed_text = test_canvas.create_text(
        0, 350, width=1200, text=user_text, fill="grey", font=("Arial", 20), anchor=W
    )

    count_down(60)

    def check_keystroke(e):
        nonlocal current_position, user_text
        # Check if the pressed key is the same as the current character that the user has reached in the test text
        if e.char == test_text_list[current_position]:
            user_text = user_text + e.char  # Add the pressed key to the guide text being formed along the bottom
            test_canvas.itemconfig(completed_text, text=user_text)
            current_position += 1  # Increment position in test text (and also score)

    # Bind the Mouse button event
    window.bind('<KeyPress>', check_keystroke)


# Create window
window = Tk()
window.title("Typing Speed App")
window.config(padx=50, pady=50, bg="white", highlightthickness=0)
window.minsize(width=600, height=600)

# Create canvas with logo and title
canvas = Canvas(width=600, height=600, bg="white", highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(300, 300, image=logo_image)
canvas.create_text(300, 100, text="Typing Speed Test!", fill="black", font=("Courier", 40, "bold"))
canvas.grid(row=0, column=0, columnspan=3)

# Create start button
start_button = Button(text="Start test", bg="white", highlightthickness=0, command=start_test)
start_button.grid(row=1, column=1)


window.update()
window.mainloop()
