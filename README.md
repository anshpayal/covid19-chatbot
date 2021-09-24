# COVID-chatbot

### Why this Project?
When covid arrived in India, there was some lack of guidance about the covid. So, at that time as a student, we got an idea to build a chatbot that can answer the queries related to COVID-19.

### My role in this project
  - My role in this project was to figure out which backend language and library is suitable for building a chatbot. 
  - I decided to go with Flask and chatterbot library to build the backend.<br/>
      - **The reason I chose flask was:** 
        - As per the deadline given for completing the project. I found Flask was easy to learn and quick for building small applications.
        - It is light weighted and can extend easily. 
        - Optional: It also provides flexibility.<br/>
    - **The reason I chose chatterbot library was:**
        - It helps to generate an automated response. 
        - The user enters the statement, library saves the request made by the user as well as it also saves the response that is sent back to the user.
        - As the number of instances increases in chatterbot, the accuracy of the response made by chatterbot also increases.

### Steps Involed
1. Create the **instance (object)** of chatbot.
2. Set the **storage adapter**, We use SQL storage adapter which helps to connect chatbot with DB. Used Database parameter create new SQLite DB.
3. **Logic adapter** logic behind the searching and selecting the response. Chatterbot allow us to use more than one logic adapters, when there is more than one logic adapters, the chatbot calucate the confidence level, and respone with high confidence level is returned. We used BestMatch and TimeLogic 
4. **Training** It involes loading the dailog into the chatbot DB. This creates kind of graph data strcture represents the set of know statments and response. train() function.
