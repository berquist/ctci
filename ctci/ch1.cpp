#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <string>

#include <gtest/gtest.h>

typedef std::map<char, int> frequencies;

frequencies make_frequencies(const std::string &s) {
    frequencies frequencies;
    for (auto &c : s) {
        if (frequencies.count(c) == 0)
            frequencies.insert(std::make_pair(c, 1));
        else
            frequencies.at(c) += 1;
    }
    return frequencies;
}

std::ostream& operator<<(std::ostream &os, const frequencies &f) {
    os << "{";
    for (auto it = f.cbegin(); it != f.cend(); ++it) {
        os << "{'" << (*it).first << "': " << (*it).second << "}, ";
    }
    os << "}";
    return os;
}

template <typename Map>
bool key_compare(Map const &lhs, Map const &rhs) {

    auto pred = [] (auto a, auto b)
                    { return a.first == b.first; };

    return lhs.size() == rhs.size()
        && std::equal(lhs.cbegin(), lhs.cend(), rhs.cbegin(), pred);
}

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

bool ch1_2_1(const std::string &s1, const std::string &s2) {
    if (s1.size() != s2.size())
        return false;
    std::string ss1 = s1;
    std::string ss2 = s2;
    std::sort(ss1.begin(), ss1.end());
    std::sort(ss2.begin(), ss2.end());
    if (ss1 != ss2)
        return false;
    return true;
}

// there is also a solution that uses a hash table to store
// frequencies
bool ch1_2_3(const std::string &s1, const std::string &s2) {
    const frequencies f1 = make_frequencies(s1);
    const frequencies f2 = make_frequencies(s2);
    // first check keys
    if (!key_compare(f1, f2))
        return false;
    // then check counts; assume keys are identical
    for (auto it = f1.cbegin(); it != f1.cend(); ++it)
        if ((*it).second != f2.at((*it).first))
            return false;
    return true;
}

bool ch1_2_4(const std::string &s1, const std::string &s2) {
    const frequencies f1 = make_frequencies(s1);
    const frequencies f2 = make_frequencies(s2);
    return f1 == f2;
}

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
//     const frequencies f1 = make_frequencies(s1);
//     const frequencies f2 = make_frequencies(s2);
//     std::cout << f1 << std::endl;
//     std::cout << f2 << std::endl;
//     return 0;
// }

TEST(test_ch1_1, ch1_1) {
    const std::string s1 = "abcddaasdfh";
    const std::string s2 = "abcdefgh";
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

TEST(test_frequencies, frequencies) {
    std::string s1 = "";
    frequencies r1 {};
    std::string s2 = "Tact Coa";
    frequencies r2 {{'T', 1}, {'a', 2}, {'c', 1}, {'t', 1}, {'C', 1}, {'o', 1}, {' ', 1}};
    std::string s3 = "tactcoapapa";
    frequencies r3 {{'t', 2}, {'a', 4}, {'c', 2}, {'o', 1}, {'p', 2}};
    frequencies o1 = make_frequencies(s1);
    frequencies o2 = make_frequencies(s2);
    frequencies o3 = make_frequencies(s3);

    EXPECT_TRUE(o1.empty());
    EXPECT_FALSE(o2.empty());
    EXPECT_FALSE(o3.empty());

    EXPECT_EQ(r1, o1);
    EXPECT_EQ(r2, o2);
    EXPECT_EQ(r3, o3);
}

TEST(test_ch1_2, ch1_2) {
    const std::string s1 = "abcddaasdfh";
    const std::string s2 = "abcdefgh";
    const std::string s2r(s2.rbegin(), s2.rend());
    const std::string s3 = "abcddassdfh";
    EXPECT_FALSE(ch1_2_1(s1, s2));
    EXPECT_TRUE(ch1_2_1(s1, s1));
    EXPECT_TRUE(ch1_2_1(s2, s2r));
    EXPECT_FALSE(ch1_2_1(s1, s3));
    // Not implemented.
    // EXPECT_FALSE(ch1_2_2(s1, s2));
    // EXPECT_TRUE(ch1_2_2(s1, s1));
    // EXPECT_TRUE(ch1_2_2(s2, s2r));
    // EXPECT_FALSE(ch1_2_2(s1, s3));
    EXPECT_FALSE(ch1_2_3(s1, s2));
    EXPECT_TRUE(ch1_2_3(s1, s1));
    EXPECT_TRUE(ch1_2_3(s2, s2r));
    EXPECT_FALSE(ch1_2_3(s1, s3));
    EXPECT_FALSE(ch1_2_4(s1, s2));
    EXPECT_TRUE(ch1_2_4(s1, s1));
    EXPECT_TRUE(ch1_2_4(s2, s2r));
    EXPECT_FALSE(ch1_2_4(s1, s3));
}
