ipt = ["See-Mong Tan",
"Stephen Pratt",
"Matthew Levine",
"Eric Breck",
"Riccardo Crepaldi"]

def everyone_sign(ipt):
    letters = {}
    for name in ipt:
        others = [other for other in ipt if other != name]
        letters[name] = "Thank you! Your friends, " + ", ".join(others)

    return letters

print(everyone_sign(ipt))