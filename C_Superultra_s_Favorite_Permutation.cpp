#include <bits/stdc++.h>
using namespace std;
 
 
 
int main()
{
    long a, b, c, n, q, r, s, i, j, k, t;
    cin>>t;
    for(j=0;j<t;j++)
    {
        cin>>n;
        if(n<5)
        {
            cout<<-1<<endl;
        }
        else
        {
            q=1;
            while(q<n+1)
            {
                if(q!=5)
                {
                    cout<<q<<" ";
                }
                q=q+2;
            }
            cout<<5<<" "<<4<<" ";
            
            q=2;
            while(q<n+1)
            {
                if(q!=4)
                {
                    cout<<q;
                    if(q==n or q==n-1)
                    {
                        cout<<endl;
                    }
                    else
                    {
                        cout<<" ";
                    }
                }
                q=q+2;
            }
        }
    }
    
    
    return 0;
}

convert this code correctly in python without changing the output.