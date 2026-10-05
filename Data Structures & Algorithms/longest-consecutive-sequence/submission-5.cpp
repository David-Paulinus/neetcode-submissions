class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()){
            return 0;
        }

        unordered_set<int> nums_set{ nums.begin(), nums.end() };
        int longest = 1;

        for( const auto num : nums ) {
            // check if num is start of sequence
            if (nums_set.contains(num-1)) {
                continue;
            }

            int next_num = num + 1;
            int curr_longest = 1; 
            while (nums_set.contains(next_num)) {
                curr_longest++;
                next_num++;
            }
            longest = max(longest, curr_longest);
        }
        
        return longest;
    }
};
