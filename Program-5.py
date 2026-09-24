"""
Program: Fractional Knapsack and Job Scheduling
Author: Shrey Tiwari

Description:
Implements the fractional knapsack algorithm to find the maximum
attainable profit and job scheduling algorithm to find an optimal
sequence of jobs that maximizes total profit.

Input: Weights, values, and capacity for fractional knapsack.
       Jobs with job ID, deadline, and profit for job scheduling.

Output: Maximum attainable profit and optimal job sequence.
"""

from typing import List
from dataclasses import dataclass


@dataclass
class Job:
    id: int
    deadline: int
    profit: int


def fractional_knapsack(weights: List[int], values: List[int], capacity: int) -> float:
    items = []

    for i in range(len(weights)):
        ratio = values[i] / weights[i]
        items.append((ratio, weights[i], values[i]))

    items.sort(reverse=True)

    total_profit = 0.0

    for ratio, weight, value in items:
        if capacity == 0:
            break

        if weight <= capacity:
            total_profit += value
            capacity -= weight
        else:
            total_profit += ratio * capacity
            capacity = 0

    return total_profit


def job_scheduling(jobs: List[Job]) -> List[int]:
    jobs.sort(key=lambda job: job.profit, reverse=True)

    max_deadline = max(job.deadline for job in jobs)

    slots = [-1] * (max_deadline + 1)

    for job in jobs:
        for j in range(job.deadline, 0, -1):
            if slots[j] == -1:
                slots[j] = job.id
                break

    return [job_id for job_id in slots[1:] if job_id != -1]


# Fractional Knapsack Input
n = int(input("Enter number of items: "))

weights = list(map(int, input("Enter weights: ").split()))
values = list(map(int, input("Enter values: ").split()))

capacity = int(input("Enter capacity: "))

profit = fractional_knapsack(weights, values, capacity)

print("Maximum attainable profit:", round(profit, 2))


# Job Scheduling Input
m = int(input("\nEnter number of jobs: "))

jobs = []

print("Enter job ID, deadline and profit:")
for i in range(m):
    job_id, deadline, job_profit = map(int, input().split())
    jobs.append(Job(job_id, deadline, job_profit))

sequence = job_scheduling(jobs)

print("Optimal job sequence:", sequence)