#!/usr/bin/env python
# coding: utf-8

# In[5]:


import re

def validate_password(pw):
    
    if len(pw) >= 6 and len(pw) <= 12 and re.match("^[A-Za-z][A-Za-z0-9._]*$", pw):
        return True
    return False

# Example usage:
# password1 = "Pass123#"  # Valid password
# password2 = "password"  # Invalid password

print(validate_password('pass1'))  # True
print(validate_password('password'))  # False


# In[ ]:





# In[ ]:





# In[ ]:




