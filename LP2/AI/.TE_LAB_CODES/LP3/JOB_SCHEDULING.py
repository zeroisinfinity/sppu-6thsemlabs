# ============================================================
# QUESTION:
# Implement Job Scheduling Problem using Greedy Algorithm
# to maximize profit with given deadlines.
# ============================================================


# ============================================================
# EXPLANATION:
#
# Job Scheduling is a Greedy Algorithm problem
# where each job has:
#
# - Job ID
# - Deadline
# - Profit
#
# Goal:
# Schedule jobs to maximize total profit
# while meeting deadlines.
#
# Steps:
# 1. Sort jobs based on profit (descending).
# 2. Find maximum deadline.
# 3. Assign job to latest possible slot.
# 4. Repeat until all jobs processed.
#
# Greedy Choice:
# Always select job with highest profit first.
# ============================================================


# ============================================================
# EXPLANATION WITH EXAMPLE:
#
# Jobs:
#
# Job   Deadline   Profit
# A        2         100
# B        1          19
# C        2          27
# D        1          25
# E        3          15
#
# After sorting by profit:
#
# A, C, D, B, E
#
# Schedule:
#
# Slot1 → C
# Slot2 → A
# Slot3 → E
#
# Total Profit = 142
# ============================================================


# ======================
# JOB SCHEDULING PROGRAM
# ======================

def job_scheduling(jobs):

    # Sort jobs by profit
    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(job[1] for job in jobs)

    slots = [-1] * max_deadline

    total_profit = 0

    for job in jobs:

        job_id, deadline, profit = job

        for j in range(deadline - 1, -1, -1):

            if slots[j] == -1:

                slots[j] = job_id

                total_profit += profit

                break

    return slots, total_profit


# Driver Code

jobs = [
    ('A', 2, 100),
    ('B', 1, 19),
    ('C', 2, 27),
    ('D', 1, 25),
    ('E', 3, 15)
]

schedule, profit = job_scheduling(jobs)

print("Job Schedule:", schedule)

print("Total Profit:", profit)