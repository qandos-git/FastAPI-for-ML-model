## Instructions:
1. Set Up the Virtual Environment
- Create a virtual environment by running:
   - `python -m venv venv `
2. Activate the virtual environment:

      For Windows:

        `venv\Scripts\activate` 
        
      For MacOS/Linux:

        `source venv/bin/activate`

2. Install Dependencies
   
      Install all required packages from requirements.txt:
   
    `pip install -r requirements.txt`

4. Start the Uvicorn Server
   
    `uvicorn main:app --reload`

6. Send a POST Request
   
Send a POST request to the server using Postman or curl, with data from artifacts/sample.json as a template.

Example curl command:
    
    curl -X POST <localhost address> -H "Content-Type: application/json" -d "{\"gender\": \"male\", \"race_ethnicity\": \"group C\", \"parental_level_of_education\": \"associate's degree\", \"lunch\": \"free/reduced\", \"test_preparation_course\": \"none\", \"writing_score\": 90, \"reading_score\": 51}"

    
Note: Replace <localhost address> with http://127.0.0.1:8000 or your server's address if different.

