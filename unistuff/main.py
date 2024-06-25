import pyperclip, wolframalpha, time
from termcolor import cprint
from scipy.optimize import minimize
import numpy as np
import math

with open('env.txt', "r") as f:
    secret = f.readline().strip()
client = wolframalpha.Client(secret)


def bargaining_game_standard(u1: str, u2: str):
    """
    Consider the bargaining problem of splitting a pie of size 1 with utility u(x) for player 1 and v(y) for player 2.
    x and y are the shares of the pie for the two players. If players don’t agree, they obtain no pie.
    """
    query = f'N[max( {u1} * ( {u2.replace("y", "(1-x)")} ) )]'
    # print(query)
    result = client.query(query)
    for pod in result.pods:
        for sub in pod.subpods:
            ctext = sub.plaintext
            
            if ctext and "at x" in ctext and "max{" in ctext:
                cprint(ctext, "light_green")
                x = float(ctext.split("≈")[-1].strip())
                y = 1-x
            else:
                print(ctext)
    cprint(f"x = {x}\ny = {y}", "light_green")


def symmetric_asymmetric_nash_bargaining_solution(const, d, u1, u2, frac1, frac2):
    """
    Args: ("9x1+8x2≤39", (0,0), "x_1", "x_2", "2/3", "1/3")
    Determine first the (symmetric) Nash bargaining solution, i.e.
    Next consider the asymmetric Nash bargaining solution.
    """
    cprint("Symmetric solution:")
    query = const.replace("x1", "x_1").replace("x2", "x_2").replace("≤", "=")
    print(query); pyperclip.copy(query)
    try :
        result = client.query(query)
        for pod in result.pods:
            for sub in pod.subpods:
                ctext = sub.plaintext
                if ctext and "x_1 = " in ctext:
                    cprint(ctext)
                    x_1 = ctext.split("=")[-1].strip()
    except:
        x_1 = input("Enter x_1:\n")
            
    # cprint(f'x_1 = {eval(x_1)}', "light_green")
    query = f'N[max( ({u2}-{d[0]}) * ( ({u1.replace("x_1", x_1)} ) - {d[1]} ))]'
    print(query); pyperclip.copy(query)
    try:
        result = client.query(query)
        for pod in result.pods:
            for sub in pod.subpods:
                ctext = sub.plaintext
                if ctext and "at x_2" in ctext:
                    cprint(ctext, "blue")
                    x_2 = ctext.split("=")[-1].strip()
    except:
        x_2 = input("Enter x_2:\n")

    query = f'N[x_1 = {x_1.replace("x_2", x_2)}]'
    print(query); pyperclip.copy(query)
    try:
        result = client.query(query)
        for pod in result.pods:
            for sub in pod.subpods:
                ctext = sub.plaintext
                cprint(ctext)
                if ctext and "x_1 = " in ctext:
                    x_1a = ctext.split('x_1 = ')[-1].strip()
    except:
        cprint('Enter query yourself')

    cprint(f"x_1 = {eval(x_1a)}", "light_green")
    cprint(f"x_2 = {eval(x_2)}", "light_green")



    cprint("Asymmetric solution:")
    query = f'max( ( ({u2} - {d[0]})^({frac2}) ) * ( ({u1.replace("x_1", x_1)} ) - {d[1]} )^({frac1}) )'
    cprint(query); pyperclip.copy(query)

    
    try:
        cprint(f'x_1: {x_1}')
        result = client.query(query)
        for pod in result.pods:
            for sub in pod.subpods:
                ctext = sub.plaintext
                if ctext and "x_2 = " in ctext:
                    cprint(ctext, 'blue')
                    x_2value = eval(ctext.split('= ')[-1].strip())
                else:
                    cprint(ctext)
    except:
        x_2value = float(input("Enter x_2 value\n").strip())

    x_1value = x_1.replace("x_2", " * " + str(x_2value)).replace("(", " * (")
    cprint(x_1value)
    cprint(f'x_1: {eval(x_1value)}', 'light_green')
    cprint(f'x_2: {x_2value}', 'light_green')



