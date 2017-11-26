#include <iostream>

using namespace std;

int numbers[200000];

int main(){
  int n,k;
  cin >> n >> k;

  bool first = true;
  int minimum = 2;
  int count = 0;
  bool finished = false;

  while(!finished){
    bool set_new_minimum = false;
    int new_minimum = -1;

    int i = minimum-2;
    while(i < n-1){
      if(first)
        numbers[i] = i+2;
      if(numbers[i] < 0){
        i += numbers[i]*-1;
        continue;
      }

      if(numbers[i]%minimum == 0){
        count++;
        if(count == k){
          cout << numbers[i];
          finished = true;
          break;
        }
        if(i < n-2 && numbers[i+1] < 0)
          numbers[i] = numbers[i+1]-1;
        else
          numbers[i] = -1;
      }
      else{
        if(!set_new_minimum){
          set_new_minimum = true;
          new_minimum = numbers[i];
        }
      }

          i++;
    }

      minimum = new_minimum;
      first = false;
  }

  return 0;
}
