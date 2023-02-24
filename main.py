"""Author:  Thomas Warenski
Date written: 2/24/23
Version 1.0
Assignment:   Final Project
Short Desc:   Design your own tkinter application.
"""
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as fileTk

# Functions that do not rely on any later definitions
def openWindow(currentWindow,newWindow):  # Pretty straightforward, switches the open window.
	currentWindow.withdraw()
	newWindow.deiconify()

def save(text):  # Offers an option to save
	saveFile = fileTk.asksaveasfile(parent = "self", filetypes = "fList")
	saveFile.append(text)

# Game variables and functions, unrelated to GUI.
goalWords = 1000
toSave = ""

# Windows and window setup. The names should be pretty self-evident.
mainWindow = tk.Tk()
mainWindow.title("Home")
mainWindow.columnconfigure(0, weight = 1)
mainWindow.rowconfigure(0, weight = 1)

playWindow = tk.Tk()
playWindow.title("Play")
playWindow.columnconfigure(0, weight = 1)
playWindow.rowconfigure(0, weight = 1)
playWindow.withdraw()

settingsWindow = tk.Tk()
settingsWindow.title("Settings")
settingsWindow.columnconfigure(0, weight = 1)
settingsWindow.rowconfigure(0, weight = 1)
settingsWindow.withdraw()

helpWindow = tk.Tk()
helpWindow.title("Help")
helpWindow.columnconfigure(0, weight = 1)
helpWindow.rowconfigure(0, weight = 1)
helpWindow.withdraw()

goalWindow = tk.Tk()
goalWindow.title("Help")
goalWindow.columnconfigure(0, weight = 1)
goalWindow.rowconfigure(0, weight = 1)
goalWindow.withdraw()

themeWindow = tk.Tk()
themeWindow.title("Help")
themeWindow.columnconfigure(0, weight = 1)
themeWindow.rowconfigure(0, weight = 1)
themeWindow.withdraw()

victoryWindow = tk.Tk()
victoryWindow.title("You Win!")
victoryWindow.columnconfigure(0, weight = 1)
victoryWindow.rowconfigure(0, weight = 1)
victoryWindow.withdraw()


# Photos for each theme. # Todo: add new themes.
# Consists of a dictionary of tuples and a tuple of dictionary keys. I used tuples because this data will not change.
themeDictionary = {
	"Test Theme" : (("image.png","Alt Text"),
								("image.png","Alt Text"),
								("image.png","Alt Text"),
								("image.png","Alt Text"),
								("image.png","Alt Text"),
								("image.png","Alt Text"),
								("image.png","Alt Text"),
								("image.png","Alt Text"),
								("image.png","Alt Text"),
								("image.png","Alt Text"))
}  # Dictionary of images.
themeList = ("Test Theme",)  # Tuple of keys.

# Contents of mainWindow.
mainFrame = tk.Frame(mainWindow)  # Holds all the widgets of the main window.
mainFrame.columnconfigure(0, weight = 1)
mainFrame.columnconfigure(1, weight = 1)
mainFrame.columnconfigure(2, weight = 1)
mainFrame.rowconfigure(0, weight = 1)
mainFrame.rowconfigure(1, weight = 1)

playButton = tk.Button(mainFrame, text = "Play", width = 10, command = lambda : openWindow(mainWindow, playWindow))  # Button opens the play window.
playButton.bind()
playButton.grid(column = 1, row = 0, sticky = "NESW")

settingsButton = tk.Button(mainFrame, text = "Settings", width = 10, command = lambda : openWindow(mainWindow, settingsWindow))  # Button opens the settings window.
settingsButton.grid(column = 0, row = 1, sticky = "NESW")

helpButton = tk.Button(mainFrame, text = "Help", width = 10, command = lambda :openWindow(mainWindow, helpWindow))  # Button opens the help window.
helpButton.grid(column = 2, row = 1, sticky = "NESW")
	
mainFrame.grid()

# Contents of playWindow. Todo: playEntrySubmitEvent: update image.
playFrame = tk.Frame(playWindow)  # Holds all of the widgets in playWindow.
playFrame.columnconfigure(0, weight = 0)
playFrame.columnconfigure(1, weight = 1)
playFrame.columnconfigure(2, weight = 5)
playFrame.columnconfigure(3, weight = 1)
playFrame.columnconfigure(4, weight = 0)
playFrame.rowconfigure(0, weight = 1)
playFrame.rowconfigure(1, weight = 5)

playEntry = tk.Text(playFrame, width = 50, height = 10)  # The main portion of the game, where all the writing input is.
playEntry.grid(row = 1, column = 1, columnspan = 3, sticky = "NESW")

returnButtonPlay = tk.Button(playFrame, text = "Back", width = 5, command = lambda : openWindow(playWindow, mainWindow))  # Button closes the playWindow and opens mainWindow again.
returnButtonPlay.grid(row = 0, column = 1, sticky = "NEW")

playEntryScroll = ttk.Scrollbar(playFrame, orient = "vertical", command = playEntry.yview)  # Scrolls the text entry playEntry.
playEntryScroll.grid(row = 0, column = 0, rowspan = 2, sticky = "NESW")
playEntry.configure(yscrollcommand = playEntryScroll.set)

sceneryImage = tk.PhotoImage(master = playFrame, file = themeDictionary["Test Theme"][0][0])  # PhotoImage widget for the scenery label.
scenery = tk.Label(playFrame, image = sceneryImage, text = themeDictionary["Test Theme"][0][1], compound = "top")  # Label with a picture and text. The "motivation" of the game.
scenery.grid(column = 2, row = 0, stick = "NSEW")

playProgress = ttk.Progressbar(playFrame, mode = "determinate", orient = "vertical", value = 0)  # Progress tracker to encourage a user and give them a rough estimate of how much they have left.
playProgress.grid(row = 0, column = 4, rowspan = 2, sticky = "NESW")

