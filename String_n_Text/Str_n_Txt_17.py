'''
This program demonstrates how we can replace HTML and XML entities with their corrosponding text.
'''
#Approach One
'''
If you need to replace charcters like '<' or '>' it is fairly simple by using html.escape()
'''
myStr = '<h1>My First Heading</h1>'
import html
print(myStr)
print(html.escape(myStr))
