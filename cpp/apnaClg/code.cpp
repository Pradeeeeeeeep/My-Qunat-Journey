#include <iostream>
using namespace std;

int main() {
    int age = 78;
    cout << sizeof(age)<< endl;
    double price = 78.99;
    int newPrice = (int)price;
    cout << "Price: " << price << endl;
    cout << "Enter new price: ";
    cin >> newPrice;
    cout << "New Price: " << newPrice << endl;
    return 0;
}