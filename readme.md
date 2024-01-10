# Welcome to Python - Daily
<details>
<summary>Apache - Configuration</summary>

# Apache Hosting on VPS: Advantages and Disadvantages

## Introduction

When it comes to hosting web applications on a Virtual Private Server (VPS), Apache remains a popular choice among developers and system administrators. This README aims to explore the advantages and disadvantages of using Apache as the web server for hosting Python applications on a VPS. Additionally, a sample Apache configuration file `app.conf` for a Django project is provided, which can serve as a starting point for other Python web applications.

## Advantages of Apache Hosting on VPS

### 1. Robust and Proven

Apache is one of the oldest and most widely used web servers globally, with a proven track record for stability and reliability. Its long-standing presence in the industry makes it a trusted choice for hosting applications on VPS environments.

### 2. Configurability

Apache offers a high level of configurability, allowing users to fine-tune various settings to meet the specific requirements of their applications. This flexibility is particularly beneficial when hosting diverse types of web applications, including Django, Flask, and other Python frameworks.

### 3. Modularity

Apache is designed with a modular architecture, enabling the use of modules to extend its functionality. This modular approach allows users to add or remove features based on their needs, enhancing performance and security without unnecessary overhead.

### 4. Support for Multiple Programming Languages

While the provided sample configuration is tailored for Django, Apache has the versatility to host web applications written in various programming languages. This includes support for Python, PHP, Ruby, and more, making it a versatile choice for multi-language environments.

### 5. SSL/TLS Support

Apache easily integrates with SSL/TLS protocols, providing a secure connection between clients and the server. This is crucial for applications that handle sensitive information, ensuring data integrity and confidentiality.

## Disadvantages of Apache Hosting on VPS

### 1. Resource Usage

Apache's process-based architecture may consume more system resources compared to event-driven web servers like Nginx. In scenarios with limited resources, Apache may not be the most efficient choice, especially when handling a large number of concurrent connections.

### 2. Configuration Complexity

While configurability is an advantage, it can also lead to complexity, especially for users unfamiliar with Apache's configuration syntax. Incorrect configurations may result in unexpected behavior or security vulnerabilities.

### 3. Learning Curve

For users new to web hosting and server management, Apache's extensive feature set and configuration options can present a steep learning curve. It may require time and effort to become proficient in optimizing Apache for specific use cases.

## Sample Apache Configuration

The provided `app.py` is a sample Apache configuration file tailored for a Django project. This configuration assumes that the project is structured similarly to the provided Django project structure and can be used as a starting point for other Python web applications. Please review and modify the paths, usernames, and domain names based on your specific setup.

### Usage

```bash
<VirtualHost *:80>
    ServerName domain.com
    ServerAlias www.domain.com

    RewriteEngine on
    RewriteCond %{HTTP:Authorization} ^(.*)
    RewriteRule .* - [e=HTTP_AUTHORIZATION:%1]

    RewriteCond %{REQUEST_URI} !^/static/
    RewriteRule ^(.*)$ https://%{SERVER_NAME}$1 [R,L]
</VirtualHost>

<VirtualHost *:443>
    ServerName domain.com
    ServerAlias www.domain.com

    Alias /static /home/username/djangoProjectName/static
    <Directory /home/username/djangoProjectName/static>
        Require all granted
    </Directory>

    Alias /media /home/username/djangoProjectName/media
    Alias /media/media /home/username/djangoProjectName/media
    <Directory /home/username/djangoProjectName/media>
        Require all granted
    </Directory>

    <Directory /home/username/djangoProjectName>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>

    WSGIDaemonProcess djangoProjectName python-path=/home/username/djangoProjectName:/home/username/djangoProjectName/venv/lib/python3.9/site-packages
    WSGIProcessGroup djangoProjectName
    WSGIScriptAlias / /home/username/djangoProjectName/raffle/wsgi.py

    WSGIPassAuthorization On

    ErrorLog ${APACHE_LOG_DIR}/djangoProjectName-error.log
    CustomLog ${APACHE_LOG_DIR}/djangoProjectName-access.log combined
    Include /etc/letsencrypt/options-ssl-apache.conf
    SSLCertificateFile /etc/letsencrypt/live/domain.com-0001/fullchain.pem
    SSLCertificateKeyFile /etc/letsencrypt/live/domain.com-0001/privkey.pem
</VirtualHost>

```

