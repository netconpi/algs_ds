#include <iostream>

int find_nod(int a, int b) {
    while (a != b) {
        if (a > b) {
            a -= 1;
        } else {
            b -= 1;
        }
    }

    return a;
}

int main() {
    int a;
    int b;

    std::cout << "Enter value for a: ";
    std::cin >> a;
    std::cout << std::endl;
    std::cout << "Enter value for b: ";
    std::cin >> b;

    std::cout << std::endl << find_nod(a, b) << std::endl;

    return 0;
}

