# importing regex and random libraries
import re
import random

class AlienBot:
  # potential negative responses
  negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")

  # keywords for exiting the conversation
  exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")

  # random starter questions
  random_questions = (
        "Why are you here? ",
        "Are there many humans like you? ",
        "What do you consume for sustenance? ",
        "Is there intelligent life on this planet? ",
        "Does Earth have a leader? ",
        "What planets have you visited? ",
        "What technology do you have on this planet? "
    )

  def __init__(self):
    self.alienbabble = {  
      'answer_why_intent': r'why\sare.*',
      'describe_planet_intent': r'tell\sme\sabout.*planet.*',
      'cubed_intent': r'.*cube.*(\d+).*'
    }

  def greet(self):
    self.name = input("Hello there! What is your name?\n")
    will_help = input("Hi {}, I'm ET. I'm not from this planet. Will you help me learn about your planet?\n".format(self.name))
    if will_help in self.negative_responses:
       return "Ok, invading it is."
    self.chat()
    
  def make_exit(self, reply):
    for words in self.exit_commands:
      if words in reply:
        print("Ok. Invading it is.")
        return -1

  def chat(self):
    reply = input(random.choice(self.random_questions)).lower()
    while not self.make_exit(reply):
      reply = input(self.match_reply(reply) + "\n")
      

  def match_reply(self, reply):
    for key, value in self.alienbabble.items():
        intent = key
        regex_pattern = value
        found_match = re.match(regex_pattern, reply.lower())
        if found_match and "describe_planet_intent" in intent:
            return self.describe_planet_intent()
        elif found_match and "answer_why_intent" in intent:
            return self.answer_why_intent()
        elif found_match and "cubed_intent" in intent:
            return self.cubed_intent(found_match.group(1))
        else:
            return self.no_match_intent()

  def describe_planet_intent(self):
    responses = (
      "My planet is a utopia of diverse orgamnisms and species. ",
      "I am from Opidipus, the capital of the Wayward Galaxies. ")
    return random.choice(responses)
    

  def answer_why_intent(self):
        responses = (
            "i come in piece",
            "I am here to collect data on your planet and its inhabitants",
            "I heard the coffee is good..")
        return random.choice(responses)
       
       
  def cubed_intent(self, number):
    cubed_number = int(number)**3
    return "The cube of {} is {}. Isn't that cool?".format(number, cubed_number)


  def no_match_intent(self):
    responses = (
      "Please tell me more.",
      "Tell me more!",
      "Why do you say that?",
      "I see. Can you elaborate?",
      "Interesting. Can you tell me more?",
      "I see. How do you think?",
      "Why?",
      "How do you think I feel when you say that?")
    return random.choice(responses)

ET = AlienBot()
ET.greet()
