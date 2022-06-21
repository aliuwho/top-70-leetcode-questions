## Problem

You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

## Solution

The key things to note when solving this problem are:
- adjacent houses cannot be broken into
- we don't care about producing a list of the houses we robbed; we just want **the total amount**

Based on these factors, we want to rob as many non-consecutive houses as possible (this means we should only skip a house if we have no other choice). This leads to the following greedy algorithm:

At house `i`, we either choose to rob or skip house `i`.

If we rob house `i`, then we cannot rob `i-1`, so the total money we make at this step is the total money we make from robbing house `i-2` plus the money we earn from house `i`.

If we skip house `i`, then we should instead rob house `i-1`. The total money we can make is the total at step `i-1`.