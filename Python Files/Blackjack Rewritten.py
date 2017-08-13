"""
AUTHOR = Chris Fisher
PROJECT NAME = Blackjack
"""
from Tkinter import *
from random import *
import os
from pygame import mixer




class Blackjack(object):

    def __init__(self):
        #GUI initilisation
        self.top = Tk()
        self.top.title("Blackjack")
        self.top.minsize(300,500)
        self.top.geometry('250x150+0+0')
        self.deckImage = []
        self.startButton = Button(self.top, text="Play", command=self.dealHand)
        self.startButton.grid(column=0, row=0)
        #Deck Variables
        for i in range(1, 53):
            self.deckImage.append(str(i) + ".png")
        hearts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        spades = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        diamonds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        clubs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        deck = hearts + spades + diamonds + clubs
        self.zipDeck = list(zip(self.deckImage, deck))
        shuffle(self.zipDeck)
        #Player variables
        self.dealer_hand = []
        self.player_hand = []
        self.playing = True
        self.player_total = 0
        self.dealer_total = 0
        #Dealing variables
        self.graphic_path = '/Users/Chris/Documents/OneDrive/Chris/A-Level/Computer Science/Programs/untitled3/Blackajck/Assets/cards/'
        os.chdir(self.graphic_path)
        self.cards = 0
        self.dcards = 0
        self.label = [None] * 5
        self.images = [None] * 5
        self.filename = [None] * 5
        self.dlabel = [None] * 5
        self.dimages = [None] * 5
        self.dfilename = [None] * 5
        self.loser_image = None
        #End screen variables
        self.winner_file = PhotoImage(file='win.gif')
        self.loser_file = PhotoImage(file = 'lose.gif')
        self.winner_image = None
        self.hidden_card = None
        #Key bindings
        self.top.bind('<Return>', self.hit)
        self.sound_path = '/Users/Chris/Documents/OneDrive/Chris/A-Level/Computer Science/Programs/untitled3/Blackajck/Assets/sounds/'
        self.sound_file = str(randint(1,2))+'.mp3'

        self.soundEngine()

    def startup(self):
        self.resetButton.grid_forget()
        self.top.destroy()
        self.__init__()

    def dealHand(self):
        while True:
            if len(self.player_hand) < 2:
                self.player_hand.append(self.zipDeck[0][1])
                self.addImage()
                del self.zipDeck[0]
            if len(self.dealer_hand) < 2:
                self.dealer_hand.append(self.zipDeck[0][1])
                if len(self.dealer_hand) == 2:
                    self.hidden_card = self.zipDeck[0][0]
                self.addDealerImage()
                del self.zipDeck[0]
            if len(self.dealer_hand) == 2 and len(self.player_hand) == 2:
                break
        self.hitButton = Button(self.top, text = "Hit", command=self.hit)
        self.hitButton.grid(row = 100, column = 0, pady = 200)
        self.standButton = Button(self.top, text="Stand", command=self.dealerDraw)
        self.standButton.grid(row = 100, column = 1,pady = 200)

    def handTotal(self):
        self.player_total = 0
        for i in self.player_hand:
            if i == 1:
                ace = messagebox.askquestion("Aces","You have an Ace! Do you want it to be worth 1?", )
                if ace == "no":
                    i = 11
            self.player_total += i
        if self.player_total > 21 and self.playing:
            self.dealerDraw()

    def compHandTotal(self):
        self.dealer_total = 0
        self.dealer_hand.sort(reverse=True)
        for i in self.dealer_hand:
            if i == 1:
                total1 = self.dealer_total + 1
                total11 = self.dealer_total + 11
                if total1 < 21 < total11:
                    i = 1
                elif self.player_total < total11 < 21:
                    i = 11
                elif total11 == 21:
                    i = 11
                elif total11 < 17 and (total11 != 21 or (self.player_total < total11 < 21)):
                    i = 1
                else:
                    i = 1
            self.dealer_total += i

    def handAdd(self):
        self.player_hand.append(self.zipDeck[0][1])
        self.addImage()
        del self.zipDeck[0]

    def dealerHandAdd(self):
        self.dealer_hand.append(self.zipDeck[0][1])
        self.addDealerImage()
        del self.zipDeck[0]

    def totalCheck(self):
        self.handTotal()
        self.compHandTotal()
        self.win = None
        if self.dealer_total > 21:
            self.win = True
        if self.player_total == 21:
            self.win = True
        elif self.dealer_total == 21:
            self.win = False
        elif self.player_total > self.dealer_total and (self.player_total < 21 and self.dealer_total < 21):
            self.win = True
        elif self.player_total < self.dealer_total and self.dealer_total > 21:
            self.win = True
        elif self.player_total == self.dealer_total:
            self.win = True
        else:
            self.win = False
        self.endScreen()

    def dealerDraw(self):
        self.playing = False
        self.hitButton.configure(state=DISABLED)
        self.standButton.configure(state=DISABLED)
        self.revealHidden()
        self.compHandTotal()
        while self.dealer_total < 17:
            self.dealerHandAdd()
            self.compHandTotal()
        self.top.after(1000, self.totalCheck)

    def hit(self, *events):
        if self.playing:
            self.handAdd()
            self.handTotal()
            if len(self.player_hand) == 5 and self.player_total < 21:
                print("FIVE CARDS IN HAND WITHOUT GOING BUST, YOU WIN!!!")

    def addImage(self):
        x_coor = self.cards * 50
        self.images[self.cards] = self.zipDeck[0][0]
        self.filename[self.cards] = PhotoImage(file = self.images[self.cards])
        self.label[self.cards] = Label(self.top, image = self.filename[self.cards])
        self.label[self.cards].place(x=x_coor, y=100)
        self.cards += 1
        self.soundEngine()

    def addDealerImage(self):
        x_coor = self.dcards * 50
        if self.dcards == 1:
            self.dimages[self.dcards] = 'back.png'
        else:
            self.dimages[self.dcards] = self.zipDeck[0][0]
        self.dfilename[self.dcards] = PhotoImage(file=self.dimages[self.dcards])
        self.dlabel[self.dcards] = Label(self.top, image=self.dfilename[self.dcards])
        self.dlabel[self.dcards].place(x=x_coor, y=0)
        self.dcards += 1

    def revealHidden(self):
        self.dfilename[1] = PhotoImage(file=self.hidden_card)
        self.dlabel[1] = Label(self.top, image=self.dfilename[1])
        self.dlabel[1].place(x=50, y=0)

    def endScreen(self):
        if self.win:
            self.winner_image = Label(self.top, image = self.winner_file)
            self.winner_image.place(x = 0, y = 0)
        else:
            self.loser_image = Label(self.top, image = self.loser_file)
            self.loser_image.place(x=0,y=0)
        self.resetButton = Button(self.top, text = 'Restart', command = self.startup)
        self.resetButton.grid(column = 0, row = 100)

    def soundEngine(self):
        os.chdir(self.sound_path)
        mixer.init(0)
        mixer.music.load(self.sound_file)
        mixer.music.play()
        os.chdir(self.graphic_path)
B = Blackjack()
B.top.mainloop()
