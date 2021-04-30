
def countP(n, k):
	
	if (n == 0 or k == 0 or k > n):
		return 0
	if (k == 1 or k == n):
		return 1
	
	return (k * countP(n - 1, k) + countP(n - 1, k - 1))

if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    k = int(input("Enter the value of k: "))
    print(countP(n,k))

