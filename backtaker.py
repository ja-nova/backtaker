<!DOCTYPE html>

<html lang="en" style="height: 100%">
    <head>
        
            <!-- Google tag (gtag.js) -->
            <script async src="https://www.googletagmanager.com/gtag/js?id=G-DHJF51F24N"></script>
            <script>
              window.dataLayer = window.dataLayer || [];
              function gtag(){dataLayer.push(arguments);}
              gtag('js', new Date());

              gtag('config', 'G-DHJF51F24N');
            </script>
        

        <meta charset="utf-8">
        <title>backTaker.py : /home/janova/backTaker.py : Editor : janova : PythonAnywhere</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="backTaker.py : /home/janova/backTaker.py : Editor : janova : PythonAnywhere">
        <meta name="author" content="PythonAnywhere LLP">
        <meta name="google-site-verification" content="O4UxDrfcHjC44jybs2vajc1GgRkTKCTRgVzeV6I9V14" />


        <!-- Le styles -->
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,300i,400,400i,700,700i" />

        <link rel="stylesheet" href="/static/CACHE/css/output.bdf8ff088d4e.css" type="text/css" media="screen">
        <link rel="stylesheet" href="/static/CACHE/css/output.b9a4961a16f7.css" type="text/css"><link rel="stylesheet" href="/static/CACHE/css/output.18c32ced1060.css" type="text/css" media="screen">

        <!-- Le javascript -->
        <script type="text/javascript">
            var Anywhere = {};
            Anywhere.urls = {};
            Anywhere.csrfToken = "JMRa24BiuUoXSuXjnOsqInD8DFsPGIJ6YXaHHl5lv6XAUWHFmrWm4tdLvwHNpDG5";
        </script>
        <script src="/static/CACHE/js/output.9912b9c89b96.js"></script>
        

        <script src="/static/CACHE/js/output.2ca775b993c5.js"></script>
        
    <script type="text/javascript">
      $(document).ready(function() {
        $.extend(Anywhere.urls, {
          file: "/user/janova/files/home/janova/backTaker.py",
          check_hash: "/user/janova/files/home/janova/backTaker.py",
          update_editor_mode_preference: "/user/janova/account/update_editor_mode_preference",
          console_api: "/api/v0/user/janova/consoles/",
        });
        var filename = "/home/janova/backTaker.py";
        var hash = "d9fe5baa78a4d87406c6ce4c65fda6ee";
        var interpreter = "python3.10";

        
            Anywhere.Editor.InitializeAce(ace, Anywhere.urls, filename, hash, interpreter, "pythonanywhere.com");
            $("#id_keybinding_mode_select").val("normal");
            $("#id_keybinding_mode_select").trigger("change");
        
        var consoleVisible = true;
        Anywhere.Editor.splitPanes(consoleVisible);

        Anywhere.WebAppControl.initialize();
        Anywhere2.initializeFileSharingOptions(
          $('#id_file_sharing_options')[0],
          {
            url: "/api/v0/user/janova/files/sharing/",
            csrfToken: "JMRa24BiuUoXSuXjnOsqInD8DFsPGIJ6YXaHHl5lv6XAUWHFmrWm4tdLvwHNpDG5",
            path: "/home/janova/backTaker.py"
          }
        );

      });
    </script>

        

    </head>

    <body style="height:100%;">
       <div style="min-height: 100%; position: relative;">
        
        
  




  <nav class="navbar navbar-default fullscreen-main-navbar">
    <div class="navbar-header">
      <a class="navbar-brand" href="/">
        <img id="id_logo" src="/static/anywhere/images/PA-logo-snake-only.svg" height="100%" />
      </a>
    </div>

    <div class="extra-nav-content">
      

  <div id="id_editor_toolbar">

    <div class="pull-left">
      <span id="id_breadcrumbs_div"><a class="breadcrumbs_link breadcrumb_entry" href="/user/janova/files/" target="_parent">/</a><a class="breadcrumbs_link breadcrumb_entry" href="/user/janova/files/home" target="_parent">home</a><span class="breadcrumb_entry">/</span><a class="breadcrumbs_link breadcrumb_entry" href="/user/janova/files/home/janova" target="_parent">janova</a><span class="breadcrumb_entry">/</span><wbr><span class="breadcrumb_entry breadcrumb_terminal">backTaker.py</span></span>

      <span>
        <span id="id_unsaved_changes_spacer">
          <span id="id_unsaved_changes" class="pa_hidden muted">(unsaved changes)</span>
        </span>
      </span>
    </div>

    <div id="id_editor_messages" class="pull-left">
      

    </div>

    <div class="pull-right">
      <div id="id_editor_buttons_right" class="form-inline">
        <span id="id_save_error" class="pa_hidden alert alert-danger">Error saving.</span>
        <img src="/static/anywhere/images/spinner-small.gif" class="pa_hidden" id="id_save_spinner" />
        
          <span id="id_keyboard_shortcuts"><a href="#">Keyboard shortcuts:</a></span>
          <select id="id_keybinding_mode_select" class="form-control input-sm">
            <option value="normal">Normal</option>
            <option value="vim">Vim</option>
          </select>
        
        <button id="id_display_sharing_options" class="btn btn-default" data-toggle="modal" data-target="#id_file_sharing_modal" title="Get a URL to share this file">
          <span class="glyphicon glyphicon-paperclip" aria-hidden="true"></span>
          Share
        </button>
        
          <button id="id_save" class="btn btn-success" title="Save (Ctrl + S)">
            <span class="glyphicon glyphicon-floppy-disk" aria-hidden="true"></span>
            Save
          </button>
          <button id="id_save_as" class="btn btn-default" title="Save As">Save as...</button>
        
        
          <button class="btn btn-info run_button" title="Save &amp; Run (Ctrl + R)">
            <span><code>&gt;&gt;&gt;</code></span>
            Run
          </button>
        

        
      </div>
    </div>

  </div>


    </div>

    <div class="dropdown fullscreen-hamburger fullscreen-mini-nav">
      <button type="button" class="navbar-toggle" data-toggle="dropdown"  role="button" aria-haspopup="true" aria-expanded="false">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <ul class="dropdown-menu pull-right">
        
  <li class=""><a id="id_dashboard_link" href="/user/janova/">Dashboard</a></li>
  <li class=""><a id="id_consoles_link" href="/user/janova/consoles/">Consoles</a></li>
  <li class=""><a id="id_files_link" href="/user/janova/files/home/janova">Files</a></li>
  <li class=""><a id="id_web_app_link" href="/user/janova/webapps/">Web</a></li>
  <li class=""><a id="id_tasks_link" href="/user/janova/tasks_tab/">Tasks</a></li>
  <li class=""><a id="id_databases_link" href="/user/janova/databases/">Databases</a></li>


        
