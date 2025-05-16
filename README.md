# COMP-49X-24-25-TransactCampus

Dashboard to view campus student dining data and trends.

To run: Run pip install requirements.txt to import necessary modules. Then run Flask application, and sign into PowerBI account when page is open.

Sprint 1: Implements PowerBI dashboard to view data summary for dummy breakfast data. Right now, you must sign into a valid PowerBi account so the report isn't public to everyone, and only viewable by users in the Workspace. In an upcoming sprint we will implement a login screen, so a PowerBI account isn't necessary. 

Sprint 2: Updated PowerBI dashboard to view data summary for dummy lunch data, and home page to view data for all times. Since we now have multiple reports, we added buttons to be able to navigate between reports. We also updated the PowerBI report to connect to a PostgreSQL database. Finally, we added a Docker Container so that our app now runs in a Local Containerized Instance. 

Sprint 3: Implemented depersonalized data from Transact. Added heatmaps for the overview pages. Finished the dinner overview dashboard. Created sidebar routes in Flask. Added comparison function where you can compare orders between different dates/weeks.

Sprint 4: Created a new Filter Data report page in PowerBi. This page is able to view and sort all the dining data. Useful for raw data and isolating elements for a PowerBi report print.

Sprint 5: Created a new report page in PowerBi that gives locations rankings and information of the foods nutritional values and popularity. Gave all food items a letter and score grade based on macro data.

Sprint 6: Created a new Health Groupings report page in PowerBi. Trained a clusting neural network to sort students into health groupings based on their eating recipt for the last 2 weeks.

Sprint 7: Added a Incentive Actions page to Health Groupings as to suggest actions to improve eating habits of the selected group. Updated Location Nutritional Score page's UI to be similar to the rest of the theme. Cleaned up Overview's UI. Updated Filter Data's UI to match the rest of the theme. Added a Home page for the project.