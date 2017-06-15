

p= input("Digite um valor para p: ")
q= input("Digite um valor para q: ")
r= input("Digite um valor para r: ")
per=""
pouv=""
pour=""
pouqer=""
pouqepour=""

if (q=="v") and (r=="v"):
    per=("v")
if (q=="v") and (r=="f"):
    per=("f")
if (q=="f") and (r=="v"):
    per=("f")
if (q=="f") and (r=="f"):
    per=("f")

print ("per = "+per)

if (p=="v") or (q=="v"):
    pouv=("v")
if (p=="v") or (q=="f"):
    pouv=("v")
if (p=="f") or (q=="v"):
    pouv=("v")
if (p=="f") or (q=="f"):
    pouv=("f")

print ("pouv= "+pouv)


if (p=="v") or (r=="v"):
    pour=("v")
if (p=="v") or(r=="f"):
    pour=("v")
if (p=="f") or (r=="v"):
    pour=("v")
if (p=="f") or (r=="f"):
    pour=("f")

print ("pour= "+pour)


if (p=="v")or (q=="v") and (r=="v"):
    pouqer=("v")
if (p=="v")or (q=="v") and (r=="f"):
    pouqer=("v")
if (p=="v")or (q=="f") and (r=="v"):
    pouqer=("v")
if (p=="v")or (q=="f") and (r=="f"):
    pouqer=("v")
if (p=="f")or (q=="v") and (r=="v"):
    pouqer=("v")
if (p=="f")or (q=="f") and (r=="f"):
    pouqer=("f")
if (p=="f")or (q=="v") and (r=="f"):
    pouqer=("f")
if (p=="f")or (q=="f") and (r=="v"):
    pouqer=("f")

print ("pouqer= "+pouqer)

if ((p=="v") or (q=="v")) and ((p=='v') or (r=="v")):
    pouqepour=("v")
if ((p=="v") or (q=="v")) and ((p=='v') or (r=="f")):
    pouqepour=("v")
if ((p=="v") or (q=="f")) and ((p=='v') or (r=="v")):
    pouqepour=("v")
if ((p=="v") or (q=="f")) and ((p=='v') or (r=="f")):
    pouqepour=("v")
if ((p=="f") or (q=="v")) and ((p=='f') or (r=="v")):
    pouqepour=("v")
if ((p=="f") or (q=="f")) and ((p=='f') or (r=="v")):
    pouqepour=("f")
if ((p=="f") or (q=="v")) and ((p=='f') or (r=="f")):
    pouqepour=("f")
if ((p=="f") or (q=="f")) and ((p=='f') or (r=="f")):
    pouqepour=("f")

print ("pouqepour= "+pouqepour)


if pouqer == pouqepour:
    print ("v")
