#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX 100

int main()
{
    char word[MAX], guess[MAX], letter;
    int i, j, len, count = 0, wrong = 0, flag = 0;
    char words[][MAX] = {"computer", "science", "programming", "hangman", "game", "random", "words", "dictionary", "array", "string", "function", "variable", "integer", "float", "double", "character", "pointer", "structure", "union", "typedef", "enum", "break", "continue", "return", "if", "else", "switch", "case", "for", "while", "do", "goto", "sizeof", "auto", "register", "static", "extern", "const", "volatile", "signed", "unsigned", "short", "long", "main", "include", "define", "ifdef", "ifndef", "endif", "undef", "error", "line", "pragma", "printf", "scanf", "puts", "gets", "puts", "fgets", "fputs", "fgetc", "fputc", "fread", "fwrite", "fscanf", "fprintf", "fseek", "ftell", "rewind", "feof", "ferror", "clearerr", "exit", "abort", "atexit", "system", "malloc", "calloc", "realloc", "free", "exit", "atof", "atoi", "atol", "strtod", "strtol", "strtoul", "rand", "srand", "abs", "div", "labs", "ldiv", "exit", "atexit", "system", "malloc", "calloc", "realloc", "free", "exit", "atof", "atoi", "atol", "strtod", "strtol", "strtoul", "rand", "srand", "abs", "div", "labs", "ldiv", "exit", "atexit", "system", "malloc", "calloc", "realloc", "free", "exit", "atof", "atoi", "atol", "strtod", "strtol", "strtoul", "rand", "srand", "abs", "div", "labs", "ldiv", "exit", "atexit", "system", "malloc", "calloc", "realloc"};
    srand(time(NULL));
    i = rand() % 100;
    strcpy(word, words[i]);
    len = strlen(word);
    for (i = 0; i < len; i++)
        guess[i] = '_';
    guess[i] = '\0';
    printf(" HANGMAN GAME \n");

    while (wrong < 6 && strcmp(word, guess) != 0)
    {
        printf(" %s ", guess);
        printf(" Enter a letter: ");
        scanf(" %c", &letter);
        flag = 0;
        for (i = 0; i < len; i++)
        {
            if (letter == word[i])
            {
                guess[i] = letter;
                flag = 1;
            }
        }
        if (flag == 0)
        {
            wrong++;
            printf(" Wrong guess. You have %d more guesses. \n", 6 - wrong);
        }
    }
    if (wrong == 6)
        printf(" You lose. The word was %s ", word);
    else
        printf(" You win. The word was %s ", word);
    return 0;
}

