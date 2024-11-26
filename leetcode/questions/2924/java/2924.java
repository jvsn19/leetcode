import java.util.HashSet;
import java.util.Set;

class Solution {
    public int findChampion(int n, int[][] edges) {
        Set<Integer> strongests = new HashSet<>();

        for (int node = 0; node < n; ++node) {
            strongests.add(node);
        }

        for (int[] edge: edges) {
            strongests.remove(edge[1]);
        }

        return strongests.size() == 1 ? strongests.iterator().next() : -1;
    }
¦}