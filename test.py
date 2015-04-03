def test():
    str = "5Java"
    for i in xrange(len(str)):
        if str[i].isdigit():
            pass
        else:
            print "NUmber: ", str[:i]
            print "Skill: ", str[i:]
            break

if __name__ == "__main__":
    test()