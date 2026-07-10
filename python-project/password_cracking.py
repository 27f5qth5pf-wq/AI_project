import random
lower = "qwertyuiopasdfghjklzxcvbnm"
upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
number ="1234567890"
symbols = """!@#$%^&*"'()}{][\|?><./';:`"""

max_str = lower + upper + number + symbols

password = "".join(random.sample(max_str,10))
print (password)