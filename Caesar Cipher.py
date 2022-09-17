alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

if direction == "encode":
	text = input("Type your message:\n").lower()
	shift = int(input("Type the shift number:\n"))

	def encrypt(message, number):
		newMessage = []
		encrypted = ""
		for i in message:
			if i in alphabet:
				index = alphabet.index(i)
				newIndex = index + int(shift)
				encrypted += alphabet[newIndex]
			else:
				encrypted += i
		print(f"Your encrypted message is '{encrypted}'.")
	encrypt(message=text, number=shift)
elif direction == "decode":
	text = input("Type your message:\n").lower()
	shift = int(input("Type the shift number:\n"))

	def decode(message, number):
		newMessage = []
		decrypted = ""
		for i in message:
			if i in alphabet:
				index = alphabet.index(i)
				newIndex = index - int(shift)
				decrypted += alphabet[newIndex]
			else:
				decrypted += i
		print(f"Your decoded message is '{decrypted}'.")
	decode(message=text, number=shift)
else:
	print("Invalid input. Try again")