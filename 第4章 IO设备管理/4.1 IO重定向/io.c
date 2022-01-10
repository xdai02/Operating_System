#include <stdio.h>

int main(int argc, char *argv[]) {
    int num;
    printf("(stdin) enter an integer: ");
    fscanf(stdin, "%d", &num);
    fprintf(stdout, "(stdout) num = %d\n", num);
    fprintf(stderr, "(stderr) This is an error message.\n");
    return 0;
}