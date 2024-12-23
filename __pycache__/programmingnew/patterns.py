class pattern:
    def psquare_num(self,n):
        for i in range(n):
            for j in range(n):
                print((i%9)+1,end=" ")
            print()
    def right_angle(self,n):
        for i in range(n):
            for j in range(n):
                if i>=j:
                  print((j%9)+1,end=" ")
                else:
                    print(" ",end=" ")
            print()
    def left_angle(self,n):
        for i in range(n):
            for j in range(n):
                if i<=j:
                    print((j%9)+1,end=" ")
                else:
                    print(" ",end=" ")
            print()
    def top_right(self,n):
        for i in range(n):
            for j in range(n):
                if i+j<=n-1:
                    print((j%9)+1,end=" ")
                else:
                    print(" ",end=" ")
            print()
    def top_left(self,n):
        for i in range(n):
            for j in range(n):
                if i+j>=n-1:
                    print((j%9)+1,end=" ")
                else:
                    print(" ",end=" ")
            print()
    def right_star(self,n):
        for i in range(n):
          for j in range(n):
             if j==0 or i==n-1 or i==j:
                print("*",end=" ")
             else:
                print(" ",end=" ")
          print()
    def tri_str_num(self,n):
        val=0
        p =True
        for i in range(n):
            for j in range(n):
                if i>=j:
                    if p:
                        print((val%9)+1,end=" ")
                        val+=1
                        p=False
                    else:
                        print("* ",end=" ")
                        p=True
                else:
                    print(" ",end=" ")
            print()
            
    def frame_str(self,n):
        for i in range(n):
            for j in range(n):
                if i==0 or i==n-2 or j==0 or j==n-1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    def x_intrev(self,n):
        for i in range(n):
          for j in range(n):
              val=(n-j-1)%9+1
              if i==j or i+j==n-1:
                 print(val,end=" ")
                 val+=1
              else:
                 print(" ",end=" ")
          print()           
    def x_str(self,n):
        for i in range(n):
          for j in range(n):
            #   val=(n-j-1)%9+1
              if i==j or i+j==n-1:
                 print("*",end=" ")
                #  val+=1
              else:
                 print(" ",end=" ")
          print()
    def x_alpharev(self,n):
        for i in range(n):
          for j in range(n):
              val=(n-j-1)%26
              if i==j or i+j==n-1:
                 print(chr(65+val),end=" ")
                 val+=1
              else:
                 print(" ",end=" ")
          print()
    def x_alpha(self,n):
        for i in range(n):
          for j in range(n):
              val=(j%26)
              if i==j or i+j==n-1:
                 print(chr(65+val),end=" ")
                 val+=1
              else:
                 print(" ",end=" ")
          print()
    def x_int(self,n):
          for i in range(n):
            for j in range(n):
               val=(j%9)
               if i==j or i+j==n-1:
                   print(val+1,end=" ")
                   val+=1
               else:
                  print(" ",end=" ")
            print()
    def right_alpha(self,n):
        for i in range(n):
            for j in range(n):
                if i>=j:
                  print((chr(65+i%26)),end=" ")
                else:
                    print(" ",end=" ")
            print()
    def right_ABC(self,n):
           for i in range(n):
            for j in range(n):
                if i>=j:
                  print((chr(65+j%26)),end=" ")
                else:
                    print(" ",end=" ")
            print()
    def left_ABC(self,n):
           for i in range(n):
            for j in range(n):
                if i<=j:
                  print((chr(65+j%26)),end=" ")
                else:
                    print(" ",end=" ")
            print()
    def left_ABC_row(self,n):
           for i in range(n):
            for j in range(n):
                if i<=j:
                  print((chr(65+i%26)),end=" ")
                else:
                    print(" ",end=" ")
            print()
    def left_ABC_order(self,n):
           for i in range(n):
            for j in range(n):
               if i==j:
                  print((chr(65+j%26)),end=" ")
                  
               else:
                    print(" ",end=" ")
            print()
    
pat=pattern()
pat.psquare_num(5)
pat.right_angle(5)
pat.left_angle(5)
pat.top_right(5)
pat.top_left(5)
pat.right_star(5)
pat.tri_str_num(5)
pat.frame_str(5)
pat.x_str(5)
pat.x_intrev(5)
pat.x_alpharev(5)
pat.x_alpha(5)
pat.x_int(5)
pat.right_alpha(5)
pat.right_ABC(5)
pat.left_ABC(5)
pat.left_ABC_row(5)
pat.left_ABC_order(5)



