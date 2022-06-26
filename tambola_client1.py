import socket
from tkinter import *
from threading import Thread
import random
from PIL import ImageTk, Image

screen_width = None
screen_height = None
SERVER = None
PORT = None
IP_ADDRESS = None
playerName = None
nameWindow = None
nameEntry = None
canvas1 = None
button = None

def receivedMsg():
    pass


def setup():
    global SERVER
    global PORT
    global IP_ADDRESS
    
    PORT = 6000
    IP_ADDRESS = '127.0.0.1'
    
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS,PORT))
    
    thread = Thread(target= receivedMsg)
    thread.start()
    
    
def saveName():
    global SERVER
    global playerName
    global nameWindow
    global nameEntry
    
    playerName = nameEntry.get()
    nameEntry.delete(0,END)
    nameWindow.destroy()
    
    SERVER.send(playerName.encode())
    

def askPlayerName():
    global playerName 
    global nameEntry
    global nameWindow
    global canvas1
    
    nameWindow = Tk()
    nameWindow.title('Tambola Family Fun')
    nameWindow.geometry('800x688')
    
    screen_width = nameWindow.winfo_screenwidth()
    screen_height = nameWindow.winfo_screenheight()
    
    bg = ImageTk.PhotoImage(file = 'C:/Users/MBajw/OneDrive/Documents/Coding.background_project.png')
    
    canvas1 = Canvas(nameWindow, widht = 500, height= 500)
    canvas1.pack(fill='both', expand= True)  
    
    canvas1.create_image(0,0, image= bg, anchor='nw')
    canvas1.create_text( screen_width/4.5, screen_height/8, text = 'Enter Name', font=('Chalkboard SE',60),fil='black')
    
    nameEntry = Entry(nameWindow, widht=15, justify='center', font= ('Chalkboard SE',30),bd=5, bg='white')  
    nameEntry.place(x= screen_width/7, y= screen_height/5.5)
    
    button = Button(nameWindow, text='Save', font= ('Chalkboard SE',30),width=11, command = saveName, height=2, bg= '#80deea',bd=3)
    button.place(x=screen_width/6, y = screen_height/4)
    
    nameWindow.resizable(True, True)
    nameWindow.mainloop()
    
    
    
gameWindow = None
ticketGrid = None
boxButton = None


def createTicket():
    global gameWindow
    global ticketGrid
    
    mainLabel = Label(gameWindow, width = 65, height = 16, relief = 'ridge', borderwidth = 5, bg='white')
    mainLabel.place(x=95, y= 119)
    
    xPos = 105
    yPos = 130
    for row in range(0,3):
        rowList = []
        for col in range(0,9):
            if (platform.system() == 'Darwin'):
                boxButton = Button(gameWindow,
                                   font = ('Chalkboard SE',18),
                                   borderwidth= 3,
                                   pady = 23,
                                   padx = 22,
                                   bg= '#fffl76',
                                   highlightbackground='#fffl76',
                                   activebackground='#c5ela5')
                
                boxButton.place(x=xPos,y=yPos)
            else:
                boxButton = tk.Button(gameWindow, 
                                      font = ('Chalkboard SE', 30),
                                      width = 3,
                                      height = 2,
                                      borderwidth = 5, 
                                      bg = '#fffl76')
                boxButton.place(x=xPos, y=yPos)
                
            rowList.append(boxButton)
            xPos += 64
        
        
        ticketGrid.append(rowList)         
        xPos = 105
        yPos += 82

currentNumberList = None

def placeNumbers():
    global ticketGrid
    global currentNumberList
    
    for row in range(0,3):
        randomColList = []
        counter = 0
        while counter <=4:
            randomCol = random.randint(0,8)
            if (randomCol not in randomColList):
                randomColList.append(randomCol)
                counter += 1
                
    numberContainer = {'0': [1,2,3,4,5,6,7,8,9],
                       '1': [10,11,12,13,14,15,16,17,18,19],
                       '2': [20,21,22,23,24,25,26,27,28,29],
                       '3': [30,31,32,33,34,35,36,37,38,39],
                       '4': [40,41,42,43,44,45,46,47,48,49],
                       '5': [50,51,52,53,54,55,56,57,58,59],
                       '6': [60,61,62,63,64,65,66,67,68,69],
                       '7': [70,71,72,73,74,75,76,77,78,79],
                       '8': [80,81,82,83,84,85,86,87,88,89,90]
                       }
    counter = 0
    while (counter < len(randomColList)):
        colNum = randomColList[counter]
        numbersListByIndex = numberContainer[str(colNum)]
        randomNumber = random.choice(numbersListByIndex)
        
        if (randomNumber not in currentNumberList):
            numberBox = ticketGrid[row][colNum]
            numberBox.configure(text=randomNumber, fg='black')
            currentNumberList.append(randomNumber)
            
            counter +=1
            
gameWindow.mainloop()