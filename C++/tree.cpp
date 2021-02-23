#include <bits/stdc++.h>
using namespace std;

struct Node {
    int data;
    struct Node* left;
    struct Node* right;

    Node(int val)
    {
        data = val;
        left = NULL;
        right = NULL;
    }
};

int main(){
    /*
             0
           /  \
          1    2
         / \  / \
        3  4  5  6
    */
    struct Node* root = new Node(0);
    root->left = new Node(1);
    root->right = new Node(2);
    root->left->left = new Node(3);
    root->left->right = new Node(4);
    root->right->left = new Node(5);
    root->right->right = new Node(6);

    return 0;
}