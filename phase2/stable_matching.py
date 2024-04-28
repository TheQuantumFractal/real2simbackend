import edge_lib

def get_matchings():
    names = [user["name"] for user in edge_lib.get_users()]
    name_mapping = {name: i for i, name in enumerate(names)}
    couples = edge_lib.get_couples()
    matrix = [[0 for _ in range(len(names))] for _ in range(len(names))]
    for couple in couples:
        i, j = name_mapping[couple["person1"]], name_mapping[couple["person2"]]
        matrix[i][j] = couple["score1"]
        matrix[j][i] = couple["score2"]
    
    preferences = []
    for i in range(len(matrix)):
        sorted_prefs = sorted([(matrix[i][j], j) for j in range(len(matrix[i]))])
        preferences.append([j for _, j in sorted_prefs])
    matchings = stable_matching(preferences)

    edge_lib.insert_compatible([(names[i], names[j]) for i, j in enumerate(matchings)])

    return [(names[i], names[j]) for i, j in enumerate(matchings)]

def wPrefersM1OverM(prefer, w, m, m1):
    N = len(prefer)
    for i in range(N):
         
        if (prefer[w][i] == m1):
            return True
        if (prefer[w][i] == m):
            return False

def stable_matching(prefer):
    N = len(prefer)
    wPartner = [-1 for i in range(N)]
    mFree = [False for i in range(N)]
 
    freeCount = N
 
    while (freeCount > 0):
        m = 0
        while (m < N):
            if (mFree[m] == False):
                break
            m += 1
        i = 0
        while i < N and mFree[m] == False:
            w = prefer[m][i]
 
            if (wPartner[w - N] == -1):
                wPartner[w - N] = m
                mFree[m] = True
                freeCount -= 1
 
            else:
                m1 = wPartner[w - N]
                
                if (wPrefersM1OverM(prefer, w, m, m1) == False):
                    wPartner[w - N] = m
                    mFree[m] = True
                    mFree[m1] = False
            i += 1
    return wPartner