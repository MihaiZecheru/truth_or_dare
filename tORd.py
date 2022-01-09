from tkinter import *
from tkinter import messagebox
from os.path import realpath
from subprocess import run
from random import randint

root = Tk()
root.title("Truth Or Dare")
root.geometry("300x170")
root.iconbitmap("tORd.ico")

root.configure(bg="#ff6600")


def add_players():
    global players_window
    players_window = Toplevel()
    players_window.title("Add Players")
    players_window.geometry("400x400")
    players_window.iconbitmap("tORd.ico")

    players_frame = LabelFrame(players_window, text="Players")
    players_frame.pack()

    _ = Label(players_frame, text="Player 1:").grid(row=0, column=0)
    _ = Label(players_frame, text="Player 2:").grid(row=1, column=0)
    _ = Label(players_frame, text="Player 3:").grid(row=2, column=0)
    _ = Label(players_frame, text="Player 4:").grid(row=3, column=0)
    _ = Label(players_frame, text="Player 5:").grid(row=4, column=0)
    _ = Label(players_frame, text="Player 6:").grid(row=5, column=0)
    _ = Label(players_frame, text="Player 7:").grid(row=6, column=0)
    _ = Label(players_frame, text="Player 8:").grid(row=7, column=0)
    _ = Label(players_frame, text="Player 9:").grid(row=8, column=0)
    _ = Label(players_frame, text="Player 10:").grid(row=9, column=0)

    global p1_entry, p2_entry, p3_entry, p4_entry, p5_entry, p6_entry, p7_entry, p8_entry, p9_entry, p10_entry

    p1_entry = Entry(players_frame)
    p2_entry = Entry(players_frame)
    p3_entry = Entry(players_frame)
    p4_entry = Entry(players_frame)
    p5_entry = Entry(players_frame)
    p6_entry = Entry(players_frame)
    p7_entry = Entry(players_frame)
    p8_entry = Entry(players_frame)
    p9_entry = Entry(players_frame)
    p10_entry = Entry(players_frame)
    p1_entry.grid(row=0, column=1)
    p2_entry.grid(row=1, column=1)
    p3_entry.grid(row=2, column=1)
    p4_entry.grid(row=3, column=1)
    p5_entry.grid(row=4, column=1)
    p6_entry.grid(row=5, column=1)
    p7_entry.grid(row=6, column=1)
    p8_entry.grid(row=7, column=1)
    p9_entry.grid(row=8, column=1)
    p10_entry.grid(row=9, column=1)

    _ = Button(players_window, text="Play", font=("Helvetica", 15), padx=20, bg="green",
               command=play).pack(pady=20)


global last_player
last_player = ""


