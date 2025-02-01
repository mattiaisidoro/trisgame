import random
import tkinter as tk
from tkinter import messagebox
import pygame

# Inizializzazione di pygame per la musica
pygame.mixer.init()

def play_background_music():
    pygame.mixer.music.load(r"C:\Users\Mattia\OneDrive\Desktop\MATTIA\Progetti\TRIS GAME\trisgame\background_Music.mp3")  # Sostituisci con il percorso del tuo file audio
    pygame.mixer.music.play(-1)  # Riproduci in loop

def stop_background_music():
    pygame.mixer.music.stop()

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def available_moves(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

def ai_move(board, difficulty):
    if difficulty == "easy":
        return random.choice(available_moves(board))
    elif difficulty == "medium":
        for move in available_moves(board):
            r, c = move
            board[r][c] = "O"
            if check_winner(board, "O"):
                return move
            board[r][c] = " "
        return random.choice(available_moves(board))
    else:
        return minimax(board, "O")[1]

def minimax(board, player):
    opponent = "X" if player == "O" else "O"
    if check_winner(board, "O"):
        return (1, None)
    if check_winner(board, "X"):
        return (-1, None)
    if not available_moves(board):
        return (0, None)
    
    best_score = -float("inf") if player == "O" else float("inf")
    best_move = None
    
    for move in available_moves(board):
        r, c = move
        board[r][c] = player
        score = minimax(board, opponent)[0]
        board[r][c] = " "
        
        if player == "O":
            if score > best_score:
                best_score = score
                best_move = move
        else:
            if score < best_score:
                best_score = score
                best_move = move
    
    return best_score, best_move

def reset_game():
    global board, buttons
    board = [[" " for _ in range(3)] for _ in range(3)]  # Resetta la board
    for r in range(3):
        for c in range(3):
            buttons[r][c].config(text=" ", state=tk.NORMAL, bg="white")  # Resetta i pulsanti

def on_click(row, col):
    global board, buttons, difficulty
    if board[row][col] == " ":
        board[row][col] = "X"
        buttons[row][col].config(text="X", state=tk.DISABLED, bg="lightblue")
        
        if check_winner(board, "X"):
            messagebox.showinfo("Game Over", "You win!")
            reset_game()  # Resetta il gioco invece di chiudere
        elif not available_moves(board):
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_game()  # Resetta il gioco invece di chiudere
        else:
            ai_r, ai_c = ai_move(board, difficulty)
            board[ai_r][ai_c] = "O"
            buttons[ai_r][ai_c].config(text="O", state=tk.DISABLED, bg="lightcoral")
            
            if check_winner(board, "O"):
                messagebox.showinfo("Game Over", "AI wins!")
                reset_game()  # Resetta il gioco invece di chiudere
            elif not available_moves(board):
                messagebox.showinfo("Game Over", "It's a tie!")
                reset_game()  # Resetta il gioco invece di chiudere

def set_difficulty(level):
    global difficulty, board
    difficulty = level
    board = [[" " for _ in range(3)] for _ in range(3)]  # Inizializza la board
    difficulty_frame.destroy()
    create_board()

def create_board():
    global buttons, board
    buttons = [[None for _ in range(3)] for _ in range(3)]
    for r in range(3):
        for c in range(3):
            buttons[r][c] = tk.Button(root, text=" ", font=('Arial', 24), width=5, height=2, bg="white",
                                      command=lambda row=r, col=c: on_click(row, col))
            buttons[r][c].grid(row=r, column=c, padx=5, pady=5)

def play_game():
    global root, difficulty_frame, board
    root = tk.Tk()
    root.title("Tic-Tac-Toe")
    root.configure(bg="gray")
    
    # Avvia la musica di sottofondo
    play_background_music()
    
    difficulty_frame = tk.Frame(root, bg="gray")
    difficulty_frame.pack(pady=20)
    
    tk.Label(difficulty_frame, text="Choose AI Difficulty:", font=("Arial", 14), bg="gray", fg="white").pack()
    tk.Button(difficulty_frame, text="Easy", font=("Arial", 12), command=lambda: set_difficulty("easy"), bg="lightgreen").pack(pady=5)
    tk.Button(difficulty_frame, text="Medium", font=("Arial", 12), command=lambda: set_difficulty("medium"), bg="yellow").pack(pady=5)
    tk.Button(difficulty_frame, text="Hard", font=("Arial", 12), command=lambda: set_difficulty("hard"), bg="red").pack(pady=5)
    
    root.mainloop()

if __name__ == "__main__":
    play_game()