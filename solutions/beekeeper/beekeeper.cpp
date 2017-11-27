#include <iostream>
#include <string>

using namespace std;

bool isVowel(string vowels, char c){
  for(int i = 0 ; i < vowels.length() ; i++){
    if(c == vowels[i])
    return true;
  }

  return false;
}
int main()
{
  string vowels = "aeiouy";

  while(true){
    int n;
    cin >> n;

    if(n == 0)
      break;

    string bestWord;
    int bestPair = -1;

    for(int _ = 0 ; _ < n ; _++){
      string word;
      cin >> word;
      int count = 0;

      for(int i = 0 ; i < word.length()-1 ; i++){
        if(word[i] == word[i+1] && isVowel(vowels, word[i]))
          count += 1;
      }

      if(count > bestPair){
        bestWord = word;
        bestPair = count;
      }
    }

    cout << bestWord << endl;
  }
  return 0;
}
