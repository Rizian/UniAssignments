/*
Create a Program that displays "True" or "False" if an element is in an array or not!

    You can make the array yourself

    has to be size of 7 or greater

    make the user input an element and check if its in an array
*/

#include <iostream>
#include <array>

using namespace std;

array<int, 7> arr = {11, 24, 63, 43, 52, 68, 70};

int main()
{
    cout << "Enter a number" << endl;

    int input;
    cin >> input;

    for (int i = 0; arr.size(); i++)
    {
        if (arr[i] == input)
        {
            cout << "True" << endl;
            break;
        }
        if (i == arr.size() - 1)
        {
            cout << "False" << endl;
        }
    }

    return 0;
}