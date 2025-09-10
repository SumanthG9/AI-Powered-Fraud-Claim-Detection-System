AI-Powered Health Insurance Claim Fraud Detection SystemThis project is a full-stack web application designed to detect fraudulent health insurance claims in real-time. It showcases an end-to-end machine learning workflow, from data generation and model training to deployment via a RESTful API and interaction through a user-friendly web dashboard.The system is built to address a core business challenge for insurance providers like Star Health, enabling proactive identification of suspicious claims to reduce financial losses.FeaturesReal-Time Fraud Prediction: Submits claim data to a backend API and receives an instant fraud probability score.Machine Learning Core: Utilizes a RandomForestClassifier trained on a synthetically generated dataset with realistic fraud patterns.RESTful API: A robust backend built with FastAPI to serve the ML model and preprocessor.Interactive Frontend: A clean and simple dashboard built with React for a claims officer to input data and view results.Complete Data Pipeline: Includes scripts for synthetic data generation, database schema creation, and data population.Tech StackCategoryTechnologiesFrontendReact, Axios, HTML5, CSS3BackendFastAPI, Python, UvicornMachine Learning & DataScikit-learn, Pandas, NumPy, imbalanced-learn, JoblibDatabasePostgreSQL, SQLAlchemySetup and InstallationFollow these steps to set up and run the project on your local machine.PrerequisitesPython 3.8+Node.js and npmPostgreSQL1. Clone the Repositorygit clone [https://github.com/your-username/starhealth-fraud-detection.git](https://github.com/your-username/starhealth-fraud-detection.git)
cd starhealth-fraud-detection
2. Backend SetupCreate and Activate a Python Virtual Environment:# Create the environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# Activate it (macOS/Linux)
source venv/bin/activate
Install Python Dependencies:pip install -r requirements.txt
Set Up the PostgreSQL Database:Ensure PostgreSQL is running.Create the database:createdb -U postgres starhealth_fraud
Execute the schema file to create the tables:psql -U postgres -d starhealth_fraud -f schema.sql
Generate and Populate Data:Run the data generation script:python data/generate_data.py
Important: Open the populate_db.py file and replace 'your_password' with your actual PostgreSQL password.Run the population script:python populate_db.py
3. Frontend SetupNavigate to the Frontend Directory:cd frontend/claim-dashboard
Install Node.js Dependencies:npm install
4. Running the ApplicationYou need to have two terminals open simultaneously.Terminal 1: Start the Backend ServerNavigate to the project's root directory.Run Uvicorn:uvicorn backend.main:app --reload
The backend will be running at http://127.0.0.1:8000.Terminal 2: Start the Frontend ServerNavigate to the frontend/claim-dashboard directory.Run the React development server:npm start
Your browser will open to the application at http://localhost:3000.You can now use the dashboard to submit claims and see the AI-powered fraud detection in action!