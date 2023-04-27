import unittest
import helper_functions

class testGED(unittest.TestCase):

    def test1_marriageBeforeDivorce(self):
        i1 = [['@I1@', 'Guy Stephenson', 'Male', '31 Dec 1999', 23, True, 'NA', '@F5@', '@F2@'],
        ['@I2@', 'Zara Theobold Lindholm', 'Female', '14 Feb 1972', 51, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Henry Colaze', 'Male', '09 Nov 1983', 39, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Mohammed Colaze', 'Male', '15 Jan 2004', 19, False, '05 Jan 2022', 'NA', '@F4@'],
        ['@I5@', 'Larsa Pippen', 'Female', '01 Apr 1970', 52, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Bryce Maximus Pippen', 'Male', '12 Jul 2001', 22, True, '07 Jan 2020', '@F2@', '@F1'],
        ['@I7@', 'William Smyffe', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Dawn O-Thyme', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Female Brianson', 'Male', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Habitat Correner', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]

        f1 = [['@F1@', '12 Sep 2070', 'NA', '@I1@', 'Bryce Maximus Pippen', '@I11@', 'Zara Theobold Lindholm', 'NA'],
        ['@F2@', '02 May 1990', 'NA', '@I1@', 'Guy Stephenson', '@10@', 'Habitat Correner', 'NA'],
        ['@F3@', '07 Jun 2002', '08 Mar 2002', '@I3@', 'Queezy Moonroof', '@I13@', 'Juicifruit Anime', '@I5@'],
        ['@F4@', '25 Nov 2005', '12 Oct 2015', '@I4@', 'Mohammed Colaze', '@I9@', 'Female Brianson', '@F2@'],
        ['@F5@', '29 Feb 1996', 'NA', '@I5@', 'Easter Saturday', '@I15@', 'Freedom March', 'NA'],
        ['@F6@', '03 Jan 1997', 'NA', '@I6@', 'Saumit Okobachevsky', '@I16@', 'Jackie Dickinson', 'NA'],
        ['@F7@', '19 Jun 2009', 'NA', '@I7@', 'Henry Pride', '@I17@', 'Samantha Sassafras', 'NA'],
        ['@F8@', '25 Dec 1985', '21 Dec 2001', '@I8@', 'Jurgo McRich', '@I18@', 'Anna-Zon LeSplore', '@F3@'],
        ['@F9@', '11 Nov 1976', '23 Nov 1999', '@I9@', 'Michael Stevens', '@I19@', 'Wacky Richardson', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Miguel Parkinson', '@I20@', 'Michelle Obama', 'NA']]
        result = helper_functions.marrBeforeDiv(f1, i1)
        self.assertEqual(result, ['Error: Zara Theobold Lindholm was divorced before they were married.'])

    def test2_marriageBeforeDivorce(self):
        i2 = [['@I1@', 'Guy Stephenson', 'Male', '31 Dec 1999', 23, True, 'NA', '@F5@', '@F2@'],
        ['@I2@', 'Zara Theobold Lindholm', 'Female', '14 Feb 1972', 51, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Henry Colaze', 'Male', '09 Nov 1983', 39, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Mohammed Colaze', 'Male', '15 Jan 2004', 19, False, '05 Jan 2022', 'NA', '@F4@'],
        ['@I5@', 'Larsa Pippen', 'Female', '01 Apr 1970', 52, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Bryce Maximus Pippen', 'Male', '12 Jul 2001', 22, True, '07 Jan 2020', '@F2@', '@F1'],
        ['@I7@', 'William Smyffe', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Dawn O-Thyme', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Female Brianson', 'Male', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Habitat Correner', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]

        f2 = [['@F1@', '12 Sep 2070', 'NA', '@I1@', 'Bryce Maximus Pippen', '@I11@', 'Zara Theobold Lindholm', 'NA'],
        ['@F2@', '02 May 1990', 'NA', '@I1@', 'Guy Stephenson', '@10@', 'Habitat Correner', 'NA'],
        ['@F3@', '07 Jun 2002', '08 Mar 2002', '@I3@', 'Queezy Moonroof', '@I13@', 'Juicifruit Anime', '@I5@'],
        ['@F4@', '25 Nov 2005', '12 Oct 2015', '@I4@', 'Mohammed Colaze', '@I9@', 'Female Brianson', '@F2@'],
        ['@F5@', '29 Feb 1996', 'NA', '@I5@', 'Easter Saturday', '@I15@', 'Freedom March', 'NA'],
        ['@F6@', '03 Jan 1997', 'NA', '@I6@', 'Saumit Okobachevsky', '@I16@', 'Jackie Dickinson', 'NA'],
        ['@F7@', '19 Jun 2009', 'NA', '@I7@', 'Henry Pride', '@I17@', 'Samantha Sassafras', 'NA'],
        ['@F8@', '25 Dec 1985', '21 Dec 2001', '@I8@', 'Jurgo McRich', '@I18@', 'Anna-Zon LeSplore', '@F3@'],
        ['@F9@', '11 Nov 1976', '23 Nov 1999', '@I9@', 'Michael Stevens', '@I19@', 'Wacky Richardson', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Miguel Parkinson', '@I20@', 'Michelle Obama', 'NA']]
        result = helper_functions.marrBeforeDiv(f2, i2)
        self.assertEqual(result, ['Error: Zara Theobold Lindholm was divorced before they were married.'])


    def test3_marriageBeforeDivorce(self):
        i3 = [['@I1@', 'Guy Stephenson', 'Male', '31 Dec 1999', 23, True, 'NA', '@F5@', '@F2@'],
        ['@I2@', 'Zara Theobold Lindholm', 'Female', '14 Feb 1972', 51, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Henry Colaze', 'Male', '09 Nov 1983', 39, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Mohammed Colaze', 'Male', '15 Jan 2004', 19, False, '05 Jan 2022', 'NA', '@F4@'],
        ['@I5@', 'Larsa Pippen', 'Female', '01 Apr 1970', 52, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Bryce Maximus Pippen', 'Male', '12 Jul 2001', 22, True, '07 Jan 2020', '@F2@', '@F1'],
        ['@I7@', 'William Smyffe', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Dawn O-Thyme', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Female Brianson', 'Male', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Habitat Correner', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]

        f3 = [['@F1@', '12 Sep 2070', 'NA', '@I1@', 'Bryce Maximus Pippen', '@I11@', 'Zara Theobold Lindholm', 'NA'],
        ['@F2@', '02 May 1990', 'NA', '@I1@', 'Guy Stephenson', '@10@', 'Habitat Correner', 'NA'],
        ['@F3@', '07 Jun 2002', '08 Mar 2002', '@I3@', 'Queezy Moonroof', '@I13@', 'Juicifruit Anime', '@I5@'],
        ['@F4@', '25 Nov 2005', '12 Oct 2015', '@I4@', 'Mohammed Colaze', '@I9@', 'Female Brianson', '@F2@'],
        ['@F5@', '29 Feb 1996', 'NA', '@I5@', 'Easter Saturday', '@I15@', 'Freedom March', 'NA'],
        ['@F6@', '03 Jan 1997', 'NA', '@I6@', 'Saumit Okobachevsky', '@I16@', 'Jackie Dickinson', 'NA'],
        ['@F7@', '19 Jun 2009', 'NA', '@I7@', 'Henry Pride', '@I17@', 'Samantha Sassafras', 'NA'],
        ['@F8@', '25 Dec 1985', '21 Dec 2001', '@I8@', 'Jurgo McRich', '@I18@', 'Anna-Zon LeSplore', '@F3@'],
        ['@F9@', '11 Nov 1976', '23 Nov 1999', '@I9@', 'Michael Stevens', '@I19@', 'Wacky Richardson', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Miguel Parkinson', '@I20@', 'Michelle Obama', 'NA']]
        result = helper_functions.marrBeforeDiv(f3, i3)
        self.assertEqual(result, ['Error: Zara Theobold Lindholm was divorced before they were married.'])


    def test1_marriageBeforeDeath(self):
        i4 = [['@I1@', 'Guy Stephenson', 'Male', '31 Dec 1999', 23, True, 'NA', '@F5@', '@F2@'],
        ['@I2@', 'Zara Theobold Lindholm', 'Female', '14 Feb 1972', 51, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Henry Colaze', 'Male', '09 Nov 1983', 39, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Mohammed Colaze', 'Male', '15 Jan 2004', 19, False, '05 Jan 2022', 'NA', '@F4@'],
        ['@I5@', 'Larsa Pippen', 'Female', '01 Apr 1970', 52, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Bryce Maximus Pippen', 'Male', '12 Jul 2001', 22, True, '07 Jan 2020', '@F2@', '@F1'],
        ['@I7@', 'William Smyffe', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Dawn O-Thyme', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Female Brianson', 'Male', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Habitat Correner', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]

        f4 = [['@F1@', '12 Sep 2070', 'NA', '@I1@', 'Bryce Maximus Pippen', '@I11@', 'Zara Theobold Lindholm', 'NA'],
        ['@F2@', '02 May 1990', 'NA', '@I1@', 'Guy Stephenson', '@10@', 'Habitat Correner', 'NA'],
        ['@F3@', '07 Jun 2002', '08 Mar 2002', '@I3@', 'Queezy Moonroof', '@I13@', 'Juicifruit Anime', '@I5@'],
        ['@F4@', '25 Nov 2005', '12 Oct 2015', '@I4@', 'Mohammed Colaze', '@I9@', 'Female Brianson', '@F2@'],
        ['@F5@', '29 Feb 1996', 'NA', '@I5@', 'Easter Saturday', '@I15@', 'Freedom March', 'NA'],
        ['@F6@', '03 Jan 1997', 'NA', '@I6@', 'Saumit Okobachevsky', '@I16@', 'Jackie Dickinson', 'NA'],
        ['@F7@', '19 Jun 2009', 'NA', '@I7@', 'Henry Pride', '@I17@', 'Samantha Sassafras', 'NA'],
        ['@F8@', '25 Dec 1985', '21 Dec 2001', '@I8@', 'Jurgo McRich', '@I18@', 'Anna-Zon LeSplore', '@F3@'],
        ['@F9@', '11 Nov 1976', '23 Nov 1999', '@I9@', 'Michael Stevens', '@I19@', 'Wacky Richardson', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Miguel Parkinson', '@I20@', 'Michelle Obama', 'NA']]
        result = helper_functions.marrBeforeDeath(f4, i4)
        self.assertEqual(result, [])

    def test2_marriageBeforeDeath(self):
        i5 = [['@I1@', 'Guy Stephenson', 'Male', '31 Dec 1999', 23, True, 'NA', '@F5@', '@F2@'],
        ['@I2@', 'Zara Theobold Lindholm', 'Female', '14 Feb 1972', 51, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Henry Colaze', 'Male', '09 Nov 1983', 39, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Mohammed Colaze', 'Male', '15 Jan 2004', 19, False, '05 Jan 2022', 'NA', '@F4@'],
        ['@I5@', 'Larsa Pippen', 'Female', '01 Apr 1970', 52, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Bryce Maximus Pippen', 'Male', '12 Jul 2001', 22, True, '07 Jan 2020', '@F2@', '@F1'],
        ['@I7@', 'William Smyffe', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Dawn O-Thyme', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Female Brianson', 'Male', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Habitat Correner', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]

        f5 = [['@F1@', '12 Sep 2070', 'NA', '@I1@', 'Bryce Maximus Pippen', '@I11@', 'Zara Theobold Lindholm', 'NA'],
        ['@F2@', '02 May 1990', 'NA', '@I1@', 'Guy Stephenson', '@10@', 'Habitat Correner', 'NA'],
        ['@F3@', '07 Jun 2002', '08 Mar 2002', '@I3@', 'Queezy Moonroof', '@I13@', 'Juicifruit Anime', '@I5@'],
        ['@F4@', '25 Nov 2005', '12 Oct 2015', '@I4@', 'Mohammed Colaze', '@I9@', 'Female Brianson', '@F2@'],
        ['@F5@', '29 Feb 1996', 'NA', '@I5@', 'Easter Saturday', '@I15@', 'Freedom March', 'NA'],
        ['@F6@', '03 Jan 1997', 'NA', '@I6@', 'Saumit Okobachevsky', '@I16@', 'Jackie Dickinson', 'NA'],
        ['@F7@', '19 Jun 2009', 'NA', '@I7@', 'Henry Pride', '@I17@', 'Samantha Sassafras', 'NA'],
        ['@F8@', '25 Dec 1985', '21 Dec 2001', '@I8@', 'Jurgo McRich', '@I18@', 'Anna-Zon LeSplore', '@F3@'],
        ['@F9@', '11 Nov 1976', '23 Nov 1999', '@I9@', 'Michael Stevens', '@I19@', 'Wacky Richardson', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Miguel Parkinson', '@I20@', 'Michelle Obama', 'NA']]
        result = helper_functions.marrBeforeDeath(f5, i5)
        self.assertEqual(result, [])

    def test3_marriageBeforeDeath(self):
        i6 = [['@I1@', 'Guy Stephenson', 'Male', '31 Dec 1999', 23, True, 'NA', '@F5@', '@F2@'],
        ['@I2@', 'Zara Theobold Lindholm', 'Female', '14 Feb 1972', 51, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Henry Colaze', 'Male', '09 Nov 1983', 39, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Mohammed Colaze', 'Male', '15 Jan 2004', 19, False, '05 Jan 2022', 'NA', '@F4@'],
        ['@I5@', 'Larsa Pippen', 'Female', '01 Apr 1970', 52, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Bryce Maximus Pippen', 'Male', '12 Jul 2001', 22, True, '07 Jan 2020', '@F2@', '@F1'],
        ['@I7@', 'William Smyffe', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Dawn O-Thyme', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Female Brianson', 'Male', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Habitat Correner', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]

        f6 = [['@F1@', '12 Sep 2070', 'NA', '@I1@', 'Bryce Maximus Pippen', '@I11@', 'Zara Theobold Lindholm', 'NA'],
        ['@F2@', '02 May 1990', 'NA', '@I1@', 'Guy Stephenson', '@10@', 'Habitat Correner', 'NA'],
        ['@F3@', '07 Jun 2002', '08 Mar 2002', '@I3@', 'Queezy Moonroof', '@I13@', 'Juicifruit Anime', '@I5@'],
        ['@F4@', '25 Nov 2005', '12 Oct 2015', '@I4@', 'Mohammed Colaze', '@I9@', 'Female Brianson', '@F2@'],
        ['@F5@', '29 Feb 1996', 'NA', '@I5@', 'Easter Saturday', '@I15@', 'Freedom March', 'NA'],
        ['@F6@', '03 Jan 1997', 'NA', '@I6@', 'Saumit Okobachevsky', '@I16@', 'Jackie Dickinson', 'NA'],
        ['@F7@', '19 Jun 2009', 'NA', '@I7@', 'Henry Pride', '@I17@', 'Samantha Sassafras', 'NA'],
        ['@F8@', '25 Dec 1985', '21 Dec 2001', '@I8@', 'Jurgo McRich', '@I18@', 'Anna-Zon LeSplore', '@F3@'],
        ['@F9@', '11 Nov 1976', '23 Nov 1999', '@I9@', 'Michael Stevens', '@I19@', 'Wacky Richardson', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Miguel Parkinson', '@I20@', 'Michelle Obama', 'NA']]
        result = helper_functions.marrBeforeDeath(f6, i6)
        self.assertEqual(result, [])


    def test1_birthBeforeMarriage(self):
        i1 = [['@I1@', 'Guy Stephenson', 'Male', '31 Dec 1999', 23, True, 'NA', '@F5@', '@F2@'],
        ['@I2@', 'Zara Theobold Lindholm', 'Female', '14 Feb 1972', 51, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Henry Colaze', 'Male', '09 Nov 1983', 39, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Mohammed Colaze', 'Male', '15 Jan 2004', 19, False, '05 Jan 2022', 'NA', '@F4@'],
        ['@I5@', 'Larsa Pippen', 'Female', '01 Apr 1970', 52, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Bryce Maximus Pippen', 'Male', '12 Jul 2001', 22, True, '07 Jan 2020', '@F2@', '@F1'],
        ['@I7@', 'William Smyffe', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Dawn O-Thyme', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Female Brianson', 'Male', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Habitat Correner', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]

        f1 = [['@F1@', '12 Sep 2070', 'NA', '@I1@', 'Bryce Maximus Pippen', '@I11@', 'Zara Theobold Lindholm', 'NA'],
        ['@F2@', '02 May 1990', 'NA', '@I1@', 'Guy Stephenson', '@10@', 'Habitat Correner', 'NA'],
        ['@F3@', '07 Mar 2002', '08 Jun 2002', '@I3@', 'Queezy Moonroof', '@I13@', 'Juicifruit Anime', '@I5@'],
        ['@F4@', '25 Nov 2005', '12 Oct 2015', '@I4@', 'Mohammed Colaze', '@I9@', 'Female Brianson', '@F2@'],
        ['@F5@', '29 Feb 1996', 'NA', '@I5@', 'Easter Saturday', '@I15@', 'Freedom March', 'NA'],
        ['@F6@', '03 Jan 1997', 'NA', '@I6@', 'Saumit Okobachevsky', '@I16@', 'Jackie Dickinson', 'NA'],
        ['@F7@', '19 Jun 2009', 'NA', '@I7@', 'Henry Pride', '@I17@', 'Samantha Sassafras', 'NA'],
        ['@F8@', '25 Dec 1985', '21 Dec 2001', '@I8@', 'Jurgo McRich', '@I18@', 'Anna-Zon LeSplore', '@F3@'],
        ['@F9@', '11 Nov 1976', '23 Nov 1999', '@I9@', 'Michael Stevens', '@I19@', 'Wacky Richardson', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Miguel Parkinson', '@I20@', 'Michelle Obama', 'NA']]
        result = helper_functions.birthBeforeMarr(f1, i1)
        self.assertEqual(result, ['ERROR: FAMILY: US02: ID: @I1@ F_ID: @F2@: Guy Stephenson was married before they were born.'])

    def test2_birthBeforeMarriage(self):
        i1 = [['@I1@', 'Guy Stephenson', 'Male', '31 Dec 1969', 23, True, 'NA', '@F5@', '@F2@'],
        ['@I2@', 'Zara Theobold Lindholm', 'Female', '14 Feb 1972', 51, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Henry Colaze', 'Male', '09 Nov 1983', 39, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Mohammed Colaze', 'Male', '15 Jan 2004', 19, False, '05 Jan 2022', 'NA', '@F4@'],
        ['@I5@', 'Larsa Pippen', 'Female', '01 Apr 1970', 52, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Bryce Maximus Pippen', 'Male', '12 Jul 2001', 22, True, '07 Jan 2020', '@F2@', '@F1'],
        ['@I7@', 'William Smyffe', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Dawn O-Thyme', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Female Brianson', 'Male', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Habitat Correner', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]

        f1 = [['@F1@', '12 Sep 2070', 'NA', '@I1@', 'Bryce Maximus Pippen', '@I11@', 'Zara Theobold Lindholm', 'NA'],
        ['@F2@', '02 May 1990', 'NA', '@I1@', 'Guy Stephenson', '@10@', 'Habitat Correner', 'NA'],
        ['@F3@', '07 Mar 2002', '08 Jun 2002', '@I3@', 'Queezy Moonroof', '@I13@', 'Juicifruit Anime', '@I5@'],
        ['@F4@', '25 Nov 2005', '12 Oct 2015', '@I4@', 'Mohammed Colaze', '@I9@', 'Female Brianson', '@F2@'],
        ['@F5@', '29 Feb 1996', 'NA', '@I5@', 'Easter Saturday', '@I15@', 'Freedom March', 'NA'],
        ['@F6@', '03 Jan 1997', 'NA', '@I6@', 'Saumit Okobachevsky', '@I16@', 'Jackie Dickinson', 'NA'],
        ['@F7@', '19 Jun 2009', 'NA', '@I7@', 'Henry Pride', '@I17@', 'Samantha Sassafras', 'NA'],
        ['@F8@', '25 Dec 1985', '21 Dec 2001', '@I8@', 'Jurgo McRich', '@I18@', 'Anna-Zon LeSplore', '@F3@'],
        ['@F9@', '11 Nov 1976', '23 Nov 1999', '@I9@', 'Michael Stevens', '@I19@', 'Wacky Richardson', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Miguel Parkinson', '@I20@', 'Michelle Obama', 'NA']]
        result = helper_functions.birthBeforeMarr(f1, i1)
        self.assertEqual(result, [])

    def test1_birthBeforeDeath(self):
        i1 = [['@I1@', 'Guy Stephenson', 'Male', '31 Dec 1999', 23, True, 'NA', '@F5@', '@F2@'],
        ['@I2@', 'Zara Theobold Lindholm', 'Female', '14 Feb 1972', 51, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Henry Colaze', 'Male', '09 Nov 1983', 39, False, '05 Jan 1982', '@F1@', '@F5@'],
        ['@I4@', 'Mohammed Colaze', 'Male', '15 Jan 2004', 19, False, '05 Jan 2022', 'NA', '@F4@'],
        ['@I5@', 'Larsa Pippen', 'Female', '01 Apr 1970', 52, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Bryce Maximus Pippen', 'Male', '12 Jul 2001', 22, True, '07 Jan 2020', '@F2@', '@F1'],
        ['@I7@', 'William Smyffe', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Dawn O-Thyme', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Female Brianson', 'Male', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Habitat Correner', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]

        f1 = [['@F1@', '12 Sep 2070', 'NA', '@I1@', 'Bryce Maximus Pippen', '@I11@', 'Zara Theobold Lindholm', 'NA'],
        ['@F2@', '02 May 1990', 'NA', '@I1@', 'Guy Stephenson', '@10@', 'Habitat Correner', 'NA'],
        ['@F3@', '07 Mar 2002', '08 Jun 2002', '@I3@', 'Queezy Moonroof', '@I13@', 'Juicifruit Anime', '@I5@'],
        ['@F4@', '25 Nov 2005', '12 Oct 2015', '@I4@', 'Mohammed Colaze', '@I9@', 'Female Brianson', '@F2@'],
        ['@F5@', '29 Feb 1996', 'NA', '@I5@', 'Easter Saturday', '@I15@', 'Freedom March', 'NA'],
        ['@F6@', '03 Jan 1997', 'NA', '@I6@', 'Saumit Okobachevsky', '@I16@', 'Jackie Dickinson', 'NA'],
        ['@F7@', '19 Jun 2009', 'NA', '@I7@', 'Henry Pride', '@I17@', 'Samantha Sassafras', 'NA'],
        ['@F8@', '25 Dec 1985', '21 Dec 2001', '@I8@', 'Jurgo McRich', '@I18@', 'Anna-Zon LeSplore', '@F3@'],
        ['@F9@', '11 Nov 1976', '23 Nov 1999', '@I9@', 'Michael Stevens', '@I19@', 'Wacky Richardson', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Miguel Parkinson', '@I20@', 'Michelle Obama', 'NA']]
        result = helper_functions.birthBeforeDeath(f1, i1)
        self.assertEqual(result, ['ERROR: INDIVIDUAL: US03: ID: @I3@: Henry Colaze died before they were born.'])

    def test2_birthBeforeDeath(self):
        i1 = [['@I1@', 'Guy Stephenson', 'Male', '31 Dec 1999', 23, True, 'NA', '@F5@', '@F2@'],
        ['@I2@', 'Zara Theobold Lindholm', 'Female', '14 Feb 1972', 51, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Henry Colaze', 'Male', '09 Nov 1983', 39, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Mohammed Colaze', 'Male', '15 Jan 2004', 19, False, '05 Jan 2022', 'NA', '@F4@'],
        ['@I5@', 'Larsa Pippen', 'Female', '01 Apr 1970', 52, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Bryce Maximus Pippen', 'Male', '12 Jul 2001', 22, True, '07 Jan 2020', '@F2@', '@F1'],
        ['@I7@', 'William Smyffe', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Dawn O-Thyme', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Female Brianson', 'Male', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Habitat Correner', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]

        f1 = [['@F1@', '12 Sep 2070', 'NA', '@I1@', 'Bryce Maximus Pippen', '@I11@', 'Zara Theobold Lindholm', 'NA'],
        ['@F2@', '02 May 1990', 'NA', '@I1@', 'Guy Stephenson', '@10@', 'Habitat Correner', 'NA'],
        ['@F3@', '07 Mar 2002', '08 Jun 2002', '@I3@', 'Queezy Moonroof', '@I13@', 'Juicifruit Anime', '@I5@'],
        ['@F4@', '25 Nov 2005', '12 Oct 2015', '@I4@', 'Mohammed Colaze', '@I9@', 'Female Brianson', '@F2@'],
        ['@F5@', '29 Feb 1996', 'NA', '@I5@', 'Easter Saturday', '@I15@', 'Freedom March', 'NA'],
        ['@F6@', '03 Jan 1997', 'NA', '@I6@', 'Saumit Okobachevsky', '@I16@', 'Jackie Dickinson', 'NA'],
        ['@F7@', '19 Jun 2009', 'NA', '@I7@', 'Henry Pride', '@I17@', 'Samantha Sassafras', 'NA'],
        ['@F8@', '25 Dec 1985', '21 Dec 2001', '@I8@', 'Jurgo McRich', '@I18@', 'Anna-Zon LeSplore', '@F3@'],
        ['@F9@', '11 Nov 1976', '23 Nov 1999', '@I9@', 'Michael Stevens', '@I19@', 'Wacky Richardson', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Miguel Parkinson', '@I20@', 'Michelle Obama', 'NA']]
        result = helper_functions.birthBeforeDeath(f1, i1)
        self.assertEqual(result, [])
        
    def test1_divorceBeforeDeath(self):
        i1 = [['@I1@', 'Guy Stephenson', 'Male', '31 Dec 1999', 23, True, 'NA', '@F5@', '@F2@'],
        ['@I2@', 'Zara Theobold Lindholm', 'Female', '14 Feb 1972', 51, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Henry Colaze', 'Male', '09 Nov 1983', 39, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Mohammed Colaze', 'Male', '15 Jan 2004', 19, False, '05 Jan 2022', 'NA', '@F4@'],
        ['@I5@', 'Larsa Pippen', 'Female', '01 Apr 1970', 52, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Bryce Maximus Pippen', 'Male', '12 Jul 2001', 22, True, '07 Jan 2020', '@F2@', '@F1'],
        ['@I7@', 'William Smyffe', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Dawn O-Thyme', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Female Brianson', 'Male', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Habitat Correner', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]

        f1 = [['@F1@', '12 Sep 2070', 'NA', '@I1@', 'Bryce Maximus Pippen', '@I11@', 'Zara Theobold Lindholm', 'NA'],
        ['@F2@', '02 May 1990', 'NA', '@I1@', 'Guy Stephenson', '@10@', 'Habitat Correner', 'NA'],
        ['@F3@', '07 Jun 2002', '08 Mar 2022', '@I3@', 'Queezy Moonroof', '@I13@', 'Juicifruit Anime', '@I5@'],
        ['@F4@', '25 Nov 2005', '12 Oct 2015', '@I4@', 'Mohammed Colaze', '@I9@', 'Female Brianson', '@F2@'],
        ['@F5@', '29 Feb 1996', '06 Jan 2022', '@I5@', 'Easter Saturday', '@I15@', 'Freedom March', 'NA'],
        ['@F6@', '03 Jan 1997', 'NA', '@I6@', 'Saumit Okobachevsky', '@I16@', 'Jackie Dickinson', 'NA'],
        ['@F7@', '19 Jun 2009', 'NA', '@I7@', 'Henry Pride', '@I17@', 'Samantha Sassafras', 'NA'],
        ['@F8@', '25 Dec 1985', '21 Dec 2001', '@I8@', 'Jurgo McRich', '@I18@', 'Anna-Zon LeSplore', '@F3@'],
        ['@F9@', '11 Nov 1976', '23 Nov 1999', '@I9@', 'Michael Stevens', '@I19@', 'Wacky Richardson', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Miguel Parkinson', '@I20@', 'Michelle Obama', 'NA']]
        result = helper_functions.divBeforeDeath(f1, i1)
        self.assertEqual(result, ['Error: Henry Colaze died before they were divorced.'])

    def test1_lessThan150yearsOld(self):
        i4 = [['@I1@', 'Guy Stephenson', 'Male', '31 Dec 1999', 23, True, 'NA', '@F5@', '@F2@'],
        ['@I2@', 'Zara Theobold Lindholm', 'Female', '14 Feb 1972', 51, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Henry Colaze', 'Male', '09 Nov 1983', 39, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Mohammed Colaze', 'Male', '15 Jan 2004', 19, False, '05 Jan 2022', 'NA', '@F4@'],
        ['@I5@', 'Larsa Pippen', 'Female', '01 Apr 1870', 152, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Bryce Maximus Pippen', 'Male', '12 Jul 2001', 22, True, '07 Jan 2020', '@F2@', '@F1'],
        ['@I7@', 'William Smyffe', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Dawn O-Thyme', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Female Brianson', 'Male', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Habitat Correner', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]

        f4 = [['@F1@', '12 Sep 2070', 'NA', '@I1@', 'Bryce Maximus Pippen', '@I11@', 'Zara Theobold Lindholm', 'NA'],
        ['@F2@', '02 May 1990', 'NA', '@I1@', 'Guy Stephenson', '@10@', 'Habitat Correner', 'NA'],
        ['@F3@', '07 Jun 2002', '08 Mar 2002', '@I3@', 'Queezy Moonroof', '@I13@', 'Juicifruit Anime', '@I5@'],
        ['@F4@', '25 Nov 2005', '12 Oct 2015', '@I4@', 'Mohammed Colaze', '@I9@', 'Female Brianson', '@F2@'],
        ['@F5@', '29 Feb 1996', 'NA', '@I5@', 'Easter Saturday', '@I15@', 'Freedom March', 'NA'],
        ['@F6@', '03 Jan 1997', 'NA', '@I6@', 'Saumit Okobachevsky', '@I16@', 'Jackie Dickinson', 'NA'],
        ['@F7@', '19 Jun 2009', 'NA', '@I7@', 'Henry Pride', '@I17@', 'Samantha Sassafras', 'NA'],
        ['@F8@', '25 Dec 1985', '21 Dec 2001', '@I8@', 'Jurgo McRich', '@I18@', 'Anna-Zon LeSplore', '@F3@'],
        ['@F9@', '11 Nov 1976', '23 Nov 1999', '@I9@', 'Michael Stevens', '@I19@', 'Wacky Richardson', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Miguel Parkinson', '@I20@', 'Michelle Obama', 'NA']]
        result = helper_functions.lessThan150(f4, i4)
        self.assertEqual(result, ['Error: Larsa Pippen is over 150 years old.'])

       
    def test1_listDeceased(self):
        i1 = [['@I1@', 'Guy Stephenson', 'Male', '31 Dec 1999', 23, True, 'NA', '@F5@', '@F2@'],
        ['@I2@', 'Zara Theobold Lindholm', 'Female', '14 Feb 1972', 51, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Henry Colaze', 'Male', '09 Nov 1983', 39, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Mohammed Colaze', 'Male', '15 Jan 2004', 19, False, '05 Jan 2022', 'NA', '@F4@'],
        ['@I5@', 'Larsa Pippen', 'Female', '01 Apr 1970', 52, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Bryce Maximus Pippen', 'Male', '12 Jul 2001', 22, False, '07 Jan 2020', '@F2@', '@F1'],
        ['@I7@', 'William Smyffe', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Dawn O-Thyme', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Female Brianson', 'Male', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Habitat Correner', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]
        result = helper_functions.listDeceased(i1)
        self.assertEqual(result, ['Henry Colaze', 'Mohammed Colaze', 'Bryce Maximus Pippen'])

    def test2_listDeceased(self):
        i2 = [['@I1@', 'Guy Stephenson', 'Male', '31 Dec 1999', 23, True, 'NA', '@F5@', '@F2@'],
        ['@I2@', 'Zara Theobold Lindholm', 'Female', '14 Feb 1972', 51, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Henry Colaze', 'Male', '09 Nov 1983', 39, True, 'NA', '@F1@', '@F5@'],
        ['@I4@', 'Mohammed Colaze', 'Male', '15 Jan 2004', 19, True, 'NA', 'NA', '@F4@'],
        ['@I5@', 'Larsa Pippen', 'Female', '01 Apr 1970', 52, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Bryce Maximus Pippen', 'Male', '12 Jul 2001', 22, True, 'NA', '@F2@', '@F1'],
        ['@I7@', 'William Smyffe', 'Male', '11 Sep 1990', 31, False, '05 Jan 2022', 'NA', '@F1@'],
        ['@I8@', 'Dawn O-Thyme', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Female Brianson', 'Male', '27 Nov 1989', 32, False, '05 Jan 2022', '@F5@', '@F4@'],
        ['@I10@', 'Habitat Correner', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]
        result = helper_functions.listDeceased(i2)
        self.assertEqual(result, ['William Smyffe', 'Female Brianson'])

    def test3_listDeceased(self):
        i3 = [['@I1@', 'Guy Stephenson', 'Male', '31 Dec 1999', 23, True, 'NA', '@F5@', '@F2@'],
        ['@I2@', 'Zara Theobold Lindholm', 'Female', '14 Feb 1972', 51, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Henry Colaze', 'Male', '09 Nov 1983', 39, True, 'NA', '@F1@', '@F5@'],
        ['@I4@', 'Mohammed Colaze', 'Male', '15 Jan 2004', 19, True, 'NA', 'NA', '@F4@'],
        ['@I5@', 'Larsa Pippen', 'Female', '01 Apr 1970', 52, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Bryce Maximus Pippen', 'Male', '12 Jul 2001', 22, True, 'NA', '@F2@', '@F1'],
        ['@I7@', 'William Smyffe', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Dawn O-Thyme', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Female Brianson', 'Male', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Habitat Correner', 'Female', '06 Feb 1960', 60, False, '12 Mar 2023', '@F3@', '@F2@']]
        result = helper_functions.listDeceased(i3)
        self.assertEqual(result, ['Habitat Correner'])

    def test4_listDeceased(self):
        i4 = [['@I1@', 'Guy Stephenson', 'Male', '31 Dec 1999', 23, True, 'NA', '@F5@', '@F2@'],
        ['@I2@', 'Zara Theobold Lindholm', 'Female', '14 Feb 1972', 51, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Henry Colaze', 'Male', '09 Nov 1983', 39, True, 'NA', '@F1@', '@F5@'],
        ['@I4@', 'Mohammed Colaze', 'Male', '15 Jan 2004', 19, True, 'NA', 'NA', '@F4@'],
        ['@I5@', 'Larsa Pippen', 'Female', '01 Apr 1970', 52, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Bryce Maximus Pippen', 'Male', '12 Jul 2001', 22, True, 'NA', '@F2@', '@F1'],
        ['@I7@', 'William Smyffe', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Dawn O-Thyme', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Female Brianson', 'Male', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Habitat Correner', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]
        result = helper_functions.listDeceased(i4)
        self.assertEqual(result, [])


    def test1_listLivingSingle(self):
        i1 = [['@I1@', 'Guy Stephenson', 'Male', '23 Dec 1985', 36, True, 'NA', '@F5@', 'NA'],
        ['@I2@', 'Zara Theobold Lindholm', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Henry Colaze', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Mohammed Colaze', 'Female', '17 Oct 1977', 44, True, 'NA', 'NA', '@F1@'],
        ['@I5@', 'Larsa Pippen', 'Male', '29 Apr 1998', 23, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Bryce Maximus Pippen', 'Female', '12 Jul 2001', 22, True, 'NA', '@F2@', 'NA'],
        ['@I7@', 'William Smyffe', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Dawn O-Thyme', 'Female', '06 Feb 1975', 48, False, '12 Dec 2021', '@F3@', '@F5@'],
        ['@I9@', 'Female Brianson', 'Male', '27 Nov 1989', 32, True, 'NA', '@F5@', 'NA'],
        ['@I10@', 'Habitat Correner', 'Female', '20 May 1995', 26, True, 'NA', 'NA', '@F2@']]

        f1 = [['@F1@', '18 Jan 2001', 'NA', '@I1@', 'Bryce Maximus Pippen', '@I11@', 'Zara Theobold Lindholm', 'NA'],
        ['@F2@', '10 Feb 1995', 'NA', '@I2@', 'Guy Stephenson', '@I12@', 'Habitat Correner', 'NA'],
        ['@F3@', '07 Mar 2002', '15 Jul 2018', '@I3@', 'Queezy Moonroof', '@I13@', 'Juicifruit Anime', '@F1@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I4@', 'Mohammed Colaze', '@I14@', 'Female Brianson', '@F2@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Easter Saturday', '@I15@', 'Freedom March', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'Saumit Okobachevsky', '@I16@', 'Jackie Dickinson', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Henry Pride', '@I17@', 'Samantha Sassafras', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Jurgo McRich', '@I18@', 'Anna-Zon LeSplore', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Eric Chen', '@I19@', 'Karen Wu', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Michael Stevens', '@I20@', 'Michelle Obama', 'NA']]
        result = helper_functions.listLivingSingle(i1, f1)
        self.assertEqual(result, [])

    def test2_listLivingSingle(self):
        i2 = [['@I1@', 'Guy Stephenson', 'Male', '23 Dec 1985', 36, True, 'NA', '@F5@', 'NA'],
        ['@I2@', 'Zara Theobold Lindholm', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', 'NA'],
        ['@I3@', 'Henry Colaze', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', 'NA'],
        ['@I4@', 'Mohammed Colaze', 'Female', '17 Oct 1977', 44, False, 'NA', 'NA', 'NA'],
        ['@I5@', 'Larsa Pippen', 'Male', '29 Apr 1998', 23, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Bryce Maximus Pippen', 'Female', '12 Jul 2001', 22, True, 'NA', '@F2@', 'NA'],
        ['@I7@', 'William Smyffe', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Dawn O-Thyme', 'Female', '06 Feb 1975', 48, False, '12 Dec 2021', '@F3@', 'NA'],
        ['@I9@', 'Female Brianson', 'Male', '27 Nov 1989', 32, True, 'NA', 'NA', 'NA'],
        ['@I10@', 'Habitat Correner', 'Female', '20 May 1995', 26, True, 'NA', 'NA', '@F2@']]

        f2 = [['@F1@', '18 Jan 2001', 'NA', '@I1@', 'Bryce Maximus Pippen', '@I11@', 'Zara Theobold Lindholm', 'NA'],
        ['@F2@', '10 Feb 1995', 'NA', '@I2@', 'Lawrence Laundormat', '@I12@', 'Habitat Correner', 'NA'],
        ['@F3@', '07 Mar 2002', '15 Jul 2018', '@I3@', 'Queezy Moonroof', '@I13@', 'Juicifruit Anime', '@F1@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I4@', 'Mohammed Colaze', '@I14@', 'Female Brianson', '@F2@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Easter Saturday', '@I15@', 'Freedom March', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'Saumit Okobachevsky', '@I16@', 'Jackie Dickinson', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Henry Pride', '@I17@', 'Samantha Sassafras', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Jurgo McRich', '@I18@', 'Anna-Zon LeSplore', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Michael Stevens', '@I19@', 'Wacky Richardson', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Miguel Parkinson', '@I20@', 'Michelle Obama', 'NA']]
        result = helper_functions.listLivingSingle(i2, f2)
        self.assertEqual(result, ['Guy Stephenson', 'William Smyffe'])

    def test3_listLivingSingle(self):
        i3 = [['@I1@', 'Guy Stephenson', 'Male', '23 Dec 1985', 36, True, 'NA', '@F5@', 'NA'],
        ['@I2@', 'Zara Theobold Lindholm', 'Female', '14 Feb 1972', 51, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Henry Colaze', 'Male', '09 Nov 1983', 39, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Mohammed Colaze', 'Male', '17 Oct 1977', 44, True, 'NA', 'NA', '@F1@'],
        ['@I5@', 'Larsa Pippen', 'Female', '01 Apr 1970', 52, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Bryce Maximus Pippen', 'Male', '12 Jul 2001', 22, True, '07 Jan 2020', '@F2@', '@F1'],
        ['@I7@', 'William Smyffe', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Dawn O-Thyme', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Female Brianson', 'Male', '27 Nov 1989', 32, True, 'NA', '@F5@', 'NA'],
        ['@I10@', 'Habitat Correner', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]

        f3 = [['@F1@', '18 Jan 2001', 'NA', '@I1@', 'Bryce Maximus Pippen', '@I11@', 'Zara Theobold Lindholm', 'NA'],
        ['@F2@', '10 Feb 1995', 'NA', '@I2@', 'Lawrence Laundormat', '@I12@', 'Habitat Correner', 'NA'],
        ['@F3@', '07 Mar 2002', '15 Jul 2018', '@I4@', 'Queezy Moonroof', '@I13@', 'Juicifruit Anime', '@F1@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I4@', 'Harrison Hazmat III', '@I14@', 'Gilgamesh Gorbichev', '@F2@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Easter Saturday', '@I15@', 'Freedom March', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'Saumit Okobachevsky', '@I16@', 'Jackie Dickinson', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Henry Pride', '@I17@', 'Samantha Sassafras', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Jurgo McRich', '@I18@', 'Anna-Zon LeSplore', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Michael Stevens', '@I19@', 'Wacky Richardson', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Miguel Parkinson', '@I20@', 'Michelle Obama', 'NA']]
        result = helper_functions.listLivingSingle(i3, f3)
        self.assertEqual(result, ['Guy Stephenson'])
        
    def test_uniqueID(self):
        i1 = [['@I1@', 'Guy Stephenson', 'Male', '31 Dec 1999', 23, True, 'NA', '@F5@', '@F2@'],
        ['@I2@', 'Zara Theobold Lindholm', 'Female', '14 Feb 1972', 51, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Henry Colaze', 'Male', '09 Nov 1983', 39, False, '05 Jan 1982', '@F1@', '@F5@'],
        ['@I4@', 'Mohammed Colaze', 'Male', '15 Jan 2004', 19, False, '05 Jan 2022', 'NA', '@F4@'],
        ['@I5@', 'Larsa Pippen', 'Female', '01 Apr 1970', 52, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Bryce Maximus Pippen', 'Male', '12 Jul 2001', 22, True, '07 Jan 2020', '@F2@', '@F1'],
        ['@I7@', 'William Smyffe', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Dawn O-Thyme', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I1@', 'Female Brianson', 'Male', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Habitat Correner', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]

        f1 = [['@F1@', '12 Sep 2070', 'NA', '@I1@', 'Bryce Maximus Pippen', '@I11@', 'Zara Theobold Lindholm', 'NA'],
        ['@F2@', '02 May 1990', 'NA', '@I1@', 'Guy Stephenson', '@10@', 'Habitat Correner', 'NA'],
        ['@F3@', '07 Mar 2002', '08 Jun 2002', '@I3@', 'Queezy Moonroof', '@I13@', 'Juicifruit Anime', '@I5@'],
        ['@F4@', '25 Nov 2005', '12 Oct 2015', '@I4@', 'Mohammed Colaze', '@I9@', 'Female Brianson', '@F2@'],
        ['@F5@', '29 Feb 1996', 'NA', '@I5@', 'Easter Saturday', '@I15@', 'Freedom March', 'NA'],
        ['@F6@', '03 Jan 1997', 'NA', '@I6@', 'Saumit Okobachevsky', '@I16@', 'Jackie Dickinson', 'NA'],
        ['@F7@', '19 Jun 2009', 'NA', '@I7@', 'Henry Pride', '@I17@', 'Samantha Sassafras', 'NA'],
        ['@F8@', '25 Dec 1985', '21 Dec 2001', '@I8@', 'Jurgo McRich', '@I18@', 'Anna-Zon LeSplore', '@F3@'],
        ['@F9@', '11 Nov 1976', '23 Nov 1999', '@I9@', 'Michael Stevens', '@I19@', 'Wacky Richardson', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Miguel Parkinson', '@I20@', 'Michelle Obama', 'NA']]
        result = helper_functions.uniqueID(i1, f1)      
        self.assertEqual(result, ["ERROR: INDIVIDUAL: US22: ID: @I1@: Female Brianson and Guy Stephenson have the same IDs"])

    def test_parentsNotTooOld(self):
        i1 = [['@I1@', 'Guy Stephenson', 'Male', '31 Dec 1989', 23, True, 'NA', '@F1@', '@F2@'],
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
        ['@F2@', '02 May 1990', 'NA', '@I1@', 'Guy Stephenson', '@10@', 'Habitat Correner', 'NA'],
        ['@F3@', '07 Mar 2002', '08 Jun 2002', '@I3@', 'Queezy Moonroof', '@I13@', 'Juicifruit Anime', "[@I2@]"],
        ['@F4@', '25 Nov 2005', '12 Oct 2015', '@I4@', 'Mohammed Colaze', '@I9@', 'Female Brianson', '[@I5@, @I6@]'],
        ['@F5@', '29 Feb 1996', 'NA', '@I5@', 'Easter Saturday', '@I15@', 'Freedom March', 'NA'],
        ['@F6@', '03 Jan 1997', 'NA', '@I6@', 'Saumit Okobachevsky', '@I16@', 'Jackie Dickinson', 'NA'],
        ['@F7@', '19 Jun 2009', 'NA', '@I7@', 'Henry Pride', '@I17@', 'Samantha Sassafras', 'NA'],
        ['@F8@', '25 Dec 1985', '21 Dec 2001', '@I8@', 'Jurgo McRich', '@I18@', 'Anna-Zon LeSplore', '[@I3@]'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Miguel Parkinson', '@I20@', 'Michelle Obama', 'NA']]
        result = helper_functions.parentsNotTooOld(i1, f1)
        self.assertEqual(result, ['ERROR: FAMILY: US12: ID: @I9@: @I9@is too old to be a parent to@I5@', 'ERROR: FAMILY: US12: ID: @I4@: @I4@is too old to be a parent to@I5@', 'ERROR: FAMILY: US12: ID: @I9@: @I9@is too old to be a parent to@I6@'])
        
    def test_bigamy(self):
        i1 = [['@I1@', 'Guy Stephenson', 'Male', '31 Dec 1999', 23, True, 'NA', '@F5@', '@F2@'],
        ['@I2@', 'Zara Theobold Lindholm', 'Female', '14 Feb 1972', 51, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Henry Colaze', 'Male', '09 Nov 1983', 39, False, '05 Jan 1982', '@F1@', '@F5@'],
        ['@I4@', 'Mohammed Colaze', 'Male', '15 Jan 2004', 19, False, '05 Jan 2022', 'NA', '@F4@'],
        ['@I5@', 'Larsa Pippen', 'Female', '01 Apr 1970', 52, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Bryce Maximus Pippen', 'Male', '12 Jul 2001', 22, True, '07 Jan 2020', '@F2@', '@F1'],
        ['@I7@', 'William Smyffe', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Dawn O-Thyme', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I1@', 'Female Brianson', 'Male', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Habitat Correner', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]

        f1 = [['@F1@', '12 Sep 2070', 'NA', '@I1@', 'Bryce Maximus Pippen', '@I11@', 'Zara Theobold Lindholm', 'NA'],
        ['@F2@', '02 May 1990', 'NA', '@I1@', 'Guy Stephenson', '@10@', 'Habitat Correner', 'NA'],
        ['@F3@', '07 Mar 2002', '08 Jun 2002', '@I3@', 'Queezy Moonroof', '@I13@', 'Juicifruit Anime', '@I5@'],
        ['@F4@', '25 Nov 2005', '12 Oct 2015', '@I4@', 'Mohammed Colaze', '@I9@', 'Female Brianson', '@F2@'],
        ['@F5@', '29 Feb 1996', 'NA', '@I5@', 'Easter Saturday', '@I15@', 'Freedom March', 'NA'],
        ['@F6@', '03 Jan 1997', 'NA', '@I6@', 'Saumit Okobachevsky', '@I16@', 'Jackie Dickinson', 'NA'],
        ['@F7@', '19 Jun 2009', 'NA', '@I7@', 'Henry Pride', '@I17@', 'Samantha Sassafras', 'NA'],
        ['@F8@', '25 Dec 1985', '21 Dec 2001', '@I8@', 'Jurgo McRich', '@I18@', 'Anna-Zon LeSplore', '@F3@'],
        ['@F9@', '11 Nov 1976', '23 Nov 1999', '@I9@', 'Michael Stevens', '@I19@', 'Wacky Richardson', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Miguel Parkinson', '@I20@', 'Michelle Obama', 'NA']]
        result = helper_functions.noBigamy(i1, f1)      
        self.assertEqual(result, ["There are no bigamy cases in this file."])
		
    def test_livingMarried(self):
        i1 = [['@I1@', 'Guy Stephenson', 'Male', '31 Dec 1999', 23, True, 'NA', '@F5@', '@F2@'],
        ['@I2@', 'Zara Theobold Lindholm', 'Female', '14 Feb 1972', 51, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Henry Colaze', 'Male', '09 Nov 1983', 39, False, '05 Jan 1982', '@F1@', '@F5@'],
        ['@I4@', 'Mohammed Colaze', 'Male', '15 Jan 2004', 19, False, '05 Jan 2022', 'NA', '@F4@'],
        ['@I5@', 'Larsa Pippen', 'Female', '01 Apr 1970', 52, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Bryce Maximus Pippen', 'Male', '12 Jul 2001', 22, True, '07 Jan 2020', '@F2@', '@F1'],
        ['@I7@', 'William Smyffe', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Dawn O-Thyme', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I1@', 'Female Brianson', 'Male', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Habitat Correner', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]

        f1 = [['@F1@', '12 Sep 2070', 'NA', '@I1@', 'Bryce Maximus Pippen', '@I11@', 'Zara Theobold Lindholm', 'NA'],
        ['@F2@', '02 May 1990', 'NA', '@I1@', 'Guy Stephenson', '@10@', 'Habitat Correner', 'NA'],
        ['@F3@', '07 Mar 2002', '08 Jun 2002', '@I3@', 'Queezy Moonroof', '@I13@', 'Juicifruit Anime', '@I5@'],
        ['@F4@', '25 Nov 2005', '12 Oct 2015', '@I4@', 'Mohammed Colaze', '@I9@', 'Female Brianson', '@F2@'],
        ['@F5@', '29 Feb 1996', 'NA', '@I5@', 'Easter Saturday', '@I15@', 'Freedom March', 'NA'],
        ['@F6@', '03 Jan 1997', 'NA', '@I6@', 'Saumit Okobachevsky', '@I16@', 'Jackie Dickinson', 'NA'],
        ['@F7@', '19 Jun 2009', 'NA', '@I7@', 'Henry Pride', '@I17@', 'Samantha Sassafras', 'NA'],
        ['@F8@', '25 Dec 1985', '21 Dec 2001', '@I8@', 'Jurgo McRich', '@I18@', 'Anna-Zon LeSplore', '@F3@'],
        ['@F9@', '11 Nov 1976', '23 Nov 1999', '@I9@', 'Michael Stevens', '@I19@', 'Wacky Richardson', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Miguel Parkinson', '@I20@', 'Michelle Obama', 'NA']]
        result = helper_functions.listLivingMarried(i1, f1)      
        self.assertEqual(result, ['Zara Theobold Lindholm', 'William Smyffe', 'Female Brianson', 'Habitat Correner'])
	

    def test1_maleLastNames(self):
        i1 = [['@I1@', 'Guy Stephenson', 'M', '23 Dec 1985', 35, True, 'NA', '@F5@', '@F2@'],
        ['@I11@', 'Zara Theobold Lindholm', 'F', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I12@', 'Female Brianson', 'M', '17 Nov 2002', 20, 'NA', '@F1@', 'NA']]  
        f1 = [['@F1@', '18 Jan 1800', 'Guy Stephenson', '@I1@', 'Guy Stephenson', '@I11@', 'Zara Theobold Lindholm', ['@I12@']]]
        result = helper_functions.maleLastNames(i1, f1)
        self.assertEqual(result, ['Error: @I12@ does not have the same name as their father.'])

    def test2_maleLastNames(self):
        i2 = [['@I1@', 'Guy Stephenson', 'M', '23 Dec 1985', 35, True, 'NA', '@F5@', '@F2@'],
        ['@I11@', 'Zara Theobold Lindholm', 'F', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@']]  
        f2 = [['@F1@', '18 Jan 1800', 'Guy Stephenson', '@I1@', 'Guy Stephenson', '@I11@', 'Zara Theobold Lindholm', 'NA']]
        result = helper_functions.maleLastNames(i2, f2)
        self.assertEqual(result, [])

    def test3_maleLastNames(self):
        i3 = [['@I1@', 'Henry Colaze', 'M', '23 Dec 1985', 35, True, 'NA', '@F5@', '@F2@'],
        ['@I11@', 'Princess Colaze', 'F', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I12@', 'Mohammed Colaze', 'M', '17 Nov 2002', 20, 'NA', '@F1@', 'NA'],
        ['@I13@', 'Queezy Moonroof', 'F', '17 Nov 2002', 20, 'NA', '@F1@', 'NA']]  
        f3 = [['@F1@', '18 Jan 1800', 'Henry Colaze', '@I1@', 'Henry Colaze', '@I11@', 'Princess Colaze', ['@I12@', '@I13@']]]
        result = helper_functions.maleLastNames(i3, f3)
        self.assertEqual(result, [])

    def test4_maleLastNames(self):
        i4 = [['@I1@', 'Henry Colaze', 'M', '23 Dec 1985', 35, True, 'NA', '@F5@', '@F2@'],
        ['@I11@', 'Princess Colaze', 'F', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I12@', 'Easter Saturday', 'M', '17 Nov 2002', 20, 'NA', '@F1@', 'NA'],
        ['@I13@', 'Freedom March', 'M', '17 Nov 2002', 20, 'NA', '@F1@', 'NA']]  
        f4 = [['@F1@', '18 Jan 1800', 'Henry Colaze', '@I1@', 'Henry Colaze', '@I11@', 'Princess Colaze', ['@I12@', '@I13@']]]
        result = helper_functions.maleLastNames(i4, f4)
        self.assertEqual(result, ['Error: @I12@ does not have the same name as their father.', 'Error: @I13@ does not have the same name as their father.'])

	
    def test1_listOrphans(self):
        i1 = [['@I1@', 'Guy Stephenson', 'Male', '23 Dec 1985', 36, True, 'NA', '@F5@', 'NA'],
        ['@I2@', 'Zara Theobold Lindholm', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Henry Colaze', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Mohammed Colaze', 'Male', '17 Oct 1977', 44, False, '05 Jan 2022', 'NA', '@F4@'],
        ['@I5@', 'Bryce Maximus Pippen', 'Male', '29 Apr 1998', 3, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Larsa Pippen', 'Female', '12 Jul 2001', 22, True, 'NA', '@F2@', 'NA'],
        ['@I7@', 'William Smyffe', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Dawn O-Thyme', 'Female', '06 Feb 1975', 48, False, '12 Dec 2021', '@F3@', '@F5@'],
        ['@I9@', 'Female Brianson', 'Male', '27 Nov 1989', 32, False, '05 Jan 2022', '@F5@', '@F4@'],
        ['@I10@', 'Habitat Correner', 'Female', '20 May 1995', 17, True, 'NA', 'NA', '@F4@']]

        f1 = [['@F1@', '18 Jan 2001', 'NA', '@I1@', 'Bryce Maximus Pippen', '@I11@', 'Zara Theobold Lindholm', 'NA'],
        ['@F2@', '10 Feb 1995', 'NA', '@I2@', 'Lawrence Laundormat', '@I12@', 'Habitat Correner', 'NA'],
        ['@F3@', '07 Mar 2002', '15 Jul 2018', '@I3@', 'Queezy Moonroof', '@I13@', 'Juicifruit Anime', '@I5@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I4@', 'Harrison Hazmat III', '@I9@', 'Gilgamesh Gorbichev', '@F2'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Easter Saturday', '@I15@', 'Freedom March', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'Saumit Okobachevsky', '@I16@', 'Jackie Dickinson', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Henry Pride', '@I17@', 'Samantha Sassafras', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Jurgo McRich', '@I18@', 'Anna-Zon LeSplore', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Michael Stevens', '@I19@', 'Wacky Richardson', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Miguel Parkinson', '@I20@', 'Michelle Obama', 'NA']]
        result = helper_functions.listOrphans(i1, f1)
        self.assertEqual(result, ['Bryce Maximus Pippen', 'Habitat Correner'])

    def test2_listOrphans(self):
        i2 = [['@I1@', 'Guy Stephenson', 'Male', '23 Dec 1985', 36, True, 'NA', '@F5@', 'NA'],
        ['@I2@', 'Zara Theobold Lindholm', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', 'NA'],
        ['@I3@', 'Henry Colaze', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', 'NA'],
        ['@I4@', 'Mohammed Colaze', 'Female', '17 Oct 1977', 44, False, 'NA', 'NA', 'NA'],
        ['@I5@', 'Larsa Pippen', 'Male', '29 Apr 1998', 23, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Bryce Maximus Pippen', 'Female', '12 Jul 2001', 22, True, 'NA', '@F2@', 'NA'],
        ['@I7@', 'William Smyffe', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Dawn O-Thyme', 'Female', '06 Feb 1975', 48, False, '12 Dec 2021', '@F3@', 'NA'],
        ['@I9@', 'Female Brianson', 'Male', '27 Nov 1989', 32, True, 'NA', 'NA', 'NA'],
        ['@I10@', 'Habitat Correner', 'Female', '20 May 1995', 26, True, 'NA', 'NA', '@F2@']]

        f2 = [['@F1@', '18 Jan 2001', 'NA', '@I1@', 'Bryce Maximus Pippen', '@I11@', 'Zara Theobold Lindholm', 'NA'],
        ['@F2@', '10 Feb 1995', 'NA', '@I2@', 'Lawrence Laundormat', '@I12@', 'Habitat Correner', 'NA'],
        ['@F3@', '07 Mar 2002', '15 Jul 2018', '@I3@', 'Queezy Moonroof', '@I13@', 'Juicifruit Anime', '@F1@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I4@', 'Mohammed Colaze', '@I14@', 'Female Brianson', '@F2@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Easter Saturday', '@I15@', 'Freedom March', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'Saumit Okobachevsky', '@I16@', 'Jackie Dickinson', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Henry Pride', '@I17@', 'Samantha Sassafras', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Jurgo McRich', '@I18@', 'Anna-Zon LeSplore', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Michael Stevens', '@I19@', 'Wacky Richardson', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Miguel Parkinson', '@I20@', 'Michelle Obama', 'NA']]
        result = helper_functions.listOrphans(i2, f2)
        self.assertEqual(result, [])

    def test3_listOrphans(self):
        i3 = [['@I1@', 'Guy Stephenson', 'Male', '23 Dec 1985', 36, True, 'NA', '@F5@', 'NA'],
        ['@I2@', 'Zara Theobold Lindholm', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Henry Colaze', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Mohammed Colaze', 'Male', '17 Oct 1977', 44, False, '05 Jan 2022', 'NA', '@F4@'],
        ['@I5@', 'Bryce Maximus Pippen', 'Male', '29 Apr 1998', 3, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Larsa Pippen', 'Female', '12 Jul 2001', 22, True, 'NA', '@F2@', 'NA'],
        ['@I7@', 'William Smyffe', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Dawn O-Thyme', 'Female', '06 Feb 1975', 48, False, '12 Dec 2021', '@F3@', '@F5@'],
        ['@I9@', 'Female Brianson', 'Male', '27 Nov 1989', 32, False, '05 Jan 2022', '@F5@', '@F4@'],
        ['@I10@', 'Habitat Correner', 'Female', '20 May 1995', 17, True, 'NA', 'NA', '@F4@']]

        f3 = [['@F1@', '18 Jan 2001', 'NA', '@I1@', 'Bryce Maximus Pippen', '@I11@', 'Zara Theobold Lindholm', 'NA'],
        ['@F2@', '10 Feb 1995', 'NA', '@I2@', 'Lawrence Laundormat', '@I12@', 'Habitat Correner', 'NA'],
        ['@F3@', '07 Mar 2002', '15 Jul 2018', '@I3@', 'Queezy Moonroof', '@I13@', 'Juicifruit Anime', '@I5@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I4@', 'Harrison Hazmat III', '@I9@', 'Gilgamesh Gorbichev', '@F2'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Easter Saturday', '@I15@', 'Freedom March', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'Saumit Okobachevsky', '@I16@', 'Jackie Dickinson', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Henry Pride', '@I17@', 'Samantha Sassafras', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Jurgo McRich', '@I18@', 'Anna-Zon LeSplore', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Michael Stevens', '@I19@', 'Wacky Richardson', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Miguel Parkinson', '@I20@', 'Michelle Obama', 'NA']]
        result = helper_functions.listOrphans(i3, f3)
        self.assertEqual(result, ['Bryce Maximus Pippen', 'Habitat Correner'])

    def test_CorrectGender1(self):
        i1 = [['@I1@', 'Guy Stephenson', 'Male', '31 Dec 1989', 23, True, 'NA', '@F1@', '@F2@'],
            ['@I2@', 'Zara Theobold Lindholm', 'Female', '14 Feb 1972', 51, True, 'NA', 'NA', '@F3@'],
            ['@I3@', 'Henry Colaze', 'Male', '09 Nov 1983', 39, False, '05 Jan 1982', '@F1@', '@F5@'],
            ['@I4@', 'Mohammed Colaze', 'Male', '15 Jan 1940', 83, False, '05 Jan 2022', 'NA', '@F4@'],
            ['@I5@', 'Larsa Pippen', 'Female', '01 Apr 2000', 2, True, 'NA', '@F4@', 'NA'],
            ['@I6@', 'Bryce Maximus Pippen', 'Male', '12 Jul 2012', 10, True, '07 Jan 2020', '@F2@', '@F1'],
            ['@I7@', 'William Smyffe', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
            ['@I8@', 'Dawn O-Thyme', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
            ['@I9@', 'Female Brianson', 'Female', '27 Nov 1950', 72, True, 'NA', '@F5@', '@F4@'],
            ['@I10@', 'Habitat Correner', 'Male', '06 Feb 1960', 60, True, 'NA', '@F1@', '@F2@']]

        f1 = [['@F1@', '12 Sep 2070', 'NA', '@I1@', 'Bryce Maximus Pippen', '@I11@', 'Zara Theobold Lindholm', 'NA'],
            ['@F2@', '02 May 1990', 'NA', '@I1@', 'Guy Stephenson', '@I10@', 'Habitat Correner', 'NA'],
            ['@F3@', '07 Mar 2002', '08 Jun 2002', '@I3@', 'Queezy Moonroof', '@I13@', 'Juicifruit Anime', "[@I2@]"],
            ['@F4@', '25 Nov 2005', '12 Oct 2015', '@I4@', 'Mohammed Colaze', '@I9@', 'Female Brianson', '[@I5@, @I6@]'],
            ['@F5@', '29 Feb 1996', 'NA', '@I15@', 'Easter Saturday', '@I5@', 'Freedom March', 'NA'],
            ['@F6@', '03 Jan 1997', 'NA', '@I6@', 'Saumit Okobachevsky', '@I16@', 'Jackie Dickinson', 'NA'],
            ['@F7@', '19 Jun 2009', 'NA', '@I7@', 'Henry Pride', '@I17@', 'Samantha Sassafras', 'NA'],
            ['@F8@', '25 Dec 1985', '21 Dec 2001', '@I18@', 'Jurgo McRich', '@I8@', 'Anna-Zon LeSplore', '[@I3@]'],
            ['@F10@', '30 Oct 2010', 'NA', '@I21@', 'Miguel Parkinson', '@I20@', 'Michelle Obama', 'NA']]
        result = helper_functions.correctGender(i1, f1)      
        self.assertEqual(result, ['Error: Individual @I10@ is wife in family @F2@ but has gender: Male'])

    def test_CorrectGender2(self):
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
            ['@F2@', '02 May 1990', 'NA', '@I41@', 'Guy Stephenson', '@I10@', 'Habitat Correner', 'NA'],
            ['@F3@', '07 Mar 2002', '08 Jun 2002', '@I3@', 'Queezy Moonroof', '@I13@', 'Juicifruit Anime', "[@I2@]"],
            ['@F4@', '25 Nov 2005', '12 Oct 2015', '@I4@', 'Mohammed Colaze', '@I9@', 'Female Brianson', '[@I5@, @I6@]'],
            ['@F5@', '29 Feb 1996', 'NA', '@I15@', 'Easter Saturday', '@I5@', 'Freedom March', 'NA'],
            ['@F6@', '03 Jan 1997', 'NA', '@I6@', 'Saumit Okobachevsky', '@I16@', 'Jackie Dickinson', 'NA'],
            ['@F7@', '19 Jun 2009', 'NA', '@I7@', 'Henry Pride', '@I17@', 'Samantha Sassafras', 'NA'],
            ['@F8@', '25 Dec 1985', '21 Dec 2001', '@I18@', 'Jurgo McRich', '@I8@', 'Anna-Zon LeSplore', '[@I3@]'],
            ['@F10@', '30 Oct 2010', 'NA', '@I21@', 'Miguel Parkinson', '@I20@', 'Michelle Obama', 'NA']]
        result = helper_functions.correctGender(i1, f1)      
        self.assertEqual(result, ['Error: Individual @I1@ is husband in family @F1@ but has gender: Female'])
	
	def test1_noMarriageDescendants(self):
        i2 = [['@I1@', 'Guy Stephenson', 'Male', '31 Dec 1999', 23, True, 'NA', '@F5@', '@F2@'],
        ['@I2@', 'Zara Theobold Lindholm', 'Female', '14 Feb 1972', 51, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Henry Colaze', 'Male', '09 Nov 1983', 39, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Mohammed Colaze', 'Male', '15 Jan 2004', 19, False, '05 Jan 2022', 'NA', '@F4@'],
        ['@I5@', 'Larsa Pippen', 'Female', '01 Apr 1970', 52, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Bryce Maximus Pippen', 'Male', '12 Jul 2001', 22, True, '07 Jan 2020', '@F2@', '@F1'],
        ['@I7@', 'William Smyffe', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Dawn O-Thyme', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Female Brianson', 'Male', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Habitat Correner', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]

        f2 = [['@F1@', '12 Sep 2070', 'NA', '@I1@', 'Bryce Maximus Pippen', '@I11@', 'Zara Theobold Lindholm', 'NA'],
        ['@F2@', '02 May 1990', 'NA', '@I1@', 'Guy Stephenson', '@10@', 'Habitat Correner', 'NA'],
        ['@F3@', '07 Jun 2002', '08 Mar 2002', '@I3@', 'Queezy Moonroof', '@I13@', 'Juicifruit Anime', '@I5@'],
        ['@F4@', '25 Nov 2005', '12 Oct 2015', '@I4@', 'Mohammed Colaze', '@I9@', 'Female Brianson', '@F2@'],
        ['@F5@', '29 Feb 1996', 'NA', '@I5@', 'Easter Saturday', '@I15@', 'Freedom March', 'NA'],
        ['@F6@', '03 Jan 1997', 'NA', '@I6@', 'Saumit Okobachevsky', '@I16@', 'Jackie Dickinson', 'NA'],
        ['@F7@', '19 Jun 2009', 'NA', '@I7@', 'Henry Pride', '@I17@', 'Samantha Sassafras', 'NA'],
        ['@F8@', '25 Dec 1985', '21 Dec 2001', '@I8@', 'Jurgo McRich', '@I18@', 'Anna-Zon LeSplore', '@F3@'],
        ['@F9@', '11 Nov 1976', '23 Nov 1999', '@I9@', 'Michael Stevens', '@I19@', 'Wacky Richardson', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Miguel Parkinson', '@I20@', 'Michelle Obama', 'NA']]
        result = helper_functions.noMarriageDescendants(i2, f2)
        self.assertEqual(result, False)
	
	def test1_lessThan15(self):
        i2 = [['@I1@', 'Guy Stephenson', 'Male', '31 Dec 1999', 23, True, 'NA', '@F5@', '@F2@'],
        ['@I2@', 'Zara Theobold Lindholm', 'Female', '14 Feb 1972', 51, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Henry Colaze', 'Male', '09 Nov 1983', 39, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Mohammed Colaze', 'Male', '15 Jan 2004', 19, False, '05 Jan 2022', 'NA', '@F4@'],
        ['@I5@', 'Larsa Pippen', 'Female', '01 Apr 1970', 52, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Bryce Maximus Pippen', 'Male', '12 Jul 2001', 22, True, '07 Jan 2020', '@F2@', '@F1'],
        ['@I7@', 'William Smyffe', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Dawn O-Thyme', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Female Brianson', 'Male', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Habitat Correner', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]

        f2 = [['@F1@', '12 Sep 2070', 'NA', '@I1@', 'Bryce Maximus Pippen', '@I11@', 'Zara Theobold Lindholm', 'NA'],
        ['@F2@', '02 May 1990', 'NA', '@I1@', 'Guy Stephenson', '@10@', 'Habitat Correner', 'NA'],
        ['@F3@', '07 Jun 2002', '08 Mar 2002', '@I3@', 'Queezy Moonroof', '@I13@', 'Juicifruit Anime', '@I5@'],
        ['@F4@', '25 Nov 2005', '12 Oct 2015', '@I4@', 'Mohammed Colaze', '@I9@', 'Female Brianson', '@F2@'],
        ['@F5@', '29 Feb 1996', 'NA', '@I5@', 'Easter Saturday', '@I15@', 'Freedom March', 'NA'],
        ['@F6@', '03 Jan 1997', 'NA', '@I6@', 'Saumit Okobachevsky', '@I16@', 'Jackie Dickinson', 'NA'],
        ['@F7@', '19 Jun 2009', 'NA', '@I7@', 'Henry Pride', '@I17@', 'Samantha Sassafras', 'NA'],
        ['@F8@', '25 Dec 1985', '21 Dec 2001', '@I8@', 'Jurgo McRich', '@I18@', 'Anna-Zon LeSplore', '@F3@'],
        ['@F9@', '11 Nov 1976', '23 Nov 1999', '@I9@', 'Michael Stevens', '@I19@', 'Wacky Richardson', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Miguel Parkinson', '@I20@', 'Michelle Obama', 'NA']]
        result = helper_functions.lessThan15Siblings(i1, f1)
        self.assertEqual(result, False)

	
	def test1_individualAges(self):
        i1 = [['@I1@', 'Henry Colaze', 'M', '23 Dec 1985', 35, True, 'NA', '@F5@', '@F2@'],
        ['@I11@', 'Princess Colaze', 'F', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I12@', 'Mohammed Colaze', 'M', '17 Nov 2002', 20, 'NA', '@F1@', 'NA'],
        ['@I13@', 'Queezy Moonroof', 'F', '17 Nov 2002', 20, 'NA', '@F1@', 'NA']]  
        result = helper_functions.individualAges(i1)
        self.assertEqual(result, ['ENTRY FOUND: @I1@: Henry Colaze is of age 35', 'ENTRY FOUND: @I11@: Princess Colaze is of age 29', 
                                  'ENTRY FOUND: @I12@: Mohammed Colaze is of age 20', 'ENTRY FOUND: @I13@: Queezy Moonroof is of age 20'])

    def test2_individualAges(self):
        i2 = [['@I1@', 'William Smyffe', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I2@', 'Dawn O-Thyme', 'Female', '06 Feb 1975', 48, False, '12 Dec 2021', '@F3@', '@F5@'],
        ['@I3@', 'Female Brianson', 'Male', '27 Nov 1989', 32, False, '05 Jan 2022', '@F5@', '@F4@'],
        ['@I4@', 'Habitat Correner', 'Female', '20 May 1995', 17, True, 'NA', 'NA', '@F4@']]
        result = helper_functions.individualAges(i2)
        self.assertEqual(result, ['ENTRY FOUND: @I1@: William Smyffe is of age 31', 'ENTRY FOUND: @I2@: Dawn O-Thyme is of age 48', 
                                    'ENTRY FOUND: @I3@: Female Brianson is of age 32', 'ENTRY FOUND: @I4@: Habitat Correner is of age 17'])
            
    def test3_individualAges(self):
        i3 = [['@I4@', 'Mohammed Colaze', 'Female', '17 Oct 1977', 44, False, 'NA', 'NA', 'NA'],
        ['@I5@', 'Larsa Pippen', 'Male', '29 Apr 1998', 23, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Bryce Maximus Pippen', 'Female', '12 Jul 2001', 22, True, 'NA', '@F2@', 'NA']]
        result = helper_functions.individualAges(i3)
        self.assertEqual(result, ['ENTRY FOUND: @I4@: Mohammed Colaze is of age 44', 'ENTRY FOUND: @I5@: Larsa Pippen is of age 23',  'ENTRY FOUND: @I6@: Bryce Maximus Pippen is of age 22'])


    def test1_datesBeforeCurrent(self):
        i1 = [['@I1@', 'Guy Stephenson', 'Male', '23 Dec 2024', 36, True, 'NA', '@F5@', 'NA'],
        ['@I2@', 'Zara Theobold Lindholm', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Henry Colaze', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Mohammed Colaze', 'Male', '17 Oct 1977', 44, False, '05 Jan 2022', 'NA', '@F4@'],
        ['@I5@', 'Bryce Maximus Pippen', 'Male', '29 Apr 1998', 3, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Larsa Pippen', 'Female', '12 Jul 2001', 22, True, 'NA', '@F2@', 'NA'],
        ['@I7@', 'William Smyffe', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Dawn O-Thyme', 'Female', '06 Feb 2026', 48, False, '12 Dec 2021', '@F3@', '@F5@'],
        ['@I9@', 'Female Brianson', 'Male', '27 Nov 1989', 32, False, '05 Jan 2022', '@F5@', '@F4@'],
        ['@I10@', 'Habitat Correner', 'Female', '20 May 1995', 17, True, 'NA', 'NA', '@F4@']]

        f1 = [['@F1@', '18 Jan 2001', 'NA', '@I1@', 'Bryce Maximus Pippen', '@I11@', 'Zara Theobold Lindholm', 'NA'],
        ['@F2@', '10 Feb 1995', 'NA', '@I2@', 'Lawrence Laundormat', '@I12@', 'Habitat Correner', 'NA'],
        ['@F3@', '07 Mar 2002', '15 Jul 2018', '@I3@', 'Queezy Moonroof', '@I13@', 'Juicifruit Anime', '@I5@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I4@', 'Harrison Hazmat III', '@I9@', 'Gilgamesh Gorbichev', '@F2'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Easter Saturday', '@I15@', 'Freedom March', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'Saumit Okobachevsky', '@I16@', 'Jackie Dickinson', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Henry Pride', '@I17@', 'Samantha Sassafras', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Jurgo McRich', '@I18@', 'Anna-Zon LeSplore', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Michael Stevens', '@I19@', 'Wacky Richardson', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Miguel Parkinson', '@I20@', 'Michelle Obama', 'NA']]
        result = helper_functions.datesBeforeCurrent(i1, f1)
        self.assertEqual(result, ['ERROR: @I1@ was born after today', 'ERROR: @I8@ was born after today'])

    def test2_datesBeforeCurrent(self):
        i2 = [['@I1@', 'Guy Stephenson', 'Male', '23 Dec 1985', 36, True, 'NA', '@F5@', 'NA'],
        ['@I2@', 'Zara Theobold Lindholm', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', 'NA'],
        ['@I3@', 'Henry Colaze', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', 'NA'],
        ['@I4@', 'Mohammed Colaze', 'Female', '17 Oct 1977', 44, False, 'NA', 'NA', 'NA'],
        ['@I5@', 'Larsa Pippen', 'Male', '29 Apr 1998', 23, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Bryce Maximus Pippen', 'Female', '12 Jul 2001', 22, True, 'NA', '@F2@', 'NA'],
        ['@I7@', 'William Smyffe', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Dawn O-Thyme', 'Female', '06 Feb 1975', 48, False, '12 Dec 2021', '@F3@', 'NA'],
        ['@I9@', 'Female Brianson', 'Male', '27 Nov 1989', 32, True, 'NA', 'NA', 'NA'],
        ['@I10@', 'Habitat Correner', 'Female', '20 May 1995', 26, True, 'NA', 'NA', '@F2@']]

        f2 = [['@F1@', '18 Jan 2001', 'NA', '@I1@', 'Bryce Maximus Pippen', '@I11@', 'Zara Theobold Lindholm', 'NA'],
        ['@F2@', '10 Feb 2027', 'NA', '@I2@', 'Lawrence Laundormat', '@I12@', 'Habitat Correner', 'NA'],
        ['@F3@', '07 Mar 2002', '15 Jul 2018', '@I3@', 'Queezy Moonroof', '@I13@', 'Juicifruit Anime', '@F1@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2028', '@I4@', 'Mohammed Colaze', '@I14@', 'Female Brianson', '@F2@'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Easter Saturday', '@I15@', 'Freedom March', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'Saumit Okobachevsky', '@I16@', 'Jackie Dickinson', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Henry Pride', '@I17@', 'Samantha Sassafras', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Jurgo McRich', '@I18@', 'Anna-Zon LeSplore', '@F3@'],
        ['@F9@', '14 Sep 1976', '23 Nov 1999', '@I9@', 'Michael Stevens', '@I19@', 'Wacky Richardson', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Miguel Parkinson', '@I20@', 'Michelle Obama', 'NA']]
        result = helper_functions.datesBeforeCurrent(i2, f2)
        self.assertEqual(result, ['ERROR: @I2@ @I12@ were married after today', 'ERROR: @I4@ @I14@ were divorced after today'])

    def test3_datesBeforeCurrent(self):
        i3 = [['@I1@', 'Guy Stephenson', 'Male', '23 Dec 1985', 36, True, 'NA', '@F5@', 'NA'],
        ['@I2@', 'Zara Theobold Lindholm', 'Female', '14 Aug 1992', 29, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Henry Colaze', 'Male', '02 Jun 1981', 42, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Mohammed Colaze', 'Male', '17 Oct 1977', 44, False, '05 Jan 2022', 'NA', '@F4@'],
        ['@I5@', 'Bryce Maximus Pippen', 'Male', '29 Apr 1998', 3, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Larsa Pippen', 'Female', '12 Jul 2001', 22, True, 'NA', '@F2@', 'NA'],
        ['@I7@', 'William Smyffe', 'Male', '11 Sep 2027', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Dawn O-Thyme', 'Female', '06 Feb 1975', 48, False, '12 Dec 2021', '@F3@', '@F5@'],
        ['@I9@', 'Female Brianson', 'Male', '27 Nov 1989', 32, False, '05 Jan 2022', '@F5@', '@F4@'],
        ['@I10@', 'Habitat Correner', 'Female', '20 May 1995', 17, True, 'NA', 'NA', '@F4@']]

        f3 = [['@F1@', '18 Jan 2001', 'NA', '@I1@', 'Bryce Maximus Pippen', '@I11@', 'Zara Theobold Lindholm', 'NA'],
        ['@F2@', '10 Feb 1995', 'NA', '@I2@', 'Lawrence Laundormat', '@I12@', 'Habitat Correner', 'NA'],
        ['@F3@', '07 Mar 2002', '15 Jul 2018', '@I3@', 'Queezy Moonroof', '@I13@', 'Juicifruit Anime', '@I5@'],
        ['@F4@', '02 Apr 2005', '12 Oct 2015', '@I4@', 'Harrison Hazmat III', '@I9@', 'Gilgamesh Gorbichev', '@F2'],
        ['@F5@', '29 May 1998', 'NA', '@I5@', 'Easter Saturday', '@I15@', 'Freedom March', 'NA'],
        ['@F6@', '13 Jun 1997', 'NA', '@I6@', 'Saumit Okobachevsky', '@I16@', 'Jackie Dickinson', 'NA'],
        ['@F7@', '22 Jul 2009', 'NA', '@I7@', 'Henry Pride', '@I17@', 'Samantha Sassafras', 'NA'],
        ['@F8@', '08 Aug 1985', '21 Dec 2001', '@I8@', 'Jurgo McRich', '@I18@', 'Anna-Zon LeSplore', '@F3@'],
        ['@F9@', '14 Sep 2026', '23 Nov 1999', '@I9@', 'Michael Stevens', '@I19@', 'Wacky Richardson', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Miguel Parkinson', '@I20@', 'Michelle Obama', 'NA']]
        result = helper_functions.datesBeforeCurrent(i3, f3)
        self.assertEqual(result, ['ERROR: @I7@ was born after today', 'ERROR: @I9@ @I19@ were married after today'])

	
    def test1_uniqueFam(self):
        i1 = [['@I1@', 'Guy Stephenson', 'Male', '31 Dec 1999', 23, True, 'NA', '@F5@', '@F2@'],
        ['@I2@', 'Zara Theobold Lindholm', 'Female', '14 Feb 1972', 51, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Henry Colaze', 'Male', '09 Nov 1983', 39, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Mohammed Colaze', 'Male', '15 Jan 2004', 19, False, '05 Jan 2022', 'NA', '@F4@'],
        ['@I5@', 'Larsa Pippen', 'Female', '01 Apr 1970', 52, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Bryce Maximus Pippen', 'Male', '12 Jul 2001', 22, True, '07 Jan 2020', '@F2@', '@F1'],
        ['@I7@', 'William Smyffe', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Dawn O-Thyme', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Female Brianson', 'Male', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Habitat Correner', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]

        f1 = [['@F1@', '12 Sep 2070', 'NA', '@I1@', 'Bryce Maximus Pippen', '@I11@', 'Zara Theobold Lindholm', 'NA'],
        ['@F2@', '02 May 1990', 'NA', '@I1@', 'Guy Stephenson', '@10@', 'Habitat Correner', 'NA'],
        ['@F3@', '07 Jun 2002', '08 Mar 2002', '@I3@', 'Queezy Moonroof', '@I13@', 'Juicifruit Anime', '@I5@'],
        ['@F4@', '25 Nov 2005', '12 Oct 2015', '@I4@', 'Mohammed Colaze', '@I9@', 'Female Brianson', '@F2@'],
        ['@F5@', '29 Feb 1996', 'NA', '@I5@', 'Easter Saturday', '@I15@', 'Freedom March', 'NA'],
        ['@F6@', '03 Jan 1997', 'NA', '@I6@', 'Saumit Okobachevsky', '@I16@', 'Jackie Dickinson', 'NA'],
        ['@F7@', '19 Jun 2009', 'NA', '@I7@', 'Henry Pride', '@I17@', 'Samantha Sassafras', 'NA'],
        ['@F8@', '25 Dec 1985', '21 Dec 2001', '@I8@', 'Jurgo McRich', '@I18@', 'Anna-Zon LeSplore', '@F3@'],
        ['@F9@', '11 Nov 1976', '23 Nov 1999', '@I9@', 'Michael Stevens', '@I19@', 'Wacky Richardson', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Miguel Parkinson', '@I20@', 'Michelle Obama', 'NA']]
        result = helper_functions.uniqueFamilies(i1, f1)
        self.assertEqual(result, True)
		
    def test1_multipleBirths(self):
        i1 = [['@I1@', 'Guy Stephenson', 'Male', '31 Dec 1999', 23, True, 'NA', '@F5@', '@F2@'],
        ['@I2@', 'Zara Theobold Lindholm', 'Female', '14 Feb 1972', 51, True, 'NA', 'NA', '@F3@'],
        ['@I3@', 'Henry Colaze', 'Male', '09 Nov 1983', 39, False, '05 Jan 2022', '@F1@', '@F5@'],
        ['@I4@', 'Mohammed Colaze', 'Male', '15 Jan 2004', 19, False, '05 Jan 2022', 'NA', '@F4@'],
        ['@I5@', 'Larsa Pippen', 'Female', '01 Apr 1970', 52, True, 'NA', '@F4@', 'NA'],
        ['@I6@', 'Bryce Maximus Pippen', 'Male', '12 Jul 2001', 22, True, '07 Jan 2020', '@F2@', '@F1'],
        ['@I7@', 'William Smyffe', 'Male', '11 Sep 1990', 31, True, 'NA', 'NA', '@F1@'],
        ['@I8@', 'Dawn O-Thyme', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', 'NA'],
        ['@I9@', 'Female Brianson', 'Male', '27 Nov 1989', 32, True, 'NA', '@F5@', '@F4@'],
        ['@I10@', 'Habitat Correner', 'Female', '06 Feb 1960', 60, True, 'NA', '@F3@', '@F2@']]

        f1 = [['@F1@', '12 Sep 2070', 'NA', '@I1@', 'Bryce Maximus Pippen', '@I11@', 'Zara Theobold Lindholm', 'NA'],
        ['@F2@', '02 May 1990', 'NA', '@I1@', 'Guy Stephenson', '@10@', 'Habitat Correner', 'NA'],
        ['@F3@', '07 Jun 2002', '08 Mar 2002', '@I3@', 'Queezy Moonroof', '@I13@', 'Juicifruit Anime', '@I5@'],
        ['@F4@', '25 Nov 2005', '12 Oct 2015', '@I4@', 'Mohammed Colaze', '@I9@', 'Female Brianson', '@F2@'],
        ['@F5@', '29 Feb 1996', 'NA', '@I5@', 'Easter Saturday', '@I15@', 'Freedom March', 'NA'],
        ['@F6@', '03 Jan 1997', 'NA', '@I6@', 'Saumit Okobachevsky', '@I16@', 'Jackie Dickinson', 'NA'],
        ['@F7@', '19 Jun 2009', 'NA', '@I7@', 'Henry Pride', '@I17@', 'Samantha Sassafras', 'NA'],
        ['@F8@', '25 Dec 1985', '21 Dec 2001', '@I8@', 'Jurgo McRich', '@I18@', 'Anna-Zon LeSplore', '@F3@'],
        ['@F9@', '11 Nov 1976', '23 Nov 1999', '@I9@', 'Michael Stevens', '@I19@', 'Wacky Richardson', '@F4@'],
        ['@F10@', '30 Oct 2010', 'NA', '@I10@', 'Miguel Parkinson', '@I20@', 'Michelle Obama', 'NA']]
        result = helper_functions.multipleBirths(i1, f1)
        self.assertEqual(result, False)
	
if __name__ == '__main__':
    unittest.main()
