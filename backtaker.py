import streamlit as st

def backtaker():
        st.write("\nHi there! Seems like you are visiting BackTaker, nice to see you.")

        # První otázka
        st.write("\nWhat brings you here today?")
        st.write("1. I want to take my bad decision back")
        st.write("2. I'm just curious")
        st.write("3. Ohh, I just accidentally clicked on some random link")

        choice = st.text_input("\nChoose an option (1/2/3):", key="1")

        if choice not in ["1", "2", "3"]:
            st.write("\nI don't understand you... Try again please.")
            st.stop()

        if choice == "1":
            st.write("\nwhat was your decision related to?")
            st.write("1. Relationships")
            st.write("2. Health")
            st.write("3. Money")
            st.write("4. Career")
            st.write("5. Education")
            st.write("6. Morality")
            st.write("7. Crimes")
            st.write("8. Time loss")

            decision_choice = st.text_input("\nChoose an option (1-8): ", key="2")

            if decision_choice not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
                st.write("\nI don't understand you... Try again please.")
                st.stop()

            # RELATIONSHIPS
            if decision_choice == "1":
                st.write("\nrelationships, hmm? these can be tricky.")
                st.write("\nwas it a family relationship, a friend, or love?")
                st.write("1. Family")
                st.write("2. Friend")
                st.write("3. Love")
                relaChoiceA = st.text_input("\nChoose an option (1/2/3): ", key="3")

                if relaChoiceA not in ["1", "2", "3"]:
                    st.write("\nI don't understand you... Try again please.")
                    st.stop()

                st.write("1. did you lose touch with them?")
                st.write("2. were there a fight, misunderstanding or you said something hurtful?")
                st.write("3. have you done something you regret now?")
                st.write("4. did you miss opportunities to be with them?")
                relaChoiceB = st.text_input("\nChoose an option (1/2/3/4): ", key="4")

                if relaChoiceB not in ["1", "2", "3", "4"]:
                    st.write("\nI don't understand you... Try again please.")
                    st.stop()

                if relaChoiceB == "1":
                    st.write("being aware that they are somewhere in the world and not being in touch with them can be hurtful.")
                    describing = st.text_input("\nhow would you describe your problem? ", key="5")
                    st.write("I've fixed your relationship now. look into your messages!")
                    st.write("though, will it actually make things better, or just create new challenges what you dont know about yet? ")
                    st.stop()

                if relaChoiceB == "2":
                    st.write("words can hurt...")
                    describing = st.text_input("\nhow would you describe your problem? ", key="6")
                    st.write("I've fixed your relationship now. look into your messages!")
                    st.write("though, will it actually make things better, or just create new challenges what you dont know about yet? ")
                    st.stop()

                if relaChoiceB == "3":
                    st.write("actions speak louder than words, dont they?")
                    describing = st.text_input("\nhow would you describe your problem? ", key="7")
                    st.write("I've fixed your relationship now. look into your messages!")
                    st.write("though, will it actually make things better, or just create new challenges what you dont know about yet? ")
                    st.stop()

                if relaChoiceB == "4":
                    st.write("being aware that they are somewhere in the world and not being in touch with them can be hurtful.")
                    describing = st.text_input("\nhow would you describe your problem? ", key="8")
                    st.write("though, will it actually make things better? or just create new challenges what you dont know about yet? ")
                    st.stop()

            # HEALTH
            elif decision_choice == "2":
                st.write("\nlet's make things nice and healthy again!")
                st.write("\nwas it about your physical or mental health?")
                st.write("1. Physical health")
                st.write("2. Mental health")
                healChoiceA = st.text_input("\nChoose an option (1/2): ", key="9")

                if healChoiceA not in ["1", "2"]:
                    st.write("\nI don't understand you... Try again please.")
                    st.stop()

                if healChoiceA == "1":
                    st.write("was is a lifestyle choice or a one-time decision?")
                    st.write("1. Lifestyle choice")
                    st.write("2. One-time decision")
                    healChoiceAA = st.text_input("\nChoose an option (1/2): ", key="10")

                    if healChoiceAA not in ["1", "2"]:
                        st.write("\nI don't understand you... Try again please.")
                        st.stop()

                    if healChoiceAA == "1":
                        st.write("it's not always easy to stay consistent in healthy lifestyle.")
                        describing = st.text_input("\nhow would you describe your problem? ", key="11")
                        st.write("i've just fixed your unhealthy life-style habits.")
                        st.write("however, do you think it will be easy to keep your new healthy habits in your life when you didnt learn how to build them step by step?")
                        st.stop()

                    if healChoiceAA == "2":
                        st.write("1. oh noo.. have you eaten or drank anything unhealthy again?")
                        st.write("2. were you being silly and your crazy ideas hurt you?")
                        st.write("3. have you done anything else that harmed your body?")
                        healChoiceB = st.text_input("\nChoose an option (1/2/3): ", key="12")

                        if healChoiceB not in ["1", "2", "3"]:
                            st.write("\nI don't understand you... Try again please.")
                            st.stop()

                        describing = st.text_input("\nhow would you describe your problem? ", key="13")
                        st.write("look and feel your body now! isn't it better?")
                        st.write("but will you be really more careful next time without this experience?")
                        st.stop()

                # Mental health option
                elif healChoiceA == "2":
                    st.write("properly understanding our mental health is often a long-term journey.")
                    st.write("do you think it was a lifestyle choice or a one-time decision?")
                    st.write("1. Lifestyle choice")
                    st.write("2. One-time decision")
                    healChoiceB = st.text_input("\nChoose an option (1/2): ", key="14")

                    if healChoiceB not in ["1", "2"]:
                        st.write("\nI don't understand you... Try again please.")
                        st.stop()

                    if healChoiceB == "1":
                        st.write("it's not always easy to learn effective methods of dealing with your mental health.")
                        describing = st.text_input("\nhow would you describe your problem? ", key="15")
                        st.write("feel what is happening in your mind right now! isn't it better like this?")
                        st.write("however, do you think it will be easy to keep your new healthy habits in your life when you didnt learn how to build them step by step?")
                        st.stop()

                    if healChoiceB == "2":
                        st.write("thank you for sharing.")
                        st.write("1. have you stayed in traumatizing situation for too long?")
                        st.write("2. have you harmed yourself or you are just dying of suicide attempt?")
                        st.write("3. have you done anything different what caused problems to your mental health?")
                        healChoiceBA = st.text_input("\nChoose an option (1/2/3): ", key="16")

                        if healChoiceBA not in ["1", "2", "3"]:
                            st.write("\nI don't understand you... Try again please.")
                            st.stop()

                        if healChoiceBA == "1":
                            describing = st.text_input("\nhow would you describe your problem? ", key="17")
                            st.write("i've just modified your past to feel better. doesn't it?")
                            st.write("do you have anything that will protect you from similar situations in the future though?")
                            st.stop()

                        if healChoiceBA == "2":
                            describing = st.text_input("\nhow would you describe your problem? ", key="18")
                            st.write("look! i've just erased all marks of your actions on your body. feel free to enjoy your new you again!")
                            st.write("just... don't you think it's more as cosmetics repair in contrast to your much deeper reasons for doing it?")
                            st.stop()

                        if healChoiceBA == "3":
                            describing = st.text_input("\nhow would you describe your problem? ", key="19")
                            st.write("i've just modified your past to feel better. doesn't it?")
                            st.write("do you have anything that will protect you from similar situations in the future though?")
                            st.stop()

            # MONEY
            elif decision_choice == "3":
                st.write("\n money, money, money... that can be a sensitive topic. let’s see how we can fix this together.")
                st.write("have you spent your money unwisely or you missed a good investment opportunity?")
                st.write("1. Unwisely spent money")
                st.write("2. Missed investment opportunity")
                moneyChoiceA = st.text_input("\nChoose an option (1/2): ", key="20")

                if moneyChoiceA not in ["1", "2"]:
                    st.write("\nI don't understand you... Try again please.")
                    st.stop()

                if moneyChoiceA == "1":
                    st.write("thank you. it's not always easy to manage finances perfectly.")
                    st.write("what was the main problem with your investment?")
                    st.write("1. have you bought something that you didn't need?")
                    st.write("2. do you struggle with long-term healthy financial habits?")
                    st.write("3. have you spent money that was not yours?")
                    st.write("4. did you end up in debt?")
                    st.write("5. do you have a different issue with your spent money?")
                    moneyChoiceB = st.text_input("\nChoose an option (1–5): ", key="21")

                    if moneyChoiceB not in ["1", "2", "3", "4", "5"]:
                        st.write("\nI don't understand you... Try again please.")
                        st.stop()

                    describing = st.text_input("\nthank you. and how did you spend them? or how would you describe your problem? ", key="22")
                    st.write("i've just restored your bank account, feel free to look!")
                    st.write("do you think this will help you to gain healthy financial habits though?")
                    st.stop()

                if moneyChoiceA == "2":
                    st.write("thank you. it's not always easy to manage finances perfectly.")
                    describing = st.text_input("\nwhat chance have you missed? or how would you describe your problem? ", key="23")
                    st.write("i've just modified your past and your opportunities are back on the table now, feel free to look!")
                    st.write("though, do you think you will recognize the right investments in the future?")
                    st.stop()

            # CAREER
            elif decision_choice == "4":
                st.write("\nyeah... finding a perfect career is not the easiest task under the sun. but I can help you with that.")
                st.write("was it about the job you took or a chance you missed?")
                st.write("1. Job I took")
                st.write("2. Chance I missed")
                careerChoiceA = st.text_input("\nChoose an option (1/2): ", key="24")

                if careerChoiceA not in ["1", "2"]:
                    st.write("\nI don't understand you... Try again please.")
                    st.stop()

                if careerChoiceA == "1":
                    st.write("1. have you stopped seeing meaning in your career path or you lost interest in it?")
                    st.write("2. did you have different expectations of your job?")
                    st.write("3. is doing your job connected to anything uncomfortable?")
                    st.write("4. do you have other reasons why you regret being in your job?")
                    careerChoiceB = st.text_input("\nChoose an option (1/2/3/4): ", key="25")

                    if careerChoiceB not in ["1", "2", "3", "4"]:
                        st.write("\nI don't understand you... Try again please.")
                        st.stop()

                    st.write("I've just fixed your career path to feel better. can you already see the new opportunities?")
                    st.write("however, if you wouldn't have gained these experiences from the job, would you even know that you don't want to do work like this?")
                    st.stop()

                if careerChoiceA == "2":
                    st.write("1. do you regret this missed change because of vision of fulfilling your dream?")
                    st.write("2. do you regret this missed change because of vision of a good salary?")
                    st.write("3. do you regret this missed change because of vision of a nice work environment?")
                    st.write("4. do you regret this missed change because of something else?")
                    careerChoiceB = st.text_input("\nChoose an option (1/2/3/4): ", key="26")

                    if careerChoiceB not in ["1", "2", "3", "4"]:
                        st.write("\nI don't understand you... Try again please.")
                        st.stop()

                    st.write("I've just fixed your career path to feel better. can you already see the new opportunities?")
                    st.stop()

                # EDUCATION
                if decision_choice == "5":
                    st.write("\n...")
                    st.write("was it about something you didn't learn, or do you regret something you studied?")
                    st.write("1. Something I didn't learn.")
                    st.write("2. Something I studied.")
                    eduChoiceA = st.text_input("\nChoose an option (1/2): ", key="27")
                    if eduChoiceA == "1":
                        st.write("it's never too late to learn! but let’s see how I can help.")
                        st.write("1. did you miss the opportunity to study?")
                        st.write("2. do you regret dropping out of school?")
                        st.write("3. do you regret failing in your study or you lack skills that you need right now?")
                        eduChoiceB = st.text_input("\nChoose an option (1/2/3): ", key="28")
                        if eduChoiceB == "1" or eduChoiceB == "2" or eduChoiceB == "3":
                            describing = st.text_input("\nhow would you describe your problem? ", key="29")
                            st.write("I've just brang your opportunities back on the table. can you already see your new chances?")
                            st.write("however, would you have known your true priorities without exploring your previous choice?")
                            st.stop()

                    elif eduChoiceA == "2":
                        st.write("regretting something we studied in not uncommon. let’s see how I can help.")
                        st.write("why do you regret your education choice? what have you studied?")
                        st.write("1. something what doesn't interest me.")
                        st.write("2. something what I cannot use in the future.")
                        st.write("3. something what others wanted me to study.")
                        st.write("4. I regret my education choice from different reason.")
                        eduChoiceB = st.text_input("\nChoose an option (1/2/3/4): ", key="30")
                        if eduChoiceB == "1" or eduChoiceB == "2" or eduChoiceB == "3" or eduChoiceB == "4":
                            describing = st.text_input("\nhow would you describe your problem? ", key="31")
                            st.write("I've just brang your opportunities back on the table. can you already see your new chances?")
                            st.write("however, would you have known your true priorities and interests without exploring your previous choice?")
                            st.stop()

                # MORALITY AND VALUES
                elif decision_choice == "6":
                    st.write("\nmorality... yeah, sometimes feels like trying to find a way out of a maze. but if you’re starting to feel bad about something, it’s a sign there’s something going on inside you.")
                    st.write("1. were you being selfish or unfair?")
                    st.write("2. did you lie or manipulate others?")
                    st.write("3. did you refuse taking responsibility for your mistakes or shift the blame to others?")
                    st.write("4. did you betray anyone?")
                    st.write("5. were you being too nice or deny your own values because of others?")
                    st.write("6. have you done anything else related to your values?")
                    moralChoiceA = st.text_input("\nChoose an option (1–6): ", key="32")
                    if moralChoiceA == "1" or moralChoiceA == "2" or moralChoiceA == "3" or moralChoiceA == "4" or moralChoiceA == "6":
                        st.write("no matter how bad thing you did, it's great that you realized your mistakes and you want to make the situation better.")
                        describing = st.text_input("\nhow would you describe what happened? ", key="33")
                        st.write("all your behavior has been undone! feel free to check it out yourself.")
                        st.write("however, do you really feel better and fair when you didn't undo your action yourself?")
                        st.stop()

                    elif moralChoiceA == "5":
                        st.write("sometimes it's difficult to recognize your boundaries and decide what is the best thing to do.")
                        describing = st.text_input("\nhow would you describe what happened? ", key="34")
                        st.write("I've just undone your previous behavior. enjoy your new start!")
                        st.write("however, would you even recognize your boundaries if you wouldn't have chances to learn it?")
                        st.stop()

                # CRIMES
                elif decision_choice == "7":
                    st.write("\nso you have a shady past, huh? life paths can be tricky and lead to shady places sometimes.")
                    st.write("was it something minor or serious?")
                    st.write("1. Minor")
                    st.write("2. Serious")
                    crimeChoiceAA = st.text_input("\nChoose an option (1/2): ", key="35")
                    if crimeChoiceAA == "1":
                        st.write("it's always great to be honest with yourself.")
                        st.write("1. did you steal anything?")
                        st.write("2. did you vandalize or damage property?")
                        st.write("3. did you commit any minor scam for personal gain?")
                        st.write("4. did you commit any driving offense?")
                        st.write("5. did you commit any other minor crime?")
                        crimeChoiceAAA = st.text_input("\nChoose an option (1/2/3/4/5): ", key="36")
                        if crimeChoiceAAA == "1":
                            describing = st.text_input("\nthank you for saying. how would you describe what you have done? ", key="37")
                            st.write("your actions are undone now! you can safely look into eyes of the people you have been stealing from.")
                            st.write("do you really feel better inside yourself though, when you didn't undo your action yourself?")
                            st.stop()

                        elif crimeChoiceAAA == "2":
                            describing = st.text_input("\nthank you for saying. how would you describe what you have done? ", key="38")
                            st.write("your actions are undone now! you can safely look into eyes of the people whose property you have damaged.")
                            st.write("do you really feel better inside yourself though, when you didn't undo your action yourself?")
                            st.stop()

                        elif crimeChoiceAAA == "3":
                            describing = st.text_input("\nthank you for saying. how would you describe what you have done? ", key="39")
                            st.write("your actions are undone now! you can safely look into eyes of the people you have scammed.")
                            st.write("do you really feel better inside yourself though, when you didn't undo your action yourself?")
                            st.stop()

                        elif crimeChoiceAAA == "4":
                            st.write("thank you for saying. just hope the others survived your ride.")
                            describing = st.text_input("\nhow would you describe what you have done? ", key="40")
                            st.write("your actions are undone now!")
                            st.write("do you really feel better inside yourself though, when you didn't undo your action yourself?")
                            st.stop()

                        elif crimeChoiceAAA == "5":
                            describing = st.text_input("\nthank you for saying. how would you describe what you have done? ", key="41")
                            st.write("your actions are undone now!")
                            st.write("do you really feel better inside yourself though, when you didn't undo your action yourself?")
                            st.stop()

                    elif crimeChoiceAA == "2":
                        st.write("it's always great to be honest with yourself.")
                        st.write("1. were you into drugs, man?")
                        st.write("2. were you involved in any large financial fraud?")
                        st.write("3. did you harm or kill anyone?")
                        st.write("4. did you sexually assault or rape anyone?")
                        st.write("5. were you involved in human trafficking?")
                        st.write("6. were you involved in human or animal torturing?")
                        st.write("7. did you commit any other serious crimes?")
                        crimeChoiceAB = st.text_input("\nChoose an option (1–7):", key="42")
                        if crimeChoiceAB == "1":
                            describing = st.text_input("\nhow would you describe what you have done? ", key="43")
                            st.write("okay well... no problem.")
                            st.write("i've just undone your drug past!")
                            st.write("do you truly feel better inside yourself though?")
                            st.stop()

                        elif crimeChoiceAB == "2":
                            describing = st.text_input("\nhow would you describe what you have done? ", key="44")
                            st.write("okay well... no problem.")
                            st.write("i've just undone your actions!")
                            st.write("do you truly feel better inside yourself though?")
                            st.stop()

                        elif crimeChoiceAB == "3":
                            describing = st.text_input("\nhow would you describe what you have done? ", key="45")
                            st.write("okay well... no problem.")
                            st.write("i've just undone your actions! you can safely look into eyes of the people you have harmed or killed.")
                            st.write("do you truly feel better inside yourself though?")
                            st.stop()

                        elif crimeChoiceAB == "4":
                            describing = st.text_input("\nhow would you describe what you have done? ", key="46")
                            st.write("okay well... no problem.")
                            st.write("i've just undone your actions! you can safely look into eyes of the people you have sexually abused.")
                            st.write("do you feel truly better and fair inside yourself though? does it help you now that you know what you're capable of?")
                            st.stop()

                        elif crimeChoiceAB == "5":
                            describing = st.text_input("\nhow would you describe what you have done? ", key="47")
                            st.write("okay well... no problem.")
                            st.write("i've just undone your actions! you can safely look into eyes of the people you have harmed.")
                            st.write("do you truly feel better and fair inside yourself though? does it help you now that you know what you're capable of?")
                            st.stop()

                        elif crimeChoiceAB == "6":
                            describing = st.text_input("\nhow would you describe what you have done? ", key="48")
                            st.write("okay well... no problem.")
                            st.write("i've just undone your actions! you can safely look into eyes of the people and animals whose lives you turned into hell.")
                            st.write("do you truly feel better and fair inside yourself though? does it help you now that you know what you're capable of?")
                            st.stop()

                        elif crimeChoiceAB == "7":
                            describing = st.text_input("\nhow would you describe what you have done? ", key="49")
                            st.write("okay well... no problem.")
                            st.write("i've just undone your actions!")
                            st.write("do you truly feel better inside yourself though?")
                            st.stop()

                else:
                    st.write("\nI don't understand you... Try again please.")

            # TIME LOSS
                    if decision_choice == "8":
                        st.write("\nnobody can escape the flow of time... they said! let’s see how we can play with it.")
                        st.write("why do you feel sorry about your passed time?")
                        st.write("1. I just missed my last connection, dammit.")
                        st.write("2. I have spend too much time on videogames and social media and now I can't do my work for tomorrow.")
                        st.write("3. I always said 'maybe later' to my dreams and now I feel like it’s too late.")
                        st.write("4. I have given my time to wrong people or wrong work.")
                        st.write("5. I have lost the best years of my life with focusing on silly things.")
                        st.write("6. I dont have enough time already to be with people I love.")
                        st.write("7. I feel sorry about something else related to my passed time.")
                        timeLossChoice = st.text_input("\nChoose an option (1–7): ", key="50")

                        if timeLossChoice == "1":
                            st.write("oh noo!")
                            describing = st.text_input("\nwhere you wanted to go? or how would you describe your problem? ", key="51")
                            st.write("you have plenty of time to catch your connection now. check on your time!")
                            st.write("will you be more careful next time in more important situation though?")
                            st.stop()

                        if timeLossChoice == "2":
                            st.write("oh noo!")
                            describing = st.text_input("\nwhat do you need to do for tomorrow? or how would you describe your problem? ", key="52")
                            st.write("you have plenty of time to do your work now. check on your time!")
                            st.write("however, do you think it will be easy to keep health time-management habits when you didnt learn how to build them step by step?")
                            st.stop()

                        if timeLossChoice == "3":
                            st.write("oh noo!")
                            describing = st.text_input("\nhow would you describe your problem? ", key="53")
                            st.write("I've just restored your lost time. check on the date!")
                            st.write("however, what would be exactly stopping you from fulfilling your dreams without my help?")
                            st.stop()

                        if timeLossChoice == "4":
                            st.write("oh noo!")
                            describing = st.text_input("\nhow would you describe your problem? ", key="54")
                            st.write("I've just restored your lost time. check on the date!")
                            st.write("however, how would you know that it is wrong without experiencing it?")
                            st.stop()

                        if timeLossChoice == "5":
                            st.write("oh noo!")
                            describing = st.text_input("\nhow would you describe your problem? ", key="55")
                            st.write("I've just restored your lost time. check on the date!")
                            st.write("though, how can you know those were the best years?")
                            st.stop()

                        if timeLossChoice == "6":
                            st.write("oh noo!")
                            describing = st.text_input("\nwho do you wish to spend more time with? or how would you describe your problem? ", key="56")
                            st.write("I've just restored your time for spending it with your loved ones. check on the date!")
                            st.write("do you think this will change your approach to the time in the future?")
                            st.stop()

                        if timeLossChoice == "7":
                            st.write("oh noo!")
                            describing = st.text_input("\nhow would you describe your regret about time? ", key="57")
                            st.write("your lost time has been restored. check on the date!")
                            st.write("do you think this will change your approach to the time in the future?")
                            st.stop()

                    else:
                        st.write("\nI don't understand you... Try again please.")
                        st.stop()

        elif choice == "2":
            st.write("\nbeing a little bit curious about new things is always good.")
            st.write("if you would like to take some of your decisions back someday, you know where to find me.")
            st.stop()

        elif choice == "3":
            st.write("\nlucky guy...")
            st.stop()

        else:
            st.write("\nI don't understand you... Try again please.")
            st.stop()

# Spuštění aplikace
backtaker()
