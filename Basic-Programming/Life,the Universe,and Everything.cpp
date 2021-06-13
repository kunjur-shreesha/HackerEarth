#include <iostream>

using namespace std;

int main()
{
    int n;
    for (int i=0;i<10000;i++)
    {
        cin>>n;
        if(n==42)
            break;
        else
            cout<<n;
        cout<<"\n";
    }


    return 0;
}
