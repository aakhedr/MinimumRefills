def minRefills(x, n, L):
	"""
	Implementations of greedy algorithm on calculating minimum number of car 
	fuel refills if traveling from point A to point B.
	O(n)
	
	Input: 	
	x: array of length (n + 2) where x[0] is point A and x[n + 1] is point B.
	n: (length of array x) - 2 (Points A and B) representing number of gas 
		stations available between points A and B.
	L: maximum distance the car can travel with full tank.
	
	Return:	Minimum number of refills.
	"""
	# How many times the car has been fueled full tank
	numRefills = 0
	
	# Position in the array x where the car is currently standing (From 0 to n)
	currentRefill = 0
	
	while currentRefill <= n:
		lastRefill = currentRefill

		while (currentRefill <= n) and ((x[currentRefill + 1] - x[lastRefill]) <= L):
			currentRefill = currentRefill + 1

		if currentRefill == lastRefill:
			return None
		
		if currentRefill <= n:
			numRefills += 1

	return numRefills

L = 400
n = 4
x = [0, 200, 375, 550, 750, 950]

print(minRefills(x, n, L))
