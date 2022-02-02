rangee = input("from where to where\n")
s = rangee.split(":")
length = (int(s[0]),int(s[1]))
what = length[1]
quiz = int(input(">>>\n"))
def solve(result):
        tech=0
        while result!=tech:
                if result>tech:
                        
                        tech+=(what-tech)//2
                        print(f"Ohh It's not {tech} I'm sorry\n")
                elif tech>result:
                        tech//=2
                        print(f"Ohh It's not {tech} I'm sorry\n")
        print(f"\n\nHAHAHAHAHA SOLVED ITTT!!\nIt's {tech} :)")
                
solve(quiz)
