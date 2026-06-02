class DS:

    def __init__(self,n):
        self.parent = list(range(n+1))


    def find(self,x):

        if self.parent[x] != x:
            self.parent[x] = self.find(
                                self.parent[x]
                            )

        return self.parent[x]


jobs = [
('J1',2,100),
('J2',1,19),
('J3',2,27),
('J4',1,25),
('J5',3,15)
]

jobs.sort(
    key = lambda x:x[2],
    reverse = True
)

mx = max(job[1] for job in jobs)

ds = DS(mx)

profit = 0
ans = []


for job,deadline,p in jobs:

    slot = ds.find(deadline)

    if slot > 0:

        ans.append(job)

        profit += p

        ds.parent[slot] = ds.find(slot-1)


print("Jobs:",ans)
print("Profit:",profit)
