public class Solution {
    public int FindChampion(int n, int[][] edges) {
        var strongests = new HashSet<int>(Enumerable.Range(0, n));
        
        foreach (var edge in edges) {
            strongests.Remove(edge[1]);
        }

        return strongests.Count == 1 ? strongests.ElementAt(0) : -1;
    }
}