class OMG : 
    def print() :
        print("Oh my god")

mystock = OMG() 
mystock.print()    

# OMG안에 print()의 인자가 없기 때문에 오류 발생
# mystock.print() = OMG.print(mystock)
# def print(self)를 사용하면 "Oh my god" 출력