def backtaker():
    while True:
        print("\nHi there! Seems like you are visiting BackTaker, nice to see you.")

        # První otázka
        print("\nWhat brings you here today?")
        print("1. I want to take my bad decision back")
        print("2. I'm just curious")
        print("3. Ohh, I just accidentally clicked on some random link")

        choice = input("\nChoose an option (1/2/3): ")

        if choice not in ["1", "2", "3"]:
            print("\nI don't understand you... Try again please.")
            continue

        if choice == "1":
            print("\nwhat was your decision related to?")
            print("1. Relationships")
            print("2. Health")
            print("3. Money")
            print("4. Career")
            print("5. Education")
            print("6. Morality")
            print("7. Crimes")
            print("8. Time loss")

            decision_choice = input("\nChoose an option (1-8): ")

            if decision_choice not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
                print("\nI don't understand you... Try again please.")
                continue

            # RELATIONSHIPS
            if decision_choice == "1":
                print("\nrelationships, hmm? these can be tricky.")
                print("\nwas it a family relationship, a friend, or love?")
                print("1. Family")
                print("2. Friend")
                print("3. Love")
                relaChoiceA = input("\nChoose an option (1/2/3): ")

                if relaChoiceA not in ["1", "2", "3"]:
                    print("\nI don't understand you... Try again please.")
                    continue

                print("1. did you lose touch with them?")
                print("2. were there a fight, misunderstanding or you said something hurtful?")
                print("3. have you done something you regret now?")
                print("4. did you miss opportunities to be with them?")
                relaChoiceB = input("\nChoose an option (1/2/3/4): ")

                if relaChoiceB not in ["1", "2", "3", "4"]:
                    print("\nI don't understand you... Try again please.")
                    continue

                if relaChoiceB == "1":
                    print("being aware that they are somewhere in the world and not being in touch with them can be hurtful.")
                    describing = input("\nhow would you describe your problem? ")
                    print("I've fixed your relationship now. look into your messages!")
                    print("though, will it actually make things better, or just create new challenges what you dont know about yet? ")
                    exit()

                if relaChoiceB == "2":
                    print("words can hurt...")
                    describing = input("\nhow would you describe your problem? ")
                    print("I've fixed your relationship now. look into your messages!")
                    print("though, will it actually make things better, or just create new challenges what you dont know about yet? ")
                    exit()

                if relaChoiceB == "3":
                    print("actions speak louder than words, dont they?")
                    describing = input("\nhow would you describe your problem? ")
                    print("I've fixed your relationship now. look into your messages!")
                    print("though, will it actually make things better, or just create new challenges what you dont know about yet? ")
                    exit()

                if relaChoiceB == "4":
                    print("being aware that they are somewhere in the world and not being in touch with them can be hurtful.")
                    describing = input("\nhow would you describe your problem? ")
                    print("though, will it actually make things better? or just create new challenges what you dont know about yet? ")
                    exit()

            # HEALTH
            elif decision_choice == "2":
                print("\nlet's make things nice and healthy again!")
                print("\nwas it about your physical or mental health?")
                print("1. Physical health")
                print("2. Mental health")
                healChoiceA = input("\nChoose an option (1/2): ")

                if healChoiceA not in ["1", "2"]:
                    print("\nI don't understand you... Try again please.")
                    continue

                if healChoiceA == "1":
                    print("was is a lifestyle choice or a one-time decision?")
                    print("1. Lifestyle choice")
                    print("2. One-time decision")
                    healChoiceAA = input("\nChoose an option (1/2): ")

                    if healChoiceAA not in ["1", "2"]:
                        print("\nI don't understand you... Try again please.")
                        continue

                    if healChoiceAA == "1":
                        print("it's not always easy to stay consistent in healthy lifestyle.")
                        describing = input("\nhow would you describe your problem? ")
                        print("i've just fixed your unhealthy life-style habits.")
                        print("however, do you think it will be easy to keep your new healthy habits in your life when you didnt learn how to build them step by step?")
                        exit()

                    if healChoiceAA == "2":
                        print("1. oh noo.. have you eaten or drank anything unhealthy again?")
                        print("2. were you being silly and your crazy ideas hurt you?")
                        print("3. have you done anything else that harmed your body?")
                        healChoiceB = input("\nChoose an option (1/2/3): ")

                        if healChoiceB not in ["1", "2", "3"]:
                            print("\nI don't understand you... Try again please.")
                            continue

                        describing = input("\nhow would you describe your problem? ")
                        print("look and feel your body now! isn't it better?")
                        print("but will you be really more careful next time without this experience?")
                        exit()

                # Mental health option
                elif healChoiceA == "2":
                    print("properly understanding our mental health is often a long-term journey.")
                    print("do you think it was a lifestyle choice or a one-time decision?")
                    print("1. Lifestyle choice")
                    print("2. One-time decision")
                    healChoiceB = input("\nChoose an option (1/2): ")

                    if healChoiceB not in ["1", "2"]:
                        print("\nI don't understand you... Try again please.")
                        continue

                    if healChoiceB == "1":
                        print("it's not always easy to learn effective methods of dealing with your mental health.")
                        describing = input("\nhow would you describe your problem? ")
                        print("feel what is happening in your mind right now! isn't it better like this?")
                        print("however, do you think it will be easy to keep your new healthy habits in your life when you didnt learn how to build them step by step?")
                        exit()

                    if healChoiceB == "2":
                        print("thank you for sharing.")
                        print("1. have you stayed in traumatizing situation for too long?")
                        print("2. have you harmed yourself or you are just dying of suicide attempt?")
                        print("3. have you done anything different what caused problems to your mental health?")
                        healChoiceBA = input("\nChoose an option (1/2/3): ")

                        if healChoiceBA not in ["1", "2", "3"]:
                            print("\nI don't understand you... Try again please.")
                            continue

                        if healChoiceBA == "1":
                            describing = input("\nhow would you describe your problem? ")
                            print("i've just modified your past to feel better. doesn't it?")
                            print("do you have anything that will protect you from similar situations in the future though?")
                            exit()

                        if healChoiceBA == "2":
                            describing = input("\nhow would you describe your problem? ")
                            print("look! i've just erased all marks of your actions on your body. feel free to enjoy your new you again!")
                            print("just... don't you think it's more as cosmetics repair in contrast to your much deeper reasons for doing it?")
                            exit()

                        if healChoiceBA == "3":
                            describing = input("\nhow would you describe your problem? ")
                            print("i've just modified your past to feel better. doesn't it?")
                            print("do you have anything that will protect you from similar situations in the future though?")
                            exit()

            # MONEY
            elif decision_choice == "3":
                print("\n money, money, money... that can be a sensitive topic. let’s see how we can fix this together.")
                print("have you spent your money unwisely or you missed a good investment opportunity?")
                print("1. Unwisely spent money")
                print("2. Missed investment opportunity")
                moneyChoiceA = input("\nChoose an option (1/2): ")

                if moneyChoiceA not in ["1", "2"]:
                    print("\nI don't understand you... Try again please.")
                    continue

                if moneyChoiceA == "1":
                    print("thank you. it's not always easy to manage finances perfectly.")
                    print("what was the main problem with your investment?")
                    print("1. have you bought something that you didn't need?")
                    print("2. do you struggle with long-term healthy financial habits?")
                    print("3. have you spent money that was not yours?")
                    print("4. did you end up in debt?")
                    print("5. do you have a different issue with your spent money?")
                    moneyChoiceB = input("\nChoose an option (1–5): ")

                    if moneyChoiceB not in ["1", "2", "3", "4", "5"]:
                        print("\nI don't understand you... Try again please.")
                        continue

                    describing = input("\nthank you. and how did you spend them? or how would you describe your problem? ")
                    print("i've just restored your bank account, feel free to look!")
                    print("do you think this will help you to gain healthy financial habits though?")
                    exit()

                if moneyChoiceA == "2":
                    print("thank you. it's not always easy to manage finances perfectly.")
                    describing = input("\nwhat chance have you missed? or how would you describe your problem? ")
                    print("i've just modified your past and your opportunities are back on the table now, feel free to look!")
                    print("though, do you think you will recognize the right investments in the future?")
                    exit()

            # CAREER
            elif decision_choice == "4":
                print("\nyeah... finding a perfect career is not the easiest task under the sun. but I can help you with that.")
                print("was it about the job you took or a chance you missed?")
                print("1. Job I took")
                print("2. Chance I missed")
                careerChoiceA = input("\nChoose an option (1/2): ")

                if careerChoiceA not in ["1", "2"]:
                    print("\nI don't understand you... Try again please.")
                    continue

                if careerChoiceA == "1":
                    print("1. have you stopped seeing meaning in your career path or you lost interest in it?")
                    print("2. did you have different expectations of your job?")
                    print("3. is doing your job connected to anything uncomfortable?")
                    print("4. do you have other reasons why you regret being in your job?")
                    careerChoiceB = input("\nChoose an option (1/2/3/4): ")

                    if careerChoiceB not in ["1", "2", "3", "4"]:
                        print("\nI don't understand you... Try again please.")
                        continue

                    print("I've just fixed your career path to feel better. can you already see the new opportunities?")
                    print("however, if you wouldn't have gained these experiences from the job, would you even know that you don't want to do work like this?")
                    exit()

                if careerChoiceA == "2":
                    print("1. do you regret this missed change because of vision of fulfilling your dream?")
                    print("2. do you regret this missed change because of vision of a good salary?")
                    print("3. do you regret this missed change because of vision of a nice work environment?")
                    print("4. do you regret this missed change because of something else?")     
                    careerChoiceB = input("\nChoose an option (1/2/3/4): ")

                    if careerChoiceB not in ["1", "2", "3", "4"]:
                        print("\nI don't understand you... Try again please.")
                        continue

                    print("I've just fixed your career path to feel better. can you already see the new opportunities?")
                    exit()

                # EDUCATION
                if decision_choice == "5":
                    print("\n...")
                    print("was it about something you didn't learn, or do you regret something you studied?")
                    print("1. Something I didn't learn.")
                    print("2. Something I studied.")
                    eduChoiceA = input("\nChoose an option (1/2): ")
                    if eduChoiceA == "1":
                        print("it's never too late to learn! but let’s see how I can help.")
                        print("1. did you miss the opportunity to study?")
                        print("2. do you regret dropping out of school?")
                        print("3. do you regret failing in your study or you lack skills that you need right now?")
                        eduChoiceB = input("\nChoose an option (1/2/3): ")
                        if eduChoiceB == "1" or eduChoiceB == "2" or eduChoiceB == "3":
                            describing = input("\nhow would you describe your problem? ")
                            print("I've just brang your opportunities back on the table. can you already see your new chances?")
                            print("however, would you have known your true priorities without exploring your previous choice?")
                            exit()

                    elif eduChoiceA == "2":
                        print("regretting something we studied in not uncommon. let’s see how I can help.")
                        print("why do you regret your education choice? what have you studied?")
                        print("1. something what doesn't interest me.")
                        print("2. something what I cannot use in the future.")
                        print("3. something what others wanted me to study.")
                        print("4. I regret my education choice from different reason.")
                        eduChoiceB = input("\nChoose an option (1/2/3/4): ")
                        if eduChoiceB == "1" or eduChoiceB == "2" or eduChoiceB == "3" or eduChoiceB == "4":
                            describing = input("\nhow would you describe your problem? ")
                            print("I've just brang your opportunities back on the table. can you already see your new chances?")
                            print("however, would you have known your true priorities and interests without exploring your previous choice?")
                            exit()

                # MORALITY AND VALUES
                elif decision_choice == "6":
                    print("\nmorality... yeah, sometimes feels like trying to find a way out of a maze. but if you’re starting to feel bad about something, it’s a sign there’s something going on inside you.")
                    print("1. were you being selfish or unfair?")
                    print("2. did you lie or manipulate others?")
                    print("3. did you refuse taking responsibility for your mistakes or shift the blame to others?")
                    print("4. did you betray anyone?")
                    print("5. were you being too nice or deny your own values because of others?")
                    print("6. have you done anything else related to your values?")
                    moralChoiceA = input("\nChoose an option (1–6): ")
                    if moralChoiceA == "1" or moralChoiceA == "2" or moralChoiceA == "3" or moralChoiceA == "4" or moralChoiceA == "6":
                        print("no matter how bad thing you did, it's great that you realized your mistakes and you want to make the situation better.")
                        describing = input("\nhow would you describe what happened? ")
                        print("all your behavior has been undone! feel free to check it out yourself.")
                        print("however, do you really feel better and fair when you didn't undo your action yourself?")
                        exit()

                    elif moralChoiceA == "5":
                        print("sometimes it's difficult to recognize your boundaries and decide what is the best thing to do.")
                        describing = input("\nhow would you describe what happened? ")
                        print("I've just undone your previous behavior. enjoy your new start!")
                        print("however, would you even recognize your boundaries if you wouldn't have chances to learn it?")
                        exit()

                # CRIMES
                elif decision_choice == "7":
                    print("\nso you have a shady past, huh? life paths can be tricky and lead to shady places sometimes.")
                    print("was it something minor or serious?")
                    print("1. Minor")
                    print("2. Serious")
                    crimeChoiceAA = input("\nChoose an option (1/2): ")
                    if crimeChoiceAA == "1":
                        print("it's always great to be honest with yourself.")
                        print("1. did you steal anything?")
                        print("2. did you vandalize or damage property?")
                        print("3. did you commit any minor scam for personal gain?")
                        print("4. did you commit any driving offense?")
                        print("5. did you commit any other minor crime?")
                        crimeChoiceAAA = input("\nChoose an option (1/2/3/4/5): ")
                        if crimeChoiceAAA == "1":
                            describing = input("\nthank you for saying. how would you describe what you have done? ")
                            print("your actions are undone now! you can safely look into eyes of the people you have been stealing from.")
                            print("do you really feel better inside yourself though, when you didn't undo your action yourself?")
                            exit()

                        elif crimeChoiceAAA == "2":
                            describing = input("\nthank you for saying. how would you describe what you have done? ")
                            print("your actions are undone now! you can safely look into eyes of the people whose property you have damaged.")
                            print("do you really feel better inside yourself though, when you didn't undo your action yourself?")
                            exit()

                        elif crimeChoiceAAA == "3":
                            describing = input("\nthank you for saying. how would you describe what you have done? ")
                            print("your actions are undone now! you can safely look into eyes of the people you have scammed.")
                            print("do you really feel better inside yourself though, when you didn't undo your action yourself?")
                            exit()

                        elif crimeChoiceAAA == "4":
                            print("thank you for saying. just hope the others survived your ride.")
                            describing = input("\nhow would you describe what you have done? ")
                            print("your actions are undone now!")
                            print("do you really feel better inside yourself though, when you didn't undo your action yourself?")
                            exit()

                        elif crimeChoiceAAA == "5":
                            describing = input("\nthank you for saying. how would you describe what you have done? ")
                            print("your actions are undone now!")
                            print("do you really feel better inside yourself though, when you didn't undo your action yourself?")
                            exit()

                    elif crimeChoiceAA == "2":
                        print("it's always great to be honest with yourself.")
                        print("1. were you into drugs, man?")
                        print("2. were you involved in any large financial fraud?")
                        print("3. did you harm or kill anyone?")
                        print("4. did you sexually assault or rape anyone?")
                        print("5. were you involved in human trafficking?")
                        print("6. were you involved in human or animal torturing?")
                        print("7. did you commit any other serious crimes?")
                        crimeChoiceAB = input("\nChoose an option (1–7):")
                        if crimeChoiceAB == "1":
                            describing = input("\nhow would you describe what you have done? ")
                            print("okay well... no problem.")
                            print("i've just undone your drug past!")
                            print("do you truly feel better inside yourself though?")
                            exit()

                        elif crimeChoiceAB == "2":
                            describing = input("\nhow would you describe what you have done? ")
                            print("okay well... no problem.")
                            print("i've just undone your actions!")
                            print("do you truly feel better inside yourself though?")
                            exit()

                        elif crimeChoiceAB == "3":
                            describing = input("\nhow would you describe what you have done? ")
                            print("okay well... no problem.")
                            print("i've just undone your actions! you can safely look into eyes of the people you have harmed or killed.")
                            print("do you truly feel better inside yourself though?")
                            exit()

                        elif crimeChoiceAB == "4":
                            describing = input("\nhow would you describe what you have done? ")
                            print("okay well... no problem.")
                            print("i've just undone your actions! you can safely look into eyes of the people you have sexually abused.")
                            print("do you feel truly better and fair inside yourself though? does it help you now that you know what you're capable of?")
                            exit()

                        elif crimeChoiceAB == "5":
                            describing = input("\nhow would you describe what you have done? ")
                            print("okay well... no problem.")
                            print("i've just undone your actions! you can safely look into eyes of the people you have harmed.")
                            print("do you truly feel better and fair inside yourself though? does it help you now that you know what you're capable of?")
                            exit()

                        elif crimeChoiceAB == "6":
                            describing = input("\nhow would you describe what you have done? ")
                            print("okay well... no problem.")
                            print("i've just undone your actions! you can safely look into eyes of the people and animals whose lives you turned into hell.")
                            print("do you truly feel better and fair inside yourself though? does it help you now that you know what you're capable of?")
                            exit()

                        elif crimeChoiceAB == "7":
                            describing = input("\nhow would you describe what you have done? ")
                            print("okay well... no problem.")
                            print("i've just undone your actions!")
                            print("do you truly feel better inside yourself though?")
                            exit()

                else:
                    print("\nI don't understand you... Try again please.")

            # TIME LOSS
                    if decision_choice == "8":
                        print("\nnobody can escape the flow of time... they said! let’s see how we can play with it.")
                        print("why do you feel sorry about your passed time?")
                        print("1. I just missed my last connection, dammit.")
                        print("2. I have spend too much time on videogames and social media and now I can't do my work for tomorrow.")
                        print("3. I always said 'maybe later' to my dreams and now I feel like it’s too late.")
                        print("4. I have given my time to wrong people or wrong work.")
                        print("5. I have lost the best years of my life with focusing on silly things.")
                        print("6. I dont have enough time already to be with people I love.")
                        print("7. I feel sorry about something else related to my passed time.")
                        timeLossChoice = input("\nChoose an option (1–7): ")

                        if timeLossChoice == "1":
                            print("oh noo!")
                            describing = input("\nwhere you wanted to go? or how would you describe your problem? ")
                            print("you have plenty of time to catch your connection now. check on your time!")
                            print("will you be more careful next time in more important situation though?")
                            continue

                        if timeLossChoice == "2":
                            print("oh noo!")
                            describing = input("\nwhat do you need to do for tomorrow? or how would you describe your problem? ")
                            print("you have plenty of time to do your work now. check on your time!")
                            print("however, do you think it will be easy to keep health time-management habits when you didnt learn how to build them step by step?")
                            continue

                        if timeLossChoice == "3":
                            print("oh noo!")
                            describing = input("\nhow would you describe your problem? ")
                            print("I've just restored your lost time. check on the date!")
                            print("however, what would be exactly stopping you from fulfilling your dreams without my help?")
                            continue

                        if timeLossChoice == "4":
                            print("oh noo!")
                            describing = input("\nhow would you describe your problem? ")
                            print("I've just restored your lost time. check on the date!")
                            print("however, how would you know that it is wrong without experiencing it?")
                            continue

                        if timeLossChoice == "5":
                            print("oh noo!")
                            describing = input("\nhow would you describe your problem? ")
                            print("I've just restored your lost time. check on the date!")
                            print("though, how can you know those were the best years?")
                            continue

                        if timeLossChoice == "6":
                            print("oh noo!")
                            describing = input("\nwho do you wish to spend more time with? or how would you describe your problem? ")
                            print("I've just restored your time for spending it with your loved ones. check on the date!")
                            print("do you think this will change your approach to the time in the future?")
                            continue

                        if timeLossChoice == "7":
                            print("oh noo!")
                            describing = input("\nhow would you describe your regret about time? ")
                            print("your lost time has been restored. check on the date!")
                            print("do you think this will change your approach to the time in the future?")
                            continue

                    else:
                        print("\nI don't understand you... Try again please.")
                        continue

        elif choice == "2":
            print("\nbeing a little bit curious about new things is always good.")
            print("if you would like to take some of your decisions back someday, you know where to find me.")
            exit()

        elif choice == "3":
            print("\nlucky guy...")
            exit()

        else:
            print("\nI don't understand you... Try again please.")
            continue

# Spuštění aplikace
backtaker()
