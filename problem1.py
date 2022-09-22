'''
39. Combination Sum

Concept = Backtracking

APPROACH 1: simple recursion with backtracking
TIME COMPLEXITY: 2 ** (M * N) M = target, N = len(candidates)
SPACE COMPLEXITY: 2 ** (M * N) M = target, N = len(candidates)
LEETCODE: Yes
DIFFICULTIES: Nope. Solved after watching the class

APPROACH 2: iteration in recursion with backtracking ( this is the optimized one )
TIME COMPLEXITY: 2 ** (M * N) M = target, N = len(candidates)
SPACE COMPLEXITY: 2 ** (M * N) M = target, N = len(candidates)
LEETCODE: NO
DIFFICULTIES: ---
Approach 2 is not a priority now.

'''

class Solution:
    def combinationSum(self, ccandidates: List[int], target: int) -> List[List[int]]:
        
        # recursion type 1
        def approach1(ccandidates, target):
            global candidates, res
            candidates = ccandidates
            res = []
            
            def rec(idx, target, temp_res):
                global candidates, res
                
                # base
                if target < 0:
                    return
                if target == 0:
                    temp = temp_res.copy()
                    res.append(temp) 
                    return 
                if idx == len(candidates):
                    return
                
                # logic
                # not choose
                rec(idx+1, target, temp_res)
                
                # choose
                temp = temp_res.copy()
                temp.append(candidates[idx]) # back tracking - step type 1
                rec(idx, target-candidates[idx], temp)
                
                
            
            rec(0, target, [])
            
            return res
        
        # recursion type 2
        def approach2(ccandidates, target):
            global candidates, res
            candidates = ccandidates
            res = []
            
            def rec(target, temp_res):
                global candidates, res
                # base case is handled in logic
                
                # logic
                # always choose
                for i in range(0, len(candidates)):
                    if target-candidates[i] < 0:
                        pass
                        # temp_res.pop()                        
                    if target-candidates[i] == 0:
                        temp_res.append(candidates[i])
                        res.append(temp_res.copy())
                        temp_res.pop()           # back tracking step - type 2             
                    else:
                        temp_res.append(candidates[i]) # use stack to optimize
                        # target -= candidates[i]
                        rec(target - candidates[i], temp_res)
                        temp_res.pop()           # back tracking step - type 2             
                    
            rec(target, [])
            
            return res
        
        return approach1(ccandidates, target)
        # return approach2(ccandidates, target)
        
