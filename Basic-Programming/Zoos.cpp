#include <iostream>

using namespace std;

int main()
{
   char str[100];
   int x=0,y=0;
   cin>>str;
   for (int i=0;str[i]!='\0';i++)
   {
       if(str[i]=='z')
            x++;
       else
            y++;
   }
   if(y==2*x)
        cout<<"Yes"<<endl;
   else
        cout<<"No"<<endl;


    return 0;
}
