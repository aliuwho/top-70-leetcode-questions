# Reverse Linked List

## Question:

Given the head of a singly linked list, reverse the list, and return
the reversed list.

## How to Solve:

Watch this video: https://www.youtube.com/watch?v=O0By4Zq0OFc It's worth a thousand words.

p.s. Start from 3:18

The main idea is to use three pointers (prev, curr, next) to
collaborately traverse the list only once yet being able to reverse
the list starting from changing the head to the tail. At each step,
`prev`, `curr`, and `next` are roughly in such left-to-right pointer
positions.