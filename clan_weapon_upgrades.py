import glob
import math

class upgrade:
    weapon = ""
    name = ""
    level = 0
    cost = 0.0
    rarity = 0
    shotsWhenFired = 0
    manufacturer = ""

    crit = 0.0
    dmg = 0
    stability = 0
    acc = 0
    heat = 0
    dmgHeat = 0
    tons = 0
    slots = 0
    projectilesPerShot = 0
    evasionIgnored = 0
    def __str__(self):
        return (self.weapon+"_"+str(self.level)+"-"+self.name)

upgradeList = []
def getUpgrades():
    file = open("upgrades.csv",'r')
    for line in file:
        if line.strip().startswith("#"):
            pass
        elif not line.split(",")[0]:
            pass
        else:
            #print(line)
            l = line.split(",")
            u = upgrade()
            u.weapon = l[0]
            u.name = l[1]
            u.level = int(l[2])
            u.cost = float(l[3])
            if not l[4]=="":
                u.rarity = int(l[4])
            if not l[5]=="":
                u.shotsWhenFired = int(l[5])
            if not l[6]=="":
                u.crit = float(l[6])
            if not l[7]=="":
                u.dmg = int(l[7])
            if not l[8]=="":
                u.stability = int(l[8])
            if not l[9]=="":
                u.acc = int(l[9])
            if not l[10]=="":
                u.heat = int(l[10])
            if not l[11]=="":
                u.dmgHeat = int(l[11])
            if not l[12]=="":
                u.tons = float(l[12])
            if not l[13].strip()=="":
                u.slots = int(l[13])
            if not l[14].strip()=="":
                u.projectilesPerShot = int(l[14])
            if not l[15].strip()=="":
                u.evasionIgnored = int(l[15])
            if not l[16].strip()=="":
                u.manufacturer = l[16]
            upgradeList.append(u)