# Special function that will be used to update the progress.
def playEntrySubmitEvent():
	global playEntry, goalWords, playProgress, toSave
	text = playEntry.get("0.0", tk.END)
	
	if playProgress["value"] < (len(text.split()) * 100) / goalWords:
		playProgress["value"] = (len(text.split()) * 100) / goalWords
		
	if playProgress["value"] >= 100:  # If the goal is met, runs the ending.
		openWindow(playWindow, victoryWindow)
		toSave = text
		playEntry.delete("0.0", tk.END)
		playProgress["value"] = 0.0

playEntrySubmit = tk.Button(playFrame, text = "Update", command = playEntrySubmitEvent)  # Button that runs the update event.
playEntrySubmit.grid(column = 3, row = 0, sticky = "NEW")

playFrame.grid()

# Contents of settingsWindow
settingsFrame = tk.Frame(settingsWindow)  # Widget holder for settingsWindow.
settingsFrame.rowconfigure(0, weight = 1)
settingsFrame.rowconfigure(1, weight = 1)
settingsFrame.columnconfigure(0, weight = 1)
settingsFrame.columnconfigure(1, weight = 1)
settingsFrame.columnconfigure(2, weight = 1)
settingsFrame.columnconfigure(3, weight = 1)

returnButtonSettings = tk.Button(settingsFrame, text = "Back", width = 5, command = lambda : openWindow(settingsWindow, mainWindow))  # Button sends the user back to mainWindow.
returnButtonSettings.grid(row = 0, column = 0, sticky = "NESW")

goalButton = tk.Button(settingsFrame, text = "Goal", width = 10, command = lambda : openWindow(settingsWindow,goalWindow))  # Button to open goalWindow.
goalButton.grid(row = 1, column = 0, columnspan = 2, sticky = "NESW")

themeButton = tk.Button(settingsFrame, text = "Theme", width = 10, command = lambda : openWindow(settingsWindow,themeWindow))  # Button to open themeWindow.
themeButton.grid(row = 1, column = 2, columnspan = 2, sticky = "NESW")

settingsFrame.grid()

# Contents of helpWindow. Todo: scrollable help guide.
helpFrame = tk.Frame(helpWindow)  # Frame for all the widgits in helpWindow.

returnButtonHelp = tk.Button(helpFrame, text = "Back", width = 5, command = lambda : openWindow(helpWindow,mainWindow))  # Reopens mainWindow and leaves helpWindow.
returnButtonHelp.grid()

helpFrame.grid()

# Contents of goalWindow.
goalFrame = tk.Frame(goalWindow)  # Frame with all the
goalFrame.rowconfigure(0, weight = 1)
goalFrame.rowconfigure(1, weight = 1)
goalFrame.rowconfigure(2, weight = 1)
goalFrame.columnconfigure(0, weight = 1)
goalFrame.columnconfigure(1, weight = 1)
goalFrame.columnconfigure(2, weight = 1)

returnButtonGoal = tk.Button(goalFrame, text = "Back", width = 5, command = lambda : openWindow(goalWindow,settingsWindow))  # Returns the user to settingsWindow
returnButtonGoal.grid(row = 0, column = 0, sticky = "NESW")

goalEntry = tk.Entry(goalFrame)  # Entry for the user to input a new goal.
goalEntry.grid(row = 2, column = 1, sticky = "NESW")

goalEntryLabel = tk.Label(goalFrame, text = "Enter your writing goal as a integer. Omit commas.")  # Label with user instructions.
goalEntryLabel.grid(row = 1, column = 0, columnspan = 3, sticky = "NESW")

currentGoalLabel = tk.Label(goalFrame, text = "Your current goal is " + str(goalWords) + " words.")  # Label to inform the user what their current goal is.
currentGoalLabel.grid(row = 0, column = 1, sticky = "NESW")

# Similar to the submit from the playWindow, reads the entry and updates the goal words.
def goalEntrySubmitEvent():
	global goalEntry, goalWords, currentGoalLabel
	if goalEntry.get().isnumeric():  # Input validation.
		goalWords = int(goalEntry.get())
		currentGoalLabel["text"] = "Your current goal is " + str(goalWords) + " words."
	
goalEntrySubmit = tk.Button(goalFrame, text = "Update", width = 5, command = goalEntrySubmitEvent)  # Button that runs goEntrySubmitEvent.
goalEntrySubmit.grid(row = 2, column = 0, sticky = "NESW")

goalFrame.grid()

# Contents of themeWindow
themeFrame = tk.Frame(themeWindow)  # Frame for themeWindow.

returnButtonTheme = tk.Button(themeFrame, text = "Back", width = 5, command = lambda : openWindow(themeWindow,settingsWindow))  # The generic back button found in every other window.
returnButtonTheme.grid()

themeFrame.grid()

# Contents of victoryWindow. Todo: geometry.
victoryFrame =tk.Frame(victoryWindow)  # Frame for the widgets in victoryWindow.

homeButtonVictory = tk.Button(victoryFrame, text = "Home", width = 5, command = lambda : openWindow(victoryWindow,mainWindow))  # Button to take the user back to mainWindow.
homeButtonVictory.grid()

playAgainButton = tk.Button(victoryFrame, text = "Play Again", width = 5, command = lambda : openWindow(victoryWindow,mainWindow))  # Button to take the user back to a restarted playWindow.
homeButtonVictory.grid()

saveButton = tk.Button(victoryFrame, text = "Save", width = 5, command = lambda : save(toSave))  # Button that allows the user to save their work to a pre-existing doc.
homeButtonVictory.grid()

victoryFrame.grid()

# mainloop()
mainWindow.mainloop()