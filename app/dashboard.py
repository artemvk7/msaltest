import streamlit as st
import msal_streamlit_authentication


login_token = msal_authentication(
    auth={
        "clientId": "aaaaaaa-bbbb-cccc-dddd-eeeeeeeeeee",
        "authority": "https://login.microsoftonline.com/aaaaaaa-bbbb-cccc-dddd-eeeeeeeeeee",
        "redirectUri": "/",
        "postLogoutRedirectUri": "/"
    }, # Corresponds to the 'auth' configuration for an MSAL Instance
    cache={
        "cacheLocation": "sessionStorage",
        "storeAuthStateInCookie": False
    }, # Corresponds to the 'cache' configuration for an MSAL Instance
    login_request={
        "scopes": ["aaaaaaa-bbbb-cccc-dddd-eeeeeeeeeee/.default"]
    }, # Optional
    logout_request={}, # Optional
    login_button_text="Login", # Optional, defaults to "Login"
    logout_button_text="Logout", # Optional, defaults to "Logout"
    key=1 # Optional if only a single instance is needed
)
st.write("Recevied login token:", login_token)
