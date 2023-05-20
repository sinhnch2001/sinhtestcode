import json

schema_guided_dict = {}

schema_ketod = json.load(open("C:\ALL\OJT\gradients.baselinev1.dialogstate\data\\raw_schema\schema_ketod.json"))
for domain in schema_ketod:
    slots_intents = {}
    if domain["service_name"] not in schema_guided_dict.keys():
        slots = domain["slots"]
        intents = domain["intents"]

        slot_description = {}
        intent_description = {}

        for slot in slots:
            slot_description.setdefault(slot["name"].strip().lower(), slot["description"].strip().lower())
        for intent in intents:
            intent_description.setdefault(intent["name"].strip().lower(), intent["description"].strip().lower())

        slots_intents.setdefault("slots", slot_description)
        slots_intents.setdefault("intents", intent_description)

    schema_guided_dict.setdefault(domain["service_name"].strip().lower(), slots_intents)

schema_fusedchat = json.load(open("C:\ALL\OJT\gradients.baselinev1.dialogstate\data\\raw_schema\schema_fusedchat.json"))
for domain in schema_fusedchat:
    slots_intents = {}
    if domain["service_name"] not in schema_guided_dict.keys():
        slots = domain["slots"]
        intents = domain["intents"]

        slot_description = {}
        intent_description = {}

        for slot in slots:
            slot_description.setdefault(slot["name"].split('-')[-1].strip().lower(), slot["description"].strip().lower())
        for intent in intents:
            intent_description.setdefault(intent["name"].strip().lower(), intent["description"].strip().lower())

        slots_intents.setdefault("slots", slot_description)
        slots_intents.setdefault("intents", intent_description)

    schema_guided_dict.setdefault(domain["service_name"].strip().lower(), slots_intents)

with open("C:\ALL\OJT\gradients.baselinev1.dialogstate\data\processed_schema\schema_final_old.json", 'w') as f:
    json.dump(schema_guided_dict, f, indent=4)