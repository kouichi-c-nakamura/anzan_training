#TODO practice mode for the ones that required 10+, or 20+ s previously
#TODO prorgam to train two digits additions and subtractions
from random import random
from random import randint
import datetime
from matplotlib import pyplot as plt
import pandas as pd
# import numpy as np
import os
import mplcursors # need to install: pip install mplcursors

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
    df_s = pd.read_excel(excel_path, index_col=0, sheet_name='successes')
    df_f = pd.read_excel(excel_path, index_col=0, sheet_name='failures')
    df_r = pd.read_excel(excel_path, index_col=0, sheet_name='rates').astype(float) #float
    df_t = pd.read_excel(excel_path, index_col=0, sheet_name='time').astype(float) #float

else:
    df_s = pd.DataFrame(0, index=range(1, 100), columns=range(1, 100))
    df_f = pd.DataFrame(0, index=range(1, 100), columns=range(1, 100))
    df_r = pd.DataFrame(float(0), index=range(1, 100), columns=range(1, 100)).astype(float)
    df_t = pd.DataFrame(float(0), index=range(1, 100), columns=range(1, 100)).astype(float)

time_out_s = 20 # inclusive, elapsed time must be <= time_out_s

failed_ind = 0

failed_in_the_past = []
for row_index, row in df_f.iterrows():
    for col_index, value in row.items():
        if value != 0:
            failed_in_the_past.append({'a': row_index, 'b': col_index})
    
def show_problem(a, b, view):

    if view == 1:
        print(f"\n{a} x {b} =\n")
    elif view == 2:
        if course == 6:
            print(f"\n  {a:>3} \nx {b:>3}\n-----\n")   
        else:
            print(f"\n  {a:>2} \nx {b:>2}\n-----\n")   

def biased_randint(min_val, max_val, bias=0.5):
    """Generate a biased random integer between min_val and max_val.

    With a bias value of 0.5, numbers towards the higher end (like 6,7,8,9 in tens place)
    will be more probable. Adjusting the bias will change the skewness. A bias of 1 will 
    give you a uniform distribution, values less than 1 will skew towards the maximum, 
    and values greater than 1 will skew towards the minimum.
    """
    return int(min_val + (max_val - min_val) * (random() ** bias))

def get_ab_from_failures():
    if len(failed) == 0:
        return 0, 0
    
    failed_ind = randint(0, len(failed)-1)
    a = failed[failed_ind]['a']
    b = failed[failed_ind]['b']
    return a, b

def get_ab_from_failures_in_the_past():
    # randomly choose a and b from the failures in the past
    # Iterate over the DataFrame to find non-zero cells

    ind = randint(0, len(failed_in_the_past)-1)

    if randint(0,1):
        a = failed_in_the_past[ind]['a']
        b = failed_in_the_past[ind]['b']
    else:
        a = failed_in_the_past[ind]['b']
        b = failed_in_the_past[ind]['a']

    return a, b

def get_ab_general():
    # a = randint(1,99)
    a = biased_randint(1,99,randbias)
    # b = randint(1,99)
    b = biased_randint(1,99,randbias)

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
def get_ab_two_by_one():
    tf = randint(0,1)
    if tf:
        a = randint(1,9)
        b = randint(1,99)
    else:
        a = randint(1,99)
        b = randint(1,9)
    return a, b

def get_ab_three_by_one():
    if view == 2:
        a = randint(100,999)
        b = randint(1,9)        
    else:
        tf = randint(0,1)
        if tf:
            a = randint(1,9)
            b = randint(100,999)
        else:
            a = randint(100,999)
            b = randint(1,9)
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


def plot_time(elapsed_time, problems, results):
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
    plt.title("Session")
    
    plt.show()

def plot_all():
    # read the latest data
    df_s = pd.read_excel(excel_path, index_col=0, sheet_name='successes')
    df_f = pd.read_excel(excel_path, index_col=0, sheet_name='failures')
    df_r = pd.read_excel(excel_path, index_col=0, sheet_name='rates').astype(float)
    df_t = pd.read_excel(excel_path, index_col=0, sheet_name='time').astype(float)

    # create lists
    res_all = []
    for i in range(1,100):
        for j in range(1,100):
            if df_s[i][j] + df_f[i][j] > 0: # remove the empty cells #TODO KeyError: 99
                res_all.append({'a':i, 'b':j, 'n':df_s[i][j] + df_f[i][j], 
                            's':df_s[i][j], 'f':df_f[i][j], 
                            'r':df_r[i][j], 't':df_t[i][j]})

    # sort l_all
    res_sorted = sorted(res_all, key=lambda x: x['t'])

    # read the saved table data and plot them
    plt.ion()
    fig, ax = plt.subplots(1,1)

    max_val = max(item['r'] for item in res_sorted)
    min_val = min(item['r'] for item in res_sorted)
    norm = plt.Normalize(min_val, max_val)

    # Choose a colormap
    colormap = plt.cm.cool_r

    x_values = [item['t'] for item in res_sorted]
    y_values = list(range(1, len(res_sorted) + 1))
    colors = colormap(norm([r['r'] for r in res_sorted]))

    # Create a single scatter plot with all points
    sc = ax.scatter(x_values, y_values, color=colors, s=100)

    tooltips = [f"{r['a']} \u00D7 {r['b']}\n" + 
                f"{r['r']*100} % ({r['s']} of {r['s'] + r['f']})\n" + 
                f"{r['t']:.1f} sec" for r in res_sorted]

    def update_annot(ind):
        return tooltips[ind]
    
    def on_hover(sel):
        sel.annotation.set_text(update_annot(sel.index))

    mplcursors.cursor(sc, hover=True).connect("add", on_hover)

    ax.set_xlabel('Time (s)')
    xlim = ax.get_xlim()
    ax.set_xlim(0, xlim[1])
    plt.title("History")
    
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
        df_t.at[row_idx, col_idx] = new_total_time / float(n + 1)

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
        if pd.isna(df_s.at[p['a'], p['b']]): # if for the first time
            df_s.at[p['a'], p['b']] = 1
        else:
            df_s.at[p['a'], p['b']] += 1
    
    for p in failed_problems:
        if pd.isna(df_f.at[p['a'], p['b']]): # if for the first time
            df_f.at[p['a'], p['b']] = 1
        else:
            df_f.at[p['a'], p['b']] += 1

    # recompute rates
    df_r = df_s.fillna(0)  / (df_s.fillna(0) + df_f.fillna(0))

       
    ## save tables
    with pd.ExcelWriter(excel_path) as writer:
        df_s.to_excel(writer, index=True, sheet_name='successes')
        df_f.to_excel(writer, index=True, sheet_name='failures')
        df_r.to_excel(writer, index=True, sheet_name='rates')
        df_t.to_excel(writer, index=True, sheet_name='time')

def show_results():
    print("Finished")
    if len(results) > 0:
        print(f"Success rate: {sum(results)/len(results) * 100:.1f} % ({sum(results)}/{len(results)})")

        ave_time = sum(elapsed_time) / len(elapsed_time) #TODO
        print(f"Average response time :{ave_time} sec\n")

        result_icons = ['X' for _ in results]
        result_icons = ''.join(['O' if r else 'X' for r, i in zip(results, result_icons)])
        print(result_icons)
        
        plot_time(elapsed_time, problems, results)

    failed_ =  [ f"{f['a']} x {f['b']} = {f['a'] * f['b']}" for f in failed]
    print("Failed calculations")
    print(failed_)

    if course != 6:
        save_result_table()
        plot_all()
        

keep_going = True

#TODO GUI for preference?
ans = int(input("Type 1 for general, 2 for Indian, 3 for mixed, 4 for 00 x 0, 5 for review, 6 for 000 x 0\n>"))
if ans == 1:
    course = 1
elif ans == 2:
    course = 2
elif ans == 3:
    course = 3
elif ans == 4:
    course = 4
elif ans == 5:
    course = 5
elif ans == 6:
    course = 6
else:
    raise ValueError("course has an invalid value")

ans = int(input("Type 1 for horizontal view, 2 for stack view\n>"))
if ans == 1:
    view = 1
elif ans == 2:
    view = 2
else:
    raise ValueError("view has an invalid value")

#TODO ask if you want to use biased random number generation
if course != 4 and course != 5 and course != 6:
    ans = float(input("Type 1 for uniform randomness, <1 for biased to have larger digits\n>"))
    if ans == 1:
        randbias = 1
    else:#
        randbias = 2 # to be biased to include larger numbers, 6,7 ,8, 9



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
    elif course == 4:
        a, b = get_ab_two_by_one()
    elif course == 5:
        a, b = get_ab_from_failures_in_the_past()
    elif course == 6:
        a, b = get_ab_three_by_one()

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

            ave_time = sum(elapsed_time) / len(elapsed_time)
            print(f"Average response time :{ave_time} sec\n")

            failed_ =  [ f"{f['a']} x {f['b']} = {f['a'] * f['b']}" for f in failed]
            print("Failed calculations")
            print(failed_)
else:
    print("Good bye")
