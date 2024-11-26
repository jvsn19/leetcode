#include <vector>
#include <set>

class Solution {
public:
    int findChampion(int n, std::vector<std::vector<int>>& edges) {
        std::set<int> strongests = {};

        for(int node = 0; node < n; ++node) {
            strongests.insert(node);
        }

        for (const auto& edge: edges) {
            strongests.erase(edge[1]);
        }

        return strongests.size() == 1 ? *strongests.begin() : -1;
    }
};