# Email Handling System Documentation

## Overview
This Python script is designed to classify incoming emails into specific categories and route them for appropriate handling. The system utilizes natural language processing (NLP) and a defined workflow to process and respond to emails efficiently. 

## Workflow
The workflow consists of the following primary steps:
1. **Categorize Email**: Identify the category of the incoming email.
2. **Route Email**: Based on the category, route the email to the appropriate handling function.
3. **Generate Response**: Create and send an appropriate response based on the category and content of the email.

## Functions

### `categorize_email(initial_email: str) -> str`
- **Description**: This function analyzes the content of the given email and categorizes it into one of the predefined categories: `availability_inquiry`, `customer_review`, `product_enquiry`, or `off_topic`.
- **Parameters**:
  - `initial_email` (str): The content of the incoming email.
- **Returns**: 
  - `category` (str): The category of the email.

### `get_items()`
- **Description**: This function retrieves items related to the inquiry email. 
- **Parameters**: None
- **Returns**: None

### `sentiment_email()`
- **Description**: This function performs sentiment analysis on the email content.
- **Parameters**: None
- **Returns**: None

### `question_handling()`
- **Description**: This function handles emails categorized as containing questions.
- **Parameters**: None
- **Returns**: None

### `Cs_email()`
- **Description**: This function handles customer service-related emails.
- **Parameters**: None
- **Returns**: None

### `inquery_email()`
- **Description**: This function handles inquiry emails.
- **Parameters**: None
- **Returns**: None

### `review_email()`
- **Description**: This function handles review emails.
- **Parameters**: None
- **Returns**: None

### `write_rag_email()`
- **Description**: This function generates responses for emails requiring detailed answers.
- **Parameters**: None
- **Returns**: None

## Workflow Configuration

### StateGraph Initialization
- The workflow is initialized using a `StateGraph` object. Each node represents a function, and edges define the transitions between these functions based on conditions.

```python
workflow = StateGraph(GraphState)

# Define the nodes
workflow.add_node("categorize_email", categorize_email)
workflow.add_node("get_items", get_items)
workflow.add_node("sentiment_email", sentiment_email)
workflow.add_node("question_handling", question_handling)
workflow.add_node("Cs_email", Cs_email)
workflow.add_node("inquery_email", inquery_email)
workflow.add_node("review_email", review_email)
workflow.add_node("write_rag_email", write_rag_email)
```
- Setting Entry Point
The entry point for the workflow is set to categorize_email.
```python
workflow.set_entry_point("categorize_email")
```
- Adding Conditional Edges
Conditional edges determine the next step based on the email category.
```python
workflow.add_conditional_edges(
    "categorize_email",
    category_seperator,
    {
        "get_items_": "get_items",
        "sentment_email_": "sentiment_email",
        "question_handling_": "question_handling",
        "cs_email_": "Cs_email",
    },
)
workflow.add_edge("get_items", "inquery_email")
workflow.add_edge("sentiment_email", "review_email")
workflow.add_edge("review_email", "Cs_email")
workflow.add_edge("question_handling", "write_rag_email")
workflow.add_edge("inquery_email", END)
workflow.add_edge("Cs_email", END)
workflow.add_edge("write_rag_email", END)
```
- Compiling and Running the Workflow
The workflow is compiled and executed with the given email input.
```python
app = workflow.compile()

EMAIL = """Your email content here"""

inputs = {"initial_email": EMAIL, "num_steps":0}
for output in app.stream(inputs):
    for key, value in output.items():
        pprint(f"Finished running: {key}:")

output = app.invoke(inputs)

print(output)

if output['final_email']:
    print(output['final_email'])
if output['CS_email']:
    print(output['CS_email'])
```
## Final Output
The final output consists of the processed email responses based on the initial email content and its categorized handling.
