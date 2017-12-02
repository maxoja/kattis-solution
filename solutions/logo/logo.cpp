#include <iostream>
#include <math.h>
#include <string>

using namespace std;

int main()
{
    int num_test;
    cin >> num_test;

    while(num_test-- > 0)
    {
        int n;
        cin >> n;

        double pos_x = 0;
        double pos_y = 0;
        double degree = 0;

        while(n-- > 0)
        {
          string cmd;
          int value;
          cin >> cmd >> value;

          if( cmd == "fd" )
          {
            pos_x += cos(degree/180*M_PI)*value;
            pos_y += sin(degree/180*M_PI)*value;
          }
          else if ( cmd == "bk" )
          {
            pos_x -= cos(degree/180*M_PI)*value;
            pos_y -= sin(degree/180*M_PI)*value;
          }
          else if ( cmd == "lt" )
          {
            degree += value;
          }
          else if ( cmd == "rt" )
          {
            degree -= value;
          }
        }

        cout << (int)round(sqrt(pos_x*pos_x + pos_y*pos_y)) << endl;
    }

    return 0;
}
