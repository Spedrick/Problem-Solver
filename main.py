import wolframalpha
    
app_id = input("Enter your api_id:-")

i=0
while i==0:
    # Taking input from user 
    question = input("Question: ")
    question = question.lower()
    if "who is" in question:
        question = question.replace("who is")
    elif "what is" in question:
        question = question.replace("what is") 
    
    if 'exit' in question:
        break
    
    # Instance of wolf ram alpha  
    # client class 
    client = wolframalpha.Client(app_id) 
    # Stores the response from  
    # wolf ram alpha 
    res = client.query(question) 
    # Includes only text from the response 
    answer = next(res.results).text
    print(answer)
print("Good Bye!!!")
