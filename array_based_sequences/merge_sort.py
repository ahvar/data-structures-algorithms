"""
merging two previously sorted sequences, S1 and S2, with the output
copied into S. The divide-and-conquer merge-sort algorithm is given in Code Fragment 12.2. 
During the process, index i represents the number of elements of S1 that have been
copied to S, while index j represents the number of elements of S2 that have been copied to S.
Assuming S1 and S2 both have at least one uncopied element, we copy the smaller of the two elements
being considered. Since i + j objects have been previously copied,  the next element is placed in S[i+ j].
(For example, when i+ j is 0, the next element is copied to S[0]).

If we reach the end of one of the sequences, we must copy  the next element from the other. 
"""

class Solution:
    def merge(s1, s2):
        s = [0 for _ in range(len(s1) + len(s2))]
        i = 0
        j = 0
        # add current indexes to get current position in final array
        while i + j < len(s):
            # get to end of s2 or the val at s1[i] < the val at s2[j]
            if j == len(s2) or (i < len(s1) and s1[i] < s2[j]):
                s[i + j] = s1[i] # insert the s1 val or put it at the end
                i += 1
            else: 
                s[i + j] = s2[j] # insert the s2 val
                j += 1




if __name__ == "__main__":
    s1 = [3,4,6,7,11,14]
    s2 = [1,2,3,4,10]
    solution = Solution()
    solution.merge(s1, s2)

    