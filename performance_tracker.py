def calculate_average(self):
        return sum(self.marks) / len(self.marks)
def calculate_average_marks(stu):
    avg = {name: round(stu.calculate_average(), 2) for name, marks in stu.items()}
    return avg


def find_top_performer(avg):
    return max(avg, key=avg.get)


students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}
averages = calculate_average_marks(students)
top_performer = find_top_performer(averages)

print(f"Average Marks: {averages}")
print(f"Top Performer: {top_performer}")