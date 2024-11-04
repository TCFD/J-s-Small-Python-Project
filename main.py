import tkinter as tk
from tkinter import messagebox
import time
import random


#Création du fichier CSV si il n'existe pas.
file1 = open("data.csv", "a+")
file1.seek(0)
old_words = set(line.split(";")[0] for line in file1)  # Prend juste le mot, pas la définition

#Stockages du dico dans une liste
with open("NEPASOUVRIR-listedemots.txt", "r") as file:
    dico = set(file.read().splitlines())

new_words = {}

root = tk.Tk()
# Création du Frame
frame = tk.Frame(root, bg = "#f0f0f0", width = 1000, height = 750)	
frame.grid(row = 0, column = 0, padx = 0, pady = 0)
# Création des zones de texte
text = []


def nv_ligne():
	text1_elmt = tk.Entry(frame, font=("arial", 20))
	text2_elmt = tk.Entry(frame, font=("arial", 20))
	lenght = len(text)
	text1_elmt.grid(row = 1 + lenght, column = 0, padx = 5, pady = 5)
	text2_elmt.grid(row = 1 + lenght, column = 1, padx = 5, pady = 5)
	text.append([text1_elmt, text2_elmt])

def build_string(lst, error):
	return_str = "Les mots :\n"
	for item in lst:
		return_str += "\t" + item + "\n"
	return_str += error
	return return_str


def ajouter():
	alreadyExistingWords = []
	nonValidWords = []
	for line in text:
		# Vérifier la présence d'un mot
		if line[0].get() not in dico:
			nonValidWords.append(line[0].get())

		elif line[0].get() in old_words or line[0].get() in new_words:
			alreadyExistingWords.append(line[0].get())

		else:
			new_words[line[0].get()] = line[1].get()

	if (len(alreadyExistingWords)):
		string = build_string(alreadyExistingWords, "Sont déjà présents dans la liste.") 
		messagebox.showerror("Mots déjà présents", string)
	elif (len(nonValidWords)):
		string = build_string(nonValidWords, "N'existent pas dans le dictionnaire") 
		messagebox.showerror("Mots déjà présents", string)
	else:
		found_words = len(new_words) + len(old_words)
		messagebox.showinfo("Bravo !", "Les mots on bien étés ajoutés à la liste.\n Vous avez trouvé " + str(found_words) + " mots sur 69163, soit " + format(found_words / 69163 * 100, '.3f') + "% des mots")

# Création des boutons avec la couleur de base
def early_window():
	add_button = tk.Button(frame, text = "Ajouter", bg = "#B0C4DE", command = ajouter, font=("Arial", 24))
	new_line_button = tk.Button(frame, text = "Nouvelle ligne", command = nv_ligne, bg = "#B0C4DE", font=("Arial", 24))
	add_button.grid(row = 0, column = 0, padx = 10, pady = 10)
	new_line_button.grid(row = 0, column = 1, padx = 10, pady = 10)
	nv_ligne()

def on_closing():
	if messagebox.askokcancel("Quit", "Vous voulez quitter?"):
		root.destroy()
		for cle,value in new_words.items():
			file1.write(cle + ';' + value + '\n')

root.protocol("WM_DELETE_WINDOW", on_closing)

early_window()
root.mainloop()	   