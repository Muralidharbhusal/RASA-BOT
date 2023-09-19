# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World! this is first")

#         return []


# Sample account dictionary
database = {
    "Ram Thapa": {
        "PhoneNumber": "9867876772",
        "AccountNumber": "12345",
        "Balance": 1000.00,
        "TransactionHistory": [
            {"Date": "2023-09-01", "Description": "Deposit", "Amount": 500.00},
            {"Date": "2023-09-05", "Description": "Withdrawal", "Amount": -200.00},
            {"Date": "2023-09-10", "Description": "Deposit", "Amount": 300.50}
        ]
    },
    "Hari Rana": {
        "PhoneNumber": "9812345678",
        "AccountNumber": "98765",
        "Balance": 2500.50,
        "TransactionHistory": [
            {"Date": "2023-09-02", "Description": "Deposit", "Amount": 1000.00},
            {"Date": "2023-09-06", "Description": "Withdrawal", "Amount": -300.75}
        ]
    },
    "Sita Sharma": {
        "PhoneNumber": "9898765432",
        "AccountNumber": "45678",
        "Balance": 500.75,
        "TransactionHistory": [
            {"Date": "2023-09-03", "Description": "Deposit", "Amount": 200.25},
            {"Date": "2023-09-08", "Description": "Withdrawal", "Amount": -100.00},
            {"Date": "2023-09-12", "Description": "Deposit", "Amount": 50.50}
        ]
    }
}


class ActionGetDetails(Action):
    def name(self) -> Text:
        return "action_get_details"
    
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = tracker.get_slot("name")
        phone_number = tracker.get_slot("phone_number")
        account_number= tracker.get_slot("account_number")

        # dispatcher.utter_message(f"{name}, has {account_number} and phone number {phone_number}")


        for account_name, account_info in database.items():
            if (account_number == account_info["AccountNumber"] and phone_number == account_info["PhoneNumber"]):

                balance = account_info["Balance"]
                history = account_info["TransactionHistory"]

                dispatcher.utter_message(f"Balance for {account_name} with account number {account_number} and phone number {phone_number} is Rs.{balance:.2f}")
                
                dispatcher.utter_message(f"\n Transaction History for {account_name} of {account_number} is {history}")

                found = True
                break
        if not found:
            dispatcher.utter_message("Invalid Credentials. Try Again with valid credentials")
        
       
        return []     
    

# class ActionGetHistory(Action):
#     def name(self) -> Text:
#         return "action_get_history"
    
#     def run(self, dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         name = tracker.get_slot("name")
#         phone_number = tracker.get_slot("phone_number")
#         account_number= tracker.get_slot("account_number")

#         # dispatcher.utter_message(f"{name}, has {account_number} and phone number {phone_number}")


#         for account_name, account_info in database.items():

#             if (account_number == account_info["AccountNumber"] and phone_number == account_info["PhoneNumber"]):

#                 history = account_info["TransactionHistory"]
#                 dispatcher.utter_message(f"Transaction History for {account_name} of {account_number} is {history}")
                

#             else:
#                 dispatcher.utter_message("Account not found.")
#                 print(history)
        
       

#     - story: get details
#   steps:
#   - intent: greet
#   - action: utter_greet
#   - intent: ask_balance
#   - action: utter_ask_balance
#   # Changes start here
#   - intent: ask_name
#     entities: 
#     - name : John Mayers
#     - slot_was_set:
#       - name : John Mayers
#   - action: utter_ask_account_number
#   - intent: ask_account_number
#     entities: 
#     - account_number : 12765
#     - slot_was_set:
#       - account_number : 12765
#   - action: utter_ask_phone_number
#   - intent: ask_phone_number
#     entities:
#     - phone_number : 9876435324
#     - slot_was_set:
#       - phone_number : 9876435324