import pandas as pd

data = {
    'Employee ID': [f'EMP{i}' for i in range(201, 221)],
    'Name': [
        'Rajesh Kumar', 'Meena Rani', 'Amitabh Das', 'Pooja Sinha', 'Ravi Verma',
        'Kavita Joshi', 'Suresh Rao', 'Anjali Mehta', 'Vikram Nair', 'Shweta Pillai',
        'Manoj Sharma', 'Divya Iyer', 'Karan Malhotra', 'Ritika Jain', 'Nitin Aggarwal',
        'Sneha Bhatt', 'Raghav Bansal', 'Neha Desai', 'Arjun Kapur', 'Isha Chopra'
    ],
    'Designation': ['Developer', 'Manager', 'Team Leader', 'Accounts', 'Developer'] * 4,
    'Salary (LPA)': [6.5, 9.2, 7.0, 5.5, 8.5, 6.2, 10.0, 7.3, 4.5, 9.5,
                     6.0, 11.2, 8.1, 5.4, 7.8, 6.9, 9.0, 4.8, 5.0, 12.0]
}

df = pd.DataFrame(data)

team_accounts_count = df[df['Designation'].isin(['Team Leader', 'Accounts'])].shape[0]
manager_count = (df['Designation'] == 'Manager').sum()
high_salary_count = (df['Salary (LPA)'] > 8).sum()
developer_ids = df[df['Designation'] == 'Developer']['Employee ID']

print("A) Employees who are Team Leaders or in Accounts:", team_accounts_count)
print("B) Number of Managers:", manager_count)
print("C) Employees with salary > 8 LPA:", high_salary_count)
print("D) Developer Employee IDs:\n", developer_ids.tolist())

df.to_excel("Employee_Analysis.xlsx", index =False)

