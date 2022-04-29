#pragma once

#include <iostream>
#include "AssignmentNode.hpp"

namespace dsa
{
    template <typename T>
    class LinkedList
    {
    public:
        // Attributes
        Node<T> *head;
        Node<T> *tail;
        int size;

    public:
        // Constructor
        LinkedList()
        {
            head = NULL;
            tail = NULL;
            size = 0;
        }

        // Methods
        T getHead();
        T getTail();
        int getSize();
        bool isEmpty();
        void addNode();
        void addNode(T data);
        void printList();
        void sort();
        bool binarySearch(T value);
    };

    template <typename T>
    T LinkedList<T>::getHead()
    {
        return this->head->data;
    }

    template <typename T>
    T LinkedList<T>::getTail()
    {
        return this->tail->data;
    }

    template <typename T>
    int LinkedList<T>::getSize()
    {
        return this->size;
    }
    template <typename T>
    bool LinkedList<T>::isEmpty()
    {
        return (this->size == 0);
    }

    template <typename T>
    void LinkedList<T>::addNode()
    {
        Node<T> *newNode = new Node<T>;
        T data;

        std::cout << "Insert data: ";
        std::cin >> data;
        newNode->setData(data);

        if (size == 0)
        {
            head = newNode;
            tail = NULL;
            size++;
        }
        else if (size == 1)
        {
            head->setNext(newNode);
            tail = newNode;
            tail->setPrev(head);
            size++;
        }
        else
        {
            newNode->setPrev(tail);
            tail->setNext(newNode);
            tail = newNode;
            size++;
        }
    }

    template <typename T>
    void LinkedList<T>::addNode(T data)
    {
        Node<T> *newNode = new Node<T>;

        newNode->setData(data);

        if (size == 0)
        {
            head = newNode;
            tail = NULL;
            size++;
        }
        else if (size == 1)
        {
            head->setNext(newNode);
            tail = newNode;
            tail->setPrev(head);
            size++;
        }
        else
        {
            newNode->setPrev(tail);
            tail->setNext(newNode);
            tail = newNode;
            size++;
        }
    }

    template <typename T>
    void LinkedList<T>::printList()
    {
        Node<T> *current = head;

        for (int i = 0; i < size; i++)
        {
            if (current != tail)
            {
                std::cout << current->data << ", ";
                current = current->navNext();
            }
            else
            {
                std::cout << current->data;
            }
        }
        std::cout << std::endl;
        std::cout << "Size of List: " << size << std::endl;
    }

    template <typename T>
    void LinkedList<T>::sort()
    {
        Node<T> *start;
        Node<T> *current;
        Node<T> *min;

        for (int i = 0; i < size; i++)
        {
            start = head;
            for (int j = 0; j < i; j++)
            {
                start = start->navNext();
            }
            current = start;
            min = current;
            for (int k = i + 1; k < size; k++)
            {
                if (current != tail)
                {
                    current = current->navNext();
                    if (current->data < min->data)
                    {
                        min = current;
                    }
                }
            }

            if (min == start)
            {
                continue;
            }
            else if (min != tail)
            {
                min->navPrev()->setNext(min->navNext());
                min->navNext()->setPrev(min->navPrev());
            }
            else
            {
                tail = min->navPrev();
                tail->unlinkNext();
            }

            if (i == 0)
            {
                min->unlinkPrev();
                head = min;
                min->setNext(start);
                start->setPrev(min);
            }
            else
            {
                min->setPrev(start->navPrev());
                start->navPrev()->setNext(min);
                min->setNext(start);
                start->setPrev(min);
            }
        }
    }

    template <typename T>
    bool LinkedList<T>::binarySearch(T value)
    {
        Node<T> *left = head;
        Node<T> *right = tail;
        Node<T> *mid;

        while (left != NULL && right != NULL && left->data <= right->data)
        {
            int i = 0;
            for (Node<T> *temp = left; temp != right; temp = temp->navNext())
            {
                i++;
            }

            i /= 2;

            mid = left;

            for (int j = 0; j < i; j++)
            {
                mid = mid->navNext();
            }

            if (mid->data < value)
            {
                left = mid->navNext();
            }
            else if (mid->data > value)
            {
                right = mid->navPrev();
            }
            else
            {
                int k = 0;
                for (Node<T> *temp = head; temp != mid; temp = temp->navNext())
                {
                    k++;
                }
                std::cout << "Element (" << value << ") found in Node " << k << std::endl;
                return true;
            }
        }
        std::cout << "Element (" << value << ") not in list" << std::endl;
        return false;
    }
}