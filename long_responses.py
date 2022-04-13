import random

F_SYMPTOMS = "Symptoms of Flu are 1. Fever or feeling feverish/chills 2. Cough 3. Sore throat 4. Runny or stuffy nose 5. Muscle or body aches 6. Headaches 7. Fatigue (tiredness) 8. Some people may have vomiting and diarrhea, though this is more common in children than adults."
F_CAUSE = "Causes of Flu are 1. A virus. 2. A bacterial infection. 3. Heat exhaustion.  4. A malignant tumor"
F_AYURVEDIC = "Ayurvedic Solution of Flu is 1. Baidyanath (Jhansi) Mrityunjay Ras Tablet.  2. Baidyanath (Jhansi) Fevercut Tablet 3. Tansukh Sudarshanghan Vati"
F_HOMEREMEDY = "Home remedy of Flu is 1. Putting Cold water napkins on head"


C_SYMPTOMS = "Symptoms of Covid are 1. Fever 2. Cough 3. Tiredness 4. Loss of taste or smell 5. Shortness of breath or difficulty breathing 6. Muscle aches, joint pains 7. Severe dizziness 8. Chills 9. Sore throat 10. Runny nose 11. Headache 12. Conjunctivitis 13. Chest pain 14. Skin rash 15. Nausea 16. Vomiting 17. Diarrhoea 18. Loss of speech 19. Loss of movement"
C_PREVENTION = " Prevention of Covid is 1. Clean your hands often. Use soap and water, or an alcohol-based hand rub. 2. Maintain a safe distance from anyone who is coughing or sneezing. 3. Wear a mask when physical distancing is not possible. 4. Don’t touch your eyes, nose or mouth. 5. Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze. 6. Stay home if you feel unwell. 7. If you have a fever, cough and difficulty breathing, seek medical attention."
C_IMMUNITY = " Immunity Boosters for Covid are 1. Take Immunity-Boosting Foods & Vitamins: fruits & vegetables contain vitamins A, C, D, and E, and minerals like magnesium, selenium, and zinc that acts as immunity-boosting vitamins. 2. Take Proper 7-8 Hours of Sleep:  Sleeping well is one of the easiest ways to increase immunity for COVID-19. 3. Drink up to 8-10 glasses of water every day:  Staying hydrated is the best way to increase immunity to fight Coronavirus because it flushes out all the toxins from the body. Immunity booster drink such as fresh fruit juices and coconut water, along with consuming enough water throughout the day helps in keeping the body hydrated. 4. Don’t skip these home workout exercises:  Home workout are another way of flushing out toxins from the body through sweat. Make sure not to skip exercises while staying home during the pandemic. Depending upon one’s stamina and routine, some of the easy workout exercises that can be done at home may include rope-skipping, push-ups, jogging on the spot, front plank, and forward lunges. 5. Practice These 3 Steps: A] Practice meditation:  Meditation is a mindful exercise that relaxes the mind of all external chaos and distractions. A mere 10 minutes of meditation every day can make a big difference not only throughout the day but also in life as a whole. A calm mind helps in better focus,  better decisions, and builds a sound body. B] Avoid Smoking and Alcohol:  Smoking and other substance abuse weaken the respiratory system, while alcohol reduces immunity. This makes the body susceptible to catching the virus and being infected. C] Avoid Non-essential travelling:  Social distancing is key to fighting novel coronavirus, and hence avoiding non-essential travel will help in protecting oneself and others from the virus."



#B_SYMPTOMS = "Symptoms of Backpain are 1. inflammation or swelling on the back. 2. persistent back pain where lying down or resting does not help. 3. a recent injury, blow, or trauma to the back 4. pain down the legs. 5. pain that reaches below the knees."
#response(long.B_SYMPTOM, ['symptoms'], required_words=['symptoms'])
#B_CURE = "Cure of Backpain is 1. Apply Ice and Heat. 2. Keep Exercising. 3. Strengthen Your Core. 4. Limit Bed Rest."
#response(long.B_CURE, ['cure'], required_words=['cure'])
#B_MEDICINES = "Medicine used for Backpain are 1. ibuprofen (Advil) 2. naproxen (Aleve). 3. NSAIDs."
#response(long.B_MEDICINE, ['medicine'], required_words=['medicine'])
#B_PREVENTION = "Prevention of Backpain is 1.  Avoid heavy lifting. 2.  Get active and eat a balanced diet. 3.  Do back-strengthening and stretching exercises at least 2 days a week."
#response(long.B_PREVENTION, ['prevention'], required_words=['prevention'])


C_SYMPTOMS = "Symptoms of Covid are 1. Fever 2. Cough 3. Tiredness 4. Loss of taste or smell 5. Shortness of breath or difficulty breathing 6. Muscle aches, joint pains 7. Severe dizziness 8. Chills 9. Sore throat 10. Runny nose 11. Headache 12. Conjunctivitis 13. Chest pain 14. Skin rash 15. Nausea 16. Vomiting 17. Diarrhoea 18. Loss of speech 19. Loss of movement"

def unknown():
    response = ['Could you please re-phrase the sentence?',
                "...",
                "Sounds about right",
                "What does that mean?"][random.randrange(4)]
    return response