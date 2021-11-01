#455. Assign Cookies (Easy)
class Solution:
#self is point this class(Solution), hungery_level and cookies_size is from outside not included in Class(Solution)
 def findContentChildren(self,hungery_level, cookies_size):
    """
    :param cookies_size:
    :param hungery_level:
    :rtype: int
    """
    hungery_level.sort()
    cookies_size.sort()
    hungery = 0
    cookies = 0
    for child in hungery_level:
        while hungery < len(cookies_size) and cookies_size[cookies] < child:
            hungery += 1
        if hungery < len(cookies_size) and cookies_size[hungery] >= child:
            cookies += 1
            hungery += 1
    return cookies

a1 = [1,2]
a2 = [1,2,3]
#Create a instance from Solution
anwser = Solution()
print(anwser.findContentChildren(a1,a2))