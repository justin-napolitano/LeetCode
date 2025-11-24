---
slug: github-leetcode
title: Python Solutions for Classic Algorithmic Problems in LeetCode
repo: justin-napolitano/LeetCode
githubUrl: https://github.com/justin-napolitano/LeetCode
generatedAt: '2025-11-23T09:13:00.328094Z'
source: github-auto
summary: >-
  Collection of Python implementations solving common algorithmic problems like Two Sum, linked
  lists, sliding windows, and sorting with explanations.
tags:
  - leetcode
  - python
  - data-structures
seoPrimaryKeyword: leetcode python solutions
seoSecondaryKeywords:
  - algorithmic problems
  - coding interview problems
  - classic algorithms
seoOptimized: true
---

# Technical Overview of the LeetCode Solutions Repository

This repository consolidates Python implementations of several foundational algorithmic problems. The motivation is to provide a reference collection of solutions that are both practical and illustrative of common problem-solving techniques used in software engineering and technical interviews.

## Motivation

Algorithmic proficiency remains a core skill for developers, particularly when preparing for interviews or tackling performance-critical code. This repository aggregates solutions to problems that exemplify key algorithmic paradigms such as hashing, linked list manipulation, sliding windows, binary search, merging, and divide-and-conquer sorting.

## Problems and Implementations

### Two Sum

The `q1_two_sum.py` file implements a hash map based approach to find two indices whose elements sum to a target value. The solution runs in linear time by storing seen elements and their indices in a dictionary.

### Add Two Numbers (Singly Linked List)

In `q2_add_two_numbers_singly_linked_list.py`, the problem is solved by iterating through two linked lists simultaneously, summing corresponding nodes with carry management. The use of a dummy head node simplifies list construction.

### Longest Substring Without Repeating Characters

The `q3_longest_substring.py` employs a sliding window technique using a list to track current substring characters. When a duplicate is found, the window is adjusted by slicing off the prefix up to the repeated character. This approach maintains a linear time complexity.

### Median of Two Sorted Arrays

Two approaches are implemented:

- `q4_binary_search_median.py` applies a binary search on the smaller array to partition both arrays correctly, achieving logarithmic time complexity. The method carefully handles edge cases and returns the median based on combined array length parity.

- `q4_merge_median.py` merges the two arrays into one sorted array and then calculates the median. This is a straightforward but less efficient approach with linear time complexity.

### Merge Intervals

The `q_56_list_intersection.py` sorts intervals by their start times and merges overlapping intervals by comparing the end of the last merged interval with the current one. This solution is efficient and commonly used in interval-related problems.

### Quick Sort

`quickSort.py` implements the classic quicksort algorithm with in-place partitioning. The pivot is chosen as the last element, and recursive calls sort the subarrays. The code modifies the input list directly.

## Design Considerations

- Solutions prioritize clarity and correctness over micro-optimizations.
- Use of Python typing hints where appropriate improves code readability.
- Dummy nodes and helper methods are used to simplify linked list operations.
- Comments provide insight into the logic and edge case handling.

## Practical Notes

- Some scripts include example usage or test code in a `main` function.
- The repository assumes familiarity with Python and basic data structures.
- No external dependencies are required.

## Conclusion

This collection serves as a practical toolkit for revisiting classic algorithmic problems. It balances straightforward implementations with some more advanced techniques, such as binary search partitioning for median finding. The repository is suitable for reference, learning, and incremental extension.

