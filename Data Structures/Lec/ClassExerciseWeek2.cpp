#include <iostream>

using namespace std;

class Person{
// Attributes
protected:
    string name;
    int age;

public:
    // Constructor
    Person(string myname, int myage){
        name = myname;
        age = myage;
    }
    ~Person(void){
        cout << "Object has been deleted." << endl;
    }

    // Class Functions
    void setName(string newname){
        name = newname;
    }
    void setAge(int newage){
        age = newage;
    }

    string getName(){
        return name;
    }
    int getAge(){
        return age;
    }

};

class Employee : public Person{
// Attributes
private:
    string id;
    float salary;
    int hours;
protected:
    string occupation;

public:
    // Constructor
    Employee(string myname, int myage, string myid="None", float mysalary=0.0, int myhours=0, string myoccupation="Jobless") : Person(myname, myage){
        id = myid;
        salary = mysalary;
        hours = myhours;
        occupation = myoccupation;
    }
    ~Employee(void){
        cout << "Object has been deleted." << endl;
    }

    // Class Functions
    void setID(string newid){
        id = newid;
    }
    void setSalary(float newsalary){
        salary = newsalary;
    }
    void setHours(int newhours){
        hours = newhours;
    }
    void setOccupation(string newoccupation){
        occupation = newoccupation;
    }

    string getID(){
        return id;
    }
    float getSalary(){
        return salary;
    }
    int getHours(){
        return hours;
    }
    string getOccupation(){
        return occupation;
    }

    void addHour(){
        hours++;
    }

    float getPay(){
        float pay;
        pay = salary * hours;
        cout << "Your pay is $" << pay << endl;
        return pay;
    }
    
};

int main(){
    Employee alfin("Alfin", 19);
    alfin.setOccupation("Student");
    alfin.setSalary(5.60);
    alfin.addHour();        // Hours: 1
    alfin.addHour();        // Hours: 2
    alfin.addHour();        // Hours: 3
    alfin.addHour();        // Hours: 4
    alfin.getPay();         // expected result: "Your pay is $22.40" | 5.60 * 4 = 22.40
}