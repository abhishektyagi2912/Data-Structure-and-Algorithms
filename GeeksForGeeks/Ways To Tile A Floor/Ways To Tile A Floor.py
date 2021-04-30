

def numberOfWays(N):
        # N == 1 
        if(N == 1):
            return 1
        # N ==2
        if(N == 2):
            return 2
        return numberOfWays(N - 1) + numberOfWays(N - 2);
