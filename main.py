# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Uniform:
    low: float
    high: float

def r_v_calaulate(agent: Uniform, value: float):   # calaulate r(v)
    F_v = (value - agent.low) / (agent.high - agent.low);
    F_v_derivative = 1 / (agent.high - agent.low);
    r_v= value-(1-F_v)/F_v_derivative;
    return r_v;

def r_v_minos1(agent: Uniform,value: float):   # calaulate r^-1(value)
    return (agent.high+value)/2;

def max_revenue_auction( agent1: Uniform, value1: float):
    """
    :param agent1:
    :param value1:
    :return: Myerson tender for one buyer

    >>> Splits=Uniform();
    >>> Splits.low=10;
    >>> Splits.high=30;
    >>> max_revenue_auction(Splits, 9);
    No agent wins

    >>> Splits=Uniform();
    >>> Splits.low=10;
    >>> Splits.high=40;
    >>> max_revenue_auction(Splits, 40);
    No agent wins

    >>> Splits=Uniform();
    >>> Splits.low=10;
    >>> Splits.high=40;
    >>> max_revenue_auction(Splits, 30);
    agent 1 pays 20.0

    >>> Splits=Uniform();
    >>> Splits.low=10;
    >>> Splits.high=30;
    >>> max_revenue_auction(Splits, 27);
    agent 1 pays 15.0

    >>> Splits=Uniform();
    >>> Splits.low=10;
    >>> Splits.high=30;
    >>> max_revenue_auction(Splits, 15);
    Saf
    agent 1 pays 15.0
    """

    r_v=r_v_calaulate(agent1,value1);
    if(value1>=agent1.high or value1<= agent1.low or r_v < 0):
       print("No agent wins");
       return;
    if (r_v == 0):
        print("Saf");
    pay = r_v_minos1(agent1,0);  #r(v)>0
    print("agent 1 pays " + str(pay));

def max_revenue_auction2(agent1: Uniform, agent2: Uniform,value1: float, value2: float):
    """
    :param agent1:
    :param agent2:
    :param value1:
    :param value2:
    :return: Myerson Tender for Two Buyers

    >>> Splits=Uniform();
    >>> Splits.low=10;
    >>> Splits.high=30;
    >>> Splits2 = Uniform();
    >>> Splits2.low = 20;
    >>> Splits2.high = 40;
    >>> max_revenue_auction2(Splits,Splits2,23,27);
    Agent 1 wins and pays 22

    >>> Splits=Uniform();
    >>> Splits.low=10;
    >>> Splits.high=30;
    >>> max_revenue_auction2(Splits,Splits,17,21);
    Agent 2 wins and pays 17

    >>> Splits=Uniform();
    >>> Splits.low=10;
    >>> Splits.high=30;
    >>> max_revenue_auction2(Splits,Splits,17,13);
    Agent 1 wins and pays 15

    >>> Splits=Uniform();
    >>> Splits.low=10;
    >>> Splits.high=30;
    >>> max_revenue_auction2(Splits,Splits,14,13);
    No agent wins

    >>> Splits=Uniform();
    >>> Splits.low=40;
    >>> Splits.high=80;
    >>> max_revenue_auction2(Splits,Splits,38,20);
    No agent wins
    """

    r_v_agent1 = r_v_calaulate(agent1, value1);
    r_v_agent2 = r_v_calaulate(agent2, value2);
    if(r_v_agent1<0 and r_v_agent2<0):
        print("No agent wins");
    else:  #Saf=
        if(r_v_agent1> r_v_agent2):
            while(r_v_calaulate(agent1,value1)>0 and r_v_calaulate(agent1,value1)>r_v_calaulate(agent2,value2)): # r(v1)>0 && r(v1)>r(v2)
                value1=value1-1; #Saf agent1
            pay=max(value1,r_v_minos1(agent1,0));   # max(Saf, r^-1(0))
            print("Agent 1 wins and pays "+str(pay));
        else:
            while(r_v_calaulate(agent2,value2)>0 and r_v_calaulate(agent1,value1)<r_v_calaulate(agent2,value2)): # r(v2)>0 && r(v1)<r(v2)
                value2 =value2-1;  #Saf agent2
            pay = max(value2, r_v_minos1(agent2, 0)); # max(Saf, r^-1(0))
            print("Agent 2 wins and pays " + str(pay));


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import doctest
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
