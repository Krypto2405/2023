#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main()
{
cout << "Maximum: " << RAND_MAX << endl;
srand((unsigned int)time(nullptr));
cout << rand() % 6 + 1 << endl;
}
