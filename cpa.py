import pandas as pd
import json

# Load JSON data
data = '''
{
  "courses": [
    { "courseId": 1, "courseName": "SQL for Beginners", "category": "Programming", "instructorId": 1 },
    { "courseId": 2, "courseName": "Advanced Excel", "category": "Data Analysis", "instructorId": 2 },
    { "courseId": 3, "courseName": "Data Analysis with Python", "category": "Data Analysis", "instructorId": 2 },
    { "courseId": 4, "courseName": "Introduction to Machine Learning", "category": "Machine Learning", "instructorId": 1 }
  ],
  "instructors": [
    { "instructorId": 1, "instructorName": "John Doe" },
    { "instructorId": 2, "instructorName": "Jane Smith" }
  ],
  "students": [
    { "studentId": 1, "studentName": "Alice Brown" },
    { "studentId": 2, "studentName": "Bob Johnson" },
    { "studentId": 3, "studentName": "Charlie Green" },
    { "studentId": 4, "studentName": "David Lee" },
    { "studentId": 5, "studentName": "Eva White" }
  ],
  "enrollments": [
    { "enrollmentId": 1, "studentId": 1, "courseId": 1, "enrollmentDate": "2024-01-15" },
    { "enrollmentId": 2, "studentId": 2, "courseId": 2, "enrollmentDate": "2024-02-01" },
    { "enrollmentId": 3, "studentId": 3, "courseId": 1, "enrollmentDate": "2024-03-10" },
    { "enrollmentId": 4, "studentId": 4, "courseId": 3, "enrollmentDate": "2024-01-20" },
    { "enrollmentId": 5, "studentId": 5, "courseId": 2, "enrollmentDate": "2024-02-15" }
  ]
}
'''

# Parse JSON data
json_data = json.loads(data)

# Create DataFrames
courses_df = pd.DataFrame(json_data['courses'])
instructors_df = pd.DataFrame(json_data['instructors'])
students_df = pd.DataFrame(json_data['students'])
enrollments_df = pd.DataFrame(json_data['enrollments'])

# Merge course and instructor data
course_instructor_df = courses_df.merge(instructors_df, on='instructorId')

# Fetch all course records
all_courses = courses_df

# Retrieve specific columns (course name, instructor name)
specific_columns = course_instructor_df[['courseName', 'instructorName']]

# Filter course records for a specific category (e.g., "Data Analysis")
specific_category = courses_df[courses_df['category'] == 'Data Analysis']

# Sort course data by enrollment date
sorted_enrollments = enrollments_df.sort_values(by='enrollmentDate')

# Count enrollments per course
enrollment_counts = enrollments_df['courseId'].value_counts().reset_index()
enrollment_counts.columns = ['courseId', 'enrollmentCount']

# Merge to get course details
course_enrollments = courses_df.merge(enrollment_counts, on='courseId')

# Limit the results to the top 10 most enrolled courses
top_10_courses = course_enrollments.sort_values(by='enrollmentCount', ascending=False).head(10)

# Count the total number of courses offered
total_courses = courses_df.shape[0]

# Calculate the average enrollment per course
average_enrollment = enrollment_counts['enrollmentCount'].mean()

# Group course data by category and count the number of courses in each category
category_counts = courses_df.groupby('category').size().reset_index(name='courseCount')

# Filter grouped data to show only categories with more than 10 courses
filtered_category_counts = category_counts[category_counts['courseCount'] > 10]

# Print the results
print("All Courses:")
print(all_courses)
print("\nSpecific Columns (Course Name, Instructor Name):")
print(specific_columns)
print("\nSpecific Category (Data Analysis):")
print(specific_category)
print("\nSorted Enrollments by Date:")
print(sorted_enrollments)
print("\nTop 10 Most Enrolled Courses:")
print(top_10_courses)
print("\nTotal Number of Courses Offered:", total_courses)
print("Average Enrollment per Course:", average_enrollment)
print("\nCourse Counts by Category:")
print(category_counts)
print("\nFiltered Category Counts (More than 10 Courses):")
print(filtered_category_counts)