def ultimatum_bargaining_game(fees, settlement):
    """
    Consider the following conflict among tenant and landlord about a deposit: When the rental agreement starts, the tenant leaves a deposit of 63 with the landlord. On termination of the rental agreement, the landlord returns y. The returned amount y is either the full deposit or a fraction: y ∈
    [0, 63]. The tenant can accept or refuse the landlord’s oﬀer of y. If the tenant refuses, then the tenant goes to court. In this case the tenant bears a non-refundable cost of 13 (litigation fees). The court then settles the case, i.e. decides that the landlord must return the amount of 21 to the tenant. Both parties, the landlord and the tenant, know that the court always awards the tenant 21, i.e. both know how the court will settle the case
    """
    d2 = settlement - fees
    cprint(f'a)\nIf the offer is greater or equal {d2} (Condition for tenant) and\nLess or equal to {settlement} (Landlord condition) its a nash equilbrium')

    cprint(f'b)\nIf the offer is equal to {d2} its a SPE')


def three_player_pie_division(total, d):
    maxd = max(d)
    d = [maxd - value for value in d]
    # print(f'23 = a + b + c')
    for idx, player in enumerate(d):
        print(f'player {idx+1}: {((total + sum(d)) / 3) - player}')


def bargaining_cost_of_delay(c1, c2):
    if eval(c1) < eval(c2):
        cprint(f'Since the delay-factor is bigger for player 2: (1, 0) in round 1')
    elif eval(c2) < eval(c1):
        cprint(f'Since the delay-factor is bigger for player 1: ({eval(c2)}, {1-eval(c2)}) in round 1')
    else:
        cprint(f'Since the delay-factor is the same: Standard bargaining game => Solve with other function')


def kalai_smorodinsky(d, b, total):
    cprint(f'Nash bargaining solution')
    query = f'N[ max( (x_1 - {d[0]} ) = ({total} - x_1 - {d[1]}) ) ]'
    print(query)
    result = client.query(query)
    end = False
    for pod in result.pods:
        for sub in pod.subpods:
            ctext = sub.plaintext
            if ctext and "x_1 =" in ctext:
                cprint(ctext, "light_green")
                x_1 = int(ctext.split("= ")[-1])
                cprint(f"x_2 = {total - x_1}", "light_green")
                end = True
                break
        if end:
            break

    cprint(f'Kalai Smorodinsky bargaining solution')
    query = f'N[ ( (x_1 - {d[0]})/({b[0]-d[0]}) ) = ( (({total} - x_1) - {d[1]})/({b[1]-d[1]}) ) ]'
    print(query)
    result = client.query(query)
    for pod in result.pods:
        for sub in pod.subpods:
            ctext = sub.plaintext
            if ctext and "x_1 =" in ctext:
                cprint(ctext, "light_green")
                x_1 = eval(ctext.split("= ")[-1])
                cprint(f"x_2 = {total - x_1}", "light_green")
                return


def outside_option(outside: str, d1, d2):
    """
    Different from the standard model, we consider the case where player 2 can choose an outside option after player 1 has made an offer and that offer was rejected by player 2.
    If player 2 chooses the outside option, player 2 obtains b=47
    and player 1 obtains nothing
    """
    cprint(f'Make sure that player 2 is the one with the outside option')
    d1 = eval(d1)
    d2 = eval(d2)
    x_1 = (1-d2) / (1 - (d1*d2))
    x_2 = (d2*(1-d1)) / (1 - (d1*d2))
    print(f'Equilibrium shares: ({x_1}, {x_2})')
    if eval(outside) >= x_2:
        cprint(f'Outside option is better than equilibrium share\nPlayer 1 has to offer: ({1-eval(outside)}, {eval(outside)})', 'light_green')
    else:
        cprint(f'Equilibrium shares can be paid out since the outside option doesn\'t matter\nPlayer 1 has to offer: ({x_1}, {x_2})', 'light_green')


