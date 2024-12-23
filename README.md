# CS-340-Journal-Portfolio-Item
CS-340 Journal: Portfolio Item AAC Project


**Technologies and Tools**
Database: I used MongoDB because it’s a flexible NoSQL database, to store the animal shelter dataset. MongoDB's structure and good querying tools made it a great fit for this project.
Backend: On the backend, I coded everything in Python. Python's huge amount of libraries and frameworks like Pandas for data manipulation and Plotly for visualization helped me provide good tools to work with.
Frontend: For the web-based user interface, I turned to the Dash framework. Dash is a Python library designed specifically for building interactive, data driven dashboards. It has great functionality for linking user inputs to dynamic data update, thus saving time.

**Development Process**
I followed the Dashboard Specifications Document provided to fully understand the required functionality and features.
Set up the Environment: After importing the necessary Python packages, I structured the project files, including the ProjectTwoDashboard Jupyter notebook.


**Implement Data Table:** Using the CRUD module I had built previously, I pulled the full dataset from the MongoDB database and set up the interactive data table for the dashboard.

**Add Filtering Options:** I created database queries to support the different rescue type filters, then integrated those into the dashboard's user interface.

**Build Visualizations:** With the filtering in place, I developed the geolocation map and breed distribution chart components making sure they updated based on the user's filter selections.

**Test and Deploy:** Finally, I ran a test to make sure all the dashboard pieces were working together smoothly. I then took screenshots to show the app’s functions under different filters

**Challenges and Solutions**
One of the challenges I faced was making sure all the different dashboard components, the filters, data table, and visualizations were communicating and updating correctly. To overcome this I took a simple approach: separating the data manipulation, view logic, and controller functionality into different components, this made it easier to manage the interactions. I also made good use of Dash's already built in functions like the call callback system to match the user’s inputs to the corresponding data updates and GUI changes.
