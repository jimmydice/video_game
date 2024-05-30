import tkinter as tk
from PIL import Image, ImageTk
import random
import os

# Define the questions
questions = [
    "Which game do you personally like the most?",
    "Which game would you rate the most if you were working in IGN?",
    "With which game are you emotionally attached the most?",
    "Which game do you think is best in its genre?"
]

# Define a dictionary with game names as keys and image file paths as values
game_covers = {
    "God of War: 2018": "covers/god_of_war.jpg",
    "The Witcher 3: Wild Hunt": "covers/witcher_3.jpg",
    "Fallout 3": "covers/fallout_3.jpg",
    "Baldur's Gate 3": "covers/baldurs_gate_3.jpg",
    "Diablo 2": "covers/diablo_2.jpg",
    "Diablo 4": "covers/diablo_4.jpg",
    "It Takes Two": "covers/it_takes_two.jpg",
    "Command and Conquer: Red Alert 2": "covers/red_alert_2.jpg",
    "Halo 2": "covers/halo_2.jpg",
    "Gears of War": "covers/gears_of_war.jpg",
    "Splinter Cell": "covers/splinter_cell.jpg",
    "Quake 3 Arena": "covers/quake_3_arena.jpg",
    "Elder Scrolls: Oblivion": "covers/oblivion.jpg",
    "Elder Scrolls: Morrowind": "covers/morrowind.jpg",
    "Elden Ring": "covers/elden_ring.jpg",
    "Grand Theft Auto 4": "covers/gta_4.jpg",
    "Warcraft 3": "covers/warcraft_3.jpg",
    "Sims 2": "covers/sims_2.jpg",
    "Max Payne 1+2": "covers/max_payne.jpg",
    "Doom 3": "covers/doom_3.jpg",
    "Last of Us": "covers/last_of_us.jpg",
    "Uncharted 4": "covers/uncharted_4.jpg",
    "Grand Theft Auto: San Andreas": "covers/gta_san_andreas.jpg"
}

class GameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Selector")
        
        self.selected_question = random.choice(questions)
        self.favorite_games = list(game_covers.keys())
        self.selected_games = random.sample(self.favorite_games, 12)
        self.game_votes = {game: 0 for game in self.selected_games}

        self.question_label = tk.Label(root, text=self.selected_question, font=("Helvetica", 14))
        self.question_label.pack(pady=20)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=20)

        self.left_button = tk.Button(self.button_frame, width=300, height=300, command=self.choose_left)
        self.left_button.grid(row=0, column=0, padx=10)

        self.right_button = tk.Button(self.button_frame, width=300, height=300, command=self.choose_right)
        self.right_button.grid(row=0, column=1, padx=10)

        self.update_buttons()

    def load_image(self, path):
        image = Image.open(path)
        image = image.resize((300, 300), Image.ANTIALIAS)
        return ImageTk.PhotoImage(image)

    def choose_left(self):
        self.handle_choice('A')

    def choose_right(self):
        self.handle_choice('B')

    def handle_choice(self, choice):
        game_a, game_b = self.current_pair
        if choice == 'A':
            self.selected_games.remove(game_b)
            self.game_votes[game_a] += 1
        elif choice == 'B':
            self.selected_games.remove(game_a)
            self.game_votes[game_b] += 1
        self.update_buttons()

    def update_buttons(self):
        if len(self.selected_games) > 1:
            self.current_pair = random.sample(self.selected_games, 2)
            self.left_image = self.load_image(game_covers[self.current_pair[0]])
            self.right_image = self.load_image(game_covers[self.current_pair[1]])
            self.left_button.config(image=self.left_image)
            self.right_button.config(image=self.right_image)
        else:
            self.display_results()

    def display_results(self):
        self.game_votes[self.selected_games[0]] += 1
        sorted_games = sorted(self.game_votes.items(), key=lambda x: x[1], reverse=True)
        top_3_games = sorted_games[:3]

        result_text = "The top 3 games are:\n"
        for i, (game, votes) in enumerate(top_3_games, start=1):
            result_text += f"{i}. {game} with {votes} votes\n"

        self.question_label.config(text=result_text)
        self.left_button.pack_forget()
        self.right_button.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()