def play():
    if p1_entry.get() == "" and p2_entry.get() == "" and p3_entry.get() == "" and p4_entry.get() == "" and p5_entry.get() == "" and p6_entry.get() == "" and p7_entry.get() == "" and p8_entry.get() == "" and p9_entry.get() == "" and p10_entry.get() == "":
        players = 0
    elif p2_entry.get() == "" and p3_entry.get() == "" and p4_entry.get() == "" and p5_entry.get() == "" and p6_entry.get() == "" and p7_entry.get() == "" and p8_entry.get() == "" and p9_entry.get() == "" and p10_entry.get() == "":
        players = 1
    elif p3_entry.get() == "" and p4_entry.get() == "" and p5_entry.get() == "" and p6_entry.get() == "" and p7_entry.get() == "" and p8_entry.get() == "" and p9_entry.get() == "" and p10_entry.get() == "":
        players = 2
    elif p4_entry.get() == "" and p5_entry.get() == "" and p6_entry.get() == "" and p7_entry.get() == "" and p8_entry.get() == "" and p9_entry.get() == "" and p10_entry.get() == "":
        players = 3
    elif p5_entry.get() == "" and p6_entry.get() == "" and p7_entry.get() == "" and p8_entry.get() == "" and p9_entry.get() == "" and p10_entry.get() == "":
        players = 4
    elif p6_entry.get() == "" and p7_entry.get() == "" and p8_entry.get() == "" and p9_entry.get() == "" and p10_entry.get() == "":
        players = 5
    elif p7_entry.get() == "" and p8_entry.get() == "" and p9_entry.get() == "" and p10_entry.get() == "":
        players = 6
    elif p8_entry.get() == "" and p9_entry.get() and p10_entry.get() == "":
        players = 7
    elif p9_entry.get() == "" and p10_entry.get() == "":
        players = 8
    elif p10_entry.get() == "":
        players = 9
    else:
        players = 10

    p1 = ""
    p2 = ""
    p3 = ""
    p4 = ""
    p5 = ""
    p6 = ""
    p7 = ""
    p8 = ""
    p9 = ""
    p10 = ""

    if players == 10:
        p1 = p1_entry.get()
        p2 = p2_entry.get()
        p3 = p3_entry.get()
        p4 = p4_entry.get()
        p5 = p5_entry.get()
        p6 = p6_entry.get()
        p7 = p7_entry.get()
        p8 = p8_entry.get()
        p9 = p9_entry.get()
        p10 = p10_entry.get()
        players_window.destroy()
    elif players == 9:
        p1 = p1_entry.get()
        p2 = p2_entry.get()
        p3 = p3_entry.get()
        p4 = p4_entry.get()
        p5 = p5_entry.get()
        p6 = p6_entry.get()
        p7 = p7_entry.get()
        p8 = p8_entry.get()
        p9 = p9_entry.get()
        players_window.destroy()
    elif players == 8:
        p1 = p1_entry.get()
        p2 = p2_entry.get()
        p3 = p3_entry.get()
        p4 = p4_entry.get()
        p5 = p5_entry.get()
        p6 = p6_entry.get()
        p7 = p7_entry.get()
        p8 = p8_entry.get()
        players_window.destroy()
    elif players == 7:
        p1 = p1_entry.get()
        p2 = p2_entry.get()
        p3 = p3_entry.get()
        p4 = p4_entry.get()
        p5 = p5_entry.get()
        p6 = p6_entry.get()
        p7 = p7_entry.get()
        players_window.destroy()
    elif players == 6:
        p1 = p1_entry.get()
        p2 = p2_entry.get()
        p3 = p3_entry.get()
        p4 = p4_entry.get()
        p5 = p5_entry.get()
        p6 = p6_entry.get()
        players_window.destroy()
    elif players == 5:
        p1 = p1_entry.get()
        p2 = p2_entry.get()
        p3 = p3_entry.get()
        p4 = p4_entry.get()
        p5 = p5_entry.get()
        players_window.destroy()
    elif players == 4:
        p1 = p1_entry.get()
        p2 = p2_entry.get()
        p3 = p3_entry.get()
        p4 = p4_entry.get()
        players_window.destroy()
    elif players == 3:
        p1 = p1_entry.get()
        p2 = p2_entry.get()
        p3 = p3_entry.get()
        players_window.destroy()
    elif players == 2:
        p1 = p1_entry.get()
        p2 = p2_entry.get()
        players_window.destroy()
    elif players == 1 or players == 0:
        players_window.destroy()
        messagebox.showerror("Not Enough Players", "The application will restart due to not having enough players.")
        script = realpath(__file__)
        root.destroy()
        run(["python", str(script)])

    play = Toplevel()
    play.title("Truth Or Dare")
    play.geometry("600x520")
    play.iconbitmap("tORd.ico")

    playerBox = LabelFrame(play, text="Current Player:", pady=5, font=("Helvetica", 15))
    playerBox.grid(row=0, column=0, columnspan=3, padx=150)

    truths = ["What is your most embarrassing moment?", "What was the last lie you told?", "What is your biggest fear?",
              "Have you gone skinny dipping?",
              "If you could go on a date with anyone from this group, who would that person be?",
              "Have you ever had a crush on someone from the group?",
              "Which person knows something about you that you don’t want revealed?",
              "What was the biggest lie you ever told?", "What is your biggest regret?",
              "What’s something you find a turn-on that you think most other people don’t?", "Do you have a fetish?",
              "What makes you feel jealous?", "What was your childhood nickname?",
              "What was/is your longest and best friendship?",
              "Who here would you date who's the same sex as you?", "What's your biggest pet peeve?",
              "Who do you like the least from this group?", "Who do you like the most out of this group?",
              "Who has the best personality out of this group?", "Who is the hottest/cutest person here?",
              "What was your last lie?", "Have you ever practiced kissing with an inanimate object",
              "Do you ever talk to yourself in the mirror?", "What do you value most in a friendship",
              "Who here do you think will end up the richest?", "What was your first impression of everyone here?",
              "What's your dirtiest pickup line", "What's the worst grade you've ever gotten?"]
    dares = ["Hold hands with the person next to you until your next turn", "Tape your mouth shut",
             "Kiss the person to your right on the back of their neck",
             "See how many grapes you can stuff in your mouth", "Fake cry",
             "Call a random number and shout angrily in another language until they hang up",
             "Trade clothes with the person next to you",
             "Do your best impersonation of someone in the group, until the group guesses who you’re impersonating",
             "Eat a whole piece of paper", "Show the most embarrassing photo of you from your phone",
             "Give the person to your right a foot massage",
             "Stuff ice inside your bra or underwear and leave it there for 60 seconds",
             "Have a intense conversation with a inanimate object", "Give the person to your right a lap dance",
             "Spin the bottle and take the shirt off of whoever it lands on using only your teeth",
             "Tell everybody an embarrassing story about yourself", "Take off a main article of clothing",
             "Slap the person to your left on the booty",
             "Blindfolded, spin around for 10 seconds. Kiss the person in front you at the end of your spinning",
             "Twerk in front of the group for 20 seconds", "Lick the foot of the person to your right",
             "Say something dirty to the person on your left", "Take off your shirt until your next turn",
             "Moan really loud", "Yell the first word that comes to your mind right now",
             "Let the person to your left go through your phone for 2 minutes", "Bite a bar of soap",
             "Sit on the person to your left's lap and move around",
             "Change clothes with the person sitting next to you", "Kiss the person across from you on the cheek",
             "Talk to a pillow like it is your crush",
             "Dance to your favorite song in front of everyone the way you would do it in private",
             "Sniff everyone's feet and rate them from stinkiest to cleanest",
             "Give your phone to the person across from you and let them send a text to whoever they want."]

    def get_player():
        global last_player
        player_list = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
        for i in reversed(range(len(player_list))):
            if player_list[i] == "":
                player_list.remove(player_list[i])
        current_player = last_player
        while current_player == last_player:
            current_player = player_list[randint(0, (len(player_list) - 1))]
        last_player = current_player
        return last_player

    _ = Label(playerBox, text=get_player(), fg="red", bg="#A9A9A9", padx=100, pady=5, font=("Helvetica", 15)).pack()

    prompt_frame = LabelFrame(play, text="Prompt", padx=20, font=("Helvetica", 15))
    prompt_frame.grid(row=2, column=0, columnspan=3, padx=10)
    _ = Label(prompt_frame, text="\t").pack()

    def get_truth():
        global last_truth
        last_truth = ""
        for widget in prompt_frame.winfo_children():
            widget.destroy()
        truth = truths[randint(0, (len(truths) - 1))]
        while truth == last_truth:
            truth = truths[randint(0, (len(truths) - 1))]
        last_truth = truth
        _ = Label(prompt_frame, text=truth).pack()

    def get_dare():
        global last_dare
        last_dare = ""
        for widget in prompt_frame.winfo_children():
            widget.destroy()
        dare = dares[randint(0, (len(dares) - 1))]
        while dare == last_dare:
            dare = truths[randint(0, (len(dares) - 1))]
        last_dare = dare
        _ = Label(prompt_frame, text=dare).pack()

    _ = Button(play, text="Truth", padx=30, pady=10, bg="cyan", command=get_truth, font=("Helvetica", 15, "bold"),
               bd=7).grid(row=1, column=0, pady=50, padx=80)
    _ = Button(play, text="Dare", padx=30, pady=10, bg="cyan", command=get_dare, font=("Helvetica", 15, "bold"),
               bd=7).grid(row=1, column=2, pady=50, padx=80)

    def next():
        for widget in prompt_frame.winfo_children():
            widget.destroy()
        _ = Label(prompt_frame, text="\t").pack()

        for widget in playerBox.winfo_children():
            widget.destroy()

        _ = Label(playerBox, text=get_player(), fg="red", bg="#A9A9A9", padx=100, pady=5, font=("Helvetica", 15)).pack()

    _ = Button(play, text="Next", command=next, padx=20, pady=5, bg="green", font=("Helvetica", 27)).grid(row=5,
                                                                                                          column=0,
                                                                                                          columnspan=3,
                                                                                                          pady=10)


_ = Button(root, text="Start", padx=100, pady=30, bg="green", font=("Helvetica", 32), bd=10, command=add_players).pack(
    ipadx=30, pady=10)

root.mainloop()
