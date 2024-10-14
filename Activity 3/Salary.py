years = int(input('How many years have they worked for the company?\n'))
children = int(input('How many children does the employee have?\n'))
spouse = int(input('Does the employee have a spouse?\nEnter 1 or Yes or 0 for No:\n'))

yearSalary = 30 * years
childrenSalary = 100 * children
spouseBonus = 250 * spouse

salarySum = yearSalary + childrenSalary + spouseBonus + 500
print('The calculated salary for this employee is:', salarySum)
