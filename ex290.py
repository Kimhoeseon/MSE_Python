class 부모:
  def __init__(self):
    print("부모생성")  

class 자식(부모):
  def __init__(self):
    print("자식생성")    # 자식()실행 될 때 "자식생성"출력 
    super().__init__()   #부모 class에 접근하여 호출이 가능하여 "부모생성"이 출력

나 = 자식()