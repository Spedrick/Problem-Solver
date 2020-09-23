import wolframalpha
    
app_id = input('Enter your api_id \n You may obtain one on the official website of Wolf ram Alpha\n api_id:-:')

i=0
while i==0:
    # Taking input from user 
    question = input("Question: ")
    question = question.lower()
    question = question.replace("in wikipedia", "search", "wikipedia", "about","on wikipedia","google","what is","who is") 
    
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
