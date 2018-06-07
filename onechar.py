st1,st2=str(raw_input()).split()
if len(st1) == len(st2):
    count_diffs = 0
    for a, b in zip(st1, st2):
        if a!=b:
            if count_diffs:
            	print("no")
            count_diffs += 1
            print("yes")
