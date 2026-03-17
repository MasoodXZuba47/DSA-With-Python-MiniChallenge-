# 🧠 DSA Challenges — Python

A growing collection of Data Structures & Algorithms problems solved in Python, ranging from Easy to Hard difficulty. Each challenge includes a clean, well-documented solution with time/space complexity analysis and test cases.

---

## 📁 Challenge List

| # | File | Problem | Difficulty | Topic |
|---|------|---------|------------|-------|
| 1 | `Chellenge1.py` | Two Sum | 🟢 Easy | Hash Map |
| 2 | `chellenge2.py` | Linked List Cycle | 🟡 Medium | Linked List / Floyd's Algorithm |
| 3 | `chellenge3.py` | Binary Search | 🟢 Easy | Binary Search |
| 4 | `chellenge4.py` | Valid Parentheses / Stack Problem | 🟡 Medium | Stack |
| 5 | `challenge5.py` | Longest Substring Without Repeating Characters | 🟡 Medium | Sliding Window |
| 6 | `challenge6.py` | 3Sum | 🟡 Medium | Two Pointers / Sorting |
| 7 | `challenge7.py` | **Trapping Rain Water** | 🔴 Hard | Two Pointers |

---

## 🔴 Challenge 7 — Trapping Rain Water (LeetCode Hard)

### Problem Statement

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can **trap after raining**.

```
Input:  height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

  █              
  █  █     █ █  
  █  █  █  █ █  
─ ─ ─ ─ ─ ─ ─ ─
  Water trapped = 6 units
```

### Approach — Two Pointer (Optimal)

The amount of water above any bar at index `i` is:

```
water[i] = min(max_left, max_right) - height[i]
```

Instead of pre-computing left/right max arrays (which would require O(n) extra space), we use **two converging pointers**:

1. Start `left = 0`, `right = n-1`, track `left_max` and `right_max`.
2. Always process the **smaller** side — that's the bottleneck.
3. Accumulate `max - height[pointer]` as trapped water.
4. Move the pointer inward and repeat.

### Complexity

| | Value |
|---|---|
| **Time** | O(n) — single pass |
| **Space** | O(1) — no extra arrays |

### Examples

```python
trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])  # → 6
trap([4, 2, 0, 3, 2, 5])                      # → 9
trap([3, 0, 2, 0, 4])                          # → 7
```

### Run

```bash
python challenge7.py
```

---

## 🚀 How to Run Any Challenge

```bash
# Clone the repo
git clone <your-repo-url>
cd "DSA USING PYTHON/Challenges"

# Run a specific challenge
python challenge7.py
```

## 🛠 Requirements

- Python 3.10+
- No external libraries needed

---

## 📌 Topics Covered

`Array` · `Hash Map` · `Two Pointers` · `Sliding Window` · `Stack` · `Binary Search` · `Linked List` · `Sorting`

---

*Solutions are written for clarity and learning — each file explains the intuition, approach, and complexity in its docstrings.*
