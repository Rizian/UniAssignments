#include <iostream>

using namespace std;

class Car
{
private:
    string name;
    string color;

public:
    // ACCESSORS AND MUTATORS
    string getName()
    {
        return name;
    }

    string getColor()
    {
        return color;
    }

    void setName(string newname)
    {
        name = newname;
    }

    void setColor(string newcolor)
    {
        color = newcolor;
    }

    // CLASS FUNCTIONS
    void drive()
    {
        cout << "Hey" << name << "Drive now!" << endl;
    }

    void drive(string mysecondname)
    {
        cout << "Hey" << mysecondname << "That's your name, drive now!" << endl;
    }

    // CONSTRUCTOR
    Car(string myname = "N/A", string mycolor = "White")
    {
        name = myname;
        color = mycolor;
    }

    ~Car(void)
    {
        cout << "The car is being deleted" << endl;
    }
};

int main()
{
    Car myCar;
    myCar.drive();
    myCar.setName("coolname");
    string n;
    n = myCar.getName();
    cout << n << endl;
    return 0;
}