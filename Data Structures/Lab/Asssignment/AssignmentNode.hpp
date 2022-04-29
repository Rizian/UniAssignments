#pragma once

#include <iostream>

namespace dsa
{
    template <typename T>
    class Node
    {
    public:
        // Attributes
        T data;
        Node<T> *next;
        Node<T> *prev;

    public:
        // Constructors
        Node()
        {
            this->data = 0;
            this->next = NULL;
            this->prev = NULL;
        }
        Node(T data)
        {
            this->data = data;
            this->next = NULL;
            this->prev = NULL;
        }

        // Methods
        T getData();
        void setData(T data);
        Node<T> *navNext();
        T getNext();
        void setNext(Node<T> *next);
        void unlinkNext();
        Node<T> *navPrev();
        T getPrev();
        void setPrev(Node<T> *prev);
        void unlinkPrev();
    };

    template <typename T>
    T Node<T>::getData()
    {
        return this->data;
    }

    template <typename T>
    void Node<T>::setData(T data)
    {
        this->data = data;
    }

    template <typename T>
    Node<T> *Node<T>::navNext()
    {
        return this->next;
    }

    template <typename T>
    T Node<T>::getNext()
    {
        return this->next->data;
    }

    template <typename T>
    void Node<T>::setNext(Node<T> *next)
    {
        this->next = next;
    }

    template <typename T>
    void Node<T>::unlinkNext()
    {
        this->next = NULL;
    }

    template <typename T>
    Node<T> *Node<T>::navPrev()
    {
        return this->prev;
    }
    template <typename T>
    T Node<T>::getPrev()
    {
        return this->prev->data;
    }

    template <typename T>
    void Node<T>::setPrev(Node<T> *prev)
    {
        this->prev = prev;
    }

    template <typename T>
    void Node<T>::unlinkPrev()
    {
        this->prev = NULL;
    }
}