#include <stdio.h>
#include <stdlib.h>

unsigned long long prod(int n,int arr[])
{
    unsigned long long x=1;
   const unsigned int M =1000000007;
   for (int i=0;i<n;i++)
   {
       x=(x*arr[i])%M;
   }
   return x;
}
int main()
{

    int n,i,a[1000];
    unsigned long long product;
    scanf("%d",&n);
    for (i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    product=prod(n,a);
    printf("%d",product);

    return 0;
}
