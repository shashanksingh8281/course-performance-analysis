import mysql.connector
from mysql.connector import Error

def create_connection():
    """ Create a database connection to a MySQL database """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='courses',
            user='root',
            password='Shashank@9119'
        )
        if connection.is_connected():
            print("Successfully connected to the database")
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

def execute_query(connection, query):
    """ Execute a single query """
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"Error: '{e}'")
        return None

def main():
    connection = create_connection()

    if connection:
        # Fetch all course records
        all_courses_query = "select * from subjects;"
        all_courses = execute_query(connection, all_courses_query)

        # Retrieve specific columns (course name, instructor name)
        specific_columns_query = '''
            select c.course_name, i.instructor_name
            from subjects c
            join instructors i on c.instructor_id = i.instructor_id;
        '''
        specific_columns = execute_query(connection, specific_columns_query)

        # Filter course records for a specific category (e.g., "Data Analysis")
        specific_category_query = "select * from subjects where category = 'Data Analysis';"
        specific_category = execute_query(connection, specific_category_query)

        # Sort course data by enrollment date
        sorted_enrollments_query = '''
            select e.enrollment_id, e.student_id, e.course_id, e.enrollment_date, c.course_name 
            from enrollments e 
            join subjects c on e.course_id = c.course_id 
            order by e.enrollment_date;
        '''
        sorted_enrollments = execute_query(connection, sorted_enrollments_query)

        # Count enrollments per course and limit the results to the top 10 most enrolled courses
        top_10_courses_query = '''
            select c.course_id, c.course_name, Count(e.enrollment_id) as enrollmentCount 
            from subjects c 
            join enrollments e on c.course_id = e.course_id 
            group by c.course_id, c.course_name 
            order by enrollmentCount desc 
            limit 10;
        '''
        top_10_courses = execute_query(connection, top_10_courses_query)

        # Count the total number of courses offered
        total_courses_query = "select count(*) as total_courses from subjects;"
        total_courses = execute_query(connection, total_courses_query)[0][0]

        # Calculate the average enrollment per course
        avg_enrollment_query = '''
            select avg(enrollmentCount) as average_enrollment 
            from (
                select Count(e.enrollment_id) as enrollmentCount 
                from subjects c 
                join enrollments e on c.course_id = e.course_id 
                group by c.course_id
            ) as subquery;
        '''
        avg_enrollment = execute_query(connection, avg_enrollment_query)[0][0]

        # Group course data by category and count the number of courses in each category
        courses_per_category_query = "select category, COUNT(*) as course_count from subjects group by category;"
        courses_per_category = execute_query(connection, courses_per_category_query)

        # Filter grouped data to show only categories with more than 10 courses
        categories_with_more_than_10_courses_query = '''
            select category, COUNT(*) AS course_count 
            from subjects 
            group by category 
            having COUNT(*) > 10;
        '''
        categories_with_more_than_10_courses = execute_query(connection, categories_with_more_than_10_courses_query)

        # Print the results
        print("All Courses:")
        for course in all_courses:
            print(course)

        print("\nSpecific Columns (Course Name, Instructor Name):")
        for course in specific_columns:
            print(course)

        print("\nSpecific Category (Data Analysis):")
        for course in specific_category:
            print(course)

        print("\nSorted Enrollments by Date:")
        for enrollment in sorted_enrollments:
            print(enrollment)

        print("\nTop 10 Most Enrolled Courses:")
        for course in top_10_courses:
            print(course)

        print("\nTotal Number of Courses Offered:", total_courses)
        print("Average Enrollment per Course:", avg_enrollment)

        print("\nCourses Per Category:")
        for category in courses_per_category:
            print(category)

        print("\nCategories With More Than 10 Courses:")
        for category in categories_with_more_than_10_courses:
            print(category)

        # Close the connection
        connection.close()

if __name__ == '__main__':
    main()
