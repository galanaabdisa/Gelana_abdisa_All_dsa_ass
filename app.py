import streamlit as st

# Define the correct username and password
USERNAME = "gelanaabdisa"
PASSWORD = "galoo"

# Ask the user to enter the username and password
username = st.sidebar.text_input("Enter your username")
password = st.sidebar.text_input("Enter your password", type="password")

# Check if the entered username and password are correct
if username == USERNAME and password == PASSWORD:
    st.title("Welcome To Your ")
    
    #  Streamlit code
    import streamlit as st
    import pandas as pd 
    from matplotlib import pyplot as plt
    from plotly import graph_objs as go
    from sklearn.linear_model import LinearRegression
    import numpy as np 


    data = pd.read_csv("Salary_Data.csv")

    x = np.array(data['year_exp']).reshape(-1,1)
    lr = LinearRegression()
    lr.fit(x,np.array(data['sal']))


    st.title("Salary Prediction Based On Experience App")
    #st.image("nota.jpeg",width = 400)
    menu = st.sidebar.radio("**MENU**",["Home","Prediction","Contribute","About us", "Comment","How to use"])
    if menu=="About us":
        
        abt=st.sidebar.selectbox("What do you want to know about us? Select one!",["None","Coverpage","About the dataset", "Advisor","Author"],index=0)
        if abt=="Coverpage":
            st.header("JIMMA UNIVERSITY")
            st.subheader("INSTITUTE OF TECHNOLOGY")
            st.subheader("FACULTY OF COMPUTING AND INFORMATICS")
            st.subheader("ARTIFICIAL INTELLIGENCE PROGRAM")
            st.subheader("PROJECT OF DATA SCINCE AND ANLYTICS")
            st.subheader("TITLE: A STREAMLIT BASED DATA VISUALIZATION DASHBOARD: *SALARY PREDICTION BASED ON EXPERIENCE*")
            st.subheader("BY: GELANA ABDISA ")
            st.subheader("ID: RM0205/15")
            st.subheader(" SUBMITTED TO: GELATAW SAHLE *(PHD CANDIDATE)*")
        elif abt=="About the dataset":
            st.write("The dataset was received from kaggle dataset repositry. originaly the data set was with 29 rows only, but now it is being enlarged by contributors, like me and you")
        elif abt== "Advisor":
            st.subheader(" I was advised by Gelataw Sahle (PHD candidate)")
        elif abt== "Author":
            st.subheader("By: Gelana Abdisa(AI Msc, student)")

        
    if menu == "Home":
        a= st.date_input("SUBMISSION DATE")
        st.write("submitted on", a)
        st.image("nota.jpeg",width = 400)
        part= st.selectbox("Show the Dataset",["Not at all","See all dataset","Original Dataset","Contributed Dataset", "The first five rows only"], index=0)
        if part == "Not at all":
            st.subheader("Enjoy The Home's media")
        if part== "See all dataset":
            
            st.table(data)
        if part== "The first five rows only":
            df= pd.DataFrame(data)
            a= df.head()
            st.write(a)
        if part=="Original Dataset":
            df= pd.DataFrame(data)
            a=df.head(30)
            st.table(a)
        elif part == "Contributed Dataset":
            df=pd.DataFrame(data)
            a=df.tail(29)
            st.write(a)

        
        
        
        graph = st.selectbox("What kind of Graph do you need ? ",["None","Non-Interactive","Interactive"], index=0)
        fig, ax = plt.subplots() # I added this to correct some error
        #val = st.slider("Filter data using years",0,20)
        #data = data.loc[data["year_exp"]>= val]
        if graph == "Non-Interactive":
            val = st.slider("Filter data using years",0,20)
            data = data.loc[data["year_exp"]>= val]
        
        
        
            plt.figure(figsize = (10,5))
            ax.scatter(data["year_exp"],data["sal"]) # this will run with ax. only note plt
            plt.ylim(0)
            plt.xlabel("Years of Experience")
            plt.ylabel("Salary")
            plt.tight_layout()
            st.pyplot(fig)
        

        if graph == "Interactive":
            val = st.slider("Filter data using years",0,20)
            data = data.loc[data["year_exp"]>= val]

            
            layout =go.Layout(
                xaxis = dict(range=[0,16]),
                yaxis = dict(range =[0,210000])
            )
            
            fig = go.Figure(data=go.Scatter(x=data["year_exp"], y=data["sal"], mode='markers'),layout = layout)
            st.plotly_chart(fig)
        if graph== "None":
            st.markdown("No Dataset found here!!")

        
    if menu == "Prediction":
        st.header("Predict  your Salary")
        val = st.number_input("Please, Enter you experience",0.00,20.00,step = 0.25)
        val = np.array(val).reshape(1,-1)
        pred =lr.predict(val)[0]

        if st.button("Predict"):
            st.success(f"Your predicted salary is:  {round(pred)}")

    if menu == "Contribute":
        st.header("Contribute to our dataset")
        ex = st.number_input("Enter your Experience",0.0,50.0)
        sal = st.number_input("Enter your Salary",0.00,1000000.00,step = 1000.0)
        if st.button("submit"):
            to_add = {"year_exp":[ex],"Salary":[sal]}
            to_add = pd.DataFrame(to_add)
            to_add.to_csv("Salary_Data.csv",mode='a',header = False,index= False)
            st.success("Submitted")
    if menu== "Comment":
        cmnt=st.text_area(" Feel free to write comment in the space provided below ")
        st.write(cmnt)



    if menu=="How to use":
        st.write("The following is elaboration about each menu")
        desc=st.sidebar.selectbox("Read the Guideline please!",["None","Coverpage","About the dataset", "Contribute","Prediction", "Comment", "About us"],index=0)
        if desc=="Home":
            st.write("This is the page where you navigate through the dataset and it is also where  you select the graph type, either interactive of non-Interactive graph ")
        if desc=="Coverpage":
            st.write("This page Is silmply the coverpage ")
        if desc=="Contribute":
            st.write("This is the page where you can contribute to the dataset simply by adding your expereinec and your salary in the space provided ")
        if desc=="Prediction":
            st.write("This is the page where our system can predict your salary when you tell it your experience ")
        if desc=="Comment":
            st.write("This page enables you to write comment about the dashboard ")
        if desc=="About us":
            st.write("This page Tells you general inforamtion about the dashboard ")
    




    
else:
    st.write("Sorry, the username and/or password you entered is incorrect.")