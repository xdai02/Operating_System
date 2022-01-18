#include <stdio.h>
#include <sys/types.h>
#include <wait.h>
#include <unistd.h>

int main() {
    pid_t pid;

    pid = getpid();
    printf("Before fork(): pid is %d\n", pid);

    // fork a child process
    pid = fork();

    if(pid < 0) {               // error
        fprintf(stderr, "Fork failed.\n");
        return 1;
    } else if(pid == 0) {       // child process
        printf("Child process: pid is %d\n", getpid());
        execlp("/bin/ls", "ls", NULL);
    } else {                    // parent process
        printf("Parent process: pid is %d\n", getpid());
        wait(NULL);
        printf("Child completed.");
    }
    
    return 0;
}