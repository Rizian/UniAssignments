#include <iostream>
#include "AssignmentNode.hpp"
#include "ASsignmentLL.hpp"

int main()
{
    dsa::LinkedList<int> list1;

    list1.addNode(13);
    list1.addNode(5);
    list1.addNode(42);
    list1.addNode(37);
    list1.addNode(1);
    list1.addNode(39);
    list1.addNode(21);
    list1.addNode(78);
    list1.addNode(50);
    list1.addNode(53);
    list1.addNode(105);
    list1.addNode(7);
    list1.addNode(3);
    list1.addNode(85);
    list1.addNode(115);
    list1.addNode(64);

    list1.printList();
    std::cout << std::endl;     // empty lines for better
                                // console command line
                                // readibility

    // Testing non-parameterized add function (don't type '100')
    list1.addNode();
    list1.addNode();
    list1.addNode();
    std::cout << std::endl;

    std::cout << "Unsorted List:" << std::endl;
    list1.printList();          // prints unsorted list
    std::cout << std::endl;

    list1.sort();               // initiates a selection sort
                                // algorithm to sort the list

    std::cout << "Sorted List:" << std::endl;
    list1.printList();          // prints sorted list
    std::cout << std::endl;

    list1.binarySearch(100);    // should return false
    std::cout << std::endl;
    list1.binarySearch(64);     // should return true
    std::cout << std::endl;

    // Testing worse-cases
    list1.binarySearch(1);      // should return true
    std::cout << std::endl;
    list1.binarySearch(115);    // should return true
    std::cout << std::endl;
}