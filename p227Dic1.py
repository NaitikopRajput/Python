students = {
    'Alice': 75,
    'Bob': 60,
    'Charlie': 90,
    'Dave': 50,
    'Eve': 80
}

passing_score = 70

print('Name\tScore\tPass')
for name, score in students.items():
    pass_status = 'Pass' if score >= passing_score else 'Fail'
    print(f'{name}\t{score}\t{pass_status}')
