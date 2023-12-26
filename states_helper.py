import json



# Load the JSON data file
with open('data/hindu_temples.json', 'r') as f:
	data = json.load(f)

# Function to print temple information
def print_temple_info(temple):
	print("==================================================================")
	print(f"Name: {temple['name']}")
	print(f"State: {temple['state']}")
	print("------------------------------------------------------------------")
	print(temple['info'])
	print("------------------------------------------------------------------")
	print(temple['story'])
	print("------------------------------------------------------------------")
	print(temple['visiting_guide'])
	print("------------------------------------------------------------------")
	print(temple['architecture'])
	print("------------------------------------------------------------------")
	print(temple['mention_in_scripture'])
	print("==================================================================")

# Function to print all temples information
def print_all_temples_info(data):
	for name in data.keys():
		temples=data[name]
		for temple in temples:
			print_temple_info(temple)


# Function to print temples by name
def print_temples_by_state_name(name):
	if name in data:
		for temple in data[name]:
			print_temple_info(temple)
	elif name.lower() in data:
		for temple in data[name]:
			print_temple_info(temple)
	else:
		print("Sorry, the temple you are looking for was not found.")
		print('available options: {}'.format(' , '.join(data.keys())))

# Function to print temple information by name
def print_temple_info_by_name(name):
	for name in data.keys():
		temples=data[name]
		for temple in temples:
			if temple['name'].lower() == name.lower():
				print_temple_info(temple)
				return
	print("Sorry, the temple you are looking for was not found.")
	for name in data.keys():
		temples=data[name]
		print('available options for God \'{}\': {}'.format(
			name,
			', '.join([temple['name'] for temple in temples])
			)
		)
		print("------------------------------------------------------------------")



# Main Function
def main():
	# Print all temples information
	print("**All Temples Information:**")
	print_all_temples_info(data)

	# Print temples information by name
	name = input("Enter a state name to see temple information: ")
	print(f"**Temples of {name}:**")
	print_temples_by_state_name(name)

	# Print temple information by name
	name = input("Enter a temple name to see its information: ")
	print(f"**Information about {name}:**")
	print_temple_info_by_name(name)


if __name__ == "__main__":
	main()

