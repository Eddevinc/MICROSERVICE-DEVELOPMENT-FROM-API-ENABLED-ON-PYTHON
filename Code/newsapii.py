import requests
import json

def News():
    #query to get the topic & complete the api url
    #query=input("Enter the topic: \n")
    main_url = "https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=b68ab2bbce7c4bca9602527a280ba533"
    open_news_page = requests.get(main_url).json()
    # getting all articles in a string article 
    article = open_news_page["articles"]

    # empty list which will  contain all trending news and the dictionary 
    results = []
    tn={}   
    
    # append the headlines into the list results
    for ar in article:
            results.append(ar["title"])
    # enter the results list to tn dictionary and jason dump it into tnews variable
    tn['headlines']=results
    tnews=json.dumps(tn)
    
    #return tnews variable to the function call 
    return(tnews)
    

# Driver Code https://www.onlinegdb.com/online_python_compiler#tab-stdin
if __name__ == '__main__':
    
    # function call 
 t= News()
 print(t)