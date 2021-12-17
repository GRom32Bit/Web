from app import app
from flask import render_template
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')
@app.route('/IL.html')
def IL():
    return render_template('IL.html')
@app.route('/ID.html')
def ID():
    return render_template('ID.html')
@app.route('/AECommon.html')
def AECommon():
    return render_template('AECommon.html')
@app.route('/ACCommon.html')
def ACCommon():
    return render_template('ACCommon.html')
@app.route('/AWCommon.html')
def AWCommon():
    return render_template('AWCommon.html')
@app.route('/AOCommon.html')
def AOCommon():
    return render_template('AOCommon.html')
@app.route('/EDCommon.html')
def EDCommon():
    return render_template('EDCommon.html')
@app.route('/DTCommon.html')
def DTCommon():
    return render_template('DTCommon.html')
@app.route('/DWCommon.html')
def DWCommon():
    return render_template('DWCommon.html')
@app.route('/DOCommon.html')
def DOCommon():
    return render_template('DOCommon.html')
@app.route('/first.html')
def first():
    return render_template('first.html')
@app.route('/second.html')
def second():
    return render_template('second.html')
@app.route('/third.html')
def third():
    return render_template('third.html')
@app.route('/forth.html')
def forth():
    return render_template('forth.html')
@app.route('/fifth.html')
def fifth():
    return render_template('fifth.html')
@app.route('/sixth.html')
def sixth():
    return render_template('sixth.html')
@app.route('/seventh.html')
def seventh():
    return render_template('seventh.html')
@app.route('/THL.html')
def THL():
    return render_template('THL.html')
@app.route('/echo.html')
def echo():
    return render_template('echo.html')
@app.route('/tyrant.html')
def tyrant():
    return render_template('tyrant.html')
@app.route('/sorrow.html')
def sorrow():
    return render_template('sorrow.html')
@app.route('/silverwolf.html')
def silverwolf():
    return render_template('silverwolf.html')
@app.route('/ripper.html')
def ripper():
    return render_template('ripper.html')
@app.route('/TCD.html')
def TCD():
    return render_template('TCD.html')
@app.route('/Aristocrat.html')
def Aristocrat():
    return render_template('Aristocrat.html')
@app.route('/Artist.html')
def Artist():
    return render_template('Artist.html')
@app.route('/Banker.html')
def Banker():
    return render_template('Banker.html')
@app.route('/BattleMaiden.html')
def BattleMaiden():
    return render_template('BattleMaiden.html')
@app.route('/Beard.html')
def Beard():
    return render_template('Beard.html')
@app.route('/Berserk.html')
def Berserk():
    return render_template('Berserk.html')
@app.route('/Buried.html')
def Buried():
    return render_template('Buried.html')
@app.route('/Butcher.html')
def Butcher():
    return render_template('Butcher.html')
@app.route('/Clicker.html')
def Clicker():
    return render_template('Clicker.html')
@app.route('/DorA.html')
def DorA():
    return render_template('DorA.html')
@app.route('/DPeer.html')
def DPeer():
    return render_template('DPeer.html')
@app.route('/Dreamer.html')
def Dreamer():
    return render_template('Dreamer.html')
@app.route('/Drummer.html')
def Drummer():
    return render_template('Drummer.html')
@app.route('/Drunkar.html')
def Drunkar():
    return render_template('Drunkar.html')
@app.route('/Envy.html')
def Envy():
    return render_template('Envy.html')
@app.route('/Faceless.html')
def Faceless():
    return render_template('Faceless.html')
@app.route('/Forester.html')
def Forester():
    return render_template('Forester.html')
@app.route('/Ghost.html')
def Ghost():
    return render_template('Ghost.html')
@app.route('/Gunsmith.html')
def Gunsmith():
    return render_template('Gunsmith.html')
@app.route('/Hawk.html')
def Hawk():
    return render_template('Hawk.html')
@app.route('/Healer.html')
def Healer():
    return render_template('Healer.html')
@app.route('/Hellmuse.html')
def Hellmuse():
    return render_template('Hellmuse.html')
@app.route('/Hive.html')
def Hive():
    return render_template('Hive.html')
@app.route('/Hydra.html')
def Hydra():
    return render_template('Hydra.html')
@app.route('/Iceberg.html')
def Iceberg():
    return render_template('Iceberg.html')
@app.route('/Illness.html')
def Illness():
    return render_template('Illness.html')
@app.route('/Illusionist.html')
def Illusionist():
    return render_template('Illusionist.html')
@app.route('/JestHarp.html')
def JestHarp():
    return render_template('JestHarp.html')
@app.route('/Judge.html')
def Judge():
    return render_template('Judge.html')
@app.route('/Lotus.html')
def Lotus():
    return render_template('Lotus.html')
@app.route('/Mirror.html')
def Mirror():
    return render_template('Mirror.html')
@app.route('/Monk.html')
def Monk():
    return render_template('Monk.html')
@app.route('/Mortar.html')
def Mortar():
    return render_template('Mortar.html')
@app.route('/Oldman.html')
def Oldman():
    return render_template('Oldman.html')
@app.route('/Outcast.html')
def Outcast():
    return render_template('Outcast.html')
@app.route('/Pain.html')
def Pain():
    return render_template('Pain.html')
@app.route('/Phoenix.html')
def Phoenix():
    return render_template('Phoenix.html')
@app.route('/Poison.html')
def Poison():
    return render_template('Poison.html')
@app.route('/PreDark.html')
def PreDark():
    return render_template('PreDark.html')
@app.route('/Raven.html')
def Raven():
    return render_template('Raven.html')
@app.route('/Reaper.html')
def Reaper():
    return render_template('Reaper.html')
@app.route('/RedThread.html')
def RedThread():
    return render_template('RedThread.html')
@app.route('/Rescuer.html')
def Rescuer():
    return render_template('Rescuer.html')
@app.route('/Rider.html')
def Rider():
    return render_template('Rider.html')
@app.route('/Scavenger.html')
def Scavenger():
    return render_template('Scavenger.html')
@app.route('/Splitted.html')
def Splitted():
    return render_template('Splitted.html')
@app.route('/Tumbler.html')
def Tumbler():
    return render_template('Tumbler.html')
@app.route('/Twins.html')
def Twins():
    return render_template('Twins.html')
@app.route('/Undertaker.html')
def Undertaker():
    return render_template('Undertaker.html')
@app.route('/Violinist.html')
def Violinist():
    return render_template('Violinist.html')
@app.route('/Vulkan.html')
def Vulkan():
    return render_template('Vulkan.html')
@app.route('/WatchMaker.html')
def WatchMaker():
    return render_template('WatchMaker.html')