def create_profile(**info):
    """
    프로필 만드는 기능
    """
    print("== 프로필 정보 ===")
    for key,value in info.items():
        print(f"{key}: {value}")

create_profile(이름='김철수', 나이 = 30,직업='프로그래머',취미='독서')
print(create_profile.__doc__)
