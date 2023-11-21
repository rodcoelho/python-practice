"""
Given a string path, which is an absolute path (starting with a slash '/') to a file or 
directory in a Unix-style file system, convert it to the simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory, 
a double period '..' refers to the directory up a level, 
and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. 

For this problem, any other format of periods such as '...' are treated as file/directory names.

The canonical path should have the following format:

The path starts with a single slash '/'.
Any two directories are separated by a single slash '/'.
The path does not end with a trailing '/'.
The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
Return the simplified canonical path."""

import unittest

class Solution:
    def simplifyPath(self, path: str) -> str:
        cannonical_path = []
        normalized_path = [x for x in path.split("/") if x]
        
        for p in normalized_path:
            # print("p", p)
            if p == "..":
                try:
                    cannonical_path.pop()
                except IndexError:
                    pass
            elif p == ".":
                continue
            else:
                cannonical_path.append(p)

        return "/" + "/".join(cannonical_path) if cannonical_path else "/"
    

class TestSolution(unittest.TestCase):
    def testSimplifyPath(self):
        s = Solution()

        path = "/home/sweet/home/"
        expected = "/home/sweet/home"
        actual = s.simplifyPath(path)
        self.assertEqual(actual, expected)

        path = "/home/"
        expected = "/home"
        actual = s.simplifyPath(path)
        self.assertEqual(actual, expected)

        path = "/../"
        expected = "/"
        actual = s.simplifyPath(path)
        self.assertEqual(actual, expected)

        path = "/home//foo/"
        expected = "/home/foo"
        actual = s.simplifyPath(path)
        self.assertEqual(actual, expected)

        path = "/a/./b/../../c/"
        expected = "/c"
        actual = s.simplifyPath(path)
        self.assertEqual(actual, expected)

        path = "/a/../../b/../c//.//"
        expected = "/c"
        actual = s.simplifyPath(path)
        self.assertEqual(actual, expected)


unittest.main()