1. Copy the `app.conf` configuration into your Apache configuration file, typically located at `/etc/apache2/sites-available/`.
2. Update paths, usernames, and domain names as needed.
3. If you don't have SSL certificates, you can comment out the lines:
   ```apache
   # SSLCertificateFile /etc/letsencrypt/live/domain.com-0001/fullchain.pem
   # SSLCertificateKeyFile /etc/letsencrypt/live/domain.com-0001/privkey.pem
   ```
**Note:** Always prioritize the security of sensitive information, such as usernames, paths, and SSL certificates.


</details>
<details>
<summary>Black Stack Hub (from whatsapp group)</summary>

# Welcome to the BlackStackHub Support Code Repository

This repository contains support code for the Python-Daily project. The code here is meant to address reported bugs, provide modifications, and support discussions within our WhatsApp group.

## How to Join Our WhatsApp Group

If you have questions, encounter issues, or want to engage in discussions, you can join our WhatsApp group. Click on the following link to join: [Join WhatsApp Group](https://chat.whatsapp.com/IVvrrF9Wq7OHWk5x4XNk9K)

## BlackStackHub GitHub Organization

Explore more projects and contributions by visiting our GitHub organization at [github.com/blackstackhub](https://github.com/blackstackhub).

## Folder Structure

- **blackstackhub/**
  - *Support Code:* Contains additional code to address reported bugs and provide solutions.
  - *Modifications:* Code modifications for enhancing features or fixing issues.

Feel free to explore, contribute, and engage with the community! If you encounter any issues or have questions, don't hesitate to reach out in the WhatsApp group.

Happy coding!

</details>
<details>
<summary>Data analysis</summary>

# Fruit Sales Analysis

This contains a Python script for analyzing and visualizing fruit sales over time. The script uses the Pandas library for data manipulation and Matplotlib for creating plots.

Data analysis is a crucial component in various fields and industries for several reasons.
Check out [django-analyst](https://github.com/devfemibadmus/python-daily) a software that provide analysis for models in your django project

![Figure_1](data-analysis/Figure_1.png?raw=true)

Here's a more detailed explanation of why data analysis is needed:

1.  **Informed Decision-Making:**
    
    -   **What it means:** Data analysis enables organizations to make informed decisions by extracting valuable insights from raw data.
    -   **Why it's needed:** Decision-makers can better understand patterns, trends, and correlations within their data, allowing them to make strategic and informed choices.
2.  **Identifying Trends and Patterns:**
    
    -   **What it means:** Data analysis helps in recognizing trends and patterns within datasets that might not be apparent at first glance.
    -   **Why it's needed:** Identifying trends can provide valuable insights into market dynamics, customer behavior, and other factors critical for business success.
3.  **Performance Measurement:**
    
    -   **What it means:** Organizations use data analysis to assess their performance against predefined metrics and goals.
    -   **Why it's needed:** Measuring performance helps in evaluating the effectiveness of strategies, campaigns, and overall business operations.
4.  **Customer Understanding:**
    
    -   **What it means:** Analyzing customer data allows businesses to understand customer preferences, behaviors, and needs.
    -   **Why it's needed:** This understanding is essential for tailoring products, services, and marketing strategies to meet customer expectations and enhance customer satisfaction.
5.  **Risk Management:**
    
    -   **What it means:** Data analysis assists in identifying and mitigating potential risks by evaluating historical data and predicting future outcomes.
    -   **Why it's needed:** Businesses can proactively manage risks, anticipate challenges, and implement strategies to minimize negative impacts.
6.  **Resource Optimization:**
    
    -   **What it means:** Data analysis helps in optimizing resource allocation, whether it's time, money, or personnel.
    -   **Why it's needed:** Efficient resource allocation ensures that organizations maximize their outputs while minimizing unnecessary costs.
7.  **Performance Monitoring and KPIs:**
    
    -   **What it means:** Key Performance Indicators (KPIs) are tracked and monitored through data analysis to measure the success of specific objectives.
    -   **Why it's needed:** Monitoring KPIs provides real-time feedback on the effectiveness of strategies and helps in making timely adjustments.
8.  **Market Research:**
    
    -   **What it means:** Data analysis is used in market research to understand market trends, consumer preferences, and competitive landscapes.
    -   **Why it's needed:** Businesses can stay competitive and adapt to changing market conditions by staying informed about industry trends and consumer behavior.

In summary, data analysis is essential for organizations to gain meaningful insights, make informed decisions, and stay competitive in today's data-driven world. It empowers businesses to understand their operations, customers, and market dynamics, leading to improved efficiency and better outcomes.

## Getting Started

Make sure you have the required libraries installed by running:

```bash
pip install pandas matplotlib
```

## Code explanation
we will be using .csv in this practice, you can get .csv file  from your database by using sample below code
```bash
import sqlite3
import csv

# Connect to the SQLite database
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

# Execute a query to select data from a table
cursor.execute('SELECT * FROM your_table')

# Fetch all the results
data = cursor.fetchall()

# Define the CSV file name
csv_file = 'output.csv'

# Write the data to a CSV file
with open(csv_file, 'w', newline='') as file:
    csv_writer = csv
```
and here we have our CVS file that's being use
```bash
Fruit,Sale,Date

Apples,15,2022-01-01
Apples,10,2022-01-02
Apples,20,2022-01-03

Bananas,5,2022-01-01
Bananas,15,2022-01-02
Bananas,25,2022-01-03

Cherries,3,2022-01-01
Cherries,9,2022-01-02
Cherries,18,2022-01-03
```
here is our `sales.py` that does the analysis for the fruit sales
```bash
# Import the pandas library and alias it as 'pd'
import pandas as pd

# Import the pyplot module from matplotlib and alias it as 'plt'
import matplotlib.pyplot as plt

# Read the CSV file 'fruit_sale.csv' into a pandas DataFrame and assign it to the variable 'df'
df = pd.read_csv('fruit_sale.csv')

# Create a new figure with a specified size (10 inches by 6 inches)
plt.figure(figsize=(10, 6))

# Iterate over each unique fruit in the 'Fruit' column of the DataFrame
for fruit in df['Fruit'].unique():
    # Create a subset of the DataFrame for the current fruit
    fruit_data = df[df['Fruit'] == fruit]
    
    # Plot the sales over time for the current fruit, using markers ('o') and a label
    plt.plot(fruit_data['Date'], fruit_data['Sale'], marker='o', label=fruit)

# Add a label to the x-axis
plt.xlabel('Date')

# Add a label to the y-axis
plt.ylabel('Sale')

# Add a title to the plot
plt.title('Sales Over Time for Each Fruit (Line Plot with Markers)')

# Display a legend to distinguish between different fruits in the plot
plt.legend()

# Display the plot
plt.show()

```
![Figure_1](data-analysis/Figure_1.png?raw=true)

This script reads a CSV file containing fruit sales data and then creates a line plot with markers to visualize the sales trends for each type of fruit over time.

## Result

The plot above illustrates the growth of sales for different fruits over the provided date range. Data Frame is created containing only the rows corresponding to that fruit type, and a line plot with markers is generated.

Here's an explanation of the result:

-   **Blue Line (Apple):**
    
    -   The blue line represents the sales over time for apples.
    -   Each marker on the blue line corresponds to a specific date, and the vertical position of the marker indicates the quantity of apples sold on that date.
-   **Orange Line (Banana):**
    
    -   The orange line represents the sales over time for bananas.
    -   Each marker on the orange line corresponds to a specific date, and the vertical position of the marker indicates the quantity of bananas sold on that date.
-   **Green Line (Cherry):**
    
    -   The green line represents the sales over time for cherries.
    -   Each marker on the green line corresponds to a specific date, and the vertical position of the marker indicates the quantity of cherries sold on that date.
-   **Reading the Plot:**
    
    -   The x-axis represents the dates (time), and the y-axis represents the quantity of sales.
    -   By looking at the markers on each line, you can easily see how many units of each fruit type were sold on a specific date.
    -   The legend on the plot helps identify which line corresponds to each fruit type.

For example, if you want to know how many apples were sold on January 2, you would look at the blue line at the position where it intersects with the date January 2 on the x-axis. Similarly, you can interpret the sales for bananas and cherries on each respective line.
</details>
<details>
<summary>Data Structure</summary>

# Graph Visualization and Shortest Path Finder(map.py)

This Python script provides a `Graph` class for working with undirected graphs. It includes functionalities to add nodes and edges, find the shortest path between nodes using Dijkstra's algorithm, and visualize the graph using NetworkX and Matplotlib.

![Figure_1.png](data-structure/Figure_1.png?raw=true)

## Usage

1.  **Install Dependencies:**
    
    -   Ensure you have the required dependencies installed. You can install them using:
                
        ```bash
        pip install matplotlib networkx
        ``` 
        
2.  **Run the Script:**
    
    -   Copy the script (`map.py`) into your project.
    -   Customize the graph data in the JSON format within the script or load your own data.
3.  **Customize Graph Data:**
    
    -   Edit the `json_data` variable in the script to represent your graph. The JSON structure should include "nodes" and "edges" with corresponding details.
4.  **Create Graph and Find Shortest Path:**
    
    -   Instantiate the `Graph` class, add nodes and edges, and use the `dijkstra` method to find the shortest path between two nodes.
        
        
        ```python
        # Example:
        map_graph = Graph()
        map_graph.add_node("A")
        map_graph.add_edge("A", "B", 2)
        # ... add more nodes and edges ...
        shortest_distance, shortest_path = map_graph.dijkstra("A", "L")
        ``` 
        
5.  **Visualize the Graph:**
    
    -   Use the `visualize` method to display the graph with Matplotlib.
        
        pythonCopy code
        
        `map_graph.visualize()` 
        

## Example

An example graph is provided in the script. Run the script to visualize the graph and find the shortest path from node "A" to node "L."

```bash
# Run the script
python graph_visualization.py
```
![Figure_1.png](data-structure/Figure_1.png?raw=true)






# Social Media Network (social.py)

This Python program implements a simple social media network using the NetworkX library. The network allows users to be added, relationships to be formed between them, and provides functionality to find connections, analyze social circles, recommend new connections, and visualize the network.

![Figure_2.png](data-structure/Figure_2.png?raw=true)

## Features

1. **Adding Users:**
   - Users can be added to the social media network.

2. **Adding Relationships:**
   - Relationships between users (edges) can be added with specified relationship types.

3. **Finding Connections:**
   - Users can find their connections (neighbors) along with the relationship types.

4. **Analyzing Social Circles:**
   - The network can be analyzed to identify social circles using connected components.

5. **Recommendations:**
   - Users can receive recommendations for potential connections based on shared connections.

6. **Visualization:**
   - The network can be visualized using Matplotlib.

## Usage

 1. **Initialization:**
   ```python
   social_media_network = SocialMediaNetwork()
   ```
 
 2. **Adding Users and Relationships:**
   ```python
   social_media_network.add_user("User1")
   social_media_network.add_user("User2")
   social_media_network.add_relationship("User1", "User2", "Friend")
   ```
  
 3.  **Finding Connections:**
   ```python
   connections = social_media_network.find_connections("User1")
   print(f"Connections for User1: {connections}")
   ```
   
 4. **Analyzing Social Circles:**
   ```python
   social_circles = social_media_network.analyze_social_circles()
   user_social_circle = [circle for circle in social_circles if  "User1" in circle]
   print(f"Social Circles for User1: {user_social_circle if user_social_circle else 0}")
   ```
   
 5. **Recommendations:**
   ```python
   recommendations = social_media_network.recommend_connections("User1")
   print(f"Recommendations for User1: {recommendations}")
   ```
   
 6. **Visualization:**
   ```python
   social_media_network.visualize()
   ```
![Figure_2.png](data-structure/Figure_2.png?raw=true)
   
</details>
<details>
<summary>Google Cloud</summary>

# Welcome Google Cloud Platform

Google Cloud Platform stands out for its reliability, scalability, and a wide range of services that support various workloads. Key reasons to choose GCP for deploying python apps include:

-   **Global Infrastructure**: GCP's extensive global infrastructure ensures low-latency access to your application for users worldwide.
    
-   **Scalability**: GCP provides scalable solutions to accommodate the growth of your application, ensuring optimal performance under varying workloads.
    
-   **Integrated Services**: GCP offers a suite of integrated services for storage, databases, machine learning, and more, facilitating a seamless development and deployment experience.
    

## Choosing the Right Service

### App Engine

-   **Managed Service**: App Engine is a fully managed platform that abstracts away infrastructure management, allowing developers to focus solely on their application code.
    
-   **Automatic Scaling**: App Engine automatically adjusts resources based on traffic, ensuring optimal performance without manual intervention.
    

### Compute Engine

-   **Customizable Virtual Machines**: Compute Engine offers virtual machines with full control over configurations, making it suitable for applications with specific requirements.
    
-   **Persistent Storage**: Ideal for applications that require persistent disk storage, Compute Engine allows you to attach and detach storage volumes as needed.
    

### Cloud Run

-   **Containerized Deployments**: Cloud Run is designed for containerized applications, providing flexibility in choosing your preferred programming language and dependencies.
    
-   **Serverless**: Cloud Run is serverless, meaning you only pay for the compute resources used during the execution of your containers.
   

## Conclusion

Google Cloud Platform provides a versatile environment for deploying python applications. Choose the service that best aligns with your application's requirements, whether it's the simplicity of App Engine, the flexibility of Compute Engine, or the containerized approach with Cloud Run. Follow the steps outlined in this guide to ensure a smooth deployment process on GCP.


## References

-   [Google Cloud Documentation](https://cloud.google.com/python/docs/getting-started)
-   [Google Cloud Codelabs](https://codelabs.developers.google.com/codelabs/cloud-app-engine-python3)
- [google-cloud-django-settings](https://github.com/devfemibadmus/python-daily/tree/master/gcloud/django/settings.py)



# Perform CRUD operation on Google Cloud Storage

```python
from google.cloud import storage
import json

# Set your Google Cloud Storage credentials (make sure it has the necessary permissions)
client = storage.Client.from_service_account_json('path/to/your/credentials.json')

# Set your bucket name
bucket_name = 'your-bucket-name'

# Create a bucket object
bucket = client.get_bucket(bucket_name)

def create_operation(data, file_name='db.json'):
    # Serialize the data to a JSON-formatted string
    json_data = json.dumps(data)
    
    # Write the JSON data to a file
    blob = bucket.blob(file_name)
    blob.upload_from_string(json_data)
    
    print(f"Data created successfully in '{file_name}'")

def read_operation(file_name='db.json'):
    # Get the blob
    blob = bucket.blob(file_name)
    
    try:
        # Download the content
        json_content = blob.download_as_text()
        
        # Deserialize the JSON data
        read_data = json.loads(json_content)
        
        print(f"Read Data from '{file_name}':")
        print(read_data)
    except storage.exceptions.NotFound:
        print(f"File '{file_name}' not found.")

def update_operation(data, file_name='db.json'):
    # Perform update by calling the create operation with new data
    create_operation(data, file_name)
    
    print(f"Data updated successfully in '{file_name}'")

def delete_operation(file_name='db.json'):
    # Get the blob
    blob = bucket.blob(file_name)
    
    try:
        # Delete the blob
        blob.delete()
        
        print(f"File '{file_name}' deleted successfully.")
    except storage.exceptions.NotFound:
        print(f"File '{file_name}' not found. Deletion failed.")

# Sample data
users = [
    {"id": 1, "name": "John Doe", "age": 25},
    {"id": 2, "name": "Jane Doe", "age": 30}
]

# CRUD operations
create_operation(users)
read_operation()
update_operation([
    {"id": 1, "name": "Updated John Doe", "age": 26},
    {"id": 3, "name": "New User", "age": 22}
])
read_operation()
delete_operation()
read_operation()  # This should indicate that the file is not found after deletion
```


## References

-   [Google Cloud Documentation](https://cloud.google.com/python/docs/getting-started)
-   [Google Cloud Codelabs](https://codelabs.developers.google.com/codelabs/cloud-app-engine-python3)
- [google-cloud-django](https://github.com/devfemibadmus/python-daily/tree/master/gcloud/django/settings.py)
</details>

<details>
<summary>SQL University management System</summary>

# University Management System

This Python script demonstrates basic CRUD (Create, Read, Update, Delete) operations for managing a university database using SQLite. The script includes functions for adding students, courses, enrollments, employees, and employee details. It also provides functionality for reading, updating, and deleting records.

## Database Connection and Table Creation

```python
# Connect to the database (creates a new file named 'university.db' if it doesn't exist)
conn = sqlite3.connect('university.db')
cursor = conn.cursor()

# Create tables if they don't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
''')

# (Similar CREATE TABLE statements for courses, enrollments, employees, and employee_details)
```
This section establishes a connection to the SQLite database named 'university.db' and creates tables for students, courses, enrollments, employees, and employee details if they don't already exist.

## Create Functions
```python
def add_student(name):
    try:
        cursor.execute('INSERT INTO students (name) VALUES (?)', (name,))
        conn.commit()
        print(f"Student '{name}' added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding student: {e}")

# (Similar functions for add_course, enroll_student, add_employee, and add_employee_details)

```
These functions handle the creation (INSERT) of new records in the respective tables. They use parameterized queries to avoid SQL injection and include error handling to catch any database-related issues.

## Read Functions
```python
def get_students():
    try:
        cursor.execute('SELECT * FROM students')
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error fetching students: {e}")
        return []

# (Similar functions for get_courses, get_enrollments, get_employees, and get_employee_details)
```
These functions retrieve data (SELECT) from the respective tables. They execute SQL queries, fetch the results, and handle errors, returning the data or an empty list if an error occurs.

## Update Functions
```python
def update_student_name(student_id, new_name):
    try:
        cursor.execute('UPDATE students SET name = ? WHERE student_id = ?', (new_name, student_id))
        conn.commit()
        print(f"Student with student_id {student_id} updated successfully.")
    except sqlite3.Error as e:
        print(f"Error updating student name: {e}")

# (Similar function for update_employee_details_address)
```
## Delete Functions
```python
def delete_student(student_id):
    try:
        cursor.execute('DELETE FROM students WHERE student_id = ?', (student_id,))
        conn.commit()
        print(f"Student with student_id {student_id} deleted successfully.")
    except sqlite3.Error as e:
        print(f"Error deleting student: {e}")

# (Similar function for delete_employee)
```

## Example Usage
```python
# Example Usage
add_student('John Doe')
add_student('Jane Doe')

add_course('Introduction to Programming')
add_course('Database Management')

enroll_student(1, 1)
enroll_student(1, 2)
enroll_student(2, 2)

add_employee('Alice Smith')
add_employee_details(1, '123 Main St')
```
This part of the code demonstrates how to use the functions by adding sample data to the tables.

## Close the Connection
```python
# Close the connection
conn.close()
```
## Closing the Database Connection

If the connection (`conn.close()`) is not closed explicitly, it can lead to various issues:

- **Resource Leakage:** Each open connection consumes system resources. If connections are not closed, it can lead to resource leakage, potentially causing your application to run out of available resources over time.

- **Locking Issues:** In some database systems, not closing connections can lead to issues with locking. For example, other processes or applications might be prevented from accessing the database if there are open transactions on the same records.

- **Data Integrity:** Open connections can impact the consistency and integrity of your data. Changes made in one session might not be visible to other sessions until the connection is closed.

- **Performance:** Over time, having numerous open connections can impact the performance of your application and the database server.

To avoid these issues, it's a good practice to always close the database connection once you have finished using it. The `conn.close()` statement in your code is responsible for closing the connection to the SQLite database.

Here's where you should typically close the connection:

```python
# Example Usage
print("\nAfter Update and Delete:")
print("Students:")
print(get_students())

print("Employees:")
print(get_employees())

# Close the connection
conn.close()
```
This part of the code, at the end of the script, is where the connection is closed. Always make sure to include this statement to properly release resources and ensure the integrity and performance of your application.
</details>