def infinite_bargaining_limited_divisions(d1, d2, size):
    """
    Consider a bargaing game with alternating offers with two players: In each round, one player makes a proposal how to divide a pie of size 1. Divisions are denoted (x1,x2)
    where x1 and x2 are the shares of the two players. Player 1 has a constant discount rate of δ1=710 and player 2 has a constant discount rate of δ2=910. Different from the standard model, we consider the case where the pie can only be divided into ten many pieces of equal size.
    Each of the two players can only obtain either no piece of the pie at all, or one piece of size 1/10, or two pieces of size 1/10, … , up to all the ten pieces each of size 1/10. Other divisions are not possible.
    """
    sep = "\t | "
    d1, d2 = map(eval, [d1, d2])
    cprint('Draw the table and check which columns have the same top and bottom row value and then take the min / max out of that set', 'light_green')

    cprint("player 1 share in t-0|", end="\t", color="light_red")
    print(sep.join([str(x) for x in range(size+1)])) 

    cprint("player 1 accpt in t-1|", end="\t", color="light_red")
    print(sep.join([str(math.ceil(x*d1)) for x in range(size+1)])) 

    cprint("player 2 share in t-1|", end="\t", color="light_red")
    temp = [size - math.ceil(x*d1) for x in range(size+1)]
    print(sep.join([str(x) for x in temp])) 

    cprint("player 2 accpt in t-2|", end="\t", color="light_red")
    temp = [math.ceil(x*d2) for x in temp]
    print(sep.join([str(x) for x in temp])) 

    cprint("player 1 share in t-2|", end="\t", color="light_red")
    temp = [str(size - x) for x in temp]
    print(sep.join(temp)) 
    cprint(", ".join([value for value, num in zip(temp, [str(x) for x in range(size+1)]) if value == num]), 'light_green')


def infinite_bargaining_ne_standard_find_q(x1, d1, d2):
    """
    Consider the standard bargaing game with alternating offers with two players: In each round, one player makes a proposal how to divide a pie of size 1. Divisions are denoted (x1,x2) where x1 and x2 are the shares of the two players. Player 1 has a constant discount rate of δ1=8/9
    and player 2 has a constant discount rate of δ2=9/10
    Players alternate in making a proposal. In round 1 player 1 makes a proposal. If players 2 agrees, then the oﬀer is implemented and the game ends. Otherwise, player 2 makes a proposal in round 2. If players 1 agrees, then the offer is implemented and the game ends. Otherwise, player 1 makes a proposal in round 3, etc.
    What is the largest value of Q, such that this combination of strategies is a Nash equilibrium? Enter -1 if there is no Nash equilibrium.

    (x1='1/3', d1='8/9', d2='9/10', p1a='1/3')
    x1, d1, d2, p1a are required
    """
    cprint('Make sure p1a and x1 are the same elisEeer', 'light_red')
    x1, d1, d2 = map(eval, [x1,  d1, d2])
    preq = x1 * (1 / d1)
    cprint(f'Q <= {x1} * {d1}^(-1) = {preq}')
    cprint(f'Check the following: {d2}*{1-preq} <  {1-x1}\n{d2 * (1-preq)} < {1-x1} is {d2 * (1-preq) < 1-x1}')


def infinite_bargaining_spe_standard(d1, d2):
    """
    Consider the standard bargaing game with alternating offers with two players: In each round, one player makes a proposal how to divide a pie of size 1. Divisions are denoted (x1,x2) where x1 and x2 are the shares of the two players. Player 1 has a constant discount rate of δ1=56 and player 2 has a constant discount rate of δ2=1011
    Players alternate in making a proposal. In round 1 player 1 starts making a proposal. If players 2 agrees, then the offer is implemented. In round 2 player 2 makes a proposal. If players 1 agrees, then the offer is implemented. In round 3 player 1 again makes a proposal, etc.
    """
    d1 = eval(d1)
    d2 = eval(d2)

    cprint(f'x_1: {(d2 - 1) / (d1*d2 - 1)}', 'light_green')
    cprint(f'x_2: {1 - ((d2 - 1) / (d1*d2 - 1))}')
    y_1 = (d1*(d2 - 1)) / (d1*d2 - 1)
    cprint(f'y_1: {y_1}')
    cprint(f'y_2: {1 - y_1}')


def economy_nash_bargaining_incorrect(u1, u2, d, eff1, eff2):
    """
    Args: ('1 + 5x_1', '7+3x_2', (5,3), (5,8), (9,3))
    Consider an economy which can produce two commodities with quantities x1 and x2
    What can you say about the Nash bargaining solution?
    """
    cprint("Don't use", "light_red")
    return
    cprint(f'Make sure to enter the equations as x_1 and x_2\nAswell as the efficient two point of the 3', 'light_red')
    x_1 = f'lambda * {eff1[0]} + (1 - lambda) * {eff1[1]}'
    x_2 = f'lambda * {eff2[0]} + (1 - lambda) * {eff2[1]}'
    query = f"maximize ( ({x_1} - {d[0]}) * ({x_2} - {d[1]}) ) for 0 <= lambda <= 1"
    print(query)
    result = client.query(query)
    for pod in result.pods:
        for sub in pod.subpods:
            ctext = sub.plaintext
            if ctext and " at λ = " in ctext and "max{" in ctext:
                cprint(ctext, "light_green")
                lamb = eval(ctext.split('at λ = ')[-1].strip())
            else:
                print(ctext)
    x_1 = lamb * 5 + (1 - lamb) * 9
    x_2 = lamb * 8 + (1 - lamb) * 3
    cprint(f'x_1: {x_1}')
    cprint(f'x_2: {x_2}')
    cprint(f'u(x_1): {eval(u1.replace("x_1", " * " + str(x_1)))}')
    cprint(f'u(x_2): {eval(u2.replace("x_2", " * " + str(x_2)))}')


def economy_nash_bargaining_correct(u1_str, u2_str, d, eff1, eff2):
    """
    Args:
        u1 = "1 + 3*x1"
        u2 = "4 + 8*x2"
        d = (8, 2)
        eff1 = (8, 6)
        eff2 = (9, 2)
    """
    cprint('Input functions as 8*x1 eg.', 'light_red')
    # Define utility functions
    def U1(x1, x2):
        return eval(u1_str)
    def U2(x1, x2):
        return eval(u2_str)
    U1_d = U1(*d)
    U2_d = U2(*d)
    def nash_product(variables):
        lamb, mu = variables
        x1 = eff1[0] * lamb + eff2[0] * mu + d[0] * (1 - lamb - mu)
        x2 = eff1[1] * lamb + eff2[1] * mu + d[1] * (1 - lamb - mu)
        u1 = U1(x1, x2) - U1_d
        u2 = U2(x1, x2) - U2_d
        return -(u1 * u2)
    # Constraints for convex combination
    def constraint1(variables):
        return variables[0]  # lambda >= 0
    def constraint2(variables):
        return variables[1]  # mu >= 0
    def constraint3(variables):
        return 1 - variables[0] - variables[1]  # lambda + mu <= 1
    cons = [{'type': 'ineq', 'fun': constraint1},
            {'type': 'ineq', 'fun': constraint2},
            {'type': 'ineq', 'fun': constraint3}]
    initial_guess = [0.33, 0.33]
    result = minimize(nash_product, initial_guess, constraints=cons, bounds=[(0, 1), (0, 1)])
    lamb_opt, mu_opt = result.x
    x1_opt = eff1[0] * lamb_opt + eff2[0] * mu_opt + d[0] * (1 - lamb_opt - mu_opt)
    x2_opt = eff1[1] * lamb_opt + eff2[1] * mu_opt + d[1] * (1 - lamb_opt - mu_opt)
    U1_opt = U1(x1_opt, x2_opt)
    U2_opt = U2(x1_opt, x2_opt)
    cprint(f'x1: {x1_opt}\nx2: {x2_opt}\nu(x1): {U1_opt}\nu(x2): {U2_opt}', 'light_green')

# To do by hand:
    # Vector Task 
    # Find the smallest Q for 3x3 Table and In which round do players agree :
        # Smallest q = discount factor of player x to the power of 2
        # if q is 1 it ends in round 1 else in round of player x proposal


