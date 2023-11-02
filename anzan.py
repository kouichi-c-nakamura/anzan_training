#TODO Keep the record for the pair of numbers
#TODO rows 1 to 99, cols 1 to 99
#TODO tables for success, failures, and rates
#TODO use pandas


from random import randint
import datetime
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import os

problems = []
results = []
elapsed_time = []
failed = []
# failed = [{'a':15, 'b':11}, {'a':96, 'b':95},  {'a':76, 'b':35},  {'a':16, 'b':77}]#TODO


plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False
plt.rcParams['font.family'] = ['Arial']

cwd = os.getcwd()
excel_path = os.path.join(cwd,'anzan_log.xlsx')
if os.path.isfile(excel_path):
    ...
    df_s = pd.read_excel(excel_path, sheet_name='successes')
    df_f = pd.read_excel(excel_path, sheet_name='failures')
    df_r = pd.read_excel(excel_path, sheet_name='rates')
    df_t = pd.read_excel(excel_path, sheet_name='time')

else:
    df_s = pd.DataFrame(0, index=range(1, 100), columns=range(1, 100))
    df_f = pd.DataFrame(0, index=range(1, 100), columns=range(1, 100))
    df_r = pd.DataFrame(0, index=range(1, 100), columns=range(1, 100))
    df_t = pd.DataFrame(0, index=range(1, 100), columns=range(1, 100))

time_out_s = 20 # inclusive, elapsed time must be <= time_out_s

failed_ind = 0
    
def show_problem(a, b, view):

    if view == 1:
        print(f"\n{a} x {b} =\n")
    elif view == 2:
        print(f"\n  {a:>2} \nx {b:>2}\n-----\n")   

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
        problems.append({'a':a,'b':b})

        keep_going = True
        try:
            ans = int(ans)
        except Exception as e:
            print('wrong input')
            results.append(float("nan"))
            return keep_going
        td = dt2 - dt1
        minutes, seconds = divmod(td.total_seconds(), 60)
        print(f"\n{minutes} min {seconds} sec\n")
        elapsed_time.append(td.total_seconds())

        if td.total_seconds() <= time_out_s :
            if ans == a * b:
                print(f"Correct! :)\n{a} x {b} = {a *b}\n")
                results.append(1)
                if reviewing:
                    failed.pop(failed_ind) # remove successful item from failed during review process

            else:
                print("\a") # didn't work
                print(f"Your answer {ans} is wrong:(\n{a} x {b} = {a *b}\n")
                results.append(0)
                failed.append({'a':a,'b':b})
        else:
            print("\a") # didn't work
            print('Too late')
            if ans == a * b:
                print(f"Correct! :)\n{a} x {b} = {a *b}\n")
            else:
                print(f"Your answer {ans} is wrong:(\n{a} x {b} = {a *b}\n")
            results.append(0)
            failed.append({'a':a,'b':b})

    return keep_going


def plot_time():
    plt.ion()
    fig, ax = plt.subplots(1,1)

    zipped = list(zip(elapsed_time, problems, results))
    zipped_sorted = sorted(zipped, key=lambda x: x[0])
    elapsed_time_sorted, problems_sorted, results_sorted = zip(*zipped_sorted)

    for i in range(0, len(elapsed_time_sorted)):
        if results_sorted[i]:
            ax.plot(elapsed_time_sorted[i], i + 1, 'ok')
        else:
            ax.plot(elapsed_time_sorted[i], i + 1, 'xr')
    ax.set_yticks([i + 1 for i in list(range(0, len(elapsed_time_sorted)))]) # +1
    ax.set_xlabel('Time (s)')
    xlim = ax.get_xlim()
    ax.set_xlim(0, xlim[1])

    problems_str =[f"{p['a']} x {p['b']}" for p in problems_sorted]
    print(f"len(elapsed_time_sorted) = {len(elapsed_time_sorted)}")
    print(f"len(problems_str) = {len(problems_str)}")
    ax.set_yticklabels(problems_str) 
    
    plt.show()    

def save_result_table():
    ## response time
    problems_ = problems
    # Ensure 'a' is always <= 'b'
    for p in problems_:
        if p['a'] > p['b']:
            p['a'], p['b'] = p['b'], p['a']

    combined = sorted(zip(problems_, elapsed_time), key=lambda x: (x[0]['a'], x[0]['b']))
    problems_sorted, elapsed_time_sorted = zip(*combined)

    for idx, p in enumerate(problems_sorted):
        row_idx, col_idx = p['a'], p['b']

        # Calculate new average

        n = df_s.at[row_idx, col_idx] + df_f.at[row_idx, col_idx]
        current_total_time = df_t.at[row_idx, col_idx] * n
        new_total_time = current_total_time + elapsed_time_sorted[idx]

        # Update df_t and df_n
        df_t.at[row_idx, col_idx] = new_total_time / (n + 1)

    ##successes and failures
    # separate successes and failures
    successful_problems = [problem for problem, result in zip(problems, results) if result == 1]
    failed_problems = [problem for problem, result in zip(problems, results) if result == 0]

    # make a <= b
    for p in successful_problems:
        if p['a'] > p['b']:
            p['a'], p['b'] = p['b'], p['a']

    for p in failed_problems:
        if p['a'] > p['b']:
            p['a'], p['b'] = p['b'], p['a']

    # sort (a, b) pairs
    successful_problems = sorted(successful_problems, key=lambda x: (x['a'], x['b']))
    failed_problems = sorted(failed_problems, key=lambda x: (x['a'], x['b']))

    # update values of cells
    for p in successful_problems:
        ...
        if pd.isna(df_s.at[p['a'], p['b']]):
            df_s.at[p['a'], p['b']] = 1
        else:
            df_s.at[p['a'], p['b']] += 1

    # recompute rates
    total_sum = df_s.fillna(0).sum().sum() + df_f.fillna(0).sum().sum()

    df_r = (df_s.fillna(0) + df_f.fillna(0)) / total_sum

       
    ## save tables
    with pd.ExcelWriter(excel_path) as writer:
        df_s.to_excel(writer, sheet_name='successes')
        df_f.to_excel(writer, sheet_name='failures')
        df_r.to_excel(writer, sheet_name='rates')
        df_t.to_excel(writer, sheet_name='time')

def show_results():
    print("Finished")
    if len(results) > 0:
        print(f"Success rate: {sum(results)/len(results) * 100:.1f} % ({sum(results)}/{len(results)})")

        ave_time = sum(elapsed_time) / len(elapsed_time) #TODO
        print(f"Average response time :{ave_time} sec\n")

        result_icons = ['X' for _ in results]
        result_icons = ''.join(['O' if r else 'X' for r, i in zip(results, result_icons)])
        print(result_icons)

        plot_time()

    failed_ =  [ f"{f['a']} x {f['b']} = {f['a'] * f['b']}" for f in failed]
    print("Failed calculations")
    print(failed_)

    save_result_table()

keep_going = True

ans = int(input("Type 1 for general, 2 for Indian, 3 for mixed\n>"))
if ans == 1:
    course = 1
elif ans == 2:
    course = 2
elif ans == 3:
    course = 3
else:
    raise ValueError("course has an invalid value")

ans = int(input("Type 1 for horizontal view, 2 for stack view\n>"))
if ans == 1:
    view = 1
elif ans == 2:
    view = 2
else:
    raise ValueError("view has an invalid value")

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
        show_results()


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
else:
    print("Good bye")
#TODO save the record as csv file and append a row
