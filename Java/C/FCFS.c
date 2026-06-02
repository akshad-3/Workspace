#include<stdio.h>

int main(){
    int bt[50],wt[50],n,i;

    printf("Enter the no. of processes :");
    scanf("%d",&n);
    printf("\n");
    for(i=0;i<n;i++){
        printf("enter the burst time for process %d:",i+1);
        scanf("%d",&bt[i]);
    }
    wt[0]=0;

    for(i=1;i<=n;i++){
        wt[i] = wt[i-1]+ bt[i-1];
    }
    printf("process\t\twt\t\ttat\n\n");

    for(i=0;i<n;i++){
        printf("p%d\t\t%d\t\t%d\n",i+1,wt[i],wt[i+1]);
    }


    return 0;
}