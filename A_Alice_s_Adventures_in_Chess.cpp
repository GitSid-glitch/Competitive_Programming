#include <bits/stdc++.h>
using namespace std;
 
int main()
{
    int s_es;  // Number of test cases
    cin >> s_es;
    
    while (s_es--) 
    {
        int d_ns_c_t;
        int _et_x;
        int _get_y;  // Directions count, target X and target Y
        cin >> d_ns_c_t >> _et_x >> _get_y;
        string d_ec_ns;  // Directions string
        cin >> d_ec_ns;
 
        int c_nt_x = 0, cu_nt_y = 0;  // Current X and Y coordinates
        bool cout_ed_t_ = false;  // Flag to indicate if the target is reached
 
        // Loop through a maximum of 100 iterations
        for (int ind_= 0; ind_ < 1000; ind_++) {
            if (c_nt_x == _et_x && cu_nt_y == _get_y) 
            {
                cout_ed_t_ = true;
                break;
            }
 
            char move = d_ec_ns[ind_ % d_ns_c_t];  // Use modulo to loop through directions
 
            if (move == 'N') {
                cu_nt_y++;
            } else if (move == 'E') {
                c_nt_x++;
            } else if (move == 'S') {
                cu_nt_y--;
            } else if (move == 'W') {
                c_nt_x--;
            }
        }
 
        if (cout_ed_t_) {
            cout << "YES" << "\n";
        } else {
            cout << "NO" << endl;
        }
    }
    return 0;
}