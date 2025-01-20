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
        st.write("\nWhat was your decision related to?")
        st.write("1. Relationships")
        st.write("2. Health")
        st.write("3. Money")
        st.write("4. Career")
        st.write("5. Education")
        st.write("6. Morality")
        st.write("7. Crimes")
        st.write("8. Time loss")

        decision_choice = st.text_input("\nChoose an option (1-8):", key="2")

        if decision_choice not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            st.write("\nI don't understand you... Try again please.")
            st.stop()

        # RELATIONSHIPS
        if decision_choice == "1":
            st.write("\nRelationships, hmm? These can be tricky.")
            st.write("\nWas it a family relationship, a friend, or love?")
            st.write("1. Family")
            st.write("2. Friend")
            st.write("3. Love")
            relaChoiceA = st.text_input("\nChoose an option (1/2/3):", key="3")

            if relaChoiceA not in ["1", "2", "3"]:
                st.write("\nI don't understand you... Try again please.")
                st.stop()

            st.write("1. Did you lose touch with them?")
            st.write("2. Was there a fight, misunderstanding, or you said something hurtful?")
            st.write("3. Have you done something you regret now?")
            st.write("4. Did you miss opportunities to be with them?")
            relaChoiceB = st.text_input("\nChoose an option (1/2/3/4):", key="4")

            if relaChoiceB not in ["1", "2", "3", "4"]:
                st.write("\nI don't understand you... Try again please.")
                st.stop()

            if relaChoiceB == "1":
                if st.button("Submit Response"):
                    st.write("Being aware that they are somewhere in the world and not being in touch with them can be hurtful.")
                    describing = st.text_input("\nHow would you describe your problem?", key="5")
                    st.write("I've fixed your relationship now. Look into your messages!")
                    st.write("Though, will it actually make things better, or just create new challenges you don't know about yet?")
                    st.stop()

            if relaChoiceB == "2":
                if st.button("Submit Response"):
                    st.write("Words can hurt...")
                    describing = st.text_input("\nHow would you describe your problem?", key="6")
                    st.write("I've fixed your relationship now. Look into your messages!")
                    st.write("Though, will it actually make things better, or just create new challenges you don't know about yet?")
                    st.stop()

            if relaChoiceB == "3":
                if st.button("Submit Response"):
                    st.write("Actions speak louder than words, don't they?")
                    describing = st.text_input("\nHow would you describe your problem?", key="7")
                    st.write("I've fixed your relationship now. Look into your messages!")
                    st.write("Though, will it actually make things better, or just create new challenges you don't know about yet?")
                    st.stop()

            if relaChoiceB == "4":
                if st.button("Submit Response"):
                    st.write("Being aware that they are somewhere in the world and not being in touch with them can be hurtful.")
                    describing = st.text_input("\nHow would you describe your problem?", key="8")
                    st.write("Though, will it actually make things better? Or just create new challenges you don't know about yet?")
                    st.stop()

        # HEALTH - This pattern will continue for all other categories (Money, Career, etc.)
        # Add similar logic for Health, Money, etc.

        # More categories such as Health, Money, etc. will follow the same pattern as shown above.

    elif choice == "2":
        st.write("\nBeing a little bit curious about new things is always good.")
        st.write("If you would like to take some of your decisions back someday, you know where to find me.")
        st.stop()

    elif choice == "3":
        st.write("\nLucky guy...")
        st.stop()

    else:
        st.write("\nI don't understand you... Try again please.")
        st.stop()

# Spuštění aplikace
backtaker()
