#include<stdio.h>

int main(){

    int blocks[10],process[10],b,p,i,j;

    printf("Enter the no of blocks");
    scanf("%d",&b);
    printf("Enter the no of processes");
    scanf("%d",&p);

    for(i=0;i<b;i++){
        printf("Value for bloack %d : ",i+1);
        scanf("%d",&blocks[i]);
    }
    for(i=0;i<p;i++){
        printf("Value for processes %d : ",i+1);
        scanf("%d",&process[i]);
    }

    for(i=0;i<p;i++){
        for(j=0;j<b;j++){
            if(blocks[j]>=process[i]){
                printf("Process %d -> Block %d\n", i+1, j+1);
                blocks[j] -= process[i];
                break;
            }
        }
    }


    return 0;
}