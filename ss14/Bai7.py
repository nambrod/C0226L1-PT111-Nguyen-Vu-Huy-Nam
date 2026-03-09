students = (
    ("An", 8.5),
    ("Bình", 7.0),
    ("Chi", 9.2)
)
point = []
for i in range(3):
    print(students[i])
    point.append(students[i][1])
point.sort()
print(point[-1])
i = 0
for i in range(3):
    if point[-1] == students[i][1]:
        print("Học sinh điểm cao nhất là:", students[i][0])
    else: continue

