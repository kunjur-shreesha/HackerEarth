#include <stdio.h>

int main()
{
    int L,N,W,H;
    scanf("%d",&L);
    scanf("%d",&N);
    for (int i=0;i<N;i++)
    {
        scanf("%d %d",&W,&H);
        if ((W <L)||(H<L))
           printf("UPLOAD ANOTHER\n");
        else if (((W==L)&&(H==L)) || (W==H))
            printf("ACCEPTED\n");
        else
            printf("CROP IT\n");

    }
    return 0;
}