<li class=""><a href="" target="_parent" class="feedback_link">Send feedback</a></li>


<li class=""><a href="/forums/" target="_parent" class="forums_link">Forums</a></li>
<li class=""><a href="https://help.pythonanywhere.com/" target="_parent" class="help_link">Help</a></li>
<li class=""><a href="https://blog.pythonanywhere.com/" target="_parent" class="blog_link">Blog</a></li>

  
  <li class=""><a href="/user/janova/account/" target="_parent" class="account_link">Account</a></li>
  <li class="">
    <form action="/logout/" method="POST" target="_parent">
      <input type="hidden" name="csrfmiddlewaretoken" value="JMRa24BiuUoXSuXjnOsqInD8DFsPGIJ6YXaHHl5lv6XAUWHFmrWm4tdLvwHNpDG5">
      <button type="submit" class="btn-link logout_link">Log out</button>
    </form>
  </li>


      </ul>
    </div>

  </nav>



        
    


        
  <div>
    <div id="id_ide_split_panes">

      
        <div id="id_editor">def backtaker():
    while True:
        print(&quot;\nHi there! Seems like you are visiting BackTaker, nice to see you.&quot;)

        # První otázka
        print(&quot;\nWhat brings you here today?&quot;)
        print(&quot;1. I want to take my bad decision back&quot;)
        print(&quot;2. I&#39;m just curious&quot;)
        print(&quot;3. Ohh, I just accidentally clicked on some random link&quot;)

        choice = input(&quot;\nChoose an option (1/2/3): &quot;)

        if choice not in [&quot;1&quot;, &quot;2&quot;, &quot;3&quot;]:
            print(&quot;\nI don&#39;t understand you... Try again please.&quot;)
            continue

        if choice == &quot;1&quot;:
            print(&quot;\nwhat was your decision related to?&quot;)
            print(&quot;1. Relationships&quot;)
            print(&quot;2. Health&quot;)
            print(&quot;3. Money&quot;)
            print(&quot;4. Career&quot;)
            print(&quot;5. Education&quot;)
            print(&quot;6. Morality&quot;)
            print(&quot;7. Crimes&quot;)
            print(&quot;8. Time loss&quot;)

            decision_choice = input(&quot;\nChoose an option (1-8): &quot;)

            if decision_choice not in [&quot;1&quot;, &quot;2&quot;, &quot;3&quot;, &quot;4&quot;, &quot;5&quot;, &quot;6&quot;, &quot;7&quot;, &quot;8&quot;]:
                print(&quot;\nI don&#39;t understand you... Try again please.&quot;)
                continue

            # RELATIONSHIPS
            if decision_choice == &quot;1&quot;:
                print(&quot;\nrelationships, hmm? these can be tricky.&quot;)
                print(&quot;\nwas it a family relationship, a friend, or love?&quot;)
                print(&quot;1. Family&quot;)
                print(&quot;2. Friend&quot;)
                print(&quot;3. Love&quot;)
                relaChoiceA = input(&quot;\nChoose an option (1/2/3): &quot;)

                if relaChoiceA not in [&quot;1&quot;, &quot;2&quot;, &quot;3&quot;]:
                    print(&quot;\nI don&#39;t understand you... Try again please.&quot;)
                    continue

                print(&quot;1. did you lose touch with them?&quot;)
                print(&quot;2. were there a fight, misunderstanding or you said something hurtful?&quot;)
                print(&quot;3. have you done something you regret now?&quot;)
                print(&quot;4. did you miss opportunities to be with them?&quot;)
                relaChoiceB = input(&quot;\nChoose an option (1/2/3/4): &quot;)

                if relaChoiceB not in [&quot;1&quot;, &quot;2&quot;, &quot;3&quot;, &quot;4&quot;]:
                    print(&quot;\nI don&#39;t understand you... Try again please.&quot;)
                    continue

                if relaChoiceB == &quot;1&quot;:
                    print(&quot;being aware that they are somewhere in the world and not being in touch with them can be hurtful.&quot;)
                    describing = input(&quot;\nhow would you describe your problem? &quot;)
                    print(&quot;I&#39;ve fixed your relationship now. look into your messages!&quot;)
                    print(&quot;though, will it actually make things better, or just create new challenges what you dont know about yet? &quot;)
                    return

                if relaChoiceB == &quot;2&quot;:
                    print(&quot;words can hurt...&quot;)
                    describing = input(&quot;\nhow would you describe your problem? &quot;)
                    print(&quot;I&#39;ve fixed your relationship now. look into your messages!&quot;)
                    print(&quot;though, will it actually make things better, or just create new challenges what you dont know about yet? &quot;)
                    return

                if relaChoiceB == &quot;3&quot;:
                    print(&quot;actions speak louder than words, dont they?&quot;)
                    describing = input(&quot;\nhow would you describe your problem? &quot;)
                    print(&quot;I&#39;ve fixed your relationship now. look into your messages!&quot;)
                    print(&quot;though, will it actually make things better, or just create new challenges what you dont know about yet? &quot;)
                    return

                if relaChoiceB == &quot;4&quot;:
                    print(&quot;being aware that they are somewhere in the world and not being in touch with them can be hurtful.&quot;)
                    describing = input(&quot;\nhow would you describe your problem? &quot;)
                    print(&quot;though, will it actually make things better? or just create new challenges what you dont know about yet? &quot;)
                    return

            # HEALTH
            elif decision_choice == &quot;2&quot;:
                print(&quot;\nlet&#39;s make things nice and healthy again!&quot;)
                print(&quot;\nwas it about your physical or mental health?&quot;)
                print(&quot;1. Physical health&quot;)
                print(&quot;2. Mental health&quot;)
                healChoiceA = input(&quot;\nChoose an option (1/2): &quot;)

                if healChoiceA not in [&quot;1&quot;, &quot;2&quot;]:
                    print(&quot;\nI don&#39;t understand you... Try again please.&quot;)
                    continue

                if healChoiceA == &quot;1&quot;:
                    print(&quot;was is a lifestyle choice or a one-time decision?&quot;)
                    print(&quot;1. Lifestyle choice&quot;)
                    print(&quot;2. One-time decision&quot;)
                    healChoiceAA = input(&quot;\nChoose an option (1/2): &quot;)

                    if healChoiceAA not in [&quot;1&quot;, &quot;2&quot;]:
                        print(&quot;\nI don&#39;t understand you... Try again please.&quot;)
                        continue

                    if healChoiceAA == &quot;1&quot;:
                        print(&quot;it&#39;s not always easy to stay consistent in healthy lifestyle.&quot;)
                        describing = input(&quot;\nhow would you describe your problem? &quot;)
                        print(&quot;i&#39;ve just fixed your unhealthy life-style habits.&quot;)
                        print(&quot;however, do you think it will be easy to keep your new healthy habits in your life when you didnt learn how to build them step by step?&quot;)
                        return

                    if healChoiceAA == &quot;2&quot;:
                        print(&quot;1. oh noo.. have you eaten or drank anything unhealthy again?&quot;)
                        print(&quot;2. were you being silly and your crazy ideas hurt you?&quot;)
                        print(&quot;3. have you done anything else that harmed your body?&quot;)
                        healChoiceB = input(&quot;\nChoose an option (1/2/3): &quot;)

                        if healChoiceB not in [&quot;1&quot;, &quot;2&quot;, &quot;3&quot;]:
                            print(&quot;\nI don&#39;t understand you... Try again please.&quot;)
                            continue

                        describing = input(&quot;\nhow would you describe your problem? &quot;)
                        print(&quot;look and feel your body now! isn&#39;t it better?&quot;)
                        print(&quot;but will you be really more careful next time without this experience?&quot;)
                        return

                # Mental health option
                elif healChoiceA == &quot;2&quot;:
                    print(&quot;properly understanding our mental health is often a long-term journey.&quot;)
                    print(&quot;do you think it was a lifestyle choice or a one-time decision?&quot;)
                    print(&quot;1. Lifestyle choice&quot;)
                    print(&quot;2. One-time decision&quot;)
                    healChoiceB = input(&quot;\nChoose an option (1/2): &quot;)

                    if healChoiceB not in [&quot;1&quot;, &quot;2&quot;]:
                        print(&quot;\nI don&#39;t understand you... Try again please.&quot;)
                        continue

                    if healChoiceB == &quot;1&quot;:
                        print(&quot;it&#39;s not always easy to learn effective methods of dealing with your mental health.&quot;)
                        describing = input(&quot;\nhow would you describe your problem? &quot;)
                        print(&quot;feel what is happening in your mind right now! isn&#39;t it better like this?&quot;)
                        print(&quot;however, do you think it will be easy to keep your new healthy habits in your life when you didnt learn how to build them step by step?&quot;)
                        return

                    if healChoiceB == &quot;2&quot;:
                        print(&quot;thank you for sharing.&quot;)
                        print(&quot;1. have you stayed in traumatizing situation for too long?&quot;)
                        print(&quot;2. have you harmed yourself or you are just dying of suicide attempt?&quot;)
                        print(&quot;3. have you done anything different what caused problems to your mental health?&quot;)
                        healChoiceBA = input(&quot;\nChoose an option (1/2/3): &quot;)

                        if healChoiceBA not in [&quot;1&quot;, &quot;2&quot;, &quot;3&quot;]:
                            print(&quot;\nI don&#39;t understand you... Try again please.&quot;)
                            continue

                        if healChoiceBA == &quot;1&quot;:
                            describing = input(&quot;\nhow would you describe your problem? &quot;)
                            print(&quot;i&#39;ve just modified your past to feel better. doesn&#39;t it?&quot;)
                            print(&quot;do you have anything that will protect you from similar situations in the future though?&quot;)
                            return

                        if healChoiceBA == &quot;2&quot;:
                            describing = input(&quot;\nhow would you describe your problem? &quot;)
                            print(&quot;look! i&#39;ve just erased all marks of your actions on your body. feel free to enjoy your new you again!&quot;)
                            print(&quot;just... don&#39;t you think it&#39;s more as cosmetics repair in contrast to your much deeper reasons for doing it?&quot;)
                            return

                        if healChoiceBA == &quot;3&quot;:
                            describing = input(&quot;\nhow would you describe your problem? &quot;)
                            print(&quot;i&#39;ve just modified your past to feel better. doesn&#39;t it?&quot;)
                            print(&quot;do you have anything that will protect you from similar situations in the future though?&quot;)
                            return

            # MONEY
            elif decision_choice == &quot;3&quot;:
                print(&quot;\n money, money, money... that can be a sensitive topic. let’s see how we can fix this together.&quot;)
                print(&quot;have you spent your money unwisely or you missed a good investment opportunity?&quot;)
                print(&quot;1. Unwisely spent money&quot;)
                print(&quot;2. Missed investment opportunity&quot;)
                moneyChoiceA = input(&quot;\nChoose an option (1/2): &quot;)

                if moneyChoiceA not in [&quot;1&quot;, &quot;2&quot;]:
                    print(&quot;\nI don&#39;t understand you... Try again please.&quot;)
                    continue

                if moneyChoiceA == &quot;1&quot;:
                    print(&quot;thank you. it&#39;s not always easy to manage finances perfectly.&quot;)
                    print(&quot;what was the main problem with your investment?&quot;)
                    print(&quot;1. have you bought something that you didn&#39;t need?&quot;)
                    print(&quot;2. do you struggle with long-term healthy financial habits?&quot;)
                    print(&quot;3. have you spent money that was not yours?&quot;)
                    print(&quot;4. did you end up in debt?&quot;)
                    print(&quot;5. do you have a different issue with your spent money?&quot;)
                    moneyChoiceB = input(&quot;\nChoose an option (1–5): &quot;)

                    if moneyChoiceB not in [&quot;1&quot;, &quot;2&quot;, &quot;3&quot;, &quot;4&quot;, &quot;5&quot;]:
                        print(&quot;\nI don&#39;t understand you... Try again please.&quot;)
                        continue

                    describing = input(&quot;\nthank you. and how did you spend them? or how would you describe your problem? &quot;)
                    print(&quot;i&#39;ve just restored your bank account, feel free to look!&quot;)
                    print(&quot;do you think this will help you to gain healthy financial habits though?&quot;)
                    return

                if moneyChoiceA == &quot;2&quot;:
                    print(&quot;thank you. it&#39;s not always easy to manage finances perfectly.&quot;)
                    describing = input(&quot;\nwhat chance have you missed? or how would you describe your problem? &quot;)
                    print(&quot;i&#39;ve just modified your past and your opportunities are back on the table now, feel free to look!&quot;)
                    print(&quot;though, do you think you will recognize the right investments in the future?&quot;)
                    return

            # CAREER
            elif decision_choice == &quot;4&quot;:
                print(&quot;\nyeah... finding a perfect career is not the easiest task under the sun. but I can help you with that.&quot;)
                print(&quot;was it about the job you took or a chance you missed?&quot;)
                print(&quot;1. Job I took&quot;)
                print(&quot;2. Chance I missed&quot;)
                careerChoiceA = input(&quot;\nChoose an option (1/2): &quot;)

                if careerChoiceA not in [&quot;1&quot;, &quot;2&quot;]:
                    print(&quot;\nI don&#39;t understand you... Try again please.&quot;)
                    continue

                if careerChoiceA == &quot;1&quot;:
                    print(&quot;1. have you stopped seeing meaning in your career path or you lost interest in it?&quot;)
                    print(&quot;2. did you have different expectations of your job?&quot;)
                    print(&quot;3. is doing your job connected to anything uncomfortable?&quot;)
                    print(&quot;4. do you have other reasons why you regret being in your job?&quot;)
                    careerChoiceB = input(&quot;\nChoose an option (1/2/3/4): &quot;)

                    if careerChoiceB not in [&quot;1&quot;, &quot;2&quot;, &quot;3&quot;, &quot;4&quot;]:
                        print(&quot;\nI don&#39;t understand you... Try again please.&quot;)
                        continue

                    print(&quot;I&#39;ve just fixed your career path to feel better. can you already see the new opportunities?&quot;)
                    print(&quot;however, if you wouldn&#39;t have gained these experiences from the job, would you even know that you don&#39;t want to do work like this?&quot;)
                    return

                if careerChoiceA == &quot;2&quot;:
                    print(&quot;1. do you regret this missed change because of vision of fulfilling your dream?&quot;)
                    print(&quot;2. do you regret this missed change because of vision of a good salary?&quot;)
                    print(&quot;3. do you regret this missed change because of vision of a nice work environment?&quot;)
                    print(&quot;4. do you regret this missed change because of something else?&quot;)
                    careerChoiceB = input(&quot;\nChoose an option (1/2/3/4): &quot;)

                    if careerChoiceB not in [&quot;1&quot;, &quot;2&quot;, &quot;3&quot;, &quot;4&quot;]:
                        print(&quot;\nI don&#39;t understand you... Try again please.&quot;)
                        continue

                    print(&quot;I&#39;ve just fixed your career path to feel better. can you already see the new opportunities?&quot;)
                    return

                # EDUCATION
                if decision_choice == &quot;5&quot;:
                    print(&quot;\n...&quot;)
                    print(&quot;was it about something you didn&#39;t learn, or do you regret something you studied?&quot;)
                    print(&quot;1. Something I didn&#39;t learn.&quot;)
                    print(&quot;2. Something I studied.&quot;)
                    eduChoiceA = input(&quot;\nChoose an option (1/2): &quot;)
                    if eduChoiceA == &quot;1&quot;:
                        print(&quot;it&#39;s never too late to learn! but let’s see how I can help.&quot;)
                        print(&quot;1. did you miss the opportunity to study?&quot;)
                        print(&quot;2. do you regret dropping out of school?&quot;)
                        print(&quot;3. do you regret failing in your study or you lack skills that you need right now?&quot;)
                        eduChoiceB = input(&quot;\nChoose an option (1/2/3): &quot;)
                        if eduChoiceB == &quot;1&quot; or eduChoiceB == &quot;2&quot; or eduChoiceB == &quot;3&quot;:
                            describing = input(&quot;\nhow would you describe your problem? &quot;)
                            print(&quot;I&#39;ve just brang your opportunities back on the table. can you already see your new chances?&quot;)
                            print(&quot;however, would you have known your true priorities without exploring your previous choice?&quot;)
                            return

                    elif eduChoiceA == &quot;2&quot;:
                        print(&quot;regretting something we studied in not uncommon. let’s see how I can help.&quot;)
                        print(&quot;why do you regret your education choice? what have you studied?&quot;)
                        print(&quot;1. something what doesn&#39;t interest me.&quot;)
                        print(&quot;2. something what I cannot use in the future.&quot;)
                        print(&quot;3. something what others wanted me to study.&quot;)
                        print(&quot;4. I regret my education choice from different reason.&quot;)
                        eduChoiceB = input(&quot;\nChoose an option (1/2/3/4): &quot;)
                        if eduChoiceB == &quot;1&quot; or eduChoiceB == &quot;2&quot; or eduChoiceB == &quot;3&quot; or eduChoiceB == &quot;4&quot;:
                            describing = input(&quot;\nhow would you describe your problem? &quot;)
                            print(&quot;I&#39;ve just brang your opportunities back on the table. can you already see your new chances?&quot;)
                            print(&quot;however, would you have known your true priorities and interests without exploring your previous choice?&quot;)
                            return

                # MORALITY AND VALUES
                elif decision_choice == &quot;6&quot;:
                    print(&quot;\nmorality... yeah, sometimes feels like trying to find a way out of a maze. but if you’re starting to feel bad about something, it’s a sign there’s something going on inside you.&quot;)
                    print(&quot;1. were you being selfish or unfair?&quot;)
                    print(&quot;2. did you lie or manipulate others?&quot;)
                    print(&quot;3. did you refuse taking responsibility for your mistakes or shift the blame to others?&quot;)
                    print(&quot;4. did you betray anyone?&quot;)
                    print(&quot;5. were you being too nice or deny your own values because of others?&quot;)
                    print(&quot;6. have you done anything else related to your values?&quot;)
                    moralChoiceA = input(&quot;\nChoose an option (1–6): &quot;)
                    if moralChoiceA == &quot;1&quot; or moralChoiceA == &quot;2&quot; or moralChoiceA == &quot;3&quot; or moralChoiceA == &quot;4&quot; or moralChoiceA == &quot;6&quot;:
                        print(&quot;no matter how bad thing you did, it&#39;s great that you realized your mistakes and you want to make the situation better.&quot;)
                        describing = input(&quot;\nhow would you describe what happened? &quot;)
                        print(&quot;all your behavior has been undone! feel free to check it out yourself.&quot;)
                        print(&quot;however, do you really feel better and fair when you didn&#39;t undo your action yourself?&quot;)
                        return

                    elif moralChoiceA == &quot;5&quot;:
                        print(&quot;sometimes it&#39;s difficult to recognize your boundaries and decide what is the best thing to do.&quot;)
                        describing = input(&quot;\nhow would you describe what happened? &quot;)
                        print(&quot;I&#39;ve just undone your previous behavior. enjoy your new start!&quot;)
                        print(&quot;however, would you even recognize your boundaries if you wouldn&#39;t have chances to learn it?&quot;)
                        return

                # CRIMES
                elif decision_choice == &quot;7&quot;:
                    print(&quot;\nso you have a shady past, huh? life paths can be tricky and lead to shady places sometimes.&quot;)
                    print(&quot;was it something minor or serious?&quot;)
                    print(&quot;1. Minor&quot;)
                    print(&quot;2. Serious&quot;)
                    crimeChoiceAA = input(&quot;\nChoose an option (1/2): &quot;)
                    if crimeChoiceAA == &quot;1&quot;:
                        print(&quot;it&#39;s always great to be honest with yourself.&quot;)
                        print(&quot;1. did you steal anything?&quot;)
                        print(&quot;2. did you vandalize or damage property?&quot;)
                        print(&quot;3. did you commit any minor scam for personal gain?&quot;)
                        print(&quot;4. did you commit any driving offense?&quot;)
                        print(&quot;5. did you commit any other minor crime?&quot;)
                        crimeChoiceAAA = input(&quot;\nChoose an option (1/2/3/4/5): &quot;)
                        if crimeChoiceAAA == &quot;1&quot;:
                            describing = input(&quot;\nthank you for saying. how would you describe what you have done? &quot;)
                            print(&quot;your actions are undone now! you can safely look into eyes of the people you have been stealing from.&quot;)
                            print(&quot;do you really feel better inside yourself though, when you didn&#39;t undo your action yourself?&quot;)
                            return

                        elif crimeChoiceAAA == &quot;2&quot;:
                            describing = input(&quot;\nthank you for saying. how would you describe what you have done? &quot;)
                            print(&quot;your actions are undone now! you can safely look into eyes of the people whose property you have damaged.&quot;)
                            print(&quot;do you really feel better inside yourself though, when you didn&#39;t undo your action yourself?&quot;)
                            return

                        elif crimeChoiceAAA == &quot;3&quot;:
                            describing = input(&quot;\nthank you for saying. how would you describe what you have done? &quot;)
                            print(&quot;your actions are undone now! you can safely look into eyes of the people you have scammed.&quot;)
                            print(&quot;do you really feel better inside yourself though, when you didn&#39;t undo your action yourself?&quot;)
                            return

                        elif crimeChoiceAAA == &quot;4&quot;:
                            print(&quot;thank you for saying. just hope the others survived your ride.&quot;)
                            describing = input(&quot;\nhow would you describe what you have done? &quot;)
                            print(&quot;your actions are undone now!&quot;)
                            print(&quot;do you really feel better inside yourself though, when you didn&#39;t undo your action yourself?&quot;)
                            return

                        elif crimeChoiceAAA == &quot;5&quot;:
                            describing = input(&quot;\nthank you for saying. how would you describe what you have done? &quot;)
                            print(&quot;your actions are undone now!&quot;)
                            print(&quot;do you really feel better inside yourself though, when you didn&#39;t undo your action yourself?&quot;)
                            return

                    elif crimeChoiceAA == &quot;2&quot;:
                        print(&quot;it&#39;s always great to be honest with yourself.&quot;)
                        print(&quot;1. were you into drugs, man?&quot;)
                        print(&quot;2. were you involved in any large financial fraud?&quot;)
                        print(&quot;3. did you harm or kill anyone?&quot;)
                        print(&quot;4. did you sexually assault or rape anyone?&quot;)
                        print(&quot;5. were you involved in human trafficking?&quot;)
                        print(&quot;6. were you involved in human or animal torturing?&quot;)
                        print(&quot;7. did you commit any other serious crimes?&quot;)
                        crimeChoiceAB = input(&quot;\nChoose an option (1–7):&quot;)
                        if crimeChoiceAB == &quot;1&quot;:
                            describing = input(&quot;\nhow would you describe what you have done? &quot;)
                            print(&quot;okay well... no problem.&quot;)
                            print(&quot;i&#39;ve just undone your drug past!&quot;)
                            print(&quot;do you truly feel better inside yourself though?&quot;)
                            return

                        elif crimeChoiceAB == &quot;2&quot;:
                            describing = input(&quot;\nhow would you describe what you have done? &quot;)
                            print(&quot;okay well... no problem.&quot;)
                            print(&quot;i&#39;ve just undone your actions!&quot;)
                            print(&quot;do you truly feel better inside yourself though?&quot;)
                            return

                        elif crimeChoiceAB == &quot;3&quot;:
                            describing = input(&quot;\nhow would you describe what you have done? &quot;)
                            print(&quot;okay well... no problem.&quot;)
                            print(&quot;i&#39;ve just undone your actions! you can safely look into eyes of the people you have harmed or killed.&quot;)
                            print(&quot;do you truly feel better inside yourself though?&quot;)
                            return

                        elif crimeChoiceAB == &quot;4&quot;:
                            describing = input(&quot;\nhow would you describe what you have done? &quot;)
                            print(&quot;okay well... no problem.&quot;)
                            print(&quot;i&#39;ve just undone your actions! you can safely look into eyes of the people you have sexually abused.&quot;)
                            print(&quot;do you feel truly better and fair inside yourself though? does it help you now that you know what you&#39;re capable of?&quot;)
                            return

                        elif crimeChoiceAB == &quot;5&quot;:
                            describing = input(&quot;\nhow would you describe what you have done? &quot;)
                            print(&quot;okay well... no problem.&quot;)
                            print(&quot;i&#39;ve just undone your actions! you can safely look into eyes of the people you have harmed.&quot;)
                            print(&quot;do you truly feel better and fair inside yourself though? does it help you now that you know what you&#39;re capable of?&quot;)
                            return

                        elif crimeChoiceAB == &quot;6&quot;:
                            describing = input(&quot;\nhow would you describe what you have done? &quot;)
                            print(&quot;okay well... no problem.&quot;)
                            print(&quot;i&#39;ve just undone your actions! you can safely look into eyes of the people and animals whose lives you turned into hell.&quot;)
                            print(&quot;do you truly feel better and fair inside yourself though? does it help you now that you know what you&#39;re capable of?&quot;)
                            return

                        elif crimeChoiceAB == &quot;7&quot;:
                            describing = input(&quot;\nhow would you describe what you have done? &quot;)
                            print(&quot;okay well... no problem.&quot;)
                            print(&quot;i&#39;ve just undone your actions!&quot;)
                            print(&quot;do you truly feel better inside yourself though?&quot;)
                            return

                else:
                    print(&quot;\nI don&#39;t understand you... Try again please.&quot;)

            # TIME LOSS
                    if decision_choice == &quot;8&quot;:
                        print(&quot;\nnobody can escape the flow of time... they said! let’s see how we can play with it.&quot;)
                        print(&quot;why do you feel sorry about your passed time?&quot;)
                        print(&quot;1. I just missed my last connection, dammit.&quot;)
                        print(&quot;2. I have spend too much time on videogames and social media and now I can&#39;t do my work for tomorrow.&quot;)
                        print(&quot;3. I always said &#39;maybe later&#39; to my dreams and now I feel like it’s too late.&quot;)
                        print(&quot;4. I have given my time to wrong people or wrong work.&quot;)
                        print(&quot;5. I have lost the best years of my life with focusing on silly things.&quot;)
                        print(&quot;6. I dont have enough time already to be with people I love.&quot;)
                        print(&quot;7. I feel sorry about something else related to my passed time.&quot;)
                        timeLossChoice = input(&quot;\nChoose an option (1–7): &quot;)

                        if timeLossChoice == &quot;1&quot;:
                            print(&quot;oh noo!&quot;)
                            describing = input(&quot;\nwhere you wanted to go? or how would you describe your problem? &quot;)
                            print(&quot;you have plenty of time to catch your connection now. check on your time!&quot;)
                            print(&quot;will you be more careful next time in more important situation though?&quot;)
                            continue

                        if timeLossChoice == &quot;2&quot;:
                            print(&quot;oh noo!&quot;)
                            describing = input(&quot;\nwhat do you need to do for tomorrow? or how would you describe your problem? &quot;)
                            print(&quot;you have plenty of time to do your work now. check on your time!&quot;)
                            print(&quot;however, do you think it will be easy to keep health time-management habits when you didnt learn how to build them step by step?&quot;)
                            continue

                        if timeLossChoice == &quot;3&quot;:
                            print(&quot;oh noo!&quot;)
                            describing = input(&quot;\nhow would you describe your problem? &quot;)
                            print(&quot;I&#39;ve just restored your lost time. check on the date!&quot;)
                            print(&quot;however, what would be exactly stopping you from fulfilling your dreams without my help?&quot;)
                            continue

                        if timeLossChoice == &quot;4&quot;:
                            print(&quot;oh noo!&quot;)
                            describing = input(&quot;\nhow would you describe your problem? &quot;)
                            print(&quot;I&#39;ve just restored your lost time. check on the date!&quot;)
                            print(&quot;however, how would you know that it is wrong without experiencing it?&quot;)
                            continue

                        if timeLossChoice == &quot;5&quot;:
                            print(&quot;oh noo!&quot;)
                            describing = input(&quot;\nhow would you describe your problem? &quot;)
                            print(&quot;I&#39;ve just restored your lost time. check on the date!&quot;)
                            print(&quot;though, how can you know those were the best years?&quot;)
                            continue

                        if timeLossChoice == &quot;6&quot;:
                            print(&quot;oh noo!&quot;)
                            describing = input(&quot;\nwho do you wish to spend more time with? or how would you describe your problem? &quot;)
                            print(&quot;I&#39;ve just restored your time for spending it with your loved ones. check on the date!&quot;)
                            print(&quot;do you think this will change your approach to the time in the future?&quot;)
                            continue

                        if timeLossChoice == &quot;7&quot;:
                            print(&quot;oh noo!&quot;)
                            describing = input(&quot;\nhow would you describe your regret about time? &quot;)
                            print(&quot;your lost time has been restored. check on the date!&quot;)
                            print(&quot;do you think this will change your approach to the time in the future?&quot;)
                            continue

                    else:
                        print(&quot;\nI don&#39;t understand you... Try again please.&quot;)
                        continue

        elif choice == &quot;2&quot;:
            print(&quot;\nbeing a little bit curious about new things is always good.&quot;)
            print(&quot;if you would like to take some of your decisions back someday, you know where to find me.&quot;)
            return

        elif choice == &quot;3&quot;:
            print(&quot;\nlucky guy...&quot;)
            return

        else:
            print(&quot;\nI don&#39;t understand you... Try again please.&quot;)
            continue

# Spuštění aplikace
backtaker()</div>
      

      <div id="id_ide_console">
        
          <iframe src="/user/janova/consoles/37648795/frame/" id="id_console" name="console" class="soft_keyboard_sensitive">
          </iframe>
        
      </div>

    </div>

    <div id="id_go_to_line_dialog" class="pa_hidden">
      <p class="form-inline">Line number: <input id="id_go_to_line_dialog_input" /></p>
      <div class="dialog_buttons">
        <button class="btn btn-default" id="id_go_to_line_dialog_ok_button">Go</button>
        <button class="btn btn-default" id="id_go_to_line_dialog_close_button">Close</button>
      </div>
    </div>

    <div id="id_file_changed_on_disk" class="pa_hidden">
      <p>Are you sure you want to save it?  Alternatively, you could re-open it in a new tab to check differences</p>
      <div class="dialog_buttons">
        <button id="id_force_save" class="btn btn-danger">Force Save</button>
        <button id="id_cancel_save" class="btn btn-default">Cancel</button>
      </div>
    </div>

    <div id="id_save_as_dialog" class="pa_hidden">
      <form class="form-inline">
        <div class="form-group">
          <label for="id_save_as_path">Please enter a path:</label>
          <input id="id_save_as_path" class="form-control" style="width: 100%;" />
        </div>
        <img id="id_save_as_spinner" class="spinner pa_hidden" src="/static/anywhere/images/spinner-small.gif" />
        <p>
          <span id="id_save_as_error" class="error_message"></span>
        </p>
        <div class="dialog_buttons">
          <button id="id_save_as_ok" type="submit" class="btn btn-primary">Save</button>
          <button id="id_save_as_cancel" type="button" class="btn btn-default">Cancel</button>
        </div>
      </form>
    </div>

    <div class="modal fade" id="id_file_sharing_modal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title" id="myModalLabel">File Sharing options</h4>
          </div>
          <div class="modal-body">
            <div id="id_file_sharing_options"></div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>

  </div>


        
      </div>

        


        <div id="id_feedback_dialog" title="Help us improve" style="display:none">
    <div id="id_feedback_dialog_blurb_big" class="dialog_blurb_big">
        It's always a pleasure to hear from you!
    </div>
    <div id="id_feedback_dialog_blurb_small">
        Ask us a question, or tell us what you love or hate about PythonAnywhere.<br/>
        We'll get back to you over email ASAP.
    </div>
    <textarea id="id_feedback_dialog_text" rows="6"></textarea>
    <input id="id_feedback_dialog_email_address" type="text" placeholder="Email address (optional - only necessary if you would like us to contact you)"/>
    
    <div id="id_feedback_dialog_error" style="display: none">
        Sorry, there was an error connecting to the server. <br/>Please try again in a few moments...
    </div>
    <div id="id_feedback_dialog_rate_limit_error" style="display: none">
        Sorry, we have had to rate-limit your feedback sending.<br/>Please try again in a few moments...
    </div>
    <div id="id_feedback_dialog_success" style="display: none">
        Thanks for the feedback! Our tireless devs will get back to you soon.
    </div>
    <div class="dialog_buttons">
        <img id="id_feedback_dialog_spinner" src="/static/anywhere/images/spinner-small.gif" />
        <button class="btn btn-primary" id="id_feedback_dialog_ok_button">OK</button>
        <button class="btn btn-default" id="id_feedback_dialog_cancel_button">Cancel</button>
    </div>
    <div id="id_feedback_dialog_only_close_button" style="display: none">
        <button class="btn btn-primary" id="id_feedback_dialog_close_button">Close</button>
    </div>
</div>


        
        <!-- preload font awesome fonts to avoid glitch when switching icons -->
        <div style="width: 0; height: 0; overflow: hidden"><i class="fa fa-square-o fa-3x" ></i></div>
    </body>
</html>