def writeUpgrade(file,l):
    critUpgraded = False            #Done
    dmgUpgraded = False             #Done
    stabUpgraded = False            #Done
    accUpgraded = False             #Done
    heatUpgraded = False            #Done
    dmgHeatUpgraded = False         #Done
    tonsUpgraded = False            #Done
    slotsUpgraded = False           #Done
    shotsUpgraded = False           #Done
    evasionIgnoredUpgraded = False  #Done

    f = open(file, "r",encoding='utf-8-sig',errors='ignore')
    print(l)
    tmpName = ""
    if not l.manufacturer == "":
        tmpName = l.manufacturer
    else:
        tmpName = l.name
    f2 = open(file.replace("input","output").replace("0-STOCK",str(l.level)+"-"+tmpName), "w",encoding='utf-8-sig',errors='ignore' )
    for line in f:
        if "\"Id\""in line:
            f2.write(line.replace("0-STOCK", str(l.level)+"-"+tmpName))
        elif "\"Name\""in line or "\"UIName\""in line:
            if l.level>0:
                f2.write(line.replace("\",", str(l.level*" +"+"\",")))
            elif l.level<0:
                f2.write(line.replace("\",", str(math.fabs(l.level)*" -"+"\",")))
            elif l.level == 0:
                f2.write(line.replace("\",", str(" ~"+"\",")))
        elif "\"Cost\""in line:
            f2.write(line.split(':')[0]+": "+str("%i"%(int(line.split(':')[1].replace(',','').strip())*l.cost))+",\n")
        elif "\"Manufacturer\""in line and not l.manufacturer=="":
            f2.write(line.split(':')[0]+": \""+l.manufacturer+"\",\n")
        #Bonus A
        elif "\"BonusValueA\""in line:
            if not dmgUpgraded and not l.dmg == 0:
                dmgUpgraded = True
                f2.write(line.replace("\"\"","\""+str("+ %g"%(l.dmg))+" Dmg.\""))
            elif not stabUpgraded and not l.stability == 0:
                stabUpgraded = True
                f2.write(line.replace("\"\"","\""+str("+ %g"%(l.stability))+" Stab.\""))
            elif not accUpgraded and not l.acc == 0:
                accUpgraded = True
                f2.write(line.replace("\"\"","\""+str("+ %g"%(l.acc))+" Acc.\""))
            elif not heatUpgraded and not l.heat == 0:
                heatUpgraded = True
                f2.write(line.replace("\"\"","\""+str("%g"%(l.heat))+" Heat\""))
            elif not dmgHeatUpgraded and not l.heat == 0:
                dmgHeatUpgraded = True
                f2.write(line.replace("\"\"","\""+str("+ %g"%(l.dmgHeat))+" Dmg. (H)\""))
            elif not evasionIgnoredUpgraded and not l.evasionIgnored == 0:
                evasionIgnoredUpgraded = True
                f2.write(line.replace("\"\"","\""+str("- %g"%(l.evasionIgnored))+" Evas.\""))
            elif not shotsUpgraded and not l.shotsWhenFired == 0:
                shotsUpgraded = True
                f2.write(line.replace("\"\"","\""+str("+ %g"%(l.shotsWhenFired))+" Shots\""))
            elif not critUpgraded and not l.crit == 0:
                critUpgraded = True
                f2.write(line.replace("\"\"","\""+str("+ %g"%(l.crit*100))+"% Crit.\""))
            elif not tonsUpgraded and not l.tons == 0:
                tonsUpgraded = True
                f2.write(line.replace("\"\"","\""+str("%g"%l.tons)+" Tons\""))
            elif not slotsUpgraded and not l.slots == 0:
                slotsUpgraded = True
                f2.write(line.replace("\"\"","\""+str(l.slots)+" Slots\""))
        #Bonus B
        elif "\"BonusValueB\""in line:
            if not stabUpgraded and not l.stability == 0:
                stabUpgraded = True
                f2.write(line.replace("\"\"","\""+str("+ %g"%(l.stability))+" Stab.\""))
            elif not accUpgraded and not l.acc == 0:
                accUpgraded = True
                f2.write(line.replace("\"\"","\""+str("+ %g"%(l.acc))+" Acc.\""))
            elif not heatUpgraded and not l.heat == 0:
                heatUpgraded = True
                f2.write(line.replace("\"\"","\""+str("%g"%(l.heat))+" Heat\""))
            elif not dmgHeatUpgraded and not l.heat == 0:
                dmgHeatUpgraded = True
                f2.write(line.replace("\"\"","\""+str("+ %g"%(l.dmgHeat))+" Dmg. (H)\""))
            elif not evasionIgnoredUpgraded and not l.evasionIgnored == 0:
                evasionIgnoredUpgraded = True
                f2.write(line.replace("\"\"","\""+str("- %g"%(l.evasionIgnored))+" Evas.\""))
            elif not shotsUpgraded and not l.shotsWhenFired == 0:
                shotsUpgraded = True
                f2.write(line.replace("\"\"","\""+str("+ %g"%(l.shotsWhenFired))+" Shots\""))
            elif not critUpgraded and not l.crit == 0:
                critUpgraded = True
                f2.write(line.replace("\"\"","\""+str("+ %g"%(l.crit*100))+"% Crit.\""))
            elif not tonsUpgraded and not l.tons == 0:
                tonsUpgraded = True
                f2.write(line.replace("\"\"","\""+str("%g"%l.tons)+" Tons\""))
            elif not slotsUpgraded and not l.slots == 0:
                slotsUpgraded = True
                f2.write(line.replace("\"\"","\""+str(l.slots)+" Slots\""))
            else:
                f2.write(line)
        elif "\"Damage\"" in line and not l.dmg == 0:
            f2.write(line.split(':')[0]+": "+str("%g"%(int(line.split(':')[1].replace(',','').strip())+l.dmg))+",\n")
        elif "\"Instability\"" in line and not l.stability == 0:
            f2.write(line.split(':')[0]+": "+str("%g"%(int(line.split(':')[1].replace(',','').strip())+l.stability))+",\n")
        elif "\"AccuracyModifier\"" in line and not l.acc == 0 and line.strip().startswith("\"AccuracyModifier\""):
            f2.write(line.split(':')[0]+": "+str("%g"%(int(line.split(':')[1].replace(',','').strip())-l.acc))+",\n")
        elif "\"HeatGenerated\"" in line and not l.heat == 0:
            f2.write(line.split(':')[0]+": "+str("%g"%(int(line.split(':')[1].replace(',','').strip())+l.heat))+",\n")
        elif "\"HeatDamage\"" in line and not l.dmgHeat == 0:
            f2.write(line.split(':')[0]+": "+str("%g"%(int(line.split(':')[1].replace(',','').strip())+l.dmgHeat))+",\n")
        elif "\"shotsWhenFired\"" in line and not l.shotsWhenFired == 0:
            f2.write(line.split(':')[0]+": "+str("%g"%(float(line.split(':')[1].replace(',','').strip())+l.shotsWhenFired))+",\n")
        elif "\"CriticalChanceMultiplier\"" in line and not l.crit == 0:
            f2.write(line.split(':')[0]+": "+str("%g"%(float(line.split(':')[1].replace(',','').strip())+l.crit))+",\n")
        elif "\"Tonnage\""in line and ( not l.tons == 0 or (l.weapon == "MachineGun" and l.level>1)):
            if l.weapon == "MachineGun" and l.level>1:
                f2.write(line.split(':')[0]+": 0,\n")
            else:
                f2.write(line.split(':')[0]+": "+str("%g"%(float(line.split(':')[1].replace(',','').strip())+l.tons))+",\n")
        elif "\"InventorySize\""in line and not l.slots == 0:
            f2.write(line.split(':')[0]+": "+str("%g"%(float(line.split(':')[1].replace(',','').strip())+l.slots))+",\n")
        elif "\"EvasivePipsIgnored\"" in line and not l.evasionIgnored == 0:
            f2.write(line.split(':')[0]+": "+str("%g"%(int(line.split(':')[1].replace(',','').strip())+l.evasionIgnored))+",\n")
        elif "\"component_type_stock\""in line:
            f2.write(line.replace("component_type_stock","component_type_variant"))
            f2.write(line.replace("component_type_stock","component_type_variant"+str(l.level)))
        else:
            f2.write(line)
    f2.close()
    f.close()

