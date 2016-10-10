'''
Description:

Karan's company makes software that provides different features based on the version of operating system of the user.

For finding which version is more recent, Karan uses the following method:

While this function worked for OS versions 10.6, 10.7, 10.8 and 10.9, the Operating system company just released OS version 10.10.

Karan's function fails for the new version:

compareVersions ("10.9", "10.10");       // returns true, while it should return false
Karan now wants to spend some time to right a more robust version comparison function that works for any future version/sub-version updates.

Help Karan write this function. Here are a few sample cases:

It can be assumed that version strings are non empty and only contain numeric literals and the character '.'
'''
def compare_versions(version1,version2):
    #your code here
    l1 = [int(x) for x in version1.split('.')]
    l2 = [int(x) for x in version2.split('.')]
    length = max(len(l1), len(l2))
    if l1!=l2:
        for x in xrange(length-len(l1)):
            l1.append(0)
        for x in xrange(length-len(l2)):
            l2.append(0)
    return all(l1[x]-l2[x]>=0 for x in xrange(length))