#include <iostream>
#include <array>

using namespace std;

int main()
{
    array<int, 9> arr = {3, 49, 1, 6, 33, 13, 9, 4, 6};

    cout << "What data are you searching for?" << endl;

    int myData;
    cin >> myData;

    
    for (int i = 0; arr.size(); i++)
    {
        if (arr[i] == myData)
        {
            cout << "Found in index " << to_string(i) << endl;
            break;
        }
        if (i == arr.size()-1)
        {
            cout << "Not found" << endl;
        }
    }

    return 0;
}