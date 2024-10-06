from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import requests
from bs4 import BeautifulSoup


def scrap_product_name(request,product_name):
##        HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
    url = f"https://www.flipkart.com/search?q={product_name}"
    response = requests.get(url)

    if response.status_code == 200:
        content_response = response.content
        soup = BeautifulSoup(content_response, "html.parser")

        item_name = soup.find_all('div',class_='KzDlHZ')        
        item_mrp_price = soup.find_all('div',class_='yRaY8j ZYYwLA')
        item_offar = soup.find_all('div',class_='UkUFwK')
        item_price = soup.find_all('div',class_='Nx9bqj _4b5DiR')
        ratings_and_reviews = soup.find_all('span',class_='Wphh3N')
        delivery = soup.find_all('div',class_='yiggsN')
        item_images = soup.find_all('img',class_='DByuf4')


        product_details = []

        for name,product_mrp,product_offar,product_price,rating_and_review,product_delivery,images in zip(item_name,item_mrp_price,item_offar,item_price,ratings_and_reviews,delivery,item_images):
            item_name_text = name.text
            item_mrp_price_text = product_mrp.text
            item_offar_text = product_offar.text
            item_price_text = product_price.text
            ratings_text = rating_and_review.text
            delivery_text = product_delivery.text
            image_get = images.get('src')


            prodect_dict = {
                'product_name': item_name_text,
                'product_mrp': item_mrp_price_text,
                'product_offar': item_offar_text,
                'product_price': item_price_text,
                'product_ratings_and_reviews': ratings_text,
                'product_delivery': delivery_text,
                'product_image_url': image_get
                
            }
            
            product_dict_append_product_details = product_details.append(prodect_dict)       
        return JsonResponse(product_details[:10], safe=False)
    else:
        message = "The request to the URL was unsuccessful. Please try again."
        return HttpResponse(message)




def productscrap_amount(request,product_name,amount):
##        HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
    url = f"https://www.flipkart.com/search?q={product_name}+under+{amount}"
    response = requests.get(url)

    if response.status_code == 200:
        content_response = response.content
        soup = BeautifulSoup(content_response, "html.parser")

        item_name = soup.find_all('div',class_='KzDlHZ')        
        item_mrp_price = soup.find_all('div',class_='yRaY8j ZYYwLA')
        item_offar = soup.find_all('div',class_='UkUFwK')
        item_price = soup.find_all('div',class_='Nx9bqj _4b5DiR')
        ratings_and_reviews = soup.find_all('span',class_='Wphh3N')
        delivery = soup.find_all('div',class_='yiggsN')
        item_images = soup.find_all('img',class_='DByuf4')


        product_details = []

        for name,product_mrp,product_offar,product_price,rating_and_review,product_delivery,images in zip(item_name,item_mrp_price,item_offar,item_price,ratings_and_reviews,delivery,item_images):
            item_name_text = name.text
            item_mrp_price_text = product_mrp.text
            item_offar_text = product_offar.text
            item_price_text = product_price.text
            ratings_text = rating_and_review.text
            delivery_text = product_delivery.text
            image_get = images.get('src')


            prodect_dict = {
                'product_name': item_name_text,
                'product_mrp': item_mrp_price_text,
                'product_offar': item_offar_text,
                'product_price': item_price_text,
                'product_ratings_and_reviews': ratings_text,
                'product_delivery': delivery_text,
                'product_image_url': image_get
                
            }

            product_dict_append_product_details = product_details.append(prodect_dict)       
        return JsonResponse(product_details[:10], safe=False)

    else:
        message = "The request to the URL was unsuccessful. Please try again."
        return HttpResponse(message)

