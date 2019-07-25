bh,js=map(int,input().split())
lisa=list(map(int,input().split()))[:bh]
ran=int(input())
sur=(sum(lisa)-lisa[js])//2
if (sur==ran):
    print("Bon Appetit")
else:
    print(abs(sur-ran))
