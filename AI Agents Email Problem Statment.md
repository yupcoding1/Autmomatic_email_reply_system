**Project: Automatic Email Reply System for Film Equipment Rental Service**

**Objective:**

Design and implement alangchain based  system that classifies incoming emails into three categories and executes specific actions based on the category. The system should enhance customer interaction by providing automated responses tailored to inquiries, reviews, and assistance requests.

**Categories and Actions:**

1. **Inquiry Handling:**  
   * **Database**: Develop an SQL database to store details about film equipment.  
   * **Action**: When an inquiry email is received, check the database for item availability.  
     * If available, reply with the item's price.  
     * If not available, suggest similar available items.  
1. **Review Handling:**  
   * **Positive Reviews**: Thank the sender and encourage them to share their experience on social media.  
   * **Negative Reviews**: Escalate to the CRM system for follow-up with a phone call from customer service and offer a gift voucher in the reply.  
1. **Assistance Request Handling:**  
   * **Documentation**: Create a document with frequently asked questions about film equipment using ChatGPT or from equipment manuals.  
   * **RAG Pipeline**: Use a Retrieval-Augmented Generation approach to search for solutions to reported equipment issues.  
     * If a suitable solution is found, provide it in the reply.  
     * If no solution is found, escalate the issue to customer service.  
1. **General Handling:**  
   * **Forwarding**: Emails that do not fit into the above categories should be forwarded to customer service for further evaluation.

**Resources:**

* **Crew AI Tutorial**: [Crew AI \- Building AI Agents](https://youtu.be/kBXYFaZ0EN0?si=OectYEcdR7rwYeWu)  
* **Langchain Email Tutorial**: [Langchain \- Orchestration of AI Agents](https://youtu.be/lvQ96Ssesfk?si=WtZs99EwzoK4lC\_2)  
* **Groq API Key for fast Inference**: [Groq LLM Backend](https://console.groq.com/keys)

**Deliverables:**

1. **Database Schema and Implementation**: The schema of the SQL database along with the actual database setup.  
1. **RAG Pipeline Document**: Documentation detailing the RAG pipeline setup and operations.  
1. **Flowchart**: A detailed flowchart outlining the logic and decision-making process for handling different types of emails.  
1. **Source Code**: Complete source code of the automatic email reply system via Github

**Contact:**

For any issues or queries, feel free to contact Farhan  \+91 8910872955 on WhatsApp.

 

