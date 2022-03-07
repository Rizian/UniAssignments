#include <iostream>
#include <array>

template <typename T>
void swap(T &a, T &b)
{
    T temp;

    temp = a;
    a = b;
    b = temp;
}

void printArray(std::array<int, 5> arr){
    for (int i : arr){
        std::cout << i << std:: endl;
    };
}

int main()
{

    // int x = 5;
    // int y = 10;

    // swap<int>(x, y);

    // std::cout << x << std::endl
    //           << y << std::endl;

    std::array<int, 5> myArr = {1,2,3,4,5};

    printArray(myArr);
}