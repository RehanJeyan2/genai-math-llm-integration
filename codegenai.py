#!/usr/bin/env python
# coding: utf-8

# In[9]:


import math
import os
import openai
openai.api_key = os.environ['OPENAI_API_KEY']


def calculate_volume_cylinder(radius,height):
    if radius < 1 or height <1:
        return "enter proper values"
    vol = 3.14 * radius * radius * height
    return round(vol,2)


functions = [
            {
                "name": "calculate_volume_cylinder",
                "description": "To find the volume of a cylinder",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "radius": {"type": "number", "description": "The radius of the cylinder"},
                        "height": {"type": "number", "description": "The height of the cylinder"}
                    },
                    "required": ["radius", "height"]
                }
            }
        ]

def chat_with_openai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        functions = functions,
        function_call = "auto"
    )
    if "function_call" in response["choices"][0]["message"]:
        function_name = response["choices"][0]["message"]["function_call"]["name"]
        arguments = eval(response["choices"][0]["message"]["function_call"]["arguments"])
        if function_name == "calculate_volume_cylinder":
            radius = arguments["radius"]
            height = arguments["height"]
            return calculate_volume_cylinder(radius, height)
                                             
    return response["choices"][0]["message"]["content"]
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

prompt = f"What is the volume of a cylinder with a radius of {radius} and a height of {height}?"
messages=[
            {"role": "system", "content": "You are an assistant that helps calculate the volume of a cylinder."},
            {"role": "user", "content": prompt},
        ]

result = chat_with_openai(prompt)
print("Result:", result)


# In[ ]:





# In[ ]:




