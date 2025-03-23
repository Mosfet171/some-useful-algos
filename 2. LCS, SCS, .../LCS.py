import time

class LCS():
	def __init__(self):
		self.dp = [[-1]]

	def createDPtable(self, str1, str2):
		m = len(str1)
		n = len(str2)

		self.dp = [[0]*(n+1) for _ in range(m+1)]

		for i in range(1,m+1):
			for j in range(1,n+1):
				if str1[i-1] == str2[j-1]:
					self.dp[i][j] = self.dp[i-1][j-1] + 1
				else:
					self.dp[i][j] = max(self.dp[i-1][j],self.dp[i][j-1])


	def createDPtable_so(self, str1, str2):
		m = len(str1)
		n = len(str2)

		if n > m:
			str1, str2 = str2, str1
			m, n = n, m

		self.dp = [[0]*(n+1) for _ in range(2)]

		for i in range(1,m+1):
			for j in range(1,n+1):
				if str1[i-1] == str2[j-1]:
					self.dp[1][j] = self.dp[0][j-1] + 1
				else:
					self.dp[1][j] = max(self.dp[0][j],self.dp[1][j-1])
			self.dp[0] = self.dp[1][:]


	def retrieveLength(self):
		return self.dp[-1][-1]


	def longestCommonSubsequence(self, str1, str2):
		m = len(str1)
		n = len(str2)

		self.createDPtable(str1,str2)

		i,j = m,n 
		res = []

		while i > 0 and j > 0:
			if str1[i-1] == str2[j-1]:
				res.append(str1[i-1])
				i -= 1
				j -= 1
			elif self.dp[i-1][j] > self.dp[i][j-1]:
				i -= 1
			else: 
				j -= 1

		return "".join(reversed(res))

	def shortestCommonSupersequence(self, str1, str2):
		m = len(str1)
		n = len(str2)

		self.createDPtable(str1, str2)

		i,j = m,n 
		res = []

		while i > 0 or j > 0:
			if i > 0 and j > 0 and str1[i-1] == str2[j-1]:
				res.append(str1[i-1])
				i -= 1
				j -= 1
			elif (i > 0 and self.dp[i-1][j] > self.dp[i][j-1]) or j == 0:
				res.append(str1[i-1])
				i -= 1
			else:
				res.append(str2[j-1])
				j -= 1

		return "".join(reversed(res))



if __name__ == "__main__":
	string1 = "abcdef"
	string2 = "axxxexx"

	print(f'Working with \"{string1}\" and \"{string2}\"\n')

	example = LCS()

	# 1. Full Table
	start = time.perf_counter()
	example.createDPtable(string1,string2)
	l1 = example.retrieveLength()
	end = time.perf_counter()
	print(f'Full DP Table\t Result={l1}\t Time={(end-start)*1000:.3f}ms')

	# 2. Space Opti
	start = time.perf_counter()
	example.createDPtable_so(string1,string2)
	l2 = example.retrieveLength()
	end = time.perf_counter()
	print(f'Opti DP Table\t Result={l2}\t Time={(end-start)*1000:.3f}ms')

	# 3. Reconstruct The LCS
	start = time.perf_counter()
	res = example.longestCommonSubsequence(string1,string2)
	end = time.perf_counter()
	print(f'\nReconstruction\t Result={res}\t Time={(end-start)*1000:.3f}ms')

	# 4. SCS
	start = time.perf_counter()
	res = example.shortestCommonSupersequence(string1,string2)
	end = time.perf_counter()
	print(f'\nSCS\t Result={res}\t Time={(end-start)*1000:.3f}ms')
