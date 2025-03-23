# Common Sequences/Strings Algorithm
Usage: `python3 LCS.py [string1] [string2]`\\
Note that you should provide exactly 0 or 2 strings. If you provide none, "abcdef" and "axxxexx" will be used as for an example.\\
Returns a bunch of different things, explained hereunder.

## The Base Case : LCS 
The Longest Common Subsequence is the base case for other algortithms.\\

We implement it using a bottom-up DP approach, creating a DP table. \\
If only the length of the common subsequence is required, we can space-optimize the algorithm to only keep 2 rows of the DP table. If we need to recover the sequence, or if we using this table for another algorithm, then we need to keep the whole table.

## LCS Retrieval
If we want to retrieve the longest common subsequence, we start at the end of the table and work our way back to the beginning. We always backtrack via the highest rank in the table, until finding a match, where we then append this match to our result. We finally return the reversed string that we created. 

## SCS : The Shortest Common Supersequence
While this problem at first glance looks a lot more difficult, once we know the LCS it is actually quite straightforward. We create the same DP table as for the LCS, but then when backtracking we just add the characters that we encounter instead of skipping them. 

