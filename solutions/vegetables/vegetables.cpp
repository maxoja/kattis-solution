#include <iostream>
#include <vector>

using namespace std;

class VeggieCut
{
  private:
    int cut;
    int weight;

  public:
    VeggieCut(int w) { weight = w; cut = 0;}

    int GetCut() { return cut; }
    int GetAllWeight() { return weight; }
    double GetCutWeight() { return weight/(cut + 1); }
    void CutMore() { ++cut; }
};

class Solver
{
  private:
    vector<VeggieCut> veggies;
    double ratio;
    int n;

  public:
    Solver() { veggies = vector<VeggieCut>(); }

    void GetInput()
    {
      cin >> ratio >> n;

      for(int _ = 0 ; _ < n ; ++_)
      {
        int weight;
        cin >> weight;
        VeggieCut newVeggie = VeggieCut(weight);

        bool added = false;
        for(int i = 0 ; i < veggies.size() ; ++i)
        {
          if(veggies[i].GetAllWeight() < newVeggie.GetAllWeight())
          {
            veggies.insert(veggies.begin()+i, newVeggie);
            added = true;
            break;
          }
        }

        if(!added)
          veggies.push_back(newVeggie);
      }
    }

    int Solve()
    {
      int cut_count = 0;

      double biggest = veggies[0].GetCutWeight();
      double smallest = veggies[veggies.size()-1].GetCutWeight();

      while(smallest/biggest <= ratio)
      {
        veggies[0].CutMore();
        ++cut_count;

        for(int i = 0 ; i < veggies.size()-1 ; ++i)
        {
          if(veggies[i].GetCutWeight() < veggies[i+1].GetCutWeight())
          {
            VeggieCut temp = veggies[i];
            veggies[i] = veggies[i+1];
            veggies[i+1] = temp;
          }
          else
            break;
        }

        biggest = veggies[0].GetCutWeight();
        smallest = veggies[veggies.size()-1].GetCutWeight();
      }

      return cut_count;
    }
};

int main()
{
  Solver solver = Solver();
  solver.GetInput();
  cout << solver.Solve() << endl;
  return 0;
}
