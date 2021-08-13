due_date = datetime.datetime(2020, 6, 18)
today = datetime.datetime.today()
def Baby(mother,father):
    pregnancy = []
    pregnancy.append(mother + father)
    if today== due_date:
        baby = pregnancy.pop()
        print("Hello World!")
return baby


