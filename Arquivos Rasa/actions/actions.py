#pip install unicode
from typing import Any, Text, Dict, List
from unidecode import unidecode
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import sqlite3

banco = sqlite3.connect('../SarsBotProject/dbacess/bancoUbs.db')

cursor = banco.cursor()

cursor.execute("SELECT * FROM UbsCidades")
records = cursor.fetchall()
ubs = []


class ActionListUbs(Action):

    def name(self) -> Text:
        return "action_list_ubs"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        currentPlace = tracker.latest_message['text']
        print(currentPlace)
        for row in records:
            if unidecode(row[1].lower()) == unidecode(currentPlace):
                localizacao = ("\nLocalização: http://maps.google.com/maps?q=%s,%s&ll=%s,%s,&z=17" %(row[3],row[4],row[3],row[4]))
                dispatcher.utter_message(response= "utter_listUbs", Cidade= row[1], Ubs=row[2], Local=localizacao)
        return []
