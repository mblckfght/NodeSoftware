#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
config dictionaries and corresponding functions

"""

### FUCTIONS TO APPLY TO DATA AFTER READING
def fixvald(data):
    return data

def fixrefs(data):
    return data

def fixnothing(data):
    return data

### CONFIG "FILES"
dummycfg = {\
    'tables':[\
        {'fname':'dummy.dat',
         'delim':' ',
         'tname':'dummy1',
         'headlines':0,
         'commentchar':'',
         'function':fixnothing,
         'columns':[\
                {'cname':'c1',
                 'cfmt':'%d',
                 'ccom':'column 1',
                 'cunit':None,
                 'cbyte':0,
                 'cnull':None,
                 'ctype':'UNSIGNED INT',
                 },
                {'cname':'c2',
                 'cfmt':'%.2f',
                 'ccom':'column 2',
                 'cunit':'Å',
                 'cbyte':1,
                 'cnull':0.0,
                 'ctype':'FLOAT',
                 },
                ]
         },
        {'fname':'dummy.dat',
         'delim':' ',
         'tname':'dummy2',
         'headlines':0,
         'commentchar':'',
         'function':fixnothing,
         'columns':[\
                {'cname':'c1',
                 'cfmt':'%d',
                 'ccom':'column 1',
                 'cunit':None,
                 'cbyte':0,
                 'cnull':None,
                 'ctype':'UNSIGNED INT',
                 },
                {'cname':'c2',
                 'cfmt':'%.2f',
                 'ccom':'column 2',
                 'cunit':'eV',
                 'cbyte':2,
                 'cnull':0.0,
                 'ctype':'UNSIGNED FLOAT',
                 },
                ],
         'relations':[{\
                'table1':'dummy1',
                'column1':'c1',
                'table2':'dummy2',
                'column2':'c1'
                }]
      
         }
        ]
    }

valdcfg={\
    'tables':[\
        {'tname':'merged',
         'fname':'merged.dat',
         'delim':'fixedcol', # delimiter character or 'fixedcol'
         'headlines':2,      # this many lies ignored in file header
         'commentchar':'',   # lines that start with this are ignored
         'function':fixvald,  # to be applied on each line
         'columns':[\
                {'cname':'wavel',     # column name
                 'cfmt':'%.5f',       # print format
                 'ccom':'Wavelength', # description
                 'cunit':'Å',         # Units
                 'cbit':(0,13),       # place in the line
                 'cnull':None,        # value to be converted to NULL
                 'ctype':'UNSIGNED FLOAT', # data format in database
                 },
                {'cname':'atomic',
                 'cfmt':'%d',
                 'ccom':'Atomic number',
                 'cunit':None,
                 'cbit':(13,16),
                 'cnull':None,
                 'ctype':'UNSIGNED TINYINT'},
                {'cname':'ion',
                 'cfmt':'%d',
                 'ccom':'Ionization stage, 0 is neutral',
                 'cunit':None,
                 'cbit':(17,19),
                 'cnull':None,
                 'ctype':'UNSIGNED TINYINT'},
                {'cname':'loggf',
                 'cfmt':'%.3f',
                 'ccom':'oscillator strength, log g*f',
                 'cunit':None,
                 'cbit':(19,27),
                 'cnull':None,
                 'ctype':'FLOAT'},
                {'cname':'lowev',
                 'cfmt':'%.3f',
                 'ccom':'excitation energy of the lower level',
                 'cunit':'eV',
                 'cbit':(27,35),
                 'cnull':None,
                 'ctype':'UNSIGNED FLOAT'},
                {'cname':'lowj',
                 'cfmt':'%.2f',
                 'ccom':'quantum number J of the lower level',
                 'cunit':None,
                 'cbit':(35,40),
                 'cnull':None,
                 'ctype':'UNSIGNED FLOAT'},
                {'cname':'hiev',
                 'cfmt':'%.3f',
                 'ccom':'excitation energy of the upper level',
                 'cunit':'eV',
                 'cbit':(40,48),
                 'cnull':None,
                 'ctype':'UNSIGNED FLOAT'},
                {'cname':'hij',
                 'ccom':'quantum number J of the upper level',
                 'cfmt':'%.2f',
                 'cunit':None,
                 'cbit':(48,53),
                 'cnull':None,
                 'ctype':'UNSIGNED FLOAT'},
                {'cname':'landup',
                 'cfmt':'%.2f',
                 'cunit':None,
                 'cbit':(53,59),
                 'cnull':99.00,
                 'ctype':'FLOAT'},
                {'cname':'landlo',
                 'cfmt':'%.2f',
                 'cunit':None,
                 'cbit':(59,65),
                 'cnull':99.00,
                 'ctype':'FLOAT'},
                {'cname':'landeff',
                 'cfmt':'%.2f',
                 'cunit':None,
                 'cbit':(65,71),
                 'cnull':99.00,
                 'ctype':'FLOAT'},
                {'cname':'broadrad',
                 'cfmt':'%.3f',
                 'ccom':'line broadening: radiative damping constant',
                 'cunit':None,
                 'cbit':(71,78),
                 'cnull':0.0,
                 'ctype':'FLOAT'},
                {'cname':'broadstark',
                 'cfmt':'%.3f',
                 'ccom':'line broadening: stark damping constant',
                 'cunit':None,
                 'cbit':(78,85),
                 'cnull':0.0,
                 'ctype':'FLOAT'},
                {'cname':'broadwaals',
                 'cfmt':'%.3f',
                 'ccom':'line broadening: Van der Waals damping constant',
                 'cunit':None,
                 'cbit':(85,93),
                 'cnull':0.0,
                 'ctype':'FLOAT'},
                {'cname':'transdesc',
                 'cfmt':'%.2f',
                 'ccom':'transition description, plus subselection of reference',
                 'cunit':None,
                 'cbit':(93,123),
                 'cnull':None,
                 'ctype':'CHAR(30)'},
                {'cname':'ref1',
                 'cfmt':'%d',
                 'ccom':'reference to VALD source file, i.e. reference',
                 'cunit':None,
                 'cbit':(123,127),
                 'cnull':None,
                 'ctype':'UNSIGNED SMALLINT'},
                {'cname':'ref2',
                 'cfmt':'%d',
                 'ccom':'reference to VALD source file, i.e. reference',
                 'cunit':None,
                 'cbit':(127,131),
                 'cnull':None,
                 'ctype':'UNSIGNED SMALLINT'},
                {'cname':'ref3',
                 'cfmt':'%d',
                 'ccom':'reference to VALD source file, i.e. reference',
                 'cunit':None,
                 'cbit':(131,135),
                 'cnull':None,
                 'ctype':'UNSIGNED SMALLINT'},
                {'cname':'ref4',
                 'cfmt':'%d',
                 'ccom':'reference to VALD source file, i.e. reference',
                 'cunit':None,
                 'cbit':(135,139),
                 'cnull':None,
                 'ctype':'UNSIGNED SMALLINT'},
                {'cname':'ref5',
                 'cfmt':'%d',
                 'ccom':'reference to VALD source file, i.e. reference',
                 'cunit':None,
                 'cbit':(139,143),
                 'cnull':None,
                 'ctype':'UNSIGNED SMALLINT'},
                {'cname':'ref6',
                 'cfmt':'%d',
                 'ccom':'reference to VALD source file, i.e. reference',
                 'cunit':None,
                 'cbit':(143,147),
                 'cnull':None,
                 'ctype':'UNSIGNED SMALLINT'},
                {'cname':'ref7',
                 'cfmt':'%d',
                 'ccom':'reference to VALD source file, i.e. reference',
                 'cunit':None,
                 'cbit':(147,151),
                 'cnull':None,
                 'ctype':'UNSIGNED SMALLINT'},
                {'cname':'ref8',
                 'cfmt':'%d',
                 'ccom':'reference to VALD source file, i.e. reference',
                 'cunit':None,
                 'cbit':(151,155),
                 'cnull':None,
                 'ctype':'UNSIGNED SMALLINT'},
                {'cname':'ref9',
                 'cfmt':'%d',
                 'ccom':'reference to VALD source file, i.e. reference',
                 'cunit':None,
                 'cbit':(155,159),
                 'cnull':None,
                 'ctype':'UNSIGNED SMALLINT'},
                ]
         },
        {'tname':'refs',
         'fname':'',
         'delim':',',
         'headlines':1,
         'commentchar':';',
         'function':fixrefs,
         'columns':[\
                {'cname':'',
                 'cfmt':'%.2f',
                 'ccom':'',
                 'cunit':None,
                 'cbit':(0,12),
                 'cnull':None,
                 'ctype':'FLOAT'},
                ]
         },
        ],
    'relations':[ # descibe which table.column is related to another
        {'table1':'',
         'column1':'',
         'table2':'',
         'column2':'',
         }
        ]
    }
