class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        str_x = str(x)
        lst = list(str_x)
        lst.reverse()
        str_palid = ''.join(lst)
        return str(x) == str_palid
        