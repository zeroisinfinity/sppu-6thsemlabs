jobs = [
    ('J1',2,100),
    ('J2',1,119),
    ('J3',2,27),
    ('J4',1,25),
    ('J5',3,15)
]

jobs.sort(key=lambda x : x[2] , reverse = True)

mx = max([job[1] for job in jobs])

profit = 0
schedule = [-1] * mx

for job , deadline , p in jobs:
    for j in range(deadline - 1 , -1 , -1):
        if schedule[j] == -1:
            schedule[j] = job
            break


print(schedule)

