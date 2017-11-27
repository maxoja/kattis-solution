#include <iostream>
#include <string>

using namespace std;

class Solver
{
  private:
    string s;
    string l;

  public:
    bool GetInput()
    {
      cin >> s;
      if(s == "0") return false;
      cin >> l;
      return true;
    }

    void SolveAndPrint()
    {
      int type_one_occurrences = SolveTypeOne();
      int type_two_occurrences = SolveTypeTwo();
      int type_three_occurrences = SolveTypeThree();

      cout
      << type_one_occurrences << " "
      << type_two_occurrences << " "
      << type_three_occurrences << endl;

      return;
    }

  private:
    bool CharacterMatched(int sidx, int lidx) { return s[sidx] == l[lidx]; }
    bool CharacterNotMatched(int sidx, int lidx) { return !CharacterMatched(sidx, lidx); }
    bool EndOfS(int sidx) { return sidx == s.length()-1; }
    bool OverLengthOfL(int lidx) { return lidx >= l.length(); }

    int SolveTypeOne()
    {
      int occurrence_count = 0;

      for(int lidx = 0 ; lidx < l.length()-s.length()+1 ; ++lidx)
      {
        int matched_count = 0;

        for(int sidx = 0 ; sidx < s.length() ; ++sidx)
        {
          int actual_sidx = sidx;
          int actual_lidx = lidx + sidx;

          if(CharacterMatched(actual_sidx, actual_lidx))
            ++matched_count;
          else
            break;
        }

        if(matched_count == s.length())
          ++occurrence_count;
      }

      return occurrence_count;
    }

    int SolveTypeTwo()
    {
      int occurrence_count = 0;

      for(int lidx = 0 ; lidx < l.length()-s.length()+1+1 ; ++lidx)
      {
        int matched_count = 0;
        int shift = 0;

        for(int sidx = 0 ; sidx < s.length()-1 ; ++sidx)
        {
          int actual_sidx = sidx + shift;
          int actual_lidx = lidx + sidx;

          if(CharacterMatched(actual_sidx, actual_lidx))
            ++matched_count;
          else
          {
            ++shift;
            if(shift > 1) break;
            --sidx;
          }
        }

        if(matched_count == s.length()-1)
          ++occurrence_count;
      }

      return occurrence_count;
    }

    int SolveTypeThree()
    {
      int occurrence_count = 0;

      for(int lidx = 0 ; lidx < l.length()-s.length()-1+1 ; ++lidx)
      {
        int matched_count = 0;
        int shift = 0;

        for(int sidx = 0 ; sidx < s.length() ; ++sidx)
        {
          int actual_sidx = sidx;
          int actual_lidx = lidx + sidx + shift;

          if(CharacterMatched(actual_sidx, actual_lidx))
            ++matched_count;
          else
          {
            ++shift;
            if(shift > 1) break;
            --sidx;
          }
        }

        if(matched_count == s.length())
          ++occurrence_count;
      }

      return occurrence_count;
    }
};

int main()
{
  while(true)
  {
    Solver solver = Solver();

    bool end_of_input = !solver.GetInput();

    if(end_of_input)
      break;

    solver.SolveAndPrint();
  }

  return 0;
}
