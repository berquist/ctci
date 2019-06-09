#include <functional>

#include <gtest/gtest.h>

/**
 * Book solution from page 131.
 */
unsigned fib1(unsigned n) {
    if (n == 0)
        return 0;
    if (n == 1)
        return 1;
    return fib1(n - 1) + fib1(n - 2);
}

typedef std::map<unsigned, unsigned> cache_type;

unsigned fib2_helper(unsigned n, cache_type &cache) {
    if (cache.count(n) > 0)
        return cache.at(n);
    cache.insert({n, fib2_helper(n - 1, cache) + fib2_helper(n - 2, cache)});
    return cache.at(n);
}

/**
 * Own solution using memoization.
 */
unsigned fib2_nolambda(unsigned n) {
    cache_type cache;
    cache.insert({0, 0});
    cache.insert({1, 1});

    return fib2_helper(n, cache);
}

unsigned fib2(unsigned n) {
    cache_type cache;
    cache.insert({0, 0});
    cache.insert({1, 1});

    // auto helper = [&](unsigned n, cache_type &c)
    std::function<unsigned(unsigned, cache_type&)> helper = [&](unsigned n, cache_type &c)
                      {
                          if (c.count(n) > 0)
                              return c.at(n);
                          c.insert({n, helper(n - 1, c) + helper(n - 2, c)});
                          return c.at(n);
                      };

    return helper(n, cache);
}

unsigned fib3(unsigned n) {
    cache_type cache;
    cache.insert({0, 0});
    cache.insert({1, 1});

    std::function<unsigned(unsigned, cache_type&)> helper = [&](unsigned n, cache_type &c)
                      {
                          if (c.count(n) == 0)
                              c.insert({n, helper(n - 1, c) + helper(n - 2, c)});
                          return c.at(n);
                      };

    return helper(n, cache);
}

unsigned fib5(unsigned n) {
    cache_type cache;
    cache.insert({0, 0});
    cache.insert({1, 1});
    for (unsigned i = 2; i < n + 1; i++)
        cache.insert({i, cache.at(i - 1) + cache.at(i - 2)});
    return cache.at(n);
}

unsigned fib6(unsigned n) {
    if (n < 2)
        return n;
    unsigned a = 0;
    unsigned b = 1;
    unsigned c;
    for (unsigned i = 2; i < n + 1; i++) {
        c = a + b;
        a = b;
        b = c;
    }
    return c;
}

const unsigned F20 = 6765;

TEST(test_fib, fib1) {
    EXPECT_EQ(fib1(20), F20);
}
TEST(test_fib, fib2_nolambda) {
    EXPECT_EQ(fib2_nolambda(0), 0);
    EXPECT_EQ(fib2_nolambda(1), 1);
    EXPECT_EQ(fib2_nolambda(20), F20);

}
TEST(test_fib, fib2) {
    EXPECT_EQ(fib2(0), 0);
    EXPECT_EQ(fib2(1), 1);
    EXPECT_EQ(fib2(20), F20);
}
TEST(test_fib, fib3) {
    EXPECT_EQ(fib3(0), 0);
    EXPECT_EQ(fib3(1), 1);
    EXPECT_EQ(fib3(20), F20);
}
TEST(test_fib, fib5) {
    EXPECT_EQ(fib5(0), 0);
    EXPECT_EQ(fib5(1), 1);
    EXPECT_EQ(fib5(20), F20);
}
TEST(test_fib, fib6) {
    EXPECT_EQ(fib6(0), 0);
    EXPECT_EQ(fib6(1), 1);
    EXPECT_EQ(fib6(20), F20);
}
