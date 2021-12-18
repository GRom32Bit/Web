from app import app
from flask import render_template
from random import randint

def AIDRandom():
    A = randint(1, 2)
    if (A == 1):
        B = 2
        while B == 2 or B == 3:
            B = randint(1, 6)
        if B == 1:
            C = randint(1, 4)
        elif B == 4:
            C = randint(1, 2)
        elif B == 5:
            C = randint(1, 10)
        else:
            C = randint(1, 5)
    if A == 2:
        B = 7
        while B == 7:
            B = randint(1, 8)
        C = 0
    ResStr = str(A) + str(B)
    if C != 0:
        ResStr = ResStr + str(C)
    return ResStr
def DIDRandom():
    A = randint(5, 7);
    if A == 5:
        B = randint(1, 6)
        C = 0
    if A == 6:
        B = randint(1, 2)
        if B == 1:
            C = randint(1, 5)
        else:
            C = 0
    if A == 7:
        B = 3
        while B == 3:
            B = randint(2, 5)
        if B == 2:
            C = randint(1, 13)
        if B == 4:
            C = randint(1, 5)
        if B == 5:
            C = randint(1, 7)
    ResStr = str(A) + str(B)
    if C != 0:
        ResStr = ResStr + str(C)
    return ResStr

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')
@app.route('/IL.html')
def IL():
    P1=P2=P3=P4=P5=P6=""
    while P1==P2 or P2==P3 or P1==P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('IL.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/ID.html')
def ID():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('ID.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/AECommon.html')
def AECommon():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('AECommon.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/ACCommon.html')
def ACCommon():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('ACCommon.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/AWCommon.html')
def AWCommon():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('AWCommon.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/AOCommon.html')
def AOCommon():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('AOCommon.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/EDCommon.html')
def EDCommon():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('EDCommon.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/DTCommon.html')
def DTCommon():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('DTCommon.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/DWCommon.html')
def DWCommon():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('DWCommon.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/DOCommon.html')
def DOCommon():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('DOCommon.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/first.html')
def first():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('first.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/second.html')
def second():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('second.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/third.html')
def third():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('third.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/forth.html')
def forth():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('forth.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/fifth.html')
def fifth():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('fifth.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/sixth.html')
def sixth():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('sixth.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/seventh.html')
def seventh():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('seventh.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/THL.html')
def THL():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('THL.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/echo.html')
def echo():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('echo.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/tyrant.html')
def tyrant():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('tyrant.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/sorrow.html')
def sorrow():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('sorrow.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/silverwolf.html')
def silverwolf():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('silverwolf.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/ripper.html')
def ripper():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('ripper.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/TCD.html')
def TCD():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('TCD.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/Aristocrat.html')
def Aristocrat():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('Aristocrat.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/Artist.html')
def Artist():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('Artist.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/Banker.html')
def Banker():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('Banker.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/BattleMaiden.html')
def BattleMaiden():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('BattleMaiden.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/Beard.html')
def Beard():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('Beard.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/Berserk.html')
def Berserk():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('Berserk.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/Buried.html')
def Buried():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('Buried.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/Butcher.html')
def Butcher():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('Butcher.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/Clicker.html')
def Clicker():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('Clicker.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/DorA.html')
def DorA():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('DorA.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/DPeer.html')
def DPeer():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('DPeer.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/Dreamer.html')
def Dreamer():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('Dreamer.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/Drummer.html')
def Drummer():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('Drummer.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/Drunkar.html')
def Drunkar():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('Drunkar.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/Envy.html')
def Envy():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('Envy.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/Faceless.html')
def Faceless():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('Faceless.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/Forester.html')
def Forester():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('Forester.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/Ghost.html')
def Ghost():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('Ghost.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/Gunsmith.html')
def Gunsmith():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('Gunsmith.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/Hawk.html')
def Hawk():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('Hawk.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/Healer.html')
def Healer():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('Healer.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/Hellmuse.html')
def Hellmuse():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('Hellmuse.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/Hive.html')
def Hive():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('Hive.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/Hydra.html')
def Hydra():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('Hydra.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/Iceberg.html')
def Iceberg():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('Iceberg.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/Illness.html')
def Illness():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('Illness.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/Illusionist.html')
def Illusionist():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('Illusionist.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/JestHarp.html')
def JestHarp():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('JestHarp.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/Judge.html')
def Judge():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('Judge.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/Lotus.html')
def Lotus():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('Lotus.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/Mirror.html')
def Mirror():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('Mirror.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/Monk.html')
def Monk():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('Monk.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/Mortar.html')
def Mortar():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('Mortar.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/Oldman.html')
def Oldman():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('Oldman.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/Outcast.html')
def Outcast():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('Outcast.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/Pain.html')
def Pain():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('Pain.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/Phoenix.html')
def Phoenix():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('Phoenix.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/Poison.html')
def Poison():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('Poison.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/PreDark.html')
def PreDark():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('PreDark.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/Raven.html')
def Raven():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('Raven.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/Reaper.html')
def Reaper():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('Reaper.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/RedThread.html')
def RedThread():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('RedThread.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/Rescuer.html')
def Rescuer():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('Rescuer.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/Rider.html')
def Rider():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('Rider.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/Scavenger.html')
def Scavenger():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('Scavenger.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/Splitted.html')
def Splitted():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('Splitted.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/Tumbler.html')
def Tumbler():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('Tumbler.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/Twins.html')
def Twins():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('Twins.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/Undertaker.html')
def Undertaker():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('Undertaker.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/Violinist.html')
def Violinist():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('Violinist.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/Vulkan.html')
def Vulkan():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('Vulkan.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")
@app.route('/WatchMaker.html')
def WatchMaker():
    P1 = P2 = P3 = P4 = P5 = P6 = ""
    while P1 == P2 or P2 == P3 or P1 == P3:
        P1 = AIDRandom()
        P2 = AIDRandom()
        P3 = AIDRandom()
    while P4 == P5 or P5 == P6 or P4 == P6:
        P4 = DIDRandom()
        P5 = DIDRandom()
        P6 = DIDRandom()
    return render_template('WatchMaker.html',A1="Preview/"+P1+".jpg",A2="Preview/"+P2+".jpg",A3="Preview/"+P3+".jpg",D1="Preview/"+P4+".jpg",D2="Preview/"+P5+".jpg",D3="Preview/"+P6+".jpg")