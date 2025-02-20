Project Description

Render URL:https://sprint-4-project-8sld.onrender.com

Vehicle Data Analysis Dashboard This project is a web-based dashboard built using Streamlit and Plotly to visualize and analyze a dataset of used vehicles in the US. The dashboard allows users to explore various trends, distributions, and relationships in the dataset, with interactive charts and filters.

Features: Data Cleaning: Cleans the dataset by handling missing values, splitting vehicle model information, and adding additional derived columns (e.g., vehicle age, annual mileage). Vehicle Distribution by Brand and Type: Visualizes the distribution of vehicle types across different brands. Condition vs Model Year Histogram: Displays the distribution of vehicle conditions across different model years. Price Distribution Comparison: Allows comparison of vehicle price distributions between different brands. Price vs Model Year and Brand: Interactive histogram showing the relationship between vehicle prices, model years, and brands. Vehicle Days Listed by Brand: Box plots showing the number of days a vehicle has been listed for sale by brand. Vehicle Age and Condition: Box plots showing the relationship between vehicle age, condition, and brand. Price vs Odometer: Scatter plot to explore the relationship between a vehicle’s price and its odometer reading (mileage). Interactive Features: Brand Filters: Select specific vehicle brands to filter and analyze the data. Year Filters: Choose vehicle model years in 5-year intervals for focused analysis. Normalization: Option to normalize histograms for better comparison of data distributions.

## Deploying on Render

1. **Create an account on Render**  
   Sign up for Render [here](https://render.com/).

2. **Connect Your GitHub Repository**  
   Once logged in, click on **New** and select **Web Service**. Then, connect your GitHub account and choose the repository you want to deploy.

3. **Configure Deployment**  
   - Choose the branch you want to deploy.
   - Render will automatically detect the environment (Node.js, Python, etc.), but you can specify your build and start commands if necessary.

4. **Set Environment Variables**  
   If your app uses environment variables (like database URLs or API keys), set them up in the **Environment** section on the Render dashboard.

5. **Start Deployment**  
   Click **Create Web Service** to start the deployment. Render will build and deploy your app automatically.

6. **Access Your Application**  
   After deployment, Render will provide a URL for your live app.

