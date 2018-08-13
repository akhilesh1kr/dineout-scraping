from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def dineout_list(request):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
        response = requests.get("https://www.dineout.co.in/bangalore-restaurants",headers=headers)


        content = response.content
        soup = BeautifulSoup(content,"html.parser")

        top_rest = soup.find_all("div",attrs={"class": "listing-cards-wrapper"})
        list_tr = top_rest[0].find_all("div",attrs={"class": "cardBg"})

        # List of restaurants
        list_rest =[]
        for tr in list_tr:
            try:
                name = (tr.find("a",attrs={"data-type": "Name"})).text.replace('\n', ' ').strip()
                location = (tr.find("a",attrs={"data-type": "Locality"})).text.replace('\n', ' ').strip() + ", " + (tr.find("a",attrs={"data-type": "Area"})).text.replace('\n', ' ').strip()
                url = (tr.find("a",attrs={"data-w-onclick":"restarant_url_click_ga|w1-restarant"}))['href']
                rating = (tr.find("a",attrs={"data-w-onclick":"reviewLinkClickHandler|w1-restarant"})).text.replace('\n', ' ').strip()
                

                # For reviews
                try:
                    review_url = "https://www.dineout.co.in"+url+"/review"
                    response2 = requests.get(review_url,headers=headers)
                    content2 = response2.content
                    soup2 = BeautifulSoup(content2,"html.parser")
                    all_reviews = soup2.find_all("div",attrs={"class": "reviews marginT0"})


                    # Extracting total number of reviews
                    num = all_reviews[0].span.text.replace('\n', ' ')
                    num = num.replace('(', '')
                    num = num.replace(')', '')
                    newnum = int(num)//10+1;
                    # print(newnum)

                    # Scraping all reviews from single page
                    review_url_new = "https://www.dineout.co.in"+url+"/review?revpage="+str(newnum)
                    response3 = requests.get(review_url_new,headers=headers)
                    content3 = response3.content
                    soup3 = BeautifulSoup(content3,"html.parser")
                    all_reviews3 = soup3.find_all("div",attrs={"class": "reviews marginT0"})

                    list_ar = all_reviews3[0].find_all("div",attrs={"class": "user-info"})
                    list_review = []
                    dataframe2 = ""
                    for tr2 in list_ar:
                        try:
                            r_name = (tr2.find("div",attrs={"class": "name"})).text.replace('\n', ' ').strip()
                            r_date = (tr2.find("span",attrs={"class": "date"})).text.replace('\n', ' ').strip()
                            r_text = (tr2.find("span",attrs={"class": "more"})).text.replace('\n', ' ').strip()
                            # dataframe2 = [r_name,r_date,r_text]
                            dataframe2 += "<strong>"+r_name+"</strong><br>"+r_date+"<br><p>"+r_text+"</p><hr>"
                        except:
                            print()
                    list_review.append(dataframe2)
                    dataframe1 = [name,location,url,rating,list_review,num]
                except:
                    dataframe1 = [name,location,url,rating, "No reviews found!"]
                print(dataframe1)
                list_rest.append(dataframe1)
            except:
                print()
    except:
        print("Problem in scraping data")

    return render(request, 'dineout/dineout_list.html', {'list_rest':list_rest})