import pandas as pd

data = {
    'Roll Number': range(101, 126),
    'Registration Number': [f'REG20{i}' for i in range(101, 126)],
    'Student Name': [f'Student{i}' for i in range(1, 26)],
    'Department': ['CSE', 'IT', 'ECE', 'ME', 'CSE'] * 5,
    'Company': ['IBM', 'TCS', 'Infosys', 'Wipro', 'IBM'] * 5,
    'Package(LPA)': [6.5, 4.8, 5.2, 3.9, 7.0, 4.5, 5.0, 8.2, 3.6, 6.9,
                     4.2, 5.1, 6.3, 2.5, 7.1, 5.7, 4.0, 3.8, 6.6, 7.2,
                     4.9, 5.4, 6.1, 2.9, 8.0]
}

df = pd.DataFrame(data)

count_above_5 = (df['Package(LPA)'] > 5).sum()
placed_in_ibm = (df['Company'] == 'IBM').sum()
below_5_lpa = df[df['Package(LPA)'] < 5]
min_package = df['Package(LPA)'].min()
max_package = df['Package(LPA)'].max()

print("A) Count of students with package > 5 LPA:", count_above_5)
print("B) Number of students placed in IBM:", placed_in_ibm)
print("C) Students with package < 5 LPA:\n", below_5_lpa)
print("D) Minimum Package:", min_package)
print("   Maximum Package:", max_package)
