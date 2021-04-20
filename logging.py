#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install restapi-logging-handler


# In[13]:


from restapi_logging_handler import RestApiHandler


# In[14]:


import logging


# In[15]:


logger = logging.getLogger(__name__)
restapiHandler = RestApiHandler('http://my.restfulapi.com/endpoint/')
logger.addHandler(restapiHandler)
logger.setLevel(logging.INFO)
logger.info("Send this to my RESTful API")


# In[ ]:





# In[ ]:




