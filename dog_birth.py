class Dog:
    def __init__( self ):
        #cnt = cnt + 1
        print("bow")
        self.name = "none still"
        self.pup_cnt = 0
        #pup[100]
    
    def name( self,name ):
        self.name = name

    def bow( self ):
        print( "bow" )

    def breed( self ):
        self.pup_cnt += 1

    def breed1( self, pup ):
        #self.pup[cnt] = Dog()
        self.pup_cnt += 1
        pup.append( Dog() )

    def news( self ):
        print( "my name is %s" % ( self.name ) )
        print( "the number of puppies is %d" % ( self.pup_cnt ) )

if __name__ == "__main__":

    cnt = 0
    print( "hello" )
    kelly = Dog()           #ケリーが生まれる
    kelly.name = "kelly"    #ケリーと名付ける
    kelly.breed()           #ケリーが子供を産む
    kelly.news()            #ケリーの近況は？
    member_dog = []
    member_dog.append( kelly )#ケリーをメンバに追加
    for i in range ( 100 ):
        #kelly.breed()
        #dog[i] = Dog()
        kelly.breed1( member_dog )
    kelly.news()            #ケリーの近況は？

    member_dog[50].news()   #50匹目に生まれたケリーの子供の状態    



