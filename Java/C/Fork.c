#include <stdio.h>
#include<unistd.h>

int main(){
    fork();
    printf("\nthis is the pid : %d",getpid());    
    return 0;
}