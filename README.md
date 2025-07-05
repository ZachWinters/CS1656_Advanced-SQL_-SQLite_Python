# SQLite Data Analysis Project- README
## Overview
This project demonstrates my ability to work with SQLite databases in Python with use of PANDAS to perform complex data analysis tasks. I created a database system for managing student course data, including students, courses, grades, and majors then wrote SQL queries to extract meaningful insights from this data

## Project Structure
* Database Schema: Created tables for Students, Courses, Grades, and Majors with appropriate relationships
* Data Loading: Implemented functionality to load data from CSV files into SQL lite database
* Data Analysis: Developed several analytical queries to answer specific questions about the data

## Analytical Queries
1. Courses Passed Per Student Per Semester
   * Counted courses passed (grade>0) and grouped by student, year, and semester
   * Sorted the results by student ID, year, and semester
2. Students Passing Multiple Courses
   * Filtered to show only the students that passed >= 2 courses per semester
   * Displayed the names of students instead of IDs
   * Sorted database by name, year, and semester
3. Students Failing Courses in Their Majors
   * Identified the students who failed (grade=0) courses in their declared majors
   * Implemented using both the view and direct table joins
4. Professor Sucess Metrics
   * Ranked the professors by the success of students (count of students passing with grade>=2)
   * Sorted success rates (descending) and the professor names (ascending)
5. Course Performance Report
   * Generated a complrehensive report showing:
     * Course numbers
     * List of the student names who passed (grade>=2)
     * Average grades (filtered for avg>3)
   * Formatted student names by "FirstName LastName" joined by commas
   * Sorted by average grade (descending), student names, and course number

Technical Skills Demonstrated
* SQLite databse creation and management
* Complex SQL query writing:
  * JOIN operations
  * GROUP BY with HAVING clauses
  * Aggregate functions (COUNT, AVG)
  * String concatentation and formatting
  * VIEW creation
* Python Database integration using sqlite3
* Data loading from CSV files
* Results formatting and presentation
