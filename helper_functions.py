from dateutil import parser
from datetime import *

# insert all functions made during sprints here
# import this with project3 code to test functions

# start sprint 1

def marrBeforeDiv(family, individual):
    arr = []
    for row in individual:
        f_id = row[8]
        name = row[1]
        for row in family:
            if row[0] == f_id:
                if row[2] != "NA":
                    marr = parser.parse(row[1])
                    div = parser.parse(row[2])
                    if (marr < div):
                        continue
                    else:
                        arr.append("Error: " + name + " was divorced before they were married.")
                else:
                    continue
    return arr
    
def marrBeforeDeath(family, individual):
    arr = []
    for row in individual:
        f_id = row[8]
        name = row[1]
        if row[6] != "NA" :
            death = parser.parse(row[6])
            for rowr in family:
                if rowr[0] == f_id:
                    marr = parser.parse(rowr[1])
                    if (marr < death):
                        continue
                    else:
                        arr.append("Error: " + name + " died before they were married.")
                else:
                    continue
    return arr



def birthBeforeMarr(family, individual):
    arr = []
    for row_i in individual:
        f_id = row_i[8]
        name = row_i[1]
        p_id = row_i[0]
        born = parser.parse(row_i[3])
        for row_f in family:
            if row_f[0] == f_id:
                marr = parser.parse(row_f[1])
                if (born < marr):
                    continue
                else:
                    arr.append("ERROR: FAMILY: US02: ID: "+ p_id +" F_ID: "+ f_id+": " + name + " was married before they were born.")
    return arr

'''
def marrBeforeDeath(family, individual):
    arr = []
    for row_i in individual:
        f_id = row_i[8]
        name = row_i[1]
        p_id = row_i[0]
        if row_i[6] != 'NA':
            death = parser.parse(row_i[6])
            for row_f in family:
                if row_f[0] == f_id:
                    marr = parser.parse(row_f[1])
                    if (marr < death):
                        continue
                    else:
                        arr.append("ERROR: FAMILY: US05: ID: "+ p_id +" F_ID: "+ f_id+": " + name + " died before they got married.")
    return arr

    '''

def birthBeforeDeath(family, individual):
    arr = []
    for row_i in individual:
        name = row_i[1]
        p_id = row_i[0]
        born = parser.parse(row_i[3])
        if row_i[6] != 'NA':
            death = parser.parse(row_i[6])
            if(born< death):
                continue
            else:
                arr.append("ERROR: INDIVIDUAL: US03: ID: "+ p_id +": " + name + " died before they were born.")
    return arr



def divBeforeDeath(family, individual):
    arr = []
    for row in individual:
        f_id = row[8]
        name = row[1]
        if row[6] != "NA":
            death = parser.parse(row[6])
            for rowr in family:
                if rowr[0] == f_id:
                    if rowr[2] != "NA":
                        div = parser.parse(rowr[2])
                        if (div < death):
                            continue
                        else:
                            arr.append("Error: " + name + " died before they were divorced.")
                else:
                    continue
    return arr

def lessThan150(family, individual):
    arr = []
    for row in individual:
        f_id = row[8]
        name = row[1]
        age = row[4]
        if (age < 150):
            continue
        else:
            arr.append("Error: " + name + " is over 150 years old.")
    return arr

def birthBeforePMarriage(family, individual):
    arr = []
    for row in individual:
        f_id = row[8]
        name = row[1]
        born = parser.parse(row[3])
        for rowf in family:
            if rowf[0] == f_id:
                marr = parser.parse(rowf[4])
                if (born < marr):
                    continue
                else:
                    arr.append("Error: " + name + " was born after their parents' marriage.")
            else:
                continue
    return arr
	
def birthBeforePDeath(family, individual):
    arr = []
    for row in individual:
        f_id = row[8]
        name = row[1]
        born = parser.parse(row[3])
        if row[6] != "NA":
            death = parser.parse(row[6])
            for rowf in family:
                if rowf[0] == f_id:
                    if (born < death):
                        continue
                    else:
                        arr.append("Error: " + name + " was born after their parents' death.")
                else:
                    continue
    return arr


# start sprint 2

def listDeceased(individual):
    deceased = []
    for row in individual:
        if row[6] != "NA":
            deceased.append(row[1])
    return deceased


def listLivingSingle(individual, family):
    single = []
    bool = False
    for row in individual:
        if row[4] >= 30 and row[5] == True:
            for r in family:
                if r[4] == row[1] or r[6] == row[1]:
                    bool = True
            if bool == False:
                single.append(row[1])
    return single


def uniqueID(individual, family):
    arr = []
    ids = []
    names = []
    for row_i in individual:
        name = row_i[1]
        p_id = row_i[0]
        if p_id not in ids:
            ids.append(p_id)
            names.append(name)
        else:
            index = ids.index(p_id)
            second_name = names[index]
            arr.append("ERROR: INDIVIDUAL: US22: ID: "+ p_id +": " + name + " and "+ second_name+ " have the same IDs")      
    return arr


def parentsNotTooOld(individual, family):
    arr = []
    for row_f in family:
        children = row_f[7]
        if children == "NA":
            continue
        dad_id = row_f[3]
        mom_id = row_f[5]
        mom_age = 0
        dad_age = 0
        for row_i in individual:
            if row_i[0] == mom_id:
                mom_age = row_i[4]
            elif row_i[0] == dad_id:
                dad_age = row_i[4]
        children_list = children.strip('][').split(', ')
        children_ages = []
        for child in children_list:
            for row_ii in individual:
                if row_ii[0] == child:
                    children_ages.append(row_ii[4])
        for i, child_age in enumerate(children_ages):
            if (mom_age - child_age) > 60:
                child_id = children_list[i]
                arr.append("ERROR: FAMILY: US12: ID: "+ mom_id +": " + mom_id + "is too old to be a parent to"+ child_id)
            if (dad_age - child_age) >80:
                child_id = children_list[i]
                arr.append("ERROR: FAMILY: US12: ID: "+ dad_id +": " + dad_id + "is too old to be a parent to"+ child_id)
    return arr

def marriageAfter14(individual, family):
    arr = []
    bool = False
    for row in individual:
        if row[4] >= 14:
            for r in family:
                if r[1] != "NA":
                    bool = True
            if bool == False:
                arr.append(row[1])
    return arr

def siblingsShouldNotMarry(family, individual):
    arr = []
    siblings = {}
    for row_i in individual:
        p_id = row_i[0]
        siblings[p_id] = row_i[5] # Store siblings' IDs and names in a dictionary

    for row_f in family:
        fam_id = row_f[0]
        husband_id = row_f[1]
        wife_id = row_f[2]
        children_ids = row_f[7]

        if husband_id in siblings.keys():
            for child_id in children_ids:
                if child_id in siblings.keys() and siblings[child_id] == wife_id:
                    arr.append("ERROR: FAMILY: US18: ID: " + fam_id + ": Sibling marriage between " + husband_id + " and " + child_id)
        
        if wife_id in siblings.keys():
            for child_id in children_ids:
                if child_id in siblings.keys() and siblings[child_id] == husband_id:
                    arr.append("ERROR: FAMILY: US18: ID: " + fam_id + ": Sibling marriage between " + wife_id + " and " + child_id)
    return arr

def noBigamy(individual, family):
	# verifies no bigamy
	bigamy = False
	spouses = []
	for row in individual:
		for fam in family:
			if fam[3] == row[1] or fam[5] == row[1]:
				spouses.append(row[1])
			if len(spouses) > 1:
				for spouse in spouses:
					for fam_2 in family:
						if fam_2 != fam:
							if spouse in fam_2:
								bigamy = True
		
	if bigamy:
		print("There are bigamy cases in this file.")
	else:
		print("There are no bigamy cases in this file.")
	
	


def listLivingMarried(individual, family):
	# listing living married individuals
	living_married = []
	bool = False
	for row in individual:
		if row[4] >= 30 and row[5] == True:
			for r in family:
				if r[4] == row[1] or r[6] == row[1]:
					bool = True
					living_married.append(row[1])
	return living_married


def maleLastNames(individual, family):
    result = []
    for i in family:
        dad = i[4]
        dad = dad.split(" ")[1]
        if i[7] == 'NA':
            pass
        else:
            children = i[7]
            for child in children:
                for i in individual:
                    if i[0] == child and i[2] == 'M':
                        child = i[1].split(" ")[1]
                        if (child != dad):
                            result.append("Error: " + i[0] + " does not have the same name as their father.")
                    else:
                        pass
    return result


def listOrphans(individual, family):
    orphans = []
    dad = 0
    mom = 0
    m_dead = False
    d_dead = False
    for row in individual:
        if row[4] < 18:
            f_id = str(row[7])
            for r in family:
                if f_id == r[0]:
                    dad = r[3]
                    mom = r[5]
                    d_dead = False
                    m_dead = False
            for r in individual:
                if r[0] == dad:
                    if r[5] == False:
                        d_dead = True
                elif r[0] == mom:
                    if r[5] == False:
                        m_dead = True
            if m_dead == True and d_dead == True:
                orphans.append(row[1])
    return orphans

def correctGender(individual, family):
    result=[]
    for frow in family:
        husbandID = frow[3]
        wifeID = frow[5]
        familyID = frow[0]
        for irow in individual:
            individualID = irow[0]
            individualGender = irow[2]
            if husbandID == individualID and individualGender == 'Female':
                result.append("Error: Individual " +individualID+ " is husband in family "+familyID+" but has gender: "+individualGender)
            elif wifeID == individualID and individualGender == 'Male':
                result.append("Error: Individual " +individualID+ " is wife in family "+familyID+" but has gender: "+individualGender)
    return result

