from account import data as dd
import random


# generate a random account for the data


def check_answer(guess,account_a_foll,account_b_foll):
    if account_a_foll > account_b_foll:
        return guess == "a"
    else:
        guess == 'b'

#for the data am hving
def format(account):
    account_name = account["name"]
    account_des = account["description"]
    account_cou = account["Country"]
    return f"{account_name},a {account_des},from { account_cou}"


score = 0;

game = True

while game:
    
    account_a = random.choice(dd);
    account_b = random.choice(dd)

    

    if account_a == account_b:
        account_b = random.choice(dd)

    print(f"compare A :{format(account_a)}");
    print(f"compare B :{format(account_b)}");

    # guess the one with more followers 

    guess = input("Who has more folowers type: A or B ").lower();

    # get the one with more followers 

    account_a_people = account_a["follower_account"];
    account_b_people = account_b["follower_account"];
    

    # GIVE IT TO A funtion



    is_correct = check_answer(guess,account_a_people,account_b_people);

    if is_correct:
        score +=1
        print(f"You are right ,youe score is {score}")
    else:
        game= False
        print(f"Sorry you are wrong your score is {score}")







