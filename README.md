### Task Description
You are given a list of non-negative integers `nums`, where each element represents your maximum jump length at that position. Starting at the first index, determine whether you can reach the last index.

### Input Format
A list of non-negative integers.

### Output Format
A boolean value:
- `True` if it's possible to reach the last index
- `False` otherwise

### Example 1
**Input:** `[2, 3, 1, 1, 4]`  
**Output:** `True`  
**Explanation:** Jump from index 0 to 1, then from 1 to 4.

### Example 2
**Input:** `[3, 2, 1, 0, 4]`  
**Output:** `False`  
**Explanation:** You get stuck at index 3 and cannot reach index 4.

### How to Run
Clone the repository:
```bash
git clone https://github.com/YuryHaurylenka/test_task_algo.git
cd test_task_algo
```
Create and activate a virutal environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```
Run the solution:
```bash
python solution.py
```
Run the unit tests:
```bash
python -m unittest test_solution.py
```