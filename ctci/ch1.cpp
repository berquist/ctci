#include <iostream>
#include <set>
#include <string>

#include <gtest/gtest.h>

// for (auto it = ss.begin(); it != ss.end(); it++) {
//     std::cout << *it << std::endl;
// }


bool ch1_1_1(const std::string &s) {
    std::set<char> ss(s.begin(), s.end());
    if (ss.size() < s.size())
        return false;
    return true;
}

bool ch1_1_2(const std::string &s) {
    std::set<char> ss;
    for (auto &c : s) {
        if (ss.count(c) > 0)
            return false;
        else
            ss.insert(c);
    }
    return true;
}

bool ch1_1_3(const std::string &s) {
    if (s.size() == 1)
        return true;
    std::string ss = s;
    std::sort(ss.begin(), ss.end());
    for (size_t i = 1; i < ss.size(); i++)
        if (ss.at(i) == ss.at(i - 1))
            return false;
    return true;
}

// bool ch1_1_4(const std::string &s) {
//     return true;
// }

// Since we are interested only in testing the correctness here,
// combine implementation and the tests. Having our own main conflicts
// with the one from googletest.

// int main() {
//     const std::string s = "I am a string";
//     const std::string s1 = "abcddaasdfh";
//     const std::string s2 = "abcdefgh";
//     std::cout << ch1_1_2(s) << std::endl;
//     std::cout << ch1_1_2(s1) << std::endl;
//     std::cout << ch1_1_2(s2) << std::endl;
//     return 0;
// }

TEST(test_ch1_1, ch1_1) {
    std::string s1 = "abcddaasdfh";
    std::string s2 = "abcdefgh";
    EXPECT_FALSE(ch1_1_1(s1));
    EXPECT_FALSE(ch1_1_2(s1));
    EXPECT_FALSE(ch1_1_3(s1));
    // Not implemented.
    // EXPECT_FALSE(ch1_1_4(s1));
    EXPECT_TRUE(ch1_1_1(s2));
    EXPECT_TRUE(ch1_1_2(s2));
    EXPECT_TRUE(ch1_1_3(s2));
    // Not implemented.
    // EXPECT_TRUE(ch1_1_4(s2));
}

// TEST(test_ch1_2, ch1_2) {
//     std::string s1 = "abcddaasdfh";
//     std::string s2 = "abcdefgh";
//     EXPECT_FALSE(ch1_2_1(s1, s2));
// }
