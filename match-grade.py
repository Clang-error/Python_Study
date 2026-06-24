grade = 'B'

match grade:
    case 'A':
        print("탁월함")
    case 'B':
        print("우수함")
    case 'C':
        print("보통임")
    case _:
        print("노력좀해라")