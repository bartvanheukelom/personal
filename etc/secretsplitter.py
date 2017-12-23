#!/usr/bin/env python3

def main():

	print('This script will tell you how to divide a secret so that multiple parties holding fragments of it must get together to restore the full secret.')
	
	
	
	### input ###

	parties = int(input('How many people/parties to split between? > '))
	criticalmass = int(input('How many should be present to form the full secret? > '))

	if parties < 2 or criticalmass < 2 or criticalmass > parties:
		print("That's nonsense!")
		exit(1)
		
		
	if criticalmass == parties:
		print("Well that's not that hard, just divide your secret in " + str(parties) + " fragments and give each party one.")
		exit(0)


	### calculate division ###

	unknowns = criticalmass - 1
	knowns = parties - unknowns
	print('Each party will have ' + str(unknowns) + ' missing piece(s)')

	print('Calculating...')
	divsPerFrag = []
	for div in range(0, 2**parties):
		arr = bitArray(div, parties)
		if sum(arr) == parties - unknowns:
			divsPerFrag.append(arr)
			print(str(arr))
			
	fragments = len(divsPerFrag)



	### verify ###

	print('Running self-test...')

	for c in range(0, 2**parties):
		partiesInCombo = bitArray(c, parties)
		result = [0 for xxx in range(0, fragments)]
		for p in range(0, parties):
			if partiesInCombo[p] == 0: continue
			for f in range(0, fragments):
				if divsPerFrag[f][p]:
					result[f] = 1;
					
		mass = sum(partiesInCombo)
		complete = sum(result) == fragments
		
		print('combi ' + str(partiesInCombo) + ' of ' + str(mass) + ' have ' + str(result) + ': ' + ('COMPLETE' if complete else ''))
		
		if complete and mass < criticalmass:
			print('OOOPS!')
			exit(1)
			
			
	### pretty print ###

	print('-----------------RESULTS------------------')
	print('Divide your secret in ' + str(fragments) + ' fragments.')
	print('Make ' + str(knowns) + ' copies of each fragment.')
	for p in range(0, parties):
		print('Give party #' + str(p+1) + ' the fragments ' + str(
			[f + 1 for f in range(0, fragments) if divsPerFrag[f][p]]))
	

def bitArray(num, bits):
	return [1 if num & 1 << b else 0 for b in range(0, bits)]
	
if __name__ == '__main__': main()