def lessthan15Siblings(individual, family):
	siblings = []
    for row in individual:
		if row[2] == "F" or row[2] == "M"
			siblings.append(row[2])
	if len(siblings) >= 15:
		return False
	return True

	
def noMarriageDescendants(individual, family):

	dad_id = 0
	mom_id = 0
	for row in individual:
		f_id = str(row[7])
		for r in family:
			if f_id == r[0]:
				dad_id = r[3]
				mom_id = r[5]
			if dad_id == r[7] or mom_id == r[7]:
				return True
				
	return False


def individualAges(individuals):
    count = 0
    list = []
    for ind in individuals:
        if ind[4] > 0:
            list.append('ENTRY FOUND: '+ind[0]+': '+ind[1]+
                         ' is of age '+str(ind[4]))
            count += 1
    if count > 0:
        return list
    else:
        list.append('ERROR: No records found')
        return list
    

def datesBeforeCurrent(individual, family):
    list = []
    today = datetime.now()
    for ind in individual:
        ind_id = ind[0]
        birth = parser.parse(ind[3])
        if birth > today:
            list.append('ERROR: '+ind_id+' was born after today')
        if ind[6] == 'NA':
            pass
        else:
            death = parser.parse(ind[6])
            if death > today:
                list.append('ERROR: '+ind_id+' has died after today')
    for fam in family:
        husband = fam[3]
        wife = fam[5]
        if fam[1] == 'NA':
            pass
        else:
            marriage = parser.parse(fam[1])
            if marriage > today:
                list.append('ERROR: '+husband+' '+wife+' were married after today')
        if fam[2] == 'NA':
            pass
        else:
            divorce = parser.parse(fam[2])
            if divorce > today:
                list.append('ERROR: '+husband+' '+wife+' were divorced after today')
    return list

i1 = [['@I1@', 'Guy Stephenson', 'Female', '31 Dec 1989', 23, True, 'NA', '@F1@', '@F2@'],
            ['@I2@', 'Zara Theobold Lindholm', 'Female', '14 Feb 1972', 51, True, 'NA', 'NA', '@F3@'],
            ['@I3@', 'Henry Colaze', 'Male', '09 Nov 1983', 39, False, '05 Jan 1982', '@F1@', '@F5@'],
            ['@I4@', 'Mohammed Colaze', 'Male', '15 Jan 1940', 83, False, '05 Jan 2022', 'NA', '@F4@'],
            ['@I5@', 'Larsa Pippen', 'Female', '01 Apr 2000', 2, True, 'NA', '@F4@', 'NA'],
            ['@I6@', 'Bryce Maximus Pippen', 'Male', '12 Jul 2012', 10, True, '07 Jan 2020', '@F2@', '@F1'],
            ['@I7@', 'William Smyffe', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
            ['@I8@', 'Dawn O-Thyme', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
            ['@I9@', 'Female Brianson', 'Female', '27 Nov 1950', 72, True, 'NA', '@F5@', '@F4@'],
            ['@I10@', 'Habitat Correner', 'Female', '06 Feb 1960', 60, True, 'NA', '@F1@', '@F2@']]

f1 = [['@F1@', '12 Sep 2070', 'NA', '@I1@', 'Bryce Maximus Pippen', '@I11@', 'Zara Theobold Lindholm', 'NA'],
            ['@F2@', '02 May 1990', 'NA', '@I1@', 'Guy Stephenson', '@I10@', 'Habitat Correner', 'NA'],
            ['@F3@', '07 Mar 2002', '08 Jun 2002', '@I3@', 'Queezy Moonroof', '@I13@', 'Juicifruit Anime', "[@I2@]"],
            ['@F4@', '25 Nov 2005', '12 Oct 2015', '@I4@', 'Mohammed Colaze', '@I9@', 'Female Brianson', '[@I5@, @I6@]'],
            ['@F5@', '29 Feb 1996', 'NA', '@I15@', 'Easter Saturday', '@I5@', 'Freedom March', 'NA'],
            ['@F6@', '03 Jan 1997', 'NA', '@I6@', 'Saumit Okobachevsky', '@I16@', 'Jackie Dickinson', 'NA'],
            ['@F7@', '19 Jun 2009', 'NA', '@I7@', 'Henry Pride', '@I17@', 'Samantha Sassafras', 'NA'],
            ['@F8@', '25 Dec 1985', '21 Dec 2001', '@I18@', 'Jurgo McRich', '@I8@', 'Anna-Zon LeSplore', '[@I3@]'],
            ['@F10@', '30 Oct 2010', 'NA', '@I21@', 'Miguel Parkinson', '@I20@', 'Michelle Obama', 'NA']]
result = correctGender(i1, f1)
print(result)


