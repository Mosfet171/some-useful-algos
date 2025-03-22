import time
from functools import cache


class Fibonnaci():
	def pure_recursion(self, n):
		if n == 1 or n == 0:
			return 1
		else: 
			return self.pure_recursion(n-1) + self.pure_recursion(n-2)

	@cache
	def cache_recursion(self, n):
		if n == 1 or n == 0:
			return 1
		else: 
			return self.cache_recursion(n-1) + self.cache_recursion(n-2)


	def memo_recursion(self, n):
		def helper(x, memo):
			if x == 0 or x == 1:
				return 1
			if x not in memo:
				memo[x] = helper(x-1,memo) + helper(x-2,memo)
			return memo[x]

		memo = {}
		return helper(n,memo)

	def bottom_up(self,n):
		dp = [0]*(n+1)

		dp[0], dp[1] = 1, 1

		for i in range(2,n+1):
			dp[i] = dp[i-1] + dp[i-2]

		return dp[n]


	def space_optimization(self,n):
		dp = [1,1,0]

		for i in range(2,n+1):
			dp[2] = dp[0] + dp[1]
			dp[0], dp[1] = dp[1], dp[2]
		return dp[2]



if __name__ == "__main__": 

	n = 20
	n_iter = 500

	fib = Fibonnaci()

	# 1. Pure Recursion 
	start = time.perf_counter()
	for _ in range(n_iter):
		fibn = fib.pure_recursion(n)
	end = time.perf_counter()
	pure_elapsed = end-start
	print(f'Pure Recursion: ({fibn})\t\t Time per iteration = {1000/n_iter*pure_elapsed:.6f} ms.')

	# 2. Recursion with built-in cache decorator
	start = time.perf_counter()
	for _ in range(n_iter):
		fibn = fib.cache_recursion(n)
	end = time.perf_counter()
	cache_elapsed = end-start
	improvement = (pure_elapsed/cache_elapsed)
	print(f'Cache Recursion: ({fibn})\t Time per iteration = {1000/n_iter*cache_elapsed:.6f} ms.\t {improvement:.0f}x faster than pure recursion.')

	# 3. Recursion with memoization
	start = time.perf_counter()
	for _ in range(n_iter):
		fibn = fib.memo_recursion(n)
	end = time.perf_counter()
	memo_elapsed = end-start
	improvement = (pure_elapsed/memo_elapsed)
	print(f'Memo Recursion: ({fibn})\t\t Time per iteration = {1000/n_iter*memo_elapsed:.6f} ms.\t {improvement:.0f}x faster than pure recursion.')

	# 4. Bottom-Up DP (tabulation)
	start = time.perf_counter()
	for _ in range(n_iter):
		fibn = fib.bottom_up(n)
	end = time.perf_counter()
	bu_elapsed = end-start
	improvement = (pure_elapsed/bu_elapsed)
	print(f'Bottom-Up DP: ({fibn})\t\t Time per iteration = {1000/n_iter*bu_elapsed:.6f} ms.\t {improvement:.0f}x faster than pure recursion.')

	# 5. Space Optimized Bottom-Up DP 
	start = time.perf_counter()
	for _ in range(n_iter):
		fibn = fib.space_optimization(n)
	end = time.perf_counter()
	so_elapsed = end-start
	improvement = (pure_elapsed/bu_elapsed)
	print(f'Space Optimized: ({fibn})\t Time per iteration = {1000/n_iter*so_elapsed:.6f} ms.\t {improvement:.0f}x faster than pure recursion.')




