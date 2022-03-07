#include <iostream>

using namespace std;

int main()
{
    cout << "What day is today?" << endl;

    string day;
    cin >> day;

    if (day == "weekday")
    {
        cout << "Studying" << endl;
    }
    else if (day == "weekend")
    {
        cout << "Fishing" << endl;
    }

    return 0;
}