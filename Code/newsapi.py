import requests
import json

def News():
    main_url = "https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=b68ab2bbce7c4bca9602527a280ba533"
    open_news_page = requests.get(main_url).json()
    # getting all articles in a string article 
    article = open_news_page["articles"]

    # empty list which will  contain all trending news 
    results = []
   

    for ar in article:
            results.append(ar["title"])
            tn={}
    for i in range(len(results)):

            # printing all trending news 
           # print(i + 1, results[i])
            tn[i]=results[i]
    #print(tn)
    t=json.dumps(tn)
   # print(t)
    return(t)
    

# Driver Code 
if __name__ == '__main__':
    
    # function call 
 t= News()
 print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')
 print(t)
   