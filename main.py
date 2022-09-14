import random
#the positive inputs
input1 = 'Im doing good'
input2 = 'Im fine'
input3 = 'Im doing very good!'
input4 = 'Im doing well'

#the negative inputs
input5 = 'Im not doing good'
input6 = 'Im not feeling well'
input7 = 'Im not ok'
input8 = 'Im not doing too well'

#the first list by which the bot starts a conversation
conversation_starters = ['What is your name? How are you doing?','Hi there! How are you?','Hello! How are you doing?','Hello, How are you?','How are you doing?']

#takes the elements from the conversation starters and picks a random one, then starts the conversation
rand_idx = random.randrange(len(conversation_starters))
random_response = conversation_starters[rand_idx]
           
print(f'I am Chatbot, {random_response}')

#The possible outputs of the chatbot to different responses
positive_responses = ['Im glad to hear that!','Very nice!','Thats awesome!','Excellent, glad to hear that!']
negative_responses = ['Im sorry to hear that','I hope you feel better soon','Hope you get better soon']

input_response = input('')

#Chooses a random statement from the positive responses list
def positive_responses_function():
  rand_idx2 = random.randrange(len(positive_responses))
  random_response2 = positive_responses[rand_idx2]
  print(random_response2)
  
#Chooses a random statement from the negative responses list
def negative_responses_function():
  rand_idx3 = random.randrange(len(negative_responses))
  random_response3 = negative_responses[rand_idx3]
  print(random_response3)


#checks if the inputs of the users are the positive ones
if(input_response == input1):
  positive_responses_function()
elif(input_response == input2):
  positive_responses_function()
elif(input_response == input3):
  positive_responses_function()
elif(input_response == input4):
  positive_responses_function()
else:
  print("")

#checks if the inputs of the users are the negative ones
if(input_response == input5):
  negative_responses_function()
elif(input_response == input6):
  negative_responses_function()
elif(input_response == input7):
  negative_responses_function()
elif(input_response == input8):
  negative_responses_function()
else:
  print("")
  



