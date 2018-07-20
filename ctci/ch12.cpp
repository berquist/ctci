#include <cassert>
#include <fstream>
#include <iostream>

/* Write a method to print the last K lines of an input file using
 * C++.
 */
void ch12_1(size_t k) {
    int ret;
    const std::string filename = "CMakeCache.txt";
    std::ifstream file(filename.c_str(), std::ifstream::in);
    size_t counter = 0;
    char buf[BUFSIZ];
    // Count the number of lines in the file.
    while (file.good()) {
        file.getline(buf, BUFSIZ);
        counter++;
    }
    // std::cout << counter << std::endl;
    file.clear();
    file.seekg(0);
    assert(k < counter);
    const size_t diff = counter - k;
    for (size_t i = 0; i < diff; i++) {
        file.getline(buf, BUFSIZ);
    }
    while (file.good()) {
        file.getline(buf, BUFSIZ);
        std::cout << buf << std::endl;
    }
    file.close();
}

int main() {
    const size_t k = 20;
    ch12_1(k);
    return 0;
}
