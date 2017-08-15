import json
import urllib2

response = urllib2.urlopen("https://uinames.com/api/")
content = response.read()
content_dict = json.loads(content)

first_name = content_dict['name']
surname = content_dict['surname']
gender = content_dict['gender']
region = content_dict['region']
print "My name is " + first_name + " and my surname " + surname + ". I am a " + gender + " and I am from " + region
