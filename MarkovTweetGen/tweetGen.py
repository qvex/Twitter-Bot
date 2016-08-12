import markovchain, re, string, os

original = open('text')
outfile = open('output', 'w')

newtext = []
mk = markovchain.Markov(original)

counter = 0
while counter < 10:  # Change 10 to however many lines you want to generate
    line = '\n' + mk.generate_markov_text()

    exclude = ['"', '(', ')', ';']
    line = ''.join(ch for ch in line if ch not in exclude)

    line = line.lower() + "."

    print(line)
    newtext.append(line)
    counter += 1

for aline in newtext:
    outfile.write(aline)  # makes text file line by line

outfile.close()
original.close()
