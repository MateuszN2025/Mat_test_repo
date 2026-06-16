import w_r

table1d = []
table2d = []

@w_r
def main():
 
    # for i in range(1,101):
    #     table1d.append(i)
    #     if i % 10 == 0:
    #         table2d.append(list(table1d))
    #         table1d.clear()
    table2d = [[i for i in range(start, start + 10)] for start in range(1, 101, 10)]

    for tab in table2d:
        print(tab)
    print("------------------------------------------")
    print(f"{table2d[9][8]}")
    
main()