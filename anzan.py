from random import randint
import datetime

results = []
elapsed_time = []
failed = []

failed = [{'a':57, 'b':40}, {'a':92, 'b':56},  {'a':79, 'b':53},  {'a':96, 'b':78}]#TODO

failed_ind = 0
    
def show_problem(a, b, view):

    if view == 1:
        print(f"\n{a} x {b} =\n")
    elif view == 2:
        print(f"\n  {a:02} \nx {b:02}\n-----\n")   

def get_ab_from_failures():
    if len(failed) == 0:
        return 0, 0
    
    failed_ind = randint(0, len(failed)-1)
    a = failed[failed_ind]['a']
    b = failed[failed_ind]['b']
    return a, b

def get_ab_general():
    a = randint(1,99)
    b = randint(1,99)
    return a, b

def get_ab_Indian():
    c_type = randint(1,3)
    if c_type == 1:
        a_ = randint(1,9)
        b_ = randint(1,9)
        c_ = 10 - b_

        a = a_ * 10 + b_ 
        b = a_ * 10 + c_ 

    elif c_type == 2:
        a_ = randint(1,9)
        b_ = randint(1,9)
        c_ = randint(1,9)

        a = a_ * 10 + b_ 
        b = a_ * 10 + c_        

    elif c_type == 3:
        a_ = randint(1,9)
        b_ = randint(1,9)
        c_ = 10 - b_

        a = b_ * 10 + a_ 
        b = c_ * 10 + a_     
    return a, b

def run_trial(a, b):

    dt1 = datetime.datetime.now()

    show_problem(a, b, view)
    ans = input("Type your answer (or 'q' to quit):\n>")
    dt2 = datetime.datetime.now()

    if ans == "q":
        keep_going = False
    else:
        keep_going = True
        try:
            ans = int(ans)
        except Exception as e:
            print('wrong input')
            return keep_going
        td = dt2 - dt1
        minutes, seconds = divmod(td.seconds, 60)
        print(f"\n{minutes} min {seconds} sec\n")
        elapsed_time.append(td)

        if ans == a * b:
            print(f"Correct! :)\n{a} x {b} = {a *b}\n")
            results.append(1)
            if reviewing:
                failed.pop(failed_ind) # remove successful item from failed during review process

        else:
            print(f"Your answer {ans} is wrong:(\n{a} x {b} = {a *b}\n")
            results.append(0)
            failed.append({'a':a,'b':b})

    return keep_going

keep_going = True

ans = int(input("Type 1 for general, 2 for Indian, 3 for mixed\n>"))
if ans == 1:
    course = 1
elif ans == 2:
    course = 2
elif ans == 3:
    course = 3

ans = int(input("Type 1 for horizontal view, 2 for stack view\n>"))
if ans == 1:
    view = 1
elif ans == 2:
    view = 2

reviewing = False
while keep_going:

    if course == 1:
        a, b = get_ab_general()
    elif course == 2:
        a, b = get_ab_Indian()
    elif course == 3:
        ans = randint(0,1)
        if ans:
            a, b = get_ab_general()
        else:
            a, b = get_ab_Indian()
    
    keep_going = run_trial(a, b)

    if not keep_going:
        print("Finished")
        print(f"Success rate: {sum(results)/len(results) * 100:.1f} % ({sum(results)}/{len(results)})")

        ave_time = sum(elapsed_time, datetime.timedelta(0)) / len(elapsed_time)
        print(f"Average response time :{ave_time.seconds} sec\n")

        failed_ =  [ f"{f['a']} x {f['b']} = {f['a'] * f['b']}" for f in failed]
        print("Failed calculations")
        print(failed_)

ans = input("Do you want to practice the failed problems again? Y/N\n>")


if ans == "y" or ans == "Y":
    results = [] #refresh
    reviewing = True

    keep_going = True
    while keep_going:
        a, b = get_ab_from_failures()
        if a == 0 and b == 0:
            keep_going = False
        else:
            keep_going = run_trial(a, b)
        
        if not keep_going:
            print("Finished")
            print(f"Success rate: {sum(results)/len(results) * 100:.1f} % ({sum(results)}/{len(results)})")

            ave_time = sum(elapsed_time, datetime.timedelta(0)) / len(elapsed_time)
            print(f"Average response time :{ave_time.seconds} sec\n")

            failed_ =  [ f"{f['a']} x {f['b']} = {f['a'] * f['b']}" for f in failed]
            print("Failed calculations")
            print(failed_)


#TODO save the record as csv file and append a row
