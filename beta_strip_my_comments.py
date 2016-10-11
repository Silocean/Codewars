'''
Description:

Comments are the most important thing that developers use in their day to day work.

Now the question is that while displaying the code on the screen it should not display any comments.

For example:

strip_it("1 + /* 2 */3") => "1 + 3"
strip_it("var Foo = 1;// Foo declared") => "var Foo = 1;"
Write a function that takes a string and returns a string without whatever there is in the comment.

Note: comments can also be multiline and will always be presente in html format, ie: /* comment with starting and closing point */ or // comment up to the end of the line.
'''
import re
def strip_it(code):
    strip = re.sub('/\*[^/]*\*/', '', code)
    strip = re.sub('//.*', '', strip)
    return strip