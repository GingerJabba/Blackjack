"""
AUTHOR = Chris Fisher
PROJECT NAME = Blackjack
"""
from Tkinter import *
from random import *
from pygame import mixer
import tkMessageBox
import os
import vlc


class Blackjack(object):

    def __init__(self):
        #Deck Variables
        self.win = None
        self.deckImage = []
        for i in range(1, 53):
            self.deckImage.append(str(i) + ".png")
        deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
                1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
                1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
                1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        self.zipDeck = zip(self.deckImage, deck)
        shuffle(self.zipDeck)
        #Player variables
        self.dealer_hand = []
        self.player_hand = []
        self.playing = True
        self.player_total = 0
        self.dealer_total = 0
        #Dealing variables
        self.cards = 0
        self.dcards = 0
        self.label = [None] * 5
        self.images = [None] * 5
        self.filename = [None] * 5
        self.dlabel = [None] * 5
        self.dimages = [None] * 5
        self.dfilename = [None] * 5
        #File Path Variables
        self.graphic_path = "Assets/cards/"
        self.sounds_path = "Assets/sounds/"
        #End screen variables
        #Key bindings
        #G.top.bind('<Return>', self.hit)

    def dealHand(self):
        while True:
            if len(self.player_hand) < 2:
                self.player_hand.append(self.zipDeck[0][1])
                G.addImage()
                del self.zipDeck[0]
            if len(self.dealer_hand) < 2:
                self.dealer_hand.append(self.zipDeck[0][1])
                if len(self.dealer_hand) == 2:
                    self.hidden_card = self.zipDeck[0][0]
                G.addDealerImage()
                del self.zipDeck[0]
            if len(self.dealer_hand) == 2 and len(self.player_hand) == 2:
                break
        self.hitButton = Button(G.top, text = "Hit", command=self.hit)
        self.hitButton.grid(row = 100, column = 0, pady = 200)
        self.standButton = Button(G.top, text="Stand", command=self.dealerDraw)
        self.standButton.grid(row = 100, column = 1,pady = 200)

    def handTotal(self):
        self.player_total = 0
        for i in self.player_hand:
            if i == 1:
                ace = tkMessageBox.askquestion("Aces","You have an Ace! Do you want it to be worth 1?", )
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
        G.addImage()
        del self.zipDeck[0]

    def dealerHandAdd(self):
        self.dealer_hand.append(self.zipDeck[0][1])
        G.addDealerImage()
        del self.zipDeck[0]

    def totalCheck(self):
        self.handTotal()
        self.compHandTotal()
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
        G.endScreen()

    def dealerDraw(self):
        self.playing = False
        self.hitButton.configure(state=DISABLED)
        self.standButton.configure(state=DISABLED)
        self.revealHidden()
        self.compHandTotal()
        while self.dealer_total < 17:
            self.dealerHandAdd()
            self.compHandTotal()
        G.top.after(1000, self.totalCheck)

    def hit(self, *events):
        if self.playing:
            self.handAdd()
            self.handTotal()
            if len(self.player_hand) == 5 and self.player_total < 21:
                print("FIVE CARDS IN HAND WITHOUT GOING BUST, YOU WIN!!!")
                self.win = True
                G.endScreen()

    def revealHidden(self):
        self.dfilename[1] = PhotoImage(file=self.graphic_path+self.hidden_card)
        self.dlabel[1] = Label(G.top, image=self.dfilename[1])
        self.dlabel[1].place(x=50, y=0)

    def soundEngine(self):
        self.sound_file = str(randint(1, 2)) + '.mp3'
        mixer.init(0)
        mixer.music.load(self.sounds_path+self.sound_file)
        mixer.music.play()

class G(Blackjack,object):

    def __init__(self):
        self.B = Blackjack()
        self.top = Tk()
        self.top.title("Blackjack")
        self.top.minsize(300,500)
        self.top.geometry('250x150+0+0')
        self.startButton = Button(self.top, text="Play", command=self.B.dealHand)
        self.startButton.grid(column=0, row=0)
        self.winner_file = PhotoImage(file=self.B.graphic_path+'test.gif')
        self.loser_file = PhotoImage(file = self.B.graphic_path+'lose.gif')
        self.label = Label(self.top)
    def endScreen(self):
        if self.B.win:
            vlc.MediaPlayer(self.B.graphic_path+'win.mp4')





        else:
            self.loser_image = Label(self.top, image=self.loser_file)
            self.loser_image.place(x=0,y=0)
        self.resetButton = Button(self.top, text='Restart', command=self.startup)
        self.resetButton.grid(column = 0, row = 100)

    def startup(self):
        self.resetButton.grid_forget()
        self.top.destroy()
        self.__init__()

    def addImage(self):
        x_coor = self.B.cards * 50
        self.B.images[self.B.cards] = self.B.zipDeck[0][0]
        self.B.filename[self.B.cards] = PhotoImage(file = self.B.graphic_path+self.B.images[self.B.cards])
        self.B.label[self.B.cards] = Label(self.top, image = self.B.filename[self.B.cards])
        self.B.label[self.B.cards].place(x=x_coor, y=100)
        self.B.cards += 1
        self.B.soundEngine()

    def addDealerImage(self):
        x_coor = self.B.dcards * 50
        if self.B.dcards == 1:
            self.B.dimages[self.B.dcards] = 'back.png'
        else:
            self.B.dimages[self.B.dcards] = self.B.zipDeck[0][0]
        self.B.dfilename[self.B.dcards] = PhotoImage(file=self.B.graphic_path+self.B.dimages[self.B.dcards])
        self.B.dlabel[self.B.dcards] = Label(self.top, image=self.B.dfilename[self.B.dcards])
        self.B.dlabel[self.B.dcards].place(x=x_coor, y=0)
        self.B.dcards += 1


G = G()
G.top.mainloop()
