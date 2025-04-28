#include <iostream>
#include <string>

using namespace std;

int main() {

    int x = 0;  // A variável é uma instância do tipo
    int y = 5;
    int z;

    int *p = &y;
    int *q = new int;  // q = int()  q = 5
    p = p + 1;

    // Python
    // x = 0   // A variável é referência para uma instância do tipo

    cout << x << " " << &x << endl;
    cout << y << " " << &y << endl;
    cout << z << " " << &z << endl;
    cout << p << " " << &p << endl;
    cout << q << " " << &q << endl;

}