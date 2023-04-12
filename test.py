def log(h, **kws):
    sum=0
    for key,val in kws.items():
        print(kws[key])

print(log(4, a=5, b=6, log="logesh"))
