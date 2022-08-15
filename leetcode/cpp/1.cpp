#ifdef NDEBUG
#undef NDEBUG
#endif

#include <cassert>
#include <unordered_map>
#include <unordered_set>
#include <vector>

typedef int val_t;
typedef std::vector<val_t> candidates_t;
typedef std::pair<std::size_t, std::size_t> indices;

indices two_sum_naive(const candidates_t &candidates, const val_t target) {
    for (std::size_t j = 0; j < candidates.size(); j++) {
        for (std::size_t i = 0; i < j; i++) {
            if (candidates[i] + candidates[j] == target) {
                return {i, j};
            }
        }
    }
    return {-1, -1};
}

// indices two_sum_set(const candidates_t &candidates, const val_t target) {

//     for (size_t i = 0; i < candidates.size(); i++) {
        
//     }
//     return {0, 0};
// }

// indices two_sum_map_1(const candidates_t &candidates, const val_t target) {
//     std::unordered_map<val_t, std::size_t> map()
//     return {-1, -1};
// }

indices two_sum_map_2(const candidates_t &candidates, const val_t target) {
    std::unordered_map<val_t, std::size_t> map;
    for (std::size_t i = 0; i < candidates.size(); i++) {
        const auto comp = target - candidates[i];
        if (map.count(comp)) {
            return {map.at(comp), i};
        }
        map.emplace(std::make_pair(candidates[i], i));
    }
    return {-1, -1};
}

int main() {
    const std::vector<int> inp_1 {2, 7, 11, 15};
    const int tgt_1 = 9;
    const indices ref_1 {0, 1};
    assert(two_sum_naive(inp_1, tgt_1) == ref_1);
    assert(two_sum_map_2(inp_1, tgt_1) == ref_1);

    const std::vector<int> inp_2 {3, 2, 4};
    const int tgt_2 = 6;
    const indices ref_2 {1, 2};
    assert(two_sum_naive(inp_2, tgt_2) == ref_2);
    assert(two_sum_map_2(inp_2, tgt_2) == ref_2);

    return 0;
}
