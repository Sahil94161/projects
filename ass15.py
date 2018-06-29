# Q.1- Extract the user id, domain name and suffix from the following email addresses.
# emails = "zuck26@facebook.com" "page33@google.com"
# "jeff42@amazon.com"
# desired_output = [('zuck26', 'facebook', 'com'), ('page33', 'google', 'com'), ('jeff42', 'amazon', 'com')] Q.2- Retrieve all the words starting with ‘b’ or ‘B’ from the following text.
# text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better." Q.3- Split the following irregular sentence into words
# sentence = "A, very very; irregular_sentence"
# desired_output = "A very very irregular sentence"

#Ans-
import re
# s= "zuck26@facebook.com"
# b=   "page33@google.com"
# c="jeff42@amazon.com"
# p=re.compile(r"([a-zA-z0-9._]+)@([a-z]+)\.([a-z]+)")
# def out(user):
#     result=p.match(user)
#
#     print(result[1],"\n")
#     print(result[2], "\n")
#     print(result[3], "\n")
# out(s)
# out(b)
# out(c)
#Q.2- Retrieve all the words starting with ‘b’ or ‘B’ from the following text.
# text = ''' "Betty bought a bit of butter, But the butter was
#        "so bitter, So she bought some better butter, To make
#         the bitter butter better."'''
# p=re.compile(r"b[a-zA-z]+ ")
# result=p.finditer(text)
# for r in result:
#     print(r)
#
# p=re.compile(r"B[a-zA-z]+ ")
# result=p.finditer(text)
# for r in result:
#     print(r)
#Q.3- Split the following irregular sentence into words
#sen = "A, very very; irregular_sentence"
#desired_output = "A very very irregular sentence"
#Ans-
# p=re.compile(r'[^a-zA-Z0-9]')
# print(p.sub(' ',sen))

#OPTIONAL QUESTION

# Q.1- Clean up the following tweet so that it contains
# only the user’s message. That is, remove all URLs,
# hashtags, mentions, punctuations, RTs and CCs.
#tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
#desired_output = 'Good advice What I would do differently
# if I was learning to code today'
#Ans-
# p=re.compile(r"(.+) RT (.+): (.+) http:(.+)")
# res=p.findall(tweet)
# print(res[0][0],res[0][2])
