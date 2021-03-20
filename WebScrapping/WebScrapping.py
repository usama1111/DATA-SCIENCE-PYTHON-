#!/usr/bin/env python
# coding: utf-8

# In[90]:


from urllib.request import urlopen 


# In[91]:


from bs4 import BeautifulSoup


# In[92]:


url_to_scrape = 'https://planetdesert.com/collections/cactus'


# In[93]:


request_page = urlopen(url_to_scrape)


# In[94]:


page_html = request_page.read()


# In[95]:


request_page.close()


# In[96]:


html_soup = BeautifulSoup(page_html , 'html.parser')


# In[97]:


cactus_items = html_soup.find_all('div', class_="grid-product__content")
filename = 'Desktop/products.csv'
f= open(filename,'w')
headers = 'Title, Price, Images  \n'
f.write(headers)


# In[98]:


for cactus in cactus_items:
    title = cactus.find('div', class_="grid-product__title").text
    price = cactus.find('div',class_="grid-product__price").text
    
    f.write(title + ',' + price)
f.close()


# In[ ]:




