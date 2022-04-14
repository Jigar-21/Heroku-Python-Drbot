import re
from urllib import response
import long_responses as long
from flask import Flask

app  = Flask(__name__)

print('Namaste, I am Dr. Bot!')
print('How can I help you with? Common Diseases or Covid 19?')

#using app decorator tp create route 
@app.route('/')
def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainity = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainity += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainity) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[],):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Response --------------------------------------------------------------------------------------------------------------
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'], single_response=True)

    # Common Diseases Code
    response(
        'Please tell me what do you want to know on Common Diseases? The common diseases with which I can help are - Flu, Backpain, Diarrhea, Stomach Ache, Conjunctivitis, Acne, Acidity, Cough ',
        ['common', 'disease', 'Common', 'Disease'], required_words=['common'])

    # Flu
    response('What do you want to know about Flu? 1. Symptoms 2. Causes 3. Ayurvedic 4. Home remedy', ['flu'],
             required_words=['flu'])
    response(
        'Symptoms of Flu are 1. Fever or feeling feverish/chills 2. Cough 3. Sore throat 4. Runny or stuffy nose 5. Muscle or body aches 6. Headaches 7. Fatigue (tiredness) 8. Some people may have vomiting and diarrhea, though this is more common in children than adults.',
        ['symptoms','flu'], required_words=['flu','symptoms'])
    response(long.F_SYMPTOMS,['symptoms'], required_words=['symptoms'])
    response(
        'Causes of Flu are 1. A virus. 2. A bacterial infection. 3. Heat exhaustion.  4. A malignant tumor',
        ['cause','flu'], required_words=['cause', 'flu'])
    response(long.F_CAUSE, ['cause'], required_words=['cause'])
    response(
        'Ayurvedic solution of cure is 1. Baidyanath (Jhansi) Mrityunjay Ras Tablet.  2. Baidyanath (Jhansi) Fevercut Tablet 3. Tansukh Sudarshanghan Vati',
        ['ayurvedic','flu'], required_words=['ayurvedic','flu'])
    response(long.F_AYURVEDIC, ['ayurvedic'], required_words=['ayurvedic'])
    response(
        'Home remedy of Flu is 1. Putting Cold water napkins on head',
        ['home', 'flu'], required_words=['home', 'flu'])
    response(long.F_HOMEREMEDY, ['home'], required_words=['home'])

    # Backpain
    response('What do you want to know about BackPain? 1. Symptoms 2. Causes 3. Ayurvedic 4. Home remedy', ['backpain'],
             required_words=['backpain'])
    response(
        'Symptoms of Backpain are 1. inflammation or swelling on the back. 2. persistent back pain where lying down or resting does not help. 3. a recent injury, blow, or trauma to the back 4. pain down the legs. 5. pain that reaches below the knees.',
        ['symptom', 'of', 'backpain'], required_words=['symptoms'])
    response(
        'Causes of Backpain is 1. Muscle or ligament strain. 2. Bulging or ruptured disks. 3. Arthritis. 4. Osteoporosis.',
        ['cause', 'backpain'], required_words=['cause', 'backpain'])
    response(
        'Ayurvedic solution of Backpain are 1. Ayurveda oil massage 2. special focus on Vasthi (Enema) 3. therapies like Podikkizhi (Choorna pinda sweda), Elakkizhi (Patrapotala sweda), Abhyanga (medicated oil massage)',
        ['ayurvedic', 'backpain'], required_words=['ayurvedic', 'backpain'])
    response(
        'Home remedy of Backpain is 1. Exercise to get muscles moving 2. Use heat and cold 3. Stretch 4. Apply a pain-relief cream.',
        ['homeremedy', 'backpain'], required_words=['homeremedy', 'backpain'])

    # Diarrhea
    response('What do you want to know about Diarrhea? 1. Symptoms 2. Causes 3. Ayurvedic 4. Home remedy', ['diarrhea'],
             required_words=['diarrhea'])
    response(
        'Symptoms of Diarrhea are 1.Frequent loose, watery stools. 2.Abdominal cramps. 3.Abdominal pain. 4.Fever. 5.Bleeding. 6.Lightheadedness or dizziness from dehydration.',
        ['symptom', 'symptoms', 'diarrhea'], required_words=['symptom', 'diarrhea'])
    response('Causes of Diarrhea are 1. Bacterial infection, caused by contaminated food or water. 2. Viral infection. 3. Parasites, which can enter the body through food or water.  4. Food intolerance, such as the inability to digest lactose, the sugar in milk. 5. Overuse of alcohol or laxatives. 6. Medication, such as some antibiotics or antacids containing magnesium. 7. Menstrual cramps. 8. Stress or a panic attack.',
             ['cause', 'diarrhea'], required_words=['cause', 'diarrhea'])
    response(
        'Ayurvedic solution of Diarrhea are 1. Mebarid Capsule - Phyto Marketing. 2. Ambimap Tablets - Maharishi Ayurveda. 3. Diarex Tablet - Himalaya. 4. Entpstal Tab - Solumiks..',
        ['ayurvedic', 'diarrhea'], required_words=['ayurvedic', 'diarrhea'])
    response(
        'Home remedy of Diarrhea is 1. Avoid foods that are milk-based, greasy, high-fiber, or very sweet because these are likely to aggravate diarrhea. 2. Avoid caffeine and alcohol. 3. Do not eat solid food if you have signs of dehydration (thirst, light-headed, dark urine). Instead, drink about 2 cups of clear fluids per hour (if vomiting isn’t present), such as sports drinks and broth. Water alone is not enough because your body needs sodium and sugar to replace what it’s losing. 4. Avoid high sugar drinks, like apple juice, grape juice, and soda, which can pull water into the intestine and make diarrhea persist. 5. Don’t drink clear liquids exclusively for more than 24 hours. 6. Begin eating normal meals within 12 hours, but stick to food that is bland and won’t irritate your intestine. Some doctors suggest the “BRAT“ diet which includes foods that are low in fiber, fat, and sugar. BRAT stands for Bananas, Rice, Applesauce, and Toast.7. Use over-the-counter lactobacillus acidophilus capsules or tablets. These bacteria help maintain a healthy intestine and are found in yogurt with live active cultures. 8. Decrease the level of exercise until symptoms are gone. 9. Over-the-counter drugs, such as Imodium A-D, should only be used if absolutely necessary because it is important to let diarrhea flush out the bacteria or parasite that’s causing the infection.',
        ['homeremedy', 'diarrhea'], required_words=['homeremedy', 'diarrhea'])

    # Stomach Ache
    response('What do you want to know about Fatigue? 1. Symptoms 2. Causes 3. Ayurvedic 4. Home remedy', ['stomach ache'],
             required_words=['stomach'])
    response(
        'Symptoms of stomach-ache are  pain between chest and groin',
        ['symptom', 'symptoms', 'stomach-ache'], required_words=['symptom', 'stomach'])
    response(
        'Causes of stomach-ache are 1. intestinal gas 2. Irritable bowel syndrome (IBS). 3. Crohn\'s disease or ulcerative colitis. 4. Food poisoning. 5. Food allergies. 6. Gas. 7. Urinary tract infection. 8. Abdominal muscle strain or pull.',
        ['cause', 'stomach-ache'], required_words=['cause', 'stomach'])
    response(
        'ayurvedic solution of stomach-ache are  1. modafinil 2. methylphenidate 3. amantadine 4. amphetamine / dextroamphetamine',
        ['medicine', 'medicines', 'stomach-ache'], required_words=['medicine', 'stomach'])
    response(
        'Home remedy of stomach-ache are  1. Manage stress and practice relaxation techniques. 2. Get exercise, but begin slowly and check with your health care practitioner before beginning any exercise program. 3. Check your medications with a health care practitioner or pharmacists to see if some medications could be responsible for fatigue.',
        ['homeremedy', 'stomach-ache'], required_words=['homeremedy', 'stomach'])

    # Conjunctivitis
    response('What do you want to know about Conjunctivitis? 1. Symptoms 2. Causes 3. Ayurvedic 4. Home remedy',
             ['conjunctivitis'], required_words=['conjunctivitis'])
    response(
        'Symptoms of Conjunctivitis are 1. Redness.  2. Itching. 3. Tearing.  4. Burning sensation.  5. pus-like discharge and/or crusting of the eyelids',
        ['symptom', 'symptoms', 'conjunctivitis'], required_words=['symptom', 'conjunctivitis'])
    response(
        'Causes of Conjunctivitis are 1. Bacterial or viral infection.  2. An allergic reaction to pollen or animal dander. 3. Result of chemical irritants (smoke, chlorine, lens solution, etc.).',
        ['cause', 'conjunctivitis'], required_words=['cure', 'conjunctivitis'])
    response(
        'Ayurvedic solution of Conjunctivitis are 1. Soak half a teaspoon of Triphala powder in a glass of water overnight. Filter the water in the morning and use it to wash the eyes. 2. Mix some turmeric with a little amount of water, dip a small and neat piece of cloth in it and let it dry. Use this cloth to wipe the affected area of eyes to help reduce infection. 3. Mix some amla juice with honey and drink it twice daily for quick healing.  4. Put a few drops of coconut oil in the eyes and lie down for some time to reduce the swelling and itching in the eyes. 5. Place a cucumber slice over the eyelid for a soothing effect on the eye. 6. Dip a small and neat towel in cold water and place it gently on the affected eye to relieve the pain and irritation. 7. Dip a cotton ball in some goat’s milk and wipe the eyes with it for the conjunctivitis to heal quickly. 8. Make a paste of neem leaves and apply it externally over the eyelids to reduce the pain. 9. Blend some coriander leaves with half a cup of water. Filter the mixture and apply the pulp on the closed eyelids. 10. Steep a teaspoonful of coriander seeds in a cup of water for 15 minutes. Strain it and apply the water externally on the eyelids for relief from conjunctivitis. 11. Drink a glass of lemon juice early in the morning on an empty stomach to reduce the infection.',
        ['ayurvedic', 'conjunctivitis'], required_words=['ayurvedic', 'conjunctivitis'])
    response(
        'Home remedy of Conjunctivitis are 1. Wash your hands frequently to prevent spreading an existing infection to your other eye, and to other people. 2. Don’t rub your eyes. 3. Use a cool wet washcloth to soak off any crusting. 4. Use a warm or cool compress to reduce discomfort. 5. Discard eye make-up because it may cause future infection. 6. Wash any clothing that may be contaminated, including towels and pillowcases. 7. Try to use clean towels and pillowcases everyday. 8. Avoid wearing contact lenses and discard current lenses. 9. If eye drops are prescribed, place drop in pocket formed by pulling down lower lid. 10. Make sure you don’t touch the bottle to the eye in order to prevent contamination.',
        ['homeremedy', 'conjunctivitis'], required_words=['homeremedy', 'conjunctivitis'])

    # Acne
    response('What do you want to know about Acne? 1. Symptoms 2. Causes 3. Ayurvedic 4. Home remedy', ['acne'],
             required_words=['acne'])
    response(
        'Symptoms of Acne are Acne presents as small to large, red bumps on the skin, which may be painful and pus-filled in some case',
        ['symptom', 'symptoms', 'acne'], required_words=['symptom', 'acne'])
    response(
        'Causes of Acne are  1. Age: Teenagers are commonly affected. 2. Excess sebum or oil production. 3. Accumulation(collection) of dead skin cells. 4. Bacterial infection of the follicle. 5. Changes in hormonal levels as noted during puberty or pregnancy. 6. Diet: Foods including chocolates, chips, etc. are known to trigger/worsen acne.  7. Stress  8. Skin contact with greasy or oily substances. 9. Friction or pressure on the skin',
        ['cause', 'acne'], required_words=['cause', 'acne'])
    response(
        'ayurvedic solution of Acne are  1. Natural Vibes Ayurvedic Anti Acne and Skin Whitening Treatment.  2. Nature Sure Anti Acne Cream With Wrinkle Defense & Skin Whitening (50g). 3. Acne Marks Reduction Kit.  4. Night Balm (Black laurel) ',
        ['ayurvedic', 'acne'], required_words=['ayurvedic', 'acne'])
    response(
        'Home remedy of Acne are 1. Tea tree oil  2. Jojoba oil  3. Aloe vera  4. Honey 5. Garlic 6. Green tea(drink) 7. Purified bee venom.  8.Coconut oil. 9. Staying hydrated',
        ['homeremedy', 'acne'], required_words=['homeremedy', 'acne'])

    # Acidity
    response('What do you want to know about Acidity? 1. Symptoms 2. Causes 3. Ayurvedic 4. Home remedy', ['acidity'],
             required_words=['acidity'])
    response(
        'Symptoms of Acididty are 1. Bloating. 2. Bloody or black stools or bloody vomiting. 3. Burping. 4. Dysphagia -- the sensation of food being stuck in your throat. 5. Hiccups that don\'t let up. 6. Nausea. 7. Weight loss for no known reason. 8. Wheezing, dry cough, hoarseness, or chronic sore throat.',
        ['symptom', 'symptoms', 'acidity'], required_words=['symptom', 'acidity'])
    response(
        'Causes of Acidity are 1. Eating large meals or lying down right after a meal. 2. Being overweight or obese. 3. Eating a heavy meal and lying on your back or bending over at the waist. 4. Snacking close to bedtime. 5. Eating certain foods, such as citrus, tomato, chocolate, mint, garlic, onions, or spicy or fatty foods..',
        ['cause', 'acidity'], required_words=['cause', 'acidity'])
    response(
        'Ayurvedic solution of Acidity are 1. Incorporate spices like turmeric, cumin, fennel seeds, coriander, and hing (asafetida) in your diet. 2. Drink ginger or cumin tea once a day. 3. Avoid ice-cold drinks or food. 4. Don\'t drink ice water as it slows agni and digestion. 5. Don\'t snack, if not hungry.',
        ['ayurvedic', 'acidity'], required_words=['ayurvedic', 'acidity'])
    response(
        'Home remedy of Acidity are 1. Fennel or Saunf 2. Black Cumin Seeds 3. Cloves 4. Lukewarm Water 5. Watermelon Juice 6. Cardamom 7. Buttermilk',
        ['homeremedy', 'acidity'], required_words=['homeremedy', 'acidity'])

    # Cough
    response('What do you want to know about Cold? 1. Symptoms 2. Causes 3. Ayurvedic 4. Home remedy', ['cough'],
             required_words=['cough'])
    response(
        'Symptoms of Cough are A chronic cough or cold can occur with other signs and symptoms, which may include: 1. A runny or stuffy nose 2. A feeling of liquid running down the back of your throat (postnasal drip) 3. Frequent throat clearing and sore throat 4. Hoarseness 5. Wheezing and shortness of breath 6. Heartburn or a sour taste in your mouth 7. In rare cases, coughing up blood.',
        ['symptom', 'symptoms', 'cough'], required_words=['symptom', 'cough'])
    response(
        'Causes of Cough are 1. The virus can enter your body  Acneoplets from a sick person’s sneezes or coughs. 2. Common cold, Influenza (flu), Inhaling smoke, dust, chemicals,  Allergies, Asthma',
        ['cause', 'cough'], required_words=['cause', 'cough'])
    response(
        'Ayurvedic solution of Cough are 1. Zandu Ayurvedic Cough Syrup. 2. 20 Microns Herbal Koff Kranti Cough Syrup. 3. Nisarga Herbs Respirade Tablet',
        ['ayurvedic', 'cough'], required_words=['ayurvedic', 'cough'])
    response(
        'Home remedy of Cough is 1. Honey  2. Turmeric The herb turmeric has a therapeutic effect on coughs, particularly a dry cough. 3. Ginger   4. Garlic  5. Hot Milk with Honey.',
        ['homeremedy', 'cough'], required_words=['homeremedy', 'cough'])

    ## Tuberculosis
    #response('What do you want to know about Tuberculosis? 1. Symptoms 2. Cure 3. Medicine 4. Prevention',
    #         ['tuberculosis'], required_words=['tuberculosis'])
    #response(
    #    'Symptoms of Tuberculosis are 1. A bad cough that lasts 3 weeks or longer 2. Pain in the chest 3. Coughing up blood or sputum (phlegm from deep inside the lungs) 4. Weakness or fatigue 5. Weight loss 6. No appetite 7. Sweating at night',
    #    ['symptom', 'symptoms', 'tuberculosis'], required_words=['symptom', 'tuberculosis'])
    #response(
    #    'Cure of Tuberculosis is 1. keep regular follow-up with the doctor. 2. Take the medicines as prescribed. 3. Report any side effects of the medicine.',
    #    ['cure', 'tuberculosis'], required_words=['cure', 'tuberculosis'])
    #response(
    #    'ayurvedic solution of Tuberculosis are 1. Isoniazid. 2. Rifampin (Rifadin, Rimactane) 3. Ethambutol (Myambutol) 4. Pyrazinamide.',
    #    ['medicine', 'medicines', 'tuberculosis'], required_words=['medicine', 'tuberculosis'])
    #response(
    #    'Home remedy of Tuberculosis is 1. Stay away from work, school or college until your TB treatment team advises you it\'s safe to return. 2. Always cover your mouth – preferably with a disposable tissue – when coughing, sneezing or laughing 3. Carefully dispose of any used tissues in a sealed plastic bag 4. Open windows when possible to ensure a good supply of fresh air in the areas where you spend time 5. Not sleep in the same room as other people – you could cough or sneeze in your sleep without realising it',
    #    ['prevention', 'tuberculosis'], required_words=['prevention', 'tuberculosis'])

   # # Polio
   # response('What do you want to know about Polio? 1. Symptoms 2. Cure 3. Medicine 4. Prevention', ['polio'],
   #          required_words=['polio'])
   # response(
   #     'Symptoms of Polio are Fever, Sore throat, Headache, Vomiting, Fatigue, Back pain or stiffness, Neck pain or stiffness, Pain or stiffness in the arms or legs.',
   #     ['symptom', 'symptoms', 'polio'], required_words=['symptom', 'polio'])
   # response(
   #     'Cure of Polio is Heat and physical therapy is used to stimulate the muscles and antispasmodic drugs are given to relax the muscles. While this can improve mobility, it cannot reverse permanent polio paralysis. Polio can be prevented through immunization.',
   #     ['cure', 'polio'], required_words=['cure', 'polio'])
   # response(
   #     'ayurvedic solution of Polio are 1. IPOL® 2. Orimune® Trivalent 3. Kinrix® (containing Diphtheria, Tetanus Toxoids, Acellular Pertussis, Polio Vaccine) 4. Pentacel® (containing Diphtheria, Tetanus Toxoids, Acellular Pertussis, Haemophilus influenzae type b, Polio Vaccine)',
   #     ['medicine', 'medicines', 'polio'], required_words=['medicine', 'polio'])
   # response(
   #     'Home remedy of Polio is 1. Provision of clean water. 2. improved hygienic practices and sanitation are important for reducing the risk of transmission of polio virus.',
   #     ['prevention', 'polio'], required_words=['prevention', 'polio'])

    # COVID-19
    response('Please tell me what do you want to know about COVID-19? Symptoms, Prevention, or Immunity Boosters?',
             ['covid-19','covid', 'Covid', 'COVID' ], required_words=['covid'])

    response(
        'Symptoms of Covid are 1. Fever 2. Cough 3. Tiredness 4. Loss of taste or smell 5. Shortness of breath or difficulty breathing 6. Muscle aches, joint pains 7. Severe dizziness 8. Chills 9. Sore throat 10. Runny nose 11. Headache 12. Conjunctivitis 13. Chest pain 14. Skin rash 15. Nausea 16. Vomiting 17. Diarrhoea 18. Loss of speech 19. Loss of movement',
        ['symptom', 'symptoms', 'covid'], required_words=['symptom', 'covid'])
    response(long.C_SYMPTOMS, ['symptoms'], required_words=['symptoms', 'covid'])
    response(
        'Prevention of Covid is 1. Clean your hands often. Use soap and water, or an alcohol-based hand rub. 2. Maintain a safe distance from anyone who is coughing or sneezing. 3. Wear a mask when physical distancing is not possible. 4. Don’t touch your eyes, nose or mouth. 5. Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze. 6. Stay home if you feel unwell. 7. If you have a fever, cough and difficulty breathing, seek medical attention.',
        ['prevention', 'covid'], required_words=['prevention', 'covid'])
    response(long.C_PREVENTION, ['prevention'], required_words=['prevention'])
    response(
        'Immunity Boosters for Covid are 1. Take Immunity-Boosting Foods & Vitamins: fruits & vegetables contain vitamins A, C, D, and E, and minerals like magnesium, selenium, and zinc that acts as immunity-boosting vitamins. 2. Take Proper 7-8 Hours of Sleep:  Sleeping well is one of the easiest ways to increase immunity for COVID-19. 3. Drink up to 8-10 glasses of water every day:  Staying hydrated is the best way to increase immunity to fight Coronavirus because it flushes out all the toxins from the body. Immunity booster drink such as fresh fruit juices and coconut water, along with consuming enough water throughout the day helps in keeping the body hydrated. 4. Don’t skip these home workout exercises:  Home workout are another way of flushing out toxins from the body through sweat. Make sure not to skip exercises while staying home during the pandemic. Depending upon one’s stamina and routine, some of the easy workout exercises that can be done at home may include rope-skipping, push-ups, jogging on the spot, front plank, and forward lunges. 5. Practice These 3 Steps: A] Practice meditation:  Meditation is a mindful exercise that relaxes the mind of all external chaos and distractions. A mere 10 minutes of meditation every day can make a big difference not only throughout the day but also in life as a whole. A calm mind helps in better focus,  better decisions, and builds a sound body. B] Avoid Smoking and Alcohol:  Smoking and other substance abuse weaken the respiratory system, while alcohol reduces immunity. This makes the body susceptible to catching the virus and being infected. C] Avoid Non-essential travelling:  Social distancing is key to fighting novel coronavirus, and hence avoiding non-essential travel will help in protecting oneself and others from the virus.',
        ['immunity', 'boosters', 'covid'], required_words=['immunity', 'boosters', 'covid'])
    response(long.C_IMMUNITY, [ 'immunity','booster'], required_words=['immunity'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)

    return long.unknown() if highest_prob_list[best_match] < 2 else best_match


def get_response(user_input):
    # splitting the message into array so we can split each word seperately
    # the re split removes all the special characters which helps to recognise text easily
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Create an infinite while true loop so we can always get new responses
# Testing the response system
while True:
    # created a function get_response for taking the input from user
    print('Dr. Bot: ' + get_response(input('You: ')))


if __name__ == "__main__":
   app.run()