def writeWeapons():
    files = glob.glob("input/*.json")
    #Seperating which weaponds get which upgrades bassed on weapon file name and weapon type in upgrades.csv
    for file in files:
        if "STOCK" in file:
            if "Gauss" in file:
                for l in upgradeList:
                    if "Gauss" in l.weapon:
                        writeUpgrade(file,l)
            elif "MachineGun" in file:
                for l in upgradeList:
                    if "MachineGun" in l.weapon:
                        writeUpgrade(file,l)
            elif "Autocannon" in file:
                if "LB" in file:
                    for l in upgradeList:
                        if "LBX" in l.weapon:
                            writeUpgrade(file,l)
                elif "UAC" in file:
                    for l in upgradeList:
                        if "UAC" in l.weapon:
                            writeUpgrade(file,l)
            elif "Pulse" in file:
                for l in upgradeList:
                    if "Pulse" in l.weapon:
                        writeUpgrade(file,l)
            elif "Laser" in file:
                for l in upgradeList:
                    if "Laser" in l.weapon:
                        writeUpgrade(file,l)
            elif "PPC" in file:
                for l in upgradeList:
                    if "PPC" in l.weapon:
                        writeUpgrade(file,l)
            elif "SRM" in file or "ATM" in file:
                for l in upgradeList:
                    if "SRM" in l.weapon:
                        writeUpgrade(file,l)
            elif "LRM" in file:
                for l in upgradeList:
                    if "LRM" in l.weapon:
                        writeUpgrade(file,l)
            elif "Flamer" in file:
                for l in upgradeList:
                    if "Flamer" in l.weapon:
                        writeUpgrade(file,l)

getUpgrades()
writeWeapons()