#include <stdio.h>

char board[3][3];
char currentPlayer;

void initializeBoard() {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            board[i][j] = ' ';
        }
    }
}

void printBoard() {
    printf(" %c | %c | %c \n", board[0][0], board[0][1], board[0][2]);
    printf("---|---|---\n");
    printf(" %c | %c | %c \n", board[1][0], board[1][1], board[1][2]);
    printf("---|---|---\n");
    printf(" %c | %c | %c \n", board[2][0], board[2][1], board[2][2]);
}

int checkWin() {
    // Controlla le righe
    for (int i = 0; i < 3; i++) {
        if (board[i][0] == currentPlayer && board[i][1] == currentPlayer && board[i][2] == currentPlayer) {
            return 1;
        }
    }
    // Controlla le colonne
    for (int i = 0; i < 3; i++) {
        if (board[0][i] == currentPlayer && board[1][i] == currentPlayer && board[2][i] == currentPlayer) {
            return 1;
        }
    }
    // Controlla le diagonali
    if (board[0][0] == currentPlayer && board[1][1] == currentPlayer && board[2][2] == currentPlayer) {
        return 1;
    }
    if (board[0][2] == currentPlayer && board[1][1] == currentPlayer && board[2][0] == currentPlayer) {
        return 1;
    }
    return 0;
}

int checkTie() {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (board[i][j] == ' ') {
                return 0;
            }
        }
    }
    return 1;
}

void switchPlayer() {
    if (currentPlayer == 'X') {
        currentPlayer = 'O';
    } else {
        currentPlayer = 'X';
    }
}

int main() {
    int row, col;
    initializeBoard();
    currentPlayer = 'X';
    
    while (1) {
        printBoard();
        printf("Giocatore %c, inserisci la riga e la colonna: ", currentPlayer);
        scanf("%d %d", &row, &col);
        
        if (row < 0 || row > 2 || col < 0 || col > 2 || board[row][col] != ' ') {
            printf("Mossa non valida. Riprova.\n");
            continue;
        }
        
        board[row][col] = currentPlayer;
        
        if (checkWin()) {
            printBoard();
            printf("Giocatore %c ha vinto!\n", currentPlayer);
            break;
        }
        
        if (checkTie()) {
            printBoard();
            printf("Pareggio!\n");
            break;
        }
        
        switchPlayer();
    }
    
    return 0;
}
