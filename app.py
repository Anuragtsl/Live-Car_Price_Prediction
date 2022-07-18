import pickle
import streamlit as st
import datetime as dt
import pyautogui


# load model
pickle_in = open('file.pkl','rb')
model = pickle.load(pickle_in)

@st.cache()

def prediction(present_price, kms_driven, owner, tot_year, fuel_type, seller_type, transmission):
    
    tot_year = dt.datetime.now().year - tot_year
    
    # if loop for assigning numerical values
    if fuel_type == "Petrol":
        fuel_P = 1
        fuel_D = 0
    else:
        fuel_P = 0
        fuel_D = 1
        
    # assigning numerical values
    if transmission == "Manual":
        transmission_manual = 1
    else:
        transmission_manual = 0
        
    if seller_type == "Individual":
        seller_individual = 1
    else:
        seller_individual = 0
    
    values = [[
        present_price,
        kms_driven,
        owner,
        tot_year,
        fuel_D,
        fuel_P,
        seller_individual,
        transmission_manual
      ]]
    
    # created a list of all the user inputed values, then using it for prediction
    if present_price==0:
        pred = 0
        return pred
    else:
        pred = model.predict(values)
        pred = round(pred[0],2)
        if pred > present_price:
            pred = present_price
            return pred
        else:
            return pred
    # returning the predicted value
    


# front end elements of the web page 
# html_temp = """ 
#     <div style ="background-color:yellow;padding:13px"> 
#     <h1 style ="color:black;text-align:center;">Car Price Prediction App</h1>
#     </div>
#     <div>
#         <br>
#     </div>
#   """
      
# display the front end aspect
st.markdown(
         f"""
        <body>
         <style>
         .stApp {{
             background-image: url("https://2684054.fs1.hubspotusercontent-na1.net/hub/2684054/hubfs/shutterstock_1461768662.jpg?width=800&name=shutterstock_1461768662.jpg");
             background-attachment: fixed;
             background-size: 100% 100%;
             background-repeat: no-repeat;
         }}
         </style>
      <div>
        <h1 style="color:red;font-size:50px;text-align: center;top: 50%;left: 50%;font-family:sans-serif;" >Car Price Prediction</h1>
            <h4 style="color:red;text-align: center;top: 50%;left: 50%;font-family:Papyrus;">Predict your old car price accordingly.</h4>
            <h4 style="color:red;text-align: center;top: 50%;left: 50%; font-family:cursive;">By Anurag Toshniwal</h4>
      </body>
      """,
    unsafe_allow_html=True)

    
# following lines create boxes in which user can enter data required to make prediction 

tot_year = st.selectbox('𝐘𝐞𝐚𝐫', range(2000, dt.datetime.now().year+1))
present_price = st.number_input('𝐂𝐚𝐫 𝐒𝐡𝐨𝐰𝐫𝐨𝐨𝐦 𝐏𝐫𝐢𝐜𝐞-(𝐢𝐧 𝐋𝐚𝐤𝐡𝐬)', min_value=0.00)
kms_driven = st.number_input('𝐊𝐢𝐥𝐨𝐦𝐞𝐭𝐞𝐫𝐬 𝐝𝐫𝐢𝐯𝐞𝐧', min_value=0.00)
owner = st.number_input('𝐍𝐮𝐦𝐛𝐞𝐫 𝐨𝐟 𝐭𝐡𝐞 𝐩𝐫𝐞𝐯𝐢𝐨𝐮𝐬 𝐨𝐰𝐧𝐞𝐫𝐬', min_value=0, step=1)
fuel_type = st.selectbox('𝐅𝐮𝐞𝐥 𝐭𝐲𝐩𝐞',('Petrol', 'Diesel'))
seller_type = st.selectbox('𝐀𝐫𝐞 𝐲𝐨𝐮, 𝐃𝐞𝐚𝐥𝐞𝐫 𝐨𝐫 𝐚𝐧 𝐈𝐧𝐝𝐢𝐯𝐢𝐝𝐮𝐚𝐥',('Dealer', 'Individual'))
transmission = st.selectbox('𝐓𝐫𝐚𝐧𝐬𝐦𝐢𝐬𝐬𝐢𝐨𝐧 𝐭𝐲𝐩𝐞',('Manual', 'Automatic'))
result =""
    
# when 'Predict' is clicked, make the prediction and store it 
if st.button("𝐂𝐚𝐥𝐜𝐮𝐥𝐚𝐭𝐞 𝐒𝐞𝐥𝐥𝐢𝐧𝐠 𝐏𝐫𝐢𝐜𝐞"): 
    result = prediction(present_price, kms_driven, owner, tot_year, fuel_type, seller_type, transmission) 
    st.success('𝐘𝐨𝐮𝐫 𝐜𝐮𝐫𝐫𝐞𝐧𝐭 𝐬𝐞𝐥𝐥𝐢𝐧𝐠 𝐩𝐫𝐢𝐜𝐞 𝐢𝐬 {} 𝐥𝐚𝐤𝐡𝐬'.format(result))
    
if st.button("𝐑𝐞𝐥𝐨𝐚𝐝"):
    pyautogui.hotkey("CTRL","F5")
            